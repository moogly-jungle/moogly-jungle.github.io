import numpy as np
import random
import time
random.seed(int(time.time()))

# La taille du labyrinthe
maze_size = (21, 15)
# La densité des murs (1/n), 1 = pas de mur, 2 = 1 mur sur 2, etc.
maze_sparsness = None
# Le nombre d'ennemis
enemy_nb = 0
# Mode piloté par l'IA (True) ou par l'utilisateur (False)
automatic_mode = True
# Obstacles:
obstacles = True
# EXERCICE: explorez les paramètres précédents.

# La stratégie du hero est définie, celle-là n'est pas terrible, à vous de jouer...
# EXERCICE: comprendre la stratégie suivante, vous pouvez la modifier. Expliquer pourquoi elle est mauvaise..
def hero_strategy(agent):
    moves = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
    for dx, dy in moves:
        if agent.game.visitable((agent.pos[0]+dx, agent.pos[1]+dy)):
            return (dx, dy)
    return (0, 0)

# EXERCICE: Implémentez la "stratégie du mur de gauche". Attention aux obstacles, ça complique un peu les choses.

# Vous pouvez jouer aussi avec la stratégie des mechants
def enemy_strategy(agent):
    choices = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    random.shuffle(choices)
    for dx,dy in choices:
        if agent.game.visitable((agent.pos[0] + dx, agent.pos[1] + dy)):
            return (dx,dy)
    return (0,0)

##############################################################################
# EXERCICE: Vous n'avez pas besoin de modifier le code qui suit, mais lisez-le !
class Agent:
    def __init__(self, game, symbol, pos):
        self.game = game
        self.symbol = symbol
        self.pos = pos
        self.startegy = None
        self.pause = 0

    def move(self, dx, dy):
        if dx != 0 and dy != 0:
            print(f'=> {self.symbol} can\'t move diagonally')
            return
        if self.pause > 0:
            print(f'=> {self.symbol}: pause because of the obstacle')
            self.pause -= 1
            return
        if self.game.visitable((self.pos[0] + dx, self.pos[1] + dy)):            
            self.pos[0] += dx
            self.pos[1] += dy
            print(f'=> {self.symbol} go to {self.pos}')
            if self.game.obstacle(self.pos):
                print(f'=> {self.symbol} meet an obstacle (cost=1)')
                self.pause = 1
        else:
            print(f'=> {self.symbol} can\'t go to {self.pos[0] + dx, self.pos[1] + dy}, there is a wall')
            

    def tick(self):
        if self.startegy is not None:
            dx,dy = self.startegy(self)
            self.move(dx,dy)

class Enemy(Agent):
    def __init__(self, game, symbol, pos):
        super().__init__(game, symbol, pos)
        self.startegy = enemy_strategy

class Game:

    def __init__(self, size = maze_size, sparsness = None):
        config_ok = False
        while not config_ok:
            self.generate_maze(size, sparsness=sparsness)
            self.hero = Agent(self, 'O', [1, 1])
            self.agents = [ self.hero ]
            self.goal = Agent(self, 'X', self.pick_free_pos(close_to=size))
            self.agents.append(self.goal)
            config_ok = self.check_maze()
        self.enemies = []
        for i in range(enemy_nb):
            self.enemies.append(Enemy(self, chr(ord('A') + i), self.pick_free_pos(close_to=(size[0]//2,size[1]//2))))
            self.agents.append(self.enemies[-1])

    def __str__(self):
        maze_str = ""
        for y in range(self.height()):
            line = ''
            for x in range(self.width()):
                is_there_some_agent = False
                for agent in self.agents:
                    if agent.pos == [x,y]:
                        line += agent.symbol
                        is_there_some_agent = True
                        break
                if not is_there_some_agent:
                    line += self.maze[x,y]
            maze_str += line + '\n'
        return maze_str

    def check_end(self):
        if self.hero.pos == self.goal.pos or self.goal.pos in self.neighbours(self.hero.pos):
            print(f'Bravo, {self.hero.symbol} a gagné !')
            return True
        for enemy in self.enemies:
            if self.hero.pos == enemy.pos:
                print(f'Perdu, {self.hero.symbol} a été mangé par {enemy.symbol} !')
                return True
        return False

    def visitable(self, pos):
        x,y = pos
        is_in =  0 < x < self.width()-1 and 0 < y < self.height()-1 and self.maze[x,y] != '#'
        if not is_in: return False
        for agent in self.agents:
            if agent.pos == pos:
                return False
        return True

    def pick_free_pos(self, close_to=(1,1)):
        x,y = close_to
        def choices(n):
            if n==0: return [[x,y]]
            L = []
            for dx in [-n, n]:
                for dy in range(-n, n+1):
                    L.append([x + dx, y + dy])
            for dy in [-n, n]:
                for dx in range(-n+1, n):
                    L.append([x + dx, y + dy])
            return L
        d = 0
        while d < max(self.width(), self.height()):
            for pos in choices(d):
                if self.visitable(pos): return pos
            d += 1
        return None

    def width(self):
        return self.maze.shape[0]
    
    def height(self):
        return self.maze.shape[1]

    def generate_maze(self, size, sparsness=None):
        self.maze = np.full(size, '#')
        DIRS = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        def carve(x, y):
            self.maze[x,y] = ' '
            random.shuffle(DIRS)
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if 0 < nx < self.width()-1 and 0 < ny < self.height()-1 and self.maze[nx,ny] == '#':
                    self.maze[x + dx // 2, y + dy // 2] = ' ' 
                    carve(nx, ny)
        carve(1,1)
        # remove 1/n walls to get several paths
        if sparsness is not None:
            for i in range(1, size[0]-1):
                for j in range(1, size[1]-1):
                    if self.maze[i,j] == '#' and random.randint(0,sparsness-1) == 0:
                        self.maze[i,j] = ' ' 

        # add some obstables
        if obstacles:
            for i in range(1, size[0]-1):
                for j in range(1, size[1]-1):
                    if self.maze[i,j] == ' ': 
                        if random.randint(0, 3) == 0:
                            self.maze[i,j] = '.'

    def neighbours(self, pos):
        N = []
        for dx,dy in [ (0, 1), (1, 0), (0, -1), (-1, 0) ]:
            if self.visitable((pos[0] + dx, pos[1] + dy)):
                N.append([pos[0] + dx, pos[1] + dy])
        return N
    
    def flood(self, pos):
        accessible = [pos]
        modif = True
        while modif:
            modif = False
            for P in accessible:
                for N in self.neighbours(P):
                    if N not in accessible:
                        accessible.append(N)
                        modif = True
        return accessible

    def check_maze(self):
        return self.goal.pos in self.flood([1,1])

    def obstacle(self, pos):
        return self.maze[pos[0], pos[1]] == '.'

    def tick(self):
        for agent in self.agents:
            agent.tick()


if __name__ == "__main__":

    def doc():
        print("Vous pilotez O, votre but est d'atteindre X en évitant les méchants")

    game = Game(sparsness=maze_sparsness)
    alive = True

    def user_strat(agent):
        global alive
        move_key = input("Déplacement: (z/q/s/d) (x pour quitter): ")
        if move_key == 'z':
            return (0, -1)
        elif move_key == 'w':
            return (0, 1)
        elif move_key == 'q':
            return (-1, 0)
        elif move_key == 's':
            return (1, 0)
        elif move_key == 'x':
            alive = False
            return (0,0)
        else: return (0,0)

    if automatic_mode :
        game.hero.startegy = hero_strategy
    else:
        game.hero.startegy = user_strat

    print(game)
    while alive:
        print('-'*(game.width()+5))
        doc()
        game.tick()
        print()
        print(game)
        if game.check_end():
            break
        time.sleep(0.02)
    
    print('Fin du jeu.')
