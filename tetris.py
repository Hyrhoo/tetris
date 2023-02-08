# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:48:47 2022

@author: jojoj
"""
import random
try:import pygame
except ImportError: raise ImportError("""
>>> La bibliothèque pygame n'est pas installer sur votre ordinateur
Pour l'installer utilisez la commende "pip install pygame" dans une invite de commande""")
pygame.init()

reso = (650,500)
fenetre_de_jeu = pygame.display.set_mode(reso)
arial_font = pygame.font.SysFont('franklin gothic heavy', 25)
clock = pygame.time.Clock()

plateau = [[0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]

coul = {0:(54,57,63),
        1:(156,207,240),
        2:(31,122,196),
        3:(242,164,49),
        4:(203,105,206),
        5:(2,161,72),
        6:(198,54,43),
        7:(251,230,50)}

formes = [[[(-1,0),(0,0),(1,0),(2,0)],[(1,-1),(1,0),(1,1),(1,2)],[(-1,1),(0,1),(1,1),(2,1)],[(0,-1),(0,0),(0,1),(0,2)]],
          [[(0,0),(1,0),(2,0),(2,1)],[(1,-1),(1,0),(1,1),(0,1)],[(0,-1),(0,0),(1,0),(2,0)],[(1,-1),(2,-1),(1,0),(1,1)]],
          [[(0,0),(1,0),(2,0),(0,1)],[(0,-1),(1,-1),(1,0),(1,1)],[(0,0),(1,0),(2,0),(2,-1)],[(1,-1),(1,0),(1,1),(2,1)]],
          [[(0,0),(1,0),(2,0),(1,1)],[(1,0),(1,-1),(0,0),(1,1)],[(1,0),(0,0),(2,0),(1,-1)],[(1,0),(1,-1),(1,1),(2,0)]],
          [[(0,1),(1,1),(1,0),(2,0)],[(1,1),(1,0),(2,1),(2,2)],[(1,1),(2,1),(1,2),(0,2)],[(1,1),(1,2),(0,1),(0,0)]],
          [[(0,0),(1,0),(1,1),(2,1)],[(1,1),(2,0),(2,1),(1,2)],[(1,1),(0,1),(1,2),(2,2)],[(1,1),(1,0),(0,1),(0,2)]],
          [[(0,0),(0,1),(1,0),(1,1)],[(0,0),(0,1),(1,0),(1,1)],[(0,0),(0,1),(1,0),(1,1)],[(0,0),(0,1),(1,0),(1,1)]]]

dep = [[[(2,1),(-1,-2),(2,0),(-1,0),(0,0),
         (0,0),(-2,0),(1,0),(-2,1),(1,-2)],
        [(-1, 2),(2,-1),(-1,0),(2,0),(0,0),
         (0,0),(-1,0),(2,0),(-1,-2),(2,1)],
        [(-2,-1),(1,2),(-2,0),(1,0),(0,0),
         (0,0),(2,0),(-1,0),(2,-1),(-1,2)],
        [(1,-2),(-2,1),(1,0),(-2,0),(0,0),
         (0,0),(1,0),(-2,0),(1,2),(-2,-1)]],

       [[(-1,2),(0,1),(-1,-1),(-1,0),(0,0),
         (0,0),(1,0),(1,-1),(0,2),(1,2)],
        [(-1,-2),(0,-2),(-1,1),(-1,0),(0,0),
         (0,0),(-1,0),(-1,1),(0,-2),(-1,-2)],
        [(1,2),(0,2),(1,-1),(1,0),(0,0),
         (0,0),(-1,0),(-1,-1),(0,2),(-1,2)],
        [(1,-2),(0,-2),(1,1),(1,0),(0,0),
         (0,0),(-1,0),(1,1),(0,-2),(1,-2)]],

       [[(-1,2),(0,2),(-1,-1),(-1,0),(0,0),
         (0,0),(1,0),(1,-1),(0,2),(1,2)],
        [(-1,-2),(0,-2),(-1,1),(-1,0),(0,0),
         (0,0),(-1,0),(-1,1),(0,-2),(-1,-2)],
        [(1,2),(0,2),(1,-1),(1,0),(0,0),
         (0,0),(-1,0),(-1,-1),(0,2),(-1,2)],
        [(1,-2),(0,-2),(1,1),(1,0),(0,0),
         (0,0),(1,0),(1,1),(0,-2),(1,-2)]],

       [[(-1,2),(0,2),(-1,-1),(-1,0),(0,0),
         (0,0),(1,0),(1,-1),(0,2),(1,2)],
        [(-1,-2),(0,-2),(-1,1),(-1,0),(0,0),
         (0,0),(-1,0),(-1,1),(0,-2),(-1,-2)],
        [(1,2),(0,2),(1,-1),(1,0),(0,0),
         (0,0),(-1,0),(-1,-1),(0,2),(-1,2)],
        [(1,-2),(0,-2),(1,1),(1,0),(0,0),
         (0,0),(1,0),(1,1),(0,-2),(1,-2)]],

       [[(1,2),(0,2),(1,-1),(1,0),(0,0),
         (0,0),(-1,0),(-1,-1),(0,2),(-1,2)],
        [(1,-2),(0,-2),(1,1),(1,0),(0,0),
         (0,0),(1,0),(1,1),(0,-2),(1,-2)],
        [(-1,2),(0,2),(-1,-1),(-1,0),(0,0),
         (0,0),(1,0),(1,-1),(0,2),(1,2)],
        [(-1,-2),(0,-2),(-1,1),(-1,0),(0,0),
         (0,0),(-1,0),(-1,1),(0,-2),(-1,-2)]],

       [[(1,2),(0,2),(1,-1),(1,0),(0,0),
         (0,0),(-1,0),(-1,-1),(0,2),(-1,2)],
        [(1,-2),(0,-2),(1,1),(1,0),(0,0),
         (0,0),(1,0),(1,1),(0,-2),(1,-2)],
        [(-1,2),(0,2),(-1,-1),(-1,0),(0,0),
         (0,0),(1,0),(1,-1),(0,2),(1,2)],
        [(-1,-2),(0,-2),(-1,1),(-1,0),(0,0),
         (0,0),(-1,0),(-1,1),(0,-2),(-1,-2)]],

       [[(0,0),(0,0),(0,0),(0,0),(0,0),
         (0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(0,0),(0,0),
         (0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(0,0),(0,0),
         (0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(0,0),(0,0),
         (0,0),(0,0),(0,0),(0,0),(0,0)]]]

mauvaises_touche = [27,13,1073741881,1073742051,1073742086,1073741953,1073741952,
                    1073742051,1073742051,1073741898,1073741901,1073741899,
                    1073741902,1073741894,1073741896,
                    1073741897,127,1073741882,1073741883,1073741884,1073741885,
                    1073741886,1073741887,1073741888,1073741889,1073741890,
                    1073741891,1073741892,1073741893,8]

dico_touche = {1073741906:"up",
               1073741905:"down",
               1073741904:"left",
               1073741903:"right",
               1073742048:"ctrl",
               1073742050:"alt",
               1073742052:"ctrl",
               1073742054:"alt.gr",
               1073742049:"shift",
               1073742053:"shift",
               32:"espace",
               9:"tab"}

def lire_touche(nbr_touche):
    """
    lie les touches du ficier

    Parameters
    ----------
    nbr_touche : TYPE int
        nombre de touches a récupéré

    Returns
    -------
    touches : TYPE list
        une liste des douches constituer de tuple (code touche, unicode).

    """
    with open("touches.txt") as file_touches:
        touches = file_touches.readlines()
    touches = touches[:nbr_touche:]
    for i in range(len(touches)):
        touches[i] = touches[i].strip("\n")
        touches[i] = touches[i].split(",")
        touches[i][0] = int(touches[i][0])
    return touches

def changer_touche(touches):
    """
    The changer_touche function allows the player to change the keys used for 
    rotation, chute and movement. It also allows you to save your changes.
    
    :param touches: Store the list of touche used for the game
    :return: :
    :doc-author: Trelent
    """
    """
    permet de changer les touche utiliser pour jouer

    Parameters
    ----------
    touches : TYPE list
        liste des touches utiliser avent le changement avec tuple (key, unicod).

    Returns
    -------
    touches : TYPE list
        liste des touches utiliser après le changement avec tuple (key, unicod).

    """
    # affichage
    fenetre_de_jeu.fill((54,57,63))
    text_surface = arial_font.render("Rotation Horaire :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 40))
    text_surface = arial_font.render("Rotation Antihoraire :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 100))
    text_surface = arial_font.render("Chute Rapide :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 160))
    text_surface = arial_font.render("Chute Instantanée :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 220))
    text_surface = arial_font.render("Deplacement à Gauche :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 280))
    text_surface = arial_font.render("Deplacement à Droite :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 340))
    text_surface = arial_font.render("Mettre En Reserve :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 400))
    text_surface = arial_font.render("Echap Pour Quitter La Sélection De Touche", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 460))
    #   ffichage des touche
    for i in range(len(touches)):
        try:
            valeur = dico_touche[touches[i][0]]
        except KeyError:
            valeur = touches[i][1]
        text_surface = arial_font.render(valeur, True, (255,255,255),(54,57,63))
        fenetre_de_jeu.blit(text_surface, (400, 40+60*i))
    pygame.display.flip()
    defin_touche = True
    while defin_touche:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] in range(40,440):
                    # detection de la touche a changer + affichage du message de changement
                    text_surface = arial_font.render("appuyer sur une touche", True, (255,255,255),(54,57,63))
                    index = ((event.pos[1]-40)//60)
                    fenetre_de_jeu.blit(text_surface, (350, 40+60*index))
                    pygame.display.flip()
                    # changement de la touche
                    nouv_touche = None
                    while nouv_touche is None:
                        for touche in pygame.event.get():
                            if touche.type == pygame.KEYDOWN:
                                nouv_touche = [touche.key, touche.unicode]
                    # verificartion de la touche entrer
                    if nouv_touche[0] not in mauvaises_touche and nouv_touche not in touches:
                        touches[index] = nouv_touche
                    #re ecriture de la touche
                    rectangle = pygame.Rect(350, 40+60*index, 400, 30)
                    pygame.draw.rect(fenetre_de_jeu, (54,57,63), rectangle)
                    try:
                        valeur = dico_touche[touches[index][0]]
                    except KeyError:
                        valeur = touches[index][1]
                    text_surface = arial_font.render(valeur, True, (255,255,255),(54,57,63))
                    fenetre_de_jeu.blit(text_surface, (400, 40+60*index))
                    pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    defin_touche = False
    # sauvgarde des touche
    with open("touches.txt", "w") as file:
        for i in touches:
            file.write(str(i[0])+","+str(i[1])+"\n")
    return touches

def init_affichage(score, ligne, level, plateau):
    """
    The init_affichage function initializes the game window and draws all of the rectangles that make up the tetris board.
    
    Parameters: 
        score (int): The player's current score. 
    
        ligne (int): The number of lines cleared by a single tetromino in a row.
    
        level (
    
    :param score: Display the score
    :param ligne: Count the number of lines done
    :param level: Determine the speed of the game
    :param plateau: Display the tetrominos that have already been placed
    :return: None
    :doc-author: Trelent
    """
    """
    affichage de l'interface
    dessine tout les rectangles pour faire l'affichage du jeu tetris

    Parameters
    ----------
    score : TYPE int
        le score du joueur.
    ligne : TYPE int
        nombre de lignes effectuer.
    level : TYPE int
        le niveau attint lors de l'affichage.
    plateau : TYPE list
        le plateau de jeu dans lequel ce place les tetros déjà poser qui devras
        être afficher.

    Returns
    -------
    None.

    """
    #   affichge des rectengle
    fenetre_de_jeu.fill((0,0,0))
    # rectengle du plateau de jeu
    rectangle = pygame.Rect(200, 0, 250, 500)
    pygame.draw.rect(fenetre_de_jeu, (54,57,63), rectangle)
    # rectangle du background du score
    rectangle = pygame.Rect(20, 85, 160, 84)
    pygame.draw.rect(fenetre_de_jeu, (54,57,63), rectangle, 0, 10)
    # rectangle du background du level
    rectangle = pygame.Rect(20, 205, 160, 84)
    pygame.draw.rect(fenetre_de_jeu, (54,57,63), rectangle, 0, 10)
    # rectangle du background du nombre de lignes
    rectangle = pygame.Rect(20, 325, 160, 84)
    pygame.draw.rect(fenetre_de_jeu, (54,57,63), rectangle, 0, 10)
    # rectangle pour le background de la reserve
    rectangle = pygame.Rect(470, 180, 150, 300)
    pygame.draw.rect(fenetre_de_jeu, (54,57,63), rectangle, 0, 10)
    # rectangle pour le background des pieces suiventes
    rectangle = pygame.Rect(470, 45, 150, 120)
    # cadrillage du plateau
    pygame.draw.rect(fenetre_de_jeu, (54,57,63), rectangle, 0, 10)
    for i in range(10):
        pygame.draw.line(fenetre_de_jeu, (0,0,0), (200+i*25, 0), (200+i*25,500))
    for i in range(20):
        pygame.draw.line(fenetre_de_jeu, (0,0,0), (200, 0+i*25), (450,0+i*25))
    # affichage des textes
    # affichage score
    text_surface = arial_font.render("SCORE :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 97))
    text_surface = arial_font.render(str(score), True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 130))
    #affichage level
    text_surface = arial_font.render("LEVEL :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 217))
    text_surface = arial_font.render(str(level+1), True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 250))
    # affichage lignes
    text_surface = arial_font.render("LIGNES :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 337))
    text_surface = arial_font.render(str(ligne), True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (35, 370))
    # affichage du texte de la reserve
    text_surface = arial_font.render("RESERVE :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (485, 57))
    # affichage du texte pour les pièces suiventes
    text_surface = arial_font.render("SUIVANT :", True, (255,255,255),(54,57,63))
    fenetre_de_jeu.blit(text_surface, (485, 192))
    # affichage du contenue de la list plateau
    for y,i in enumerate(plateau):
        for x,j in enumerate(i):
            rectangle = pygame.Rect(201+25*x, -49+25*y, 24, 24)
            pygame.draw.rect(fenetre_de_jeu, coul[j], rectangle)
    pygame.display.flip()

def changer_couleur(couleur, opperation):
    """
    The changer_couleur function takes a color (r,g,b) and an operation as input.
    It returns the new color after applying the operation to each of its values.
    
    :param couleur: Store the color of the pixel
    :param opperation: Reduce the value of each color channel by a certain amount
    :return: :
    :doc-author: Trelent
    """
    """
    asombrie la couleur

    Parameters
    ----------
    couleur : TYPE tuple
        la couleur a assombrir (r,g,b).
    opperation : TYPE int
        le nombre par lequelle réduire les trois laveleur de la coueur.
        la valeur est réduite par l'opperation seulement si elle est a 255, 
        sinon c'est en fonction de la valeur qu'il manque pour arriver a 255

    Returns
    -------
    n_coul : TYPE tuple
        la couleur après le calcule (r,g,b).

    """
    n_coul = []
    for i in couleur:
        n_coul.append(int(round((i/255)*(255-opperation), 0)))
    return n_coul

def suppression_ligne(plateau):
    """
    The suppression_ligne function removes all full lines from the board.
    
    Parameters:
        plateau (list): The game board to remove lines from.
        
    Returns: 
        int: The number of removed lines.
    
    :param plateau: Store the game board
    :return: ?
    :doc-author: Trelent
    """
    """
    suprime une les ligne plaine du plateau

    Parameters
    ----------
    plateau : TYPE list
        le plaueat de jeu dans lequelle il y a toutes les piece déjà poser.

    Returns
    -------
    TYPE int
        le nombre de lignes suprimer.

    """
    pos_lignes = []
    # detection ligne plein
    for i in range(len(plateau)):
        plein = True
        for y in plateau[i]:
            if y == 0:
                plein = False
        if plein:
            pos_lignes.append(i)
    # annimation
    if pos_lignes != []:
        for i in range(4):
            # supression de l'afichage de la ligne
            for j in pos_lignes:
                for k in range(10):
                    rectangle = pygame.Rect(201 + 25*k, -49 + 25*j, 24, 24)
                    pygame.draw.rect(fenetre_de_jeu, (54,57,63), rectangle)
            pygame.display.flip()
            pygame.time.wait(100)
            # reaffichage de la ligne
            for j in pos_lignes:
                for k in range(10):
                    rectangle = pygame.Rect(201 + 25*k, -49 + 25*j, 24, 24)
                    pygame.draw.rect(fenetre_de_jeu, coul[plateau[j][k]], rectangle)
            pygame.display.flip()
            pygame.time.wait(100)
    # retrait lignes
    enleve = 0
    for i in pos_lignes:
        plateau.pop(i-enleve)
        enleve += 1
    # ajoue ligne vide
    for i in range(len(pos_lignes)):
        plateau.insert(0, [0,0,0,0,0,0,0,0,0,0])
    return len(pos_lignes)

class Tetros:
    """la pièce qui tombe"""
    sac_plein = [1,2,3,4,5,6,7]
    sac = []
    sac_sui = []
    reserve = None

    def __init__(self, type_piece = None):
        """
        initialise l'objet

        Parameters
        ----------
        type_piece : TYPE int, optional
            la piece que l'on soute créé non aléatoirement. The default is None.

        Returns
        -------
        None.

        """
        # initialisation de la pièce en fonction des pieces du tableau de suite aléatoir
        if type_piece is None:
            Tetros.reset_sac()
            self.type = Tetros.sac[0]
            Tetros.sac.pop(0)
        # initialisation non aléatoir
        else: self.type = type_piece
        #self.type = 4
        self.forme = formes[self.type-1][0]
        self.type_forme = 0
        self.pos = [4,2]

    def placer(self, pos = None):
        """
        affichage de la piece en coure

        Parameters
        ----------
        pos : TYPE tuple, optional
            la position a laquelle on souaite dessiner la piece.
            The default is None.

        Returns
        -------
        None.

        """
        # si position non indiquer on prand la position de la piece
        if pos is None: pos = self.pos
        # affichage pour tout les partie de la piece
        for i in self.forme:
            rectangle = pygame.Rect(201+25*(i[0]+pos[0]), -49+25*(i[1]+pos[1]), 24, 24)
            pygame.draw.rect(fenetre_de_jeu, coul[self.type], rectangle)
        pygame.display.flip()
    
    def dessendre(self, t0):
        """
        description

        Parameters
        ----------
        t0 : TYPE int
            le nombre de coup d'orloge récupéré depuis la dernière dessente de
            la piece (non colision).
        
        Returns
        -------
        col : TYPE bool
            True si la piece ne peut pas dessendre, sinon False.
        """
        self.pos[1] += 1
        col = self.detect_col()
        if col:
            self.pos[1] -= 1
            if t0 + 750 <= pygame.time.get_ticks():
                for i in self.forme:
                    plateau[i[1]+self.pos[1]][i[0]+self.pos[0]] = self.type
        return col
    
    def deplacement(self, dep):
        """
        The deplacement function moves the player in a given direction.
        The function takes one argument, dep, which is a list of two elements.
        The first element is the change in x position and the second element is 
        the change in y position.
        
        :param self: Access the attributes and methods of the class
        :param dep: Define the deplacement of the object
        :return: The new position of the object after a move
        :doc-author: Trelent
        """
        self.pos[0] += dep[0]
        self.pos[1] += dep[1]
        if self.detect_col():
            self.pos[0] -= dep[0]
            self.pos[1] -= dep[1]
    
    def rotation(self, sense):
        """
        The rotation function rotates the shape of the tetromino.
        It takes a sense argument, which is either 1 or -2.
        If sense = 1, then it rotates clockwise and if sense = -2, then it rotates counterclockwise.
        
        :param self: Access variables that belongs to the class
        :param sense: Rotate the shape clockwise or counterclockwise
        :return: The number of rotations to do so that the piece does not collide with a block
        :doc-author: Trelent
        """
        type_forme_base = self.type_forme
        pos_base = self.pos.copy()
        forme_base = self.forme.copy()
        self.type_forme += sense
        if self.type_forme > 3:
            self.type_forme = 0
        elif self.type_forme < 0:
            self.type_forme = 3
        self.forme = formes[self.type-1][self.type_forme]
        if sense == 1:
            deb, fin, pas = 5,None,None
        else:
            deb, fin, pas = 4,None,-1
        rota = 0
        #print("")
        #print("")
        #print(self.forme)
        #print(self.pos)
        #print("")
        for i in dep[self.type-1][type_forme_base][deb:fin:pas]:
            #print(i)
            rota += 1
            self.pos = [pos_base[0] + i[0], pos_base[1] + i[1]]
            col = self.detect_col(rotation=True)
            if not col:
                break
        if col:
            rota = 0
            self.forme = forme_base
            self.type_forme = type_forme_base
            self.pos = pos_base
        return rota

    def detect_col(self, pos = None, rotation = False):
        """
        The detect_col function checks if the piece is out of bounds or if it collides with another piece.
        It returns True if there is a collision and False otherwise.
        
        :param self: Refer to the object of the class
        :param pos=None: Indicate the position of the piece
        :param rotation=False: Prevent the rotation of the tetrimino when it is placed
        :return: A boolean value indicating whether the shape is colliding with a block or not
        :doc-author: Trelent
        """
        col = False
        case = []
        if pos is None:
            pos = self.pos
        for i in self.forme:
            case.append((i[1]+pos[1], i[0]+pos[0]))
            if (i[1]+pos[1]) not in range(len(plateau)) or (i[0]+pos[0]) not in range(len(plateau[1])):
                col = True
                break
            else:
                if plateau[i[1]+pos[1]][i[0]+pos[0]]:
                    col = True
                    break
        #if rotation: print(case)
        return col
    
    def detect_move(self, rotation, rota):
        """
        The detect_move function checks if the piece has move in a certain direction to detect a spesific move.
        It returns "T-spin" or "mini T-spin" (depending of the move) if it can, and "ligne" otherwise.
        
        :param self: Refer to the object of the class
        :param rotation: Check if the current tetrimino is rotating
        :param rota: Determine if the rotation is a valid one
        :return: A string that indicates the type of move
        :doc-author: Trelent
        """
        if self.type == 4 and rotation:
            if rota == 5: return "T-spin"
            try:
                if plateau[self.pos[1]+1][self.pos[0]] and plateau[self.pos[1]+1][self.pos[0]+2]:
                    if(plateau[self.pos[1]-1][self.pos[0]] or plateau[self.pos[1]-1][self.pos[0]+2]):
                        return "mini T-spin" if self.type_forme == 2 else "T-spin"
            except IndexError:
                try:
                    if plateau[self.pos[1]-1][self.pos[0]] or plateau[self.pos[1]-1][self.pos[0]+2]:
                        return "mini T-spin" if self.type_forme == 2 else "T-spin"
                except IndexError: 
                    return "ligne"
        return "ligne"

    def utilise_reserve(self):
        """
        The utilise_reserve function takes a Tetros object and places it in reserve.
        If the reserve is empty, then it will place the current Tetros object into reserve.
        If there is already a tetromino in reserve, then it will replace that tetromino with the current one and return to its original position.
        
        :param self: Refer to the object itself
        :return: The type of the reserve tetromino
        :doc-author: Trelent
        """
        if Tetros.reserve is None:
            Tetros.reserve = self.type
            self.__init__()
        else:
            tempo = self.type
            self.__init__(Tetros.reserve)
            Tetros.reserve = tempo
            del tempo
    
    def affiche_reserve(poser):
        """
        The affiche_reserve function displays the reserve of tetrominos.
            Parameters:
                poser (bool): True if a tetromino is being placed befor the last us of the reserve, False otherwise.
        
        
        :param poser: Know if the reserve is used to pose a tetromino or not
        :return: The reserve form
        :doc-author: Trelent
        """
        if Tetros.reserve is not None:
            for j in formes[Tetros.reserve-1][0]:
                rectangle = pygame.Rect(520+25*(j[0]), 90+25*(j[1]), 24, 24)
                pygame.draw.rect(fenetre_de_jeu, coul[Tetros.reserve] if poser else (75,75,75), rectangle)
    
    def affiche_suit():
        """
        The affiche_suit function displays the next four pieces that will be used in the game.
        The function takes no arguments and returns nothing.
        
        :return: The color of the suit
        :doc-author: Trelent
        """
        for i in range(4):
            for j in formes[Tetros.sac[i]-1][0]:
                rectangle = pygame.Rect(520+25*(j[0]), 225+25*(j[1])+60*i, 24, 24)
                pygame.draw.rect(fenetre_de_jeu, coul[Tetros.sac[i]], rectangle)
    
    def affiche_ombre(self):
        """
        The affiche_ombre function displays the shadow of the block.
        It takes as an argument a position and returns nothing.
        
        :param self: Refer to the object itself
        :return: False
        :doc-author: Trelent
        """
        pos = self.pos.copy()
        pos[1] -= 1
        col = False
        while not col:
            pos[1] += 1
            col = self.detect_col(pos)
        pos[1] -= 1
        #self.placer(pos, changer_couleur(coul[self.type], 100))
        for i in self.forme:
            rectangle = pygame.Rect(201+25*(i[0]+pos[0]), -49+25*(i[1]+pos[1]), 24, 24)
            pygame.draw.rect(fenetre_de_jeu, changer_couleur(coul[self.type], 130), rectangle)
        return pos
    
    def reset_sac(piece = None):
        """
        The reset_sac function takes a piece as an argument.
        If the sac_sui list is empty, it copies the sac_plein list and shuffles it.
        It then adds a new tetromino to the sac list and removes one from the sui list.
        
        :param piece=None: Make sure that the piece is not in the sac_sui list when it is added to the sac list
        :return: The piece that has been removed from the sac_sui list and added to the sac list
        :doc-author: Trelent
        """
        if len(Tetros.sac_sui) == 0:
            Tetros.sac_sui = Tetros.sac_plein.copy()
            random.shuffle(Tetros.sac_sui)
        Tetros.sac.append(Tetros.sac_sui[0])
        Tetros.sac_sui.pop(0)
        if piece is not None:
            Tetros.sac_sui = [piece,]*7
            Tetros.sac = [piece,]*7
    
    def reset(piece = None):
        """
        The reset function is used to reset the game. It is called when a new game starts or after a player loses.
        It shuffles the pieces in the reserve and sets Tetros.reserve to None, Tetros.sac_plein to [0, 1, 2, 3, 4 ,5 ,6]
        
        
        :param piece=None: Initialize the game
        :return: The list of pieces that are not used
        :doc-author: Trelent
        """
        Tetros.reserve = None
        Tetros.sac_plein = [1,2,3,4,5,6,7]
        Tetros.sac_sui = Tetros.sac_plein.copy()
        Tetros.sac = Tetros.sac_plein.copy()
        random.shuffle(Tetros.sac)
        random.shuffle(Tetros.sac_sui)
        if piece is not None:
            Tetros.sac_sui = [piece,]*7
            Tetros.sac = [piece,]*7

mot = {0:"",
       1:"simple",
       2:"double",
       3:"triple"}

def calculer_score(score, lignes, combo, B2B, move, level):
    """
    The calculer_score function takes in a score, the number of lines cleared,
    whether or not it was a B2B (back to back) tetris, the move that was made and
    the level. It then calculates how much points you got for clearing those lines.
    It also takes into account if you used up your combos
    
    :param score: Calculate the score of a move
    :param lignes: Calculate the score
    :param combo: Calculate the score
    :param B2B: Know if the last tetrimino was a back to back t-spin or mini t-spin or tetris
    :param move: Determine if the player has used a line clear, mini t-spin or t-spin
    :param level: Increase the speed of the game as it increases
    :return: The score of the move
    :doc-author: Trelent
    """
    if move is None:
        print("ATENTION, PORBLEME")
        move = "ligne"
    if move != "ligne": print(move, mot[lignes])
    if lignes == 4: print("tetris")
    if B2B: 
        if move != "ligne" or lignes == 4:
            print("back to back")
    if combo not in (0,1):
        print("combo :", combo)
    def score_ligne(lignes, B2B, level):
        point = [0,100,300,500,800]
        score = point[lignes] * (1.5 if lignes == 4 and B2B else 1)
        score *= (level+1)
        return score
    def score_mini_tspin(lignes, B2B, level):
        point = [100,200,400]
        score = point[lignes] * (1.5 if lignes == 2 and B2B else 1)
        score *= (level+1)
        return score
    def score_tspin(lignes, B2B, levle):
        point = [400,800,1200,1600]
        score = point[lignes] * (1.5 if lignes in (2,3) and B2B else 1)
        score *= (level+1)
        return score
    def score_all_clear(lignes):
        point = [0,800,1200,1800,2000]
        score = point[lignes]
        score *= (level+1)
        print("all clear")
        return score
    dic_fonc = {"ligne": score_ligne,
                "mini T-spin": score_mini_tspin,
                "T-spin": score_tspin}
    score += dic_fonc[move](lignes, B2B, level)
    if combo == 1:
        combo = 0
    score += 50*combo*(level+1)
    vide = True
    for i in plateau:
        for j in i:
            if j:
                vide = False
                break
    if vide: score += score_all_clear(lignes)
    score = int(round(score, 0))
    return score

def lancer_jeu(score, ligne, level):
    """
    The lancer_jeu function is the main function of the game. It is called by the main menu and contains all other functions.
    It initializes pygame, creates a window with a title, and calls all other functions to run the game.
    
    :param score: Display the score
    :param ligne: Determine the level of the game
    :param level: Determine the speed of the tetrominos
    :return: The score, the number of lines cleared and the current level
    :doc-author: Trelent
    """
    jouer = True
    t0 = pygame.time.get_ticks()
    t1 = pygame.time.get_ticks()
    t2 = pygame.time.get_ticks()
    t3 = pygame.time.get_ticks()
    att_dep, n_dep = 150, -1
    init_affichage(score, ligne, level, plateau)
    poser = True
    rotation = False
    Tetros.reset()
    combo = 0
    move = "ligne"
    lignes_sup = 0
    n_rota = 0
    while jouer:
        level = ligne // 10
        if level > 19:
            level = 20
        try: tetros
        except NameError: tetros = Tetros()
        pos_bas = tetros.affiche_ombre()
        tetros.placer()
        Tetros.affiche_suit()
        Tetros.affiche_reserve(poser)
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == 27:
                    jouer = False
                    del tetros
                    for i in range(len(plateau)):
                        for j in range(len(plateau[i])):
                            plateau[i][j] = 0
                    score, ligne, level = 0,0,0
                    init_affichage(score, ligne, level, plateau)
                elif e.key == res[0]:
                    if poser: 
                        tetros.utilise_reserve()
                        poser = False
                        init_affichage(score, ligne, level, plateau)
                        t0 = pygame.time.get_ticks()
                        t1 = pygame.time.get_ticks()
                        t2 = pygame.time.get_ticks()
                elif e.key == rot_h[0]:
                    n_rota = tetros.rotation(1)
                    init_affichage(score, ligne, level, plateau)
                    t2 = pygame.time.get_ticks()
                    rotation = True
                elif e.key == rot_a[0]:
                    n_rota = tetros.rotation(-1)
                    init_affichage(score, ligne, level, plateau)
                    t2 = pygame.time.get_ticks()
                    rotation = True
                elif e.key == haut[0] and t3 + 200 <= pygame.time.get_ticks():
                    if tetros.pos != pos_bas: rotation = False
                    score += (pos_bas[1] - tetros.pos[1]) * 2
                    tetros.pos = pos_bas
                    tetros.dessendre(-750)
                    init_affichage(score, ligne, level, plateau)
                    tetros.placer()
                    Tetros.affiche_suit()
                    Tetros.affiche_reserve(poser)
                    nouv_move = tetros.detect_move(rotation, n_rota)
                    del tetros
                    poser = True
                    nouv_lignes_sup = suppression_ligne(plateau)
                    if move == nouv_move and lignes_sup == nouv_lignes_sup:
                        B2B = True
                    else: B2B = False
                    lignes_sup, move = nouv_lignes_sup, nouv_move
                    ligne += lignes_sup
                    if lignes_sup: combo += 1
                    else: combo = 0
                    score = calculer_score(score, lignes_sup, combo, B2B, move, level)
                    init_affichage(score, ligne, level, plateau)
                    t0 = pygame.time.get_ticks()
                    t1 = pygame.time.get_ticks()
                    t2 = pygame.time.get_ticks()
                    t3 = pygame.time.get_ticks()
                    rotation = False
            if e.type == pygame.KEYUP:
                if e.key == bas[0]:
                    t0 = pygame.time.get_ticks()
        if pygame.key.get_pressed()[bas[0]]:
            att = 25
        else:
            att = 1000
            for i in range(level):
                att -= (att/100)*17
        att = int(round(att,0))
        if pygame.key.get_pressed()[droite[0]] and t1 + att_dep <= pygame.time.get_ticks():
            tetros.deplacement((1,0))
            init_affichage(score, ligne, level, plateau)
            t1 = pygame.time.get_ticks()
            n_dep += 1
            if n_dep:
                att_dep = 25
        elif pygame.key.get_pressed()[gauche[0]] and t1 + att_dep <= pygame.time.get_ticks():
            tetros.deplacement((-1,0))
            init_affichage(score, ligne, level, plateau)
            t1 = pygame.time.get_ticks()
            n_dep += 1
            if n_dep:
                att_dep = 25
        elif not pygame.key.get_pressed()[droite[0]] and not pygame.key.get_pressed()[gauche[0]]:
            att_dep, n_dep = int(round(((-((att-1000)**2))/8659)+200,0)), -1
            #att_dep, n_dep = int(round((((att-24)**2)/8659)+100,0)), -1
            #print(att_dep)
        if t0 + att <= pygame.time.get_ticks():
            col = tetros.dessendre(t2)
            if col:
                if t2 + 750 <= pygame.time.get_ticks():
                    nouv_move = tetros.detect_move(rotation, n_rota)
                    del tetros
                    poser = True
                    t0 = pygame.time.get_ticks()
                    t1 = pygame.time.get_ticks()
                    t2 = pygame.time.get_ticks()
                    t3 = pygame.time.get_ticks()
                    nouv_lignes_sup = suppression_ligne(plateau)
                    if move == nouv_move and lignes_sup == nouv_lignes_sup:
                        B2B = True
                    else: B2B = False
                    lignes_sup, move = nouv_lignes_sup, nouv_move
                    ligne += lignes_sup
                    if lignes_sup: combo += 1
                    else: combo = 0
                    rotation = False
                    score = calculer_score(score, lignes_sup, combo, B2B, move, level)
            else:
                rotation = False
                t2 = pygame.time.get_ticks()
                score += 1
            t0 = pygame.time.get_ticks()
            init_affichage(score, ligne, level, plateau)
        if plateau[1][4] or plateau[2][5] or plateau[2][6] or plateau[1][7]:
            jouer = False
            entrer = False
            while not entrer:
                for e in pygame.event.get(pygame.KEYDOWN):
                    if e.key == 27:
                        entrer = True
                        for i in range(len(plateau)):
                            for j in range(len(plateau[i])):
                                plateau[i][j] = 0
                        score, ligne, level = 0,0,0
                        init_affichage(score, ligne, level, plateau)
        #clock.tick(60)
            
rot_h, rot_a, bas, haut, gauche, droite, res = lire_touche(7)
score, ligne, level = 0,0,0
init_affichage(score, ligne, level, plateau)
lancer = True

while lancer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lancer = False
        if event.type == pygame.KEYDOWN:
            print(event)
            if event.key == 27:
                rot_h, rot_a, bas, haut, gauche, droite, res = changer_touche([rot_h, rot_a, bas, haut, gauche, droite, res])
                init_affichage(score, ligne, level, plateau)
            if event.key == 13:
                Tetros.reset_sac()
                lancer_jeu(score, ligne, level)
pygame.quit()
