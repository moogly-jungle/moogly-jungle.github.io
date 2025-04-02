# Un graphe est un ensemble de sommets et d'arêtes.
# Les arêtes sont non orientées, non multiples et étiquetées
# Les sommets peuvent être également étiquetés, mais c'est optionnel.
# On ne formalisera pas plus que ça 
class Graph:
    
    def __init__(self, sommets, aretes):
        self.sommets = sommets # les sommets peuvent être ce que l'on veut (entier, chaine de caractère..)
        self.aretes = aretes # les aretes sont des triplets (s1,w,s2) où s1 et s2 sont des sommets et
                             # w est un nombre
        self.label = {} # Les étiquettes optionnelles des sommets sous la forme de dictionnaire
        if not self.check_consistency(): # voir plus bas
            print('ATTENTION: le graphe n\'est pas consistent')

    def __str__(self):
        return 'SOMMETS: ' + str(self.sommets) + '\nARETES: ' + str(self.aretes)

    # dans la fonction suivante, labels est une liste de forme (s,l)
    # où s est un sommet et l est un label les labels sont optionnels
    def set_labels(self, labels):
        for (s,l) in labels:
            if not s in self.sommets: self.sommets.append(s)
            self.label[s] = l

    # ici, on assigne le même le même label à tous les sommets
    def set_all_labels(self, l):
        for s in self.sommets: self.label[s] = l

    # ici, on veut vérifier qu'un graphe est consistant. C'est à dire que
    # les étiquettes de sommets doivent être assignées à des sommets
    # existants, et que les arêtes doivent également parler de sommets
    # existants.
    # EXERCICE: implémentez cette fonction, en l'état, elle ne vérifie rien.
    def check_consistency(self):
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#       # < A VOUS DE JOUER >
       return True
#==============================================================================
    
    # retourne le poid d'une arete, ou bien None
    # s'il n'y a pas d'arete entre a et b
    def arete(self, a, b):
        for (s1,k,s2) in self.aretes:
            if (s1==a and s2==b) or (s1==b and s2==a): return k
        return None

    # EXERCICE: écrire le code de la fonction suivante qui retourne la
    # liste des voisins d'un sommet donné avec les poids associés sous
    # la forme [ ... (sommet, poid) ... ]
    def neighbours(self, a):
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#       # < A VOUS DE JOUER >
       pass
#==============================================================================
    
# Un exemple de graphe sans étiquette de sommet.
g1 = Graph(['a','b','c'], [('a', 1, 'b'), ('b', 2, 'c')])

# EXERCICE: dessinez ce graphe sur une feuille de papier

# EXECICE: écrire la fonction grid(n,m) qui construit et retourne un
# graphe en forme de grille rectangulaire de taille n x m
def grid(n,m):
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#   # < A VOUS DE JOUER >
   pass
#==============================================================================

# Par exemple, grid(3,2) produira le graphe suivant:
# Sommets: [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
# Aretes: [((1, 1), 1, (1, 2)), ((1, 1), 1, (2, 1)), ((1, 2), 1, (2, 2)), ((2, 1), 1, (2, 2)), ((2, 1), 1, (3, 1)), ((2, 2), 1, (3, 2)), ((3, 1), 1, (3, 2))]

# EXERCICE: testez votre méthode neighbours produite précédemment

# Deux sommets d'un graphe sont dit connecté s'il existe un chemin
# d'arêtes entre eux.
# EXERCICE: Ecrire une fonction connecte(g,s1,s2) qui dit s'il existe
# un chemin entre s1 et s2 dans g.

# Un graphe est connexe si toute paire de sommet peut être relié par un chemin d'arete.
# EXERCICE: écrire une fonction connexe(g) qui indique si un graphe est connexe ou non.
# (le graphe vide (sans sommet) sera par convention connexe.

# ALGORITHME DE DIJKSTRA
# Visionnez la vidéo explicative suivante: https://www.youtube.com/watch?v=rHylCtXtdNs

# EXERCICE: définir le graphe utilisé dans la vidéo.

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
g3 = None

# EXERCICE: écrire le code de la fonction suivante qui retourne un
# plus court chemin entre les sommets start et dest de g.

def dijkstra(g, start, dest):
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#   # < A VOUS DE JOUER >
   pass
#==============================================================================
print(dijkstra(grid(3,3), (1,1), (3,3)))
print(dijkstra(g3, 'A', 'G'))

# Algorithme A*
# Visionnez la vidéo suivante: https://www.youtube.com/watch?v=5RcAYMzT6jY&t=356s

# EXERCICE: définir le graphe utilisé dans la vidéo.

# EXERCICE: en utilisant dijkstra, écrire une stratégie pour résoudre le jeu 
# de la séance précédente.
# - à partir du labyrinthe, construisez un graphe, puis trouvez un plus court 
# chemin vers le 'X' est faite le suivre par le hero.

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
g4 = None

# EXERCICE: écrire le code de la fonction suivate qui implémente
# l'heuristique A* en produisant un chemin de start vers dest (où
# start et dest sont des sommets de g)
def AStar(g, start, dest):
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#   # < A VOUS DE JOUER >
   pass
#==============================================================================
print(AStar(g4, 'n0', 'n6'))    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
