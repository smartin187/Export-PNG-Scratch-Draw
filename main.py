"""
Ce module est le module principal de cette aplication.

Ce module contient :
- L'interface utilisateur
- Les fonction permettant d'analiser le fichier
- Les fonction permettant de générer l'image a l'aide des fonction d'analise

La structure d'un fichier Scratch Draw :
Plusieur formes :
 1 : un point
 2 : un cercle
 3 : un rectangle
 4 : un triangle
 5 : un carré

 Le 1 du point est suivi par des informations sur la couleur
   Le premier chiffre est le nombre de chiffres de la couleur. La couleur prend un nombre entre 1 et 15 chiffres.
   Si ce chiffre vaut 1, le chiffre suivant est la couleur
   Si ce chiffre vaut 2, les deux chiffres suivants sont la couleur
   Ensuite, on a la coordonnée x du point. D'abord, le chiffre précise la longueur de la coordonnée x. Par exemple, si le chiffre vaut 3, la coordonnée x fait 3 chiffres.
  La longueur de la coordonnée va de 1 à 3 maximum.
   Si ce chiffre vaut 1, le chiffre suivant est la coordonnée x ; si ce chiffre vaut 2, les deux chiffres suivants sont la coordonnée x ; si ce chiffre vaut 3, les trois chiffres suivants sont la coordonnée x.#   Ensuite, on a la coordonnée y du point. D'abord, le chiffre précise la longueur de la coordonnée y. Par exemple, si le chiffre vaut 3, la coordonnée y fait 3 chiffres.
   Ensuite, on a la coordonnée y du point. D'abord, le chiffre précise la longueur de la coordonnée y. Par exemple, si le chiffre vaut 3, la coordonnée y fait 3 chiffres.
   Si ce chiffre vaut 1, le chiffre suivant est la coordonnée y ; si ce chiffre vaut 2, les deux chiffres suivants sont la coordonnée y ; si ce chiffre vaut 3, les trois chiffres suivants sont la coordonnée y.
   Enfin, on a la taille du point. D'abord, le chiffre précise la longueur de la taille du point. La longueur de la taille va de 1 à 3 maximum (càd 999 en valeur).
Si ce chiffre vaut 1, le chiffre suivant est la taille du point ; si ce chiffre vaut 2, les deux chiffres suivants sont la taille du point ; si ce chiffre vaut 3, les trois chiffres suivants sont la taille du point.

Le fichier doit avoir tout son contenu sur une seule ligne

Un exemple d'un tel fichier image est :
1213340032032896000
J'ai donné l'extension .sdrw à ces fichiers
"""

import logging
from tkinter import filedialog
logging.basicConfig(level=logging.DEBUG)
from tkinter import *
from PIL import Image, ImageDraw, Image
import os
import platform
import subprocess
from couleur_scrach_draw import *
from infocmation_sur_élément import *


caractèrelecture = 0

# fonction pour le point :--------------------------------------------------------------------------------------
def tracer_point():
    """permet de tracer le point sur l'image, en fonction du dictonnaire information_sur_point"""
    logging.debug ("rentrer dans la fonction tracer_point")
    
    if information_sur_point["couleur"]=="1":
        couleur_temporaire_fond=baige
        logging.debug(couleur_temporaire_fond)

    elif information_sur_point["couleur"]=="2":
        couleur_temporaire_fond=jaune

    elif information_sur_point["couleur"]=="3":
        couleur_temporaire_fond=marron

    elif information_sur_point["couleur"]=="4":
        couleur_temporaire_fond=vert_clair
    
    elif information_sur_point["couleur"]=="5":
        couleur_temporaire_fond=vert_foncé
    
    elif information_sur_point["couleur"]=="6":
        couleur_temporaire_fond=bleu_clair
    
    elif information_sur_point["couleur"]=="7":
        couleur_temporaire_fond=bleu_foncé
    
    elif information_sur_point["couleur"]=="8":
        couleur_temporaire_fond=orange
    
    elif information_sur_point["couleur"]=="13":
        couleur_temporaire_fond=rouge
    
    elif information_sur_point["couleur"]=="10":
        couleur_temporaire_fond=girs_clair

    elif information_sur_point["couleur"]=="11":
        couleur_temporaire_fond=rose

    elif information_sur_point["couleur"]=="12":
        couleur_temporaire_fond=violet

    elif information_sur_point["couleur"]=="9":
        couleur_temporaire_fond=blanc
    
    elif information_sur_point["couleur"]=="14":
        couleur_temporaire_fond=noir
    
    elif information_sur_point["couleur"]=="15":
        couleur_temporaire_fond=gris_foncé
    
    elif information_sur_point["couleur"]=="16":
        couleur_temporaire_fond=transparence
    
    taille_temporaire=int(information_sur_point["taille"])

    logging.debug("taille temporaire"+str(taille_temporaire))

    position_de_départ=(round(int(information_sur_point["coord_x"])-taille_temporaire/2), round(int(information_sur_point["coord_y"])-taille_temporaire/2))

    position_finale=(round(int(information_sur_point["coord_x"])+taille_temporaire/2), round(int(information_sur_point["coord_y"])+taille_temporaire/2))

    epaiseur_du_bord=int((round((int(information_sur_point["taille"])/100*10), 0))/2)

    d.ellipse((position_de_départ, position_finale), fill=couleur_temporaire_fond)


def point(caractèrelecture: int):
    """permet de mettre dans le dictionaire information_sur_point toutes les donné pour tracer le point."""

    global annuler_ouverture
    
    logging.debug ("rentrer dans la fonction point")
    #logging.debug ("en entrée j'ai eu " + str(caractèrelecture))
    #logging.debug ("cela correspond à la valeur dans le fichier " + str(fichier[caractèrelecture]))
    
    #   couleur du point ----------------------------------------------------
    
    if fichier[caractèrelecture] == "1":
        caractèrelecture = caractèrelecture + 1
        information_sur_point["couleur"]= fichier[caractèrelecture]

    elif fichier[caractèrelecture] == "2":
        caractèrelecture = caractèrelecture + 1
        information_sur_point["couleur"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_point["couleur"] += fichier[caractèrelecture]

    else:
        print("erreur de structure pour le point, pour la couleur")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    #   position du point  ----------------------------------------------------

    #   position x :

    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_x"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_x"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_x"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_x"] += fichier[caractèrelecture]
    
    else:
        print("erreur de structure pour le point, pour la position x")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    #   position y :

    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_y"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_y"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_y"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_point["coord_y"] += fichier[caractèrelecture]
    
    else:
        logging.debug("caractère avec problème : " + str(caractèrelecture))
        print("erreur de structure pour le point, pour la position y")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    # taille du point --------------------------------------------
    
    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_point["taille"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_point["taille"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_point["taille"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_point["taille"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_point["taille"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_point["taille"] += fichier[caractèrelecture]
    else:

        print("erreur de structure pour le point, pour la taille")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture


    logging.debug("point de couleur " + information_sur_point["couleur"])

    logging.debug("dicionaire infocmation sur point " + str(information_sur_point))

    return caractèrelecture
    

# fonction pour le cercle :--------------------------------------------------------------------------------------

def tracer_cercle():
    """permet de tracer le cercle avec le dicionaire infocmation_sur_cercle"""

    logging.debug("entrer dans la fonction tracer_cercle")

    if information_sur_cercle["couleur fond"]=="1":
        couleur_temporaire_fond=baige
        logging.debug(couleur_temporaire_fond)

    elif information_sur_cercle["couleur fond"]=="2":
        couleur_temporaire_fond=jaune

    elif information_sur_cercle["couleur fond"]=="3":
        couleur_temporaire_fond=marron

    elif information_sur_cercle["couleur fond"]=="4":
        couleur_temporaire_fond=vert_clair
    
    elif information_sur_cercle["couleur fond"]=="5":
        couleur_temporaire_fond=vert_foncé
    
    elif information_sur_cercle["couleur fond"]=="6":
        couleur_temporaire_fond=bleu_clair
    
    elif information_sur_cercle["couleur fond"]=="7":
        couleur_temporaire_fond=bleu_foncé
    
    elif information_sur_cercle["couleur fond"]=="8":
        couleur_temporaire_fond=orange
    
    elif information_sur_cercle["couleur fond"]=="13":
        couleur_temporaire_fond=rouge
    
    elif information_sur_cercle["couleur fond"]=="10":
        couleur_temporaire_fond=girs_clair

    elif information_sur_cercle["couleur fond"]=="11":
        couleur_temporaire_fond=rose

    elif information_sur_cercle["couleur fond"]=="12":
        couleur_temporaire_fond=violet

    elif information_sur_cercle["couleur fond"]=="9":
        couleur_temporaire_fond=blanc
    
    elif information_sur_cercle["couleur fond"]=="14":
        couleur_temporaire_fond=noir
    
    elif information_sur_cercle["couleur fond"]=="15":
        couleur_temporaire_fond=gris_foncé
    
    elif information_sur_cercle["couleur fond"]=="16":
        couleur_temporaire_fond=transparence

    #       2. contour
    if information_sur_cercle["couleur contour"]=="1":
        couleur_temporaire_contour=baige
        logging.debug(couleur_temporaire_contour)

    elif information_sur_cercle["couleur contour"]=="2":
        couleur_temporaire_contour=jaune

    elif information_sur_cercle["couleur contour"]=="3":
        couleur_temporaire_contour=marron

    elif information_sur_cercle["couleur contour"]=="4":
        couleur_temporaire_contour=vert_clair
    
    elif information_sur_cercle["couleur contour"]=="5":
        couleur_temporaire_contour=vert_foncé
    
    elif information_sur_cercle["couleur contour"]=="6":
        couleur_temporaire_contour=bleu_clair
    
    elif information_sur_cercle["couleur contour"]=="7":
        couleur_temporaire_contour=bleu_foncé
    
    elif information_sur_cercle["couleur contour"]=="8":
        couleur_temporaire_contour=orange
    
    elif information_sur_cercle["couleur contour"]=="13":
        couleur_temporaire_contour=rouge
    
    elif information_sur_cercle["couleur contour"]=="10":
        couleur_temporaire_contour=girs_clair

    elif information_sur_cercle["couleur contour"]=="11":
        couleur_temporaire_contour=rose

    elif information_sur_cercle["couleur contour"]=="12":
        couleur_temporaire_contour=violet

    elif information_sur_cercle["couleur contour"]=="9":
        couleur_temporaire_contour=blanc
    
    elif information_sur_cercle["couleur contour"]=="14":
        couleur_temporaire_contour=noir
    
    elif information_sur_cercle["couleur contour"]=="15":
        couleur_temporaire_contour=gris_foncé
    
    elif information_sur_cercle["couleur contour"]=="16":
        couleur_temporaire_contour=transparence

    taille_temporaire=int(round(91*int(information_sur_cercle["taille"])/100))

    logging.debug("taille temporaire"+str(taille_temporaire))

    position_de_départ=(round(int(information_sur_cercle["coord_x"])-taille_temporaire/2), round(int(information_sur_cercle["coord_y"])-taille_temporaire/2))

    position_finale=(round(int(information_sur_cercle["coord_x"])+taille_temporaire/2), round(int(information_sur_cercle["coord_y"])+taille_temporaire/2))

    epaiseur_du_bord=int((round((int(information_sur_cercle["taille"])/100*10), 0))/2)

    d_forme.ellipse((position_de_départ, position_finale), fill=couleur_temporaire_fond, outline=couleur_temporaire_contour, width=epaiseur_du_bord)

def cercle (caractèrelecture: int):
    
    """permet de mettre dans le dictionaire information_sur_cercle toutes les donné pour tracer le cercle."""

    global annuler_ouverture

    logging.debug("entrer dans la fonction cercle")

    # couleur du fond ---------------

    if fichier[caractèrelecture] == "1":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["couleur fond"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["couleur fond"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["couleur fond"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le cercle, pour la couleur du fond")

        print("erreur de structure pour le cercle, pour la couleur du fond")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    # couleur du contoure --------------
    
    caractèrelecture = caractèrelecture + 1

    if fichier[caractèrelecture] == "1":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["couleur contour"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["couleur contour"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["couleur contour"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le cercle, pour la couleur du contoure")
        print("erreur de structure pour le cercle, pour la couleur du contoure")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    

    #   position x :

    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_x"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_x"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_x"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_x"] += fichier[caractèrelecture]
    
    else:
        #logging.debug ("erreur de structure pour le cercle, pour position x")
        
        print("erreur de structure pour le cercle, pour la position x")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    #   position y :

    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_y"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_y"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_y"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["coord_y"] += fichier[caractèrelecture]
    
    else:
        #logging.debug ("erreur de structure pour le cercle, pour position y")
        print("erreur de structure pour le cercle, pour la position y")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture

        # taille du cercle --------------------------------------------
    
    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["taille"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["taille"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["taille"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["taille"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["taille"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_cercle["taille"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le cercle, pour la taille")
        print("erreur de structure pour le cercle, pour la taille")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture



    logging.debug("dicionaire infocmation sur cercle " + str(information_sur_cercle))

    return caractèrelecture


# fonction pour le recrtangle :     --------------------------------------------------------------------------------------

def tracer_rectangle():
    """permet de tracer le rectangle avec le dicionaire infocmation_sur_rectangle"""

    #   couleur de la forme :
    #      1. fond
    if information_sur_rectangle["couleur fond"]=="1":
        couleur_temporaire_fond=baige
        logging.debug(couleur_temporaire_fond)

    elif information_sur_rectangle["couleur fond"]=="2":
        couleur_temporaire_fond=jaune

    elif information_sur_rectangle["couleur fond"]=="3":
        couleur_temporaire_fond=marron

    elif information_sur_rectangle["couleur fond"]=="4":
        couleur_temporaire_fond=vert_clair
    
    elif information_sur_rectangle["couleur fond"]=="5":
        couleur_temporaire_fond=vert_foncé
    
    elif information_sur_rectangle["couleur fond"]=="6":
        couleur_temporaire_fond=bleu_clair
    
    elif information_sur_rectangle["couleur fond"]=="7":
        couleur_temporaire_fond=bleu_foncé
    
    elif information_sur_rectangle["couleur fond"]=="8":
        couleur_temporaire_fond=orange
    
    elif information_sur_rectangle["couleur fond"]=="13":
        couleur_temporaire_fond=rouge
    
    elif information_sur_rectangle["couleur fond"]=="10":
        couleur_temporaire_fond=girs_clair

    elif information_sur_rectangle["couleur fond"]=="11":
        couleur_temporaire_fond=rose

    elif information_sur_rectangle["couleur fond"]=="12":
        couleur_temporaire_fond=violet

    elif information_sur_rectangle["couleur fond"]=="9":
        couleur_temporaire_fond=blanc
    
    elif information_sur_rectangle["couleur fond"]=="14":
        couleur_temporaire_fond=noir
    
    elif information_sur_rectangle["couleur fond"]=="15":
        couleur_temporaire_fond=gris_foncé
    
    elif information_sur_rectangle["couleur fond"]=="16":
        couleur_temporaire_fond=transparence

    #       2. contour
    if information_sur_rectangle["couleur contour"]=="1":
        couleur_temporaire_contour=baige
        logging.debug(couleur_temporaire_contour)

    elif information_sur_rectangle["couleur contour"]=="2":
        couleur_temporaire_contour=jaune

    elif information_sur_rectangle["couleur contour"]=="3":
        couleur_temporaire_contour=marron

    elif information_sur_rectangle["couleur contour"]=="4":
        couleur_temporaire_contour=vert_clair
    
    elif information_sur_rectangle["couleur contour"]=="5":
        couleur_temporaire_contour=vert_foncé
    
    elif information_sur_rectangle["couleur contour"]=="6":
        couleur_temporaire_contour=bleu_clair
    
    elif information_sur_rectangle["couleur contour"]=="7":
        couleur_temporaire_contour=bleu_foncé
    
    elif information_sur_rectangle["couleur contour"]=="8":
        couleur_temporaire_contour=orange
    
    elif information_sur_rectangle["couleur contour"]=="13":
        couleur_temporaire_contour=rouge
    
    elif information_sur_rectangle["couleur contour"]=="10":
        couleur_temporaire_contour=girs_clair

    elif information_sur_rectangle["couleur contour"]=="11":
        couleur_temporaire_contour=rose

    elif information_sur_rectangle["couleur contour"]=="12":
        couleur_temporaire_contour=violet

    elif information_sur_rectangle["couleur contour"]=="9":
        couleur_temporaire_contour=blanc
    
    elif information_sur_rectangle["couleur contour"]=="14":
        couleur_temporaire_contour=noir
    
    elif information_sur_rectangle["couleur contour"]=="15":
        couleur_temporaire_contour=gris_foncé
    
    elif information_sur_rectangle["couleur contour"]=="16":
        couleur_temporaire_contour=transparence
    
    # fin detection de la couleur

    tailletemporaire_hauteur=int(round(((226*(int(information_sur_rectangle["taille"]))/100)/2), 0))             #convertion du % de la forme en pixel
    tailletemporaire_largeur=int(round(((372*(int(information_sur_rectangle["taille"]))/100)/2), 0))

    
    #   convertion des mesure scratch draw pour la coordonée utiliser par PIL
    position_de_départ=(int(information_sur_rectangle["coord_x"]) - tailletemporaire_largeur/2, (int(information_sur_rectangle["coord_y"]) - tailletemporaire_hauteur/2))

    position_final=(int(information_sur_rectangle["coord_x"]) + tailletemporaire_largeur/2, int(information_sur_rectangle["coord_y"]) + tailletemporaire_hauteur/2)

    epaiseur_du_bord=int(round((int(information_sur_rectangle["taille"])/100*5), 0))

    logging.debug("position_de_départ")
    logging.debug(position_de_départ)

    logging.debug("position_final")
    logging.debug(position_final)

    d_forme.rectangle([position_de_départ, position_final], fill=couleur_temporaire_fond, outline=couleur_temporaire_contour, width=epaiseur_du_bord)
    


def rectangle(caractèrelecture: int):
    """permet de mettre dans le dictionaire information_sur_rectangle toutes les donné pour tracer le rectangle."""

    global annuler_ouverture

    logging.debug("entrer dans la fonction rectangle")

    # couleur du fond ---------------

    if fichier[caractèrelecture] == "1":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["couleur fond"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["couleur fond"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["couleur fond"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le rectangle, pour la couleur du fond")
        print("erreur de structure pour le rectangle, pour la couleur du fond")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    # couleur du contoure --------------
    
    caractèrelecture = caractèrelecture + 1

    if fichier[caractèrelecture] == "1":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["couleur contour"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["couleur contour"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["couleur contour"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le rectangle, pour la couleur du contour")
        print("erreur de structure pour le rectangle, pour la couleur du contour")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    

        #   position x :

    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_x"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_x"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_x"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_x"] += fichier[caractèrelecture]
    
    else:
        # logging.debug ("erreur de structure pour le rectangle, pour position x")
        print("erreur de structure pour le rectangle, pour la position x")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    #   position y :

    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_y"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_y"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_y"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["coord_y"] += fichier[caractèrelecture]
    
    else:
        # logging.debug ("erreur de structure pour le rectangle, pour position y")
        print("erreur de structure pour le rectangle, pour la position y")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture

    # taille du rectangle    --------------------------------------------
    
    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["taille"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["taille"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["taille"] += fichier[caractèrelecture]

    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["taille"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["taille"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_rectangle["taille"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le rectangle, pour la taille")
        print("erreur de structure pour le rectangle, pour la taille")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture



    logging.debug("dicionaire infocmation sur rectangle " + str(information_sur_rectangle))


    return caractèrelecture

def tracer_triangle():
    """permet de tracer le triangle avec le dicionaire infocmation_sur_triangle"""

    logging.debug("rentré dans la fonction cracer_triangle")

        #   couleur de la forme :
    #      1. fond
    if information_sur_triangle["couleur fond"]=="1":
        couleur_temporaire_fond=baige
        logging.debug(couleur_temporaire_fond)

    elif information_sur_triangle["couleur fond"]=="2":
        couleur_temporaire_fond=jaune

    elif information_sur_triangle["couleur fond"]=="3":
        couleur_temporaire_fond=marron

    elif information_sur_triangle["couleur fond"]=="4":
        couleur_temporaire_fond=vert_clair
    
    elif information_sur_triangle["couleur fond"]=="5":
        couleur_temporaire_fond=vert_foncé
    
    elif information_sur_triangle["couleur fond"]=="6":
        couleur_temporaire_fond=bleu_clair
    
    elif information_sur_triangle["couleur fond"]=="7":
        couleur_temporaire_fond=bleu_foncé
    
    elif information_sur_triangle["couleur fond"]=="8":
        couleur_temporaire_fond=orange
    
    elif information_sur_triangle["couleur fond"]=="13":
        couleur_temporaire_fond=rouge
    
    elif information_sur_triangle["couleur fond"]=="10":
        couleur_temporaire_fond=girs_clair

    elif information_sur_triangle["couleur fond"]=="11":
        couleur_temporaire_fond=rose

    elif information_sur_triangle["couleur fond"]=="12":
        couleur_temporaire_fond=violet

    elif information_sur_triangle["couleur fond"]=="9":
        couleur_temporaire_fond=blanc
    
    elif information_sur_triangle["couleur fond"]=="14":
        couleur_temporaire_fond=noir
    
    elif information_sur_triangle["couleur fond"]=="15":
        couleur_temporaire_fond=gris_foncé
    
    elif information_sur_triangle["couleur fond"]=="16":
        couleur_temporaire_fond=transparence

    #       2. contour
    if information_sur_triangle["couleur contour"]=="1":
        couleur_temporaire_contour=baige
        logging.debug(couleur_temporaire_contour)

    elif information_sur_triangle["couleur contour"]=="2":
        couleur_temporaire_contour=jaune

    elif information_sur_triangle["couleur contour"]=="3":
        couleur_temporaire_contour=marron

    elif information_sur_triangle["couleur contour"]=="4":
        couleur_temporaire_contour=vert_clair
    
    elif information_sur_triangle["couleur contour"]=="5":
        couleur_temporaire_contour=vert_foncé
    
    elif information_sur_triangle["couleur contour"]=="6":
        couleur_temporaire_contour=bleu_clair
    
    elif information_sur_triangle["couleur contour"]=="7":
        couleur_temporaire_contour=bleu_foncé
    
    elif information_sur_triangle["couleur contour"]=="8":
        couleur_temporaire_contour=orange
    
    elif information_sur_triangle["couleur contour"]=="13":
        couleur_temporaire_contour=rouge
    
    elif information_sur_triangle["couleur contour"]=="10":
        couleur_temporaire_contour=girs_clair

    elif information_sur_triangle["couleur contour"]=="11":
        couleur_temporaire_contour=rose

    elif information_sur_triangle["couleur contour"]=="12":
        couleur_temporaire_contour=violet

    elif information_sur_triangle["couleur contour"]=="9":
        couleur_temporaire_contour=blanc
    
    elif information_sur_triangle["couleur contour"]=="14":
        couleur_temporaire_contour=noir
    
    elif information_sur_triangle["couleur contour"]=="15":
        couleur_temporaire_contour=gris_foncé
    
    elif information_sur_triangle["couleur contour"]=="16":
        couleur_temporaire_contour=transparence

    auteur_somet=round(32/100*int(information_sur_triangle["taille"]))
    auteur_inferieur=round(51/100*int(information_sur_triangle["taille"]))
    demi_largeur=round(84.5/100*int(information_sur_triangle["taille"]))

    

    epaiseur_du_bord=round((15/100*int(information_sur_triangle["taille"]))/2)
    
    #localisation des plusieur point :
    points=[
        (int(information_sur_triangle["coord_x"]), int(information_sur_triangle["coord_y"])+auteur_somet),
        (int(information_sur_triangle["coord_x"])-demi_largeur, int(information_sur_triangle["coord_y"])-auteur_inferieur),
        (int(information_sur_triangle["coord_x"])+demi_largeur, int(information_sur_triangle["coord_y"])-auteur_inferieur)
        ]
    
    d_forme.polygon(points, fill=couleur_temporaire_fond, outline=couleur_temporaire_contour, width=epaiseur_du_bord)
    


def triangle(caractèrelecture: int):
    """permet de mettre dans le dictionaire information_sur_triangle toutes les donné pour tracer le triangle."""

    global annuler_ouverture

    logging.debug("entrer dans la fonction triangle")

    # couleur du fond ---------------

    if fichier[caractèrelecture] == "1":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["couleur fond"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["couleur fond"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["couleur fond"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le triangle, pour la couleur du fond")
        print("erreur de structure pour le triangle, pour la couleur du fond")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    # couleur du contoure --------------
    
    caractèrelecture = caractèrelecture + 1

    if fichier[caractèrelecture] == "1":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["couleur contour"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["couleur contour"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["couleur contour"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le triangle, pour la couleur du contoure")
        print("erreur de structure pour le triangle, pour la couleur du contoure")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    

        #   position x :

    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_x"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_x"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_x"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_x"] += fichier[caractèrelecture]
    
    else:
        # logging.debug ("erreur de structure pour le triangle, pour position x")
        print("erreur de structure pour le triangle, pour la position x")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    #   position y :

    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_y"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_y"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_y"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["coord_y"] += fichier[caractèrelecture]
    
    else:
        # logging.debug ("erreur de structure pour le triangle, pour position y")
        print("erreur de structure pour le triangle, pour la position y")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture

    # taille du triangle    --------------------------------------------
    
    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["taille"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["taille"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["taille"] += fichier[caractèrelecture]

    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["taille"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["taille"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_triangle["taille"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le triangle, pour la taille")
        print("erreur de structure pour le triangle, pour la taille")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture



    logging.debug("dicionaire infocmation sur triangle " + str(information_sur_triangle))


    return caractèrelecture

def tracer_carré():
    """permet de tracer le carré avec le dicionaire infocmation_sur_carré"""

    logging.debug("entrer dans la fonction tracer_carré")
    
    
    logging.debug("ligne suivant : information_sur_carré taille")
    logging.debug(information_sur_carré["taille"])

        #   couleur de la forme :
    #      1. fond
    if information_sur_carré["couleur fond"]=="1":
        couleur_temporaire_fond=baige
        logging.debug(couleur_temporaire_fond)

    elif information_sur_carré["couleur fond"]=="2":
        couleur_temporaire_fond=jaune

    elif information_sur_carré["couleur fond"]=="3":
        couleur_temporaire_fond=marron

    elif information_sur_carré["couleur fond"]=="4":
        couleur_temporaire_fond=vert_clair
    
    elif information_sur_carré["couleur fond"]=="5":
        couleur_temporaire_fond=vert_foncé
    
    elif information_sur_carré["couleur fond"]=="6":
        couleur_temporaire_fond=bleu_clair
    
    elif information_sur_carré["couleur fond"]=="7":
        couleur_temporaire_fond=bleu_foncé
    
    elif information_sur_carré["couleur fond"]=="8":
        couleur_temporaire_fond=orange
    
    elif information_sur_carré["couleur fond"]=="13":
        couleur_temporaire_fond=rouge
    
    elif information_sur_carré["couleur fond"]=="10":
        couleur_temporaire_fond=girs_clair

    elif information_sur_carré["couleur fond"]=="11":
        couleur_temporaire_fond=rose

    elif information_sur_carré["couleur fond"]=="12":
        couleur_temporaire_fond=violet

    elif information_sur_carré["couleur fond"]=="9":
        couleur_temporaire_fond=blanc
    
    elif information_sur_carré["couleur fond"]=="14":
        couleur_temporaire_fond=noir
    
    elif information_sur_carré["couleur fond"]=="15":
        couleur_temporaire_fond=gris_foncé
    
    elif information_sur_carré["couleur fond"]=="16":
        couleur_temporaire_fond=transparence

    #       2. contour
    if information_sur_carré["couleur contour"]=="1":
        couleur_temporaire_contour=baige
        logging.debug(couleur_temporaire_contour)

    elif information_sur_carré["couleur contour"]=="2":
        couleur_temporaire_contour=jaune

    elif information_sur_carré["couleur contour"]=="3":
        couleur_temporaire_contour=marron

    elif information_sur_carré["couleur contour"]=="4":
        couleur_temporaire_contour=vert_clair
    
    elif information_sur_carré["couleur contour"]=="5":
        couleur_temporaire_contour=vert_foncé
    
    elif information_sur_carré["couleur contour"]=="6":
        couleur_temporaire_contour=bleu_clair
    
    elif information_sur_carré["couleur contour"]=="7":
        couleur_temporaire_contour=bleu_foncé
    
    elif information_sur_carré["couleur contour"]=="8":
        couleur_temporaire_contour=orange
    
    elif information_sur_carré["couleur contour"]=="13":
        couleur_temporaire_contour=rouge
    
    elif information_sur_carré["couleur contour"]=="10":
        couleur_temporaire_contour=girs_clair

    elif information_sur_carré["couleur contour"]=="11":
        couleur_temporaire_contour=rose

    elif information_sur_carré["couleur contour"]=="12":
        couleur_temporaire_contour=violet

    elif information_sur_carré["couleur contour"]=="9":
        couleur_temporaire_contour=blanc
    
    elif information_sur_carré["couleur contour"]=="14":
        couleur_temporaire_contour=noir
    
    elif information_sur_carré["couleur contour"]=="15":
        couleur_temporaire_contour=gris_foncé
    
    elif information_sur_carré["couleur contour"]=="16":
        couleur_temporaire_contour=transparence
    
    # fin detection de la couleur

    tailletemporaire=int(round((((206*int(information_sur_carré["taille"]))/100)/2), 0))           #convertion du % de la forme en pixel

    logging.debug("taille temporaire :")
    logging.debug(tailletemporaire)

    #   convertion des mesure scratch draw pour la coordonée utiliser par PIL
    position_de_départ=(int(information_sur_carré["coord_x"]) - tailletemporaire/2, (int(information_sur_carré["coord_y"]) - tailletemporaire/2))

    position_final=(int(information_sur_carré["coord_x"]) + tailletemporaire/2, int(information_sur_carré["coord_y"]) + tailletemporaire/2)

    epaiseur_du_bord=int(round((int(information_sur_carré["taille"])/100*10), 0))

    logging.debug("position_de_départ")
    logging.debug(position_de_départ)

    logging.debug("position_final")
    logging.debug(position_final)

    d_forme.rectangle([position_de_départ, position_final], fill=couleur_temporaire_fond, outline=couleur_temporaire_contour, width=epaiseur_du_bord)


def carré(caractèrelecture: int):
    """permet de mettre dans le dictionaire information_sur_carré toutes les donné pour tracer le carré."""

    global annuler_ouverture

    logging.debug("entrer dans la fonction carré")

    # couleur du fond ---------------

    if fichier[caractèrelecture] == "1":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_carré["couleur fond"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_carré["couleur fond"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["couleur fond"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le carré, pour la couleur du fond")
        print("erreur de structure pour le carré, pour la couleur du fond")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    # couleur du contoure --------------
    
    caractèrelecture = caractèrelecture + 1

    if fichier[caractèrelecture] == "1":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_carré["couleur contour"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_carré["couleur contour"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["couleur contour"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le carré, pour la couleur du contour")
        print("erreur de structure pour le carré, pour la couleur du contour")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    

        #   position x :

    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_x"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_x"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_x"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_x"] += fichier[caractèrelecture]
    
    else:
        # logging.debug ("erreur de structure pour le carré, pour position x")
        print("erreur de structure pour le carré, pour la position x")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    #   position y :

    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_y"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_y"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_y"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["coord_y"] += fichier[caractèrelecture]
    
    else:
        # logging.debug ("erreur de structure pour le carré, pour position y")
        print("erreur de structure pour le carré, pour la position y")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture

    # taille du carré    --------------------------------------------
    
    caractèrelecture = caractèrelecture + 1
    
    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["taille"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["taille"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["taille"] += fichier[caractèrelecture]

    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["taille"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["taille"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_carré["taille"] += fichier[caractèrelecture]
    else:
        #raise Exception("erreur de structure pour le carré, pour la taille")
        print("erreur de structure pour le carré, pour la taille")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    logging.debug("dicionaire infocmation sur carré " + str(information_sur_carré))

    return caractèrelecture


def tracer_remplisage():
    """permet de tracer le remplisage avec le dicionaire information sur remplisage"""          # ajouter la couleur
    logging.debug("rentrer dans la fonction tracer_remplisage")

    if information_sur_remplisage["couleur"]=="1":
        couleur_temporaire_contour=baige
        logging.debug(couleur_temporaire_contour)

    elif information_sur_remplisage["couleur"]=="2":
        couleur_temporaire_contour=jaune

    elif information_sur_remplisage["couleur"]=="3":
        couleur_temporaire_contour=marron

    elif information_sur_remplisage["couleur"]=="4":
        couleur_temporaire_contour=vert_clair
    
    elif information_sur_remplisage["couleur"]=="5":
        couleur_temporaire_contour=vert_foncé
    
    elif information_sur_remplisage["couleur"]=="6":
        couleur_temporaire_contour=bleu_clair
    
    elif information_sur_remplisage["couleur"]=="7":
        couleur_temporaire_contour=bleu_foncé
    
    elif information_sur_remplisage["couleur"]=="8":
        couleur_temporaire_contour=orange
    
    elif information_sur_remplisage["couleur"]=="13":
        couleur_temporaire_contour=rouge
    
    elif information_sur_remplisage["couleur"]=="10":
        couleur_temporaire_contour=girs_clair

    elif information_sur_remplisage["couleur"]=="11":
        couleur_temporaire_contour=rose

    elif information_sur_remplisage["couleur"]=="12":
        couleur_temporaire_contour=violet

    elif information_sur_remplisage["couleur"]=="9":
        couleur_temporaire_contour=blanc
    
    elif information_sur_remplisage["couleur"]=="14":
        couleur_temporaire_contour=noir
    
    elif information_sur_remplisage["couleur"]=="15":
        couleur_temporaire_contour=gris_foncé
    
    elif information_sur_remplisage["couleur"]=="16":
        couleur_temporaire_contour=transparence

    ImageDraw.floodfill(image_point, (int(information_sur_remplisage["coord_x"]), int(information_sur_remplisage["coord_y"])), couleur_temporaire_contour, thresh=0)

def remplisage(caractèrelecture: int):
    """permet d'analyser le fichier pour un remplisage. met toutes les donné dans le dictionaire information sur remplisage
    note : il peut y avoir des problème avec le remplisage a cause de bug de Scratch Draw, et non pas de ce projet."""
    logging.debug("rentrer dans la fonction remplisage")

    global annuler_ouverture

    if fichier[caractèrelecture] == "1":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["couleur"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":
        
        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["couleur"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["couleur"] += fichier[caractèrelecture]
    else:
        print("erreur de structure pour le remplisage, pour la couleur")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture

    caractèrelecture = caractèrelecture + 1

    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_x"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_x"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_x"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_x"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_x"] += fichier[caractèrelecture]
    
    else:
        print("erreur de structure pour le remplisage, pour la position x")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture
    
    caractèrelecture = caractèrelecture + 1

    logging.debug("caractèrelècture : " + str(caractèrelecture))
    logging.debug("caractère en cours de lecture : " + fichier[caractèrelecture])

    if fichier[caractèrelecture] == "1":

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_y"]= fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "2":

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_y"] += fichier[caractèrelecture]
    
    elif fichier[caractèrelecture] == "3":

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_y"]= fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_y"] += fichier[caractèrelecture]

        caractèrelecture = caractèrelecture + 1
        information_sur_remplisage["coord_y"] += fichier[caractèrelecture]
    
    else:
        print("erreur de structure pour le remplisage, pour la position y")
        varibale_pour_validation=input("Apuiller sur entré pour retourner au menu principal")
        annuler_ouverture=True
        return caractèrelecture

    logging.debug("information du remplisage : " + str(information_sur_remplisage))
    
    return caractèrelecture

def grille():
    """
    Cette fonction permet de tracer le grille si le paramètre est activer.
    nombre de ligne en largeur de la grille : 15
    nombre de ligne en hauteur de la grille : 11
    """
    logging.debug("entrer dans la fonction grille")

    def ligne_orisontal(position_y_départ:int):
        """permet de tracer une ligne de la grille (ligne orisontal)"""
        d_forme.line((0, position_y_départ, 480, position_y_départ), fill=noir, width=2)
    
    def ligne_vertical(position_x_départ:int):
        """permet de tracer une ligne de la grille (ligne vertical)"""
        d_forme.line((position_x_départ, 0, position_x_départ, 360), fill=noir, width=2)

    conteur_position_y=32

    while not(conteur_position_y==384):
        ligne_orisontal(conteur_position_y)
        conteur_position_y=conteur_position_y+32
    
    conteur_position_x=24

    while not(conteur_position_x==504):
        ligne_vertical(conteur_position_x)
        conteur_position_x=conteur_position_x+32

image_fond=None

def couleur_du_fond(couleur):
    global image_fond
    image_fond = Image.new('RGBA', (480, 360), color = couleur)
    d_fond = ImageDraw.Draw(image_fond)

#       -----------------------------------------------------

global annuler_ouverture
annuler_ouverture=False

ecriture_menue_principal=True
commande_menu=""

# intercafe graphique -----------------------------------------------------------------------------------------------------

fermeture_volontaire={"fermeture_ouverture_fichier_choix_d_ouverture":False, "fermeture_ouverture_par_le_press_papier":False}

fênetre_principal_choix_d_ouverture=None
def ouverture_fichier_choix_d_ouverture():
    """Cette fonction crée une fênetre pour choisire comment ouvrir un fichier : coller le fichier ou ouvrir un fichier."""
    
    try:
        fênetre_principal.destroy()
        logging.debug("fênetre principal fermé")
    except:
        logging.debug("Imposible de fermer la fênetre, car elle est déjà fermer.")
    

    global fênetre_choix_d_ouverture
    global fermeture_volontaire
    fermeture_volontaire["fermeture_ouverture_fichier_choix_d_ouverture"]=False

    fênetre_choix_d_ouverture = Tk()
    fênetre_choix_d_ouverture.title("Ouverture d'un fichier")
    Texte_choix_d_ouverture = Label(fênetre_choix_d_ouverture, text="Comment vouler-vous ouvrir le fichier ?")
    Texte_choix_d_ouverture.pack()

    choix_d_ouvertre_bouton_ouvrir_en_collan = Button(fênetre_choix_d_ouverture, text="Ouvrir un fichier en le collen avec le presse papier", command=ouverture_par_le_press_papier)
    choix_d_ouvertre_bouton_ouvrir_en_collan.pack()

    annuler_choix_d_ouverture=Button(fênetre_choix_d_ouverture, text="Annuler", command=fênetre_choix_d_ouverture.destroy)
    annuler_choix_d_ouverture.pack()

    fênetre_choix_d_ouverture.mainloop()
    if fermeture_volontaire["fermeture_ouverture_fichier_choix_d_ouverture"]==False:     #la fermeture n'est pas volontaire, mais elle a était fait par l'utilisateur
        menu_principal()

fênetre_ouverture_press_papier=None
chant_texte_du_fichier=None
def ouverture_par_le_press_papier():
    """Cette fonction crée une fênetre avec un chant texte de saisie pour coller le fichier à ouvrire."""
    global fermeture_volontaire
    fermeture_volontaire["fermeture_ouverture_fichier_choix_d_ouverture"]=True
    fermeture_volontaire["fermeture_ouverture_par_le_press_papier"]=False
    
    fênetre_choix_d_ouverture.destroy()
    global fênetre_ouverture_press_papier

    fênetre_ouverture_press_papier = Tk()
    fênetre_ouverture_press_papier.title("Ouverture d'un fichier par le press papier")

    texte_ouverture_par_le_press_papier = Label(fênetre_ouverture_press_papier, text="Copier et coller votre fichier.")
    texte_ouverture_par_le_press_papier.pack()

    global chant_texte_du_fichier

    chant_texte_du_fichier = Entry(fênetre_ouverture_press_papier, width=250)
    chant_texte_du_fichier.pack()

    fênetre_ouverture_press_papier_boutton_valider=Button(fênetre_ouverture_press_papier, text="Valider", command=valider_chan_texte_ouverture)
    fênetre_ouverture_press_papier_boutton_valider.pack()

    annuler_press_papier=Button(fênetre_ouverture_press_papier, text="Annuler", command=fênetre_ouverture_press_papier.destroy)
    annuler_press_papier.pack()

    fênetre_ouverture_press_papier.mainloop()
    
    logging.debug("la mainloop de press papier est arrêter")
    if fermeture_volontaire["fermeture_ouverture_par_le_press_papier"]==False:
        ouverture_fichier_choix_d_ouverture()

chant_texte_temporaire=None

def valider_chan_texte_ouverture():
    """Cette fonction est apeller losque le chant texte d'ouverture de fichier est valide"""
    global fermeture_volontaire
    fermeture_volontaire["fermeture_ouverture_par_le_press_papier"]=True
    global chant_texte_du_fichier
    global chant_texte_temporaire
    chant_texte_temporaire=chant_texte_du_fichier.get()

    fênetre_ouverture_press_papier.destroy()
    fênetre_ouverture_en_cours()

fênetre_ouverture_en_cours_barre_de_progresion=None

def fênetre_ouverture_en_cours():
    global chant_texte_temporaire
    global fênetre_ouverture_en_cours_barre_de_progresion
    fênetre_ouverture_en_cours_barre_de_progresion=Tk()
    fênetre_ouverture_en_cours_barre_de_progresion.title("Ouverture en cours...")

    texte_ouverture_en_cours=Label(fênetre_ouverture_en_cours_barre_de_progresion, text="L'ouverture est en cours, merci de patienter...")
    texte_ouverture_en_cours.pack()
    
    global fichier
    fichier=chant_texte_temporaire

    fênetre_ouverture_en_cours_barre_de_progresion.after(500, ouverture_fichier_principal)          # attention : ne pas mettre un temps trop faible : la fênetre n'a pas le temps d'être correctement crée. 500 ms, c'est bon

    fênetre_ouverture_en_cours_barre_de_progresion.protocol("WM_DELETE_WINDOW", lambda: None)

    fênetre_ouverture_en_cours_barre_de_progresion.mainloop()

    logging.debug("mainloop de ouverture en cours terminer")
    fin_de_fichier()

ouverture_terminer_fênetre=None

def ouverture_terminé():
    """fênetre qui s'ouvre quand l'ouverture est terminer. Posibilité : quitter ou enregistrer"""
    def quitter_ouverture_terminé():
        """Fonction pour quitter la fênetre"""
        global ouverture_terminer_fênetre
        ouverture_terminer_fênetre.destroy()
        menu_principal()

    global ouverture_terminer_fênetre
    ouverture_terminer_fênetre=Tk()

    ouverture_terminer_fênetre.title("Ouverture terminer")

    texte_ouverture_terminer=Label(ouverture_terminer_fênetre, text="L'ouverture est terminer. Vous pouver enregistrer votre image")
    texte_ouverture_terminer.pack()

    bouton_ouverture_terminer_enregistrer=Button(ouverture_terminer_fênetre, text="Enregistrer l'image", command=enregistrer_l_image_fênetre)
    bouton_ouverture_terminer_enregistrer.pack()
    
    bouton_ouverture_terminer_quitter=Button(ouverture_terminer_fênetre, text="Quitter", command=quitter_ouverture_terminé)
    bouton_ouverture_terminer_quitter.pack()

    ouverture_terminer_fênetre.protocol("WM_DELETE_WINDOW", quitter_ouverture_terminé)

    ouverture_terminer_fênetre.mainloop()

chemain_d_accer_fichier_enregistrer=None

def enregistrer_l_image_fênetre():
    global chemain_d_accer_fichier_enregistrer
    chemain_d_accer_fichier_enregistrer=filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Enregistrer l'image"
    )
    ouverture_terminer_fênetre.destroy()
    if chemain_d_accer_fichier_enregistrer=="":
        ouverture_terminé()
    
def enregistrement_réussit():
    def retour_menu_principal():
        fênetre_enregistrement_réussit_fênetre.destroy()
        menu_principal()
    
    def ouvrir_dans_explorateur():
        # Obtenir le chemin absolu du fichier
        chemin_absolu = os.path.abspath(chemain_d_accer_fichier_enregistrer)
        # Détecter le système d'exploitation et utiliser la commande appropriée
        systeme = platform.system()
        try:
            if systeme == "Windows":
                # Utiliser le paramètre /select pour sélectionner le fichier dans l'explorateur
                subprocess.Popen(f'explorer /select,"{chemin_absolu}"')
            elif systeme == "Darwin":  # MacOS
                subprocess.Popen(["open", "-R", chemin_absolu])
            elif systeme == "Linux":
                subprocess.Popen(["xdg-open", os.path.dirname(chemin_absolu)])
        except Exception as e:
            logging.error(f"Erreur lors de l'ouverture de l'explorateur: {str(e)}")
    
    fênetre_enregistrement_réussit_fênetre=Tk()
    fênetre_enregistrement_réussit_fênetre.title("L'enregistrement terminer")

    texte_fênetre_enregistrement_réussit_fênetre=Label(fênetre_enregistrement_réussit_fênetre, text="L'enregistrement a étais effectuer avec succés.")
    texte_fênetre_enregistrement_réussit_fênetre.pack()
    
    cadre_ouverture=LabelFrame(fênetre_enregistrement_réussit_fênetre, text="Ouvrir...",)
    cadre_ouverture.pack()

    afficher_dans_explorateur_fichier_fênetre_enregistrement_réussit_fênetre=Button(cadre_ouverture, text="Afficher dans l'explorateur de fichier", command=ouvrir_dans_explorateur)
    afficher_dans_explorateur_fichier_fênetre_enregistrement_réussit_fênetre.pack()

    ouvrir_l_image=Button(cadre_ouverture, text="Ouvrir l'image", command=image_pour_afficher.show)
    ouvrir_l_image.pack()

    retour_menue_principal_fênetre_enregistrement_réussit_fênetre=Button(fênetre_enregistrement_réussit_fênetre, text="Retourner au menu principal", command=retour_menu_principal)
    retour_menue_principal_fênetre_enregistrement_réussit_fênetre.pack()

    fênetre_enregistrement_réussit_fênetre.protocol("WM_DELETE_WINDOW", retour_menu_principal)

    fênetre_enregistrement_réussit_fênetre.mainloop()

fênetre_principal=None
d=None
d_forme=None
image_point=None

fichier=None
def menu_principal():
    """Fenetre graphique du menu principal."""
    global fênetre_principal
    fênetre_principal = Tk()
    fênetre_principal.title("Export PNG Scratch Draw")
    Texte_menu_principal = Label(fênetre_principal, text="Bienvenu")
    Texte_menu_principal.pack()

    menu_principal_bouton_ouverture_fichier_simple = Button(fênetre_principal, text="Ouvrir et exporter un fichier", command=ouverture_fichier_choix_d_ouverture)
    menu_principal_bouton_ouverture_fichier_simple.pack()

    menu_principal_bouton_quitter = Button(fênetre_principal, text="Quitter", command=fênetre_principal.destroy)
    menu_principal_bouton_quitter.pack()

    fênetre_principal.mainloop()

# fin intercafe graphique -----------------------------------------------------------------------------------------------------

fond=None
imageforme=None

def ouverture_fichier_principal():        
    """Cette fonction gère l'ouverture d'un fichier. Elle utilise d'autre fonction pour analiser plus précisément les élément et pour tracer les élément."""
    
    # variable / dicionaire global
    global fichier
    global information_sur_carré
    global information_sur_cercle
    global information_sur_point
    global information_sur_rectangle
    global information_sur_remplisage
    global information_sur_triangle
    global fênetre_ouverture_en_cours_barre_de_progresion
    global fond
    global image_point
    global imageforme

    image_point = Image.new('RGBA', (480, 360), color = (255, 255, 255, 0))
            
    global d
    d = ImageDraw.Draw(image_point)

    imageforme = Image.new('RGBA', (480, 360), color = (255, 255, 255, 0))
    global d_forme
    d_forme = ImageDraw.Draw(imageforme)

    caractèrelecture = 0


    # Afficher la taille du fichier
    logging.debug("Taille du fichier : " + str(len(fichier)))
    logging.debug("contenu du fichier : " + fichier )

    # premier controle du fichier : la longueur
    if len(fichier)<13:
        print("Votre fichier contient une taille anormale de caratrères. Il est donc potentiellement corrompu, ou provient d'une vertion différnete de Scratch Draw.")
        print("Appuiller sur Entrée pour ouvrir ce fichier et Q pour quiter.")
        réponse_controle_fichier_longueur=input("")

        if réponse_controle_fichier_longueur=="":
            print ("Le fichier sera ouver, mais il y a des risque de dysfonctionnement...")

        elif (réponse_controle_fichier_longueur=="q") or (réponse_controle_fichier_longueur=="Q"):
            logging.debug("l'ouverture du fichier est anulé en raison de la taille anormal")
            annuler_ouverture=True
    
    # Elément de fin de fichier       -----------------------

    logging.debug ("fichier[-1] " + fichier[-1])
    logging.debug ("fichier[-2] " + fichier[-2])
    logging.debug ("fichier[-3] " + fichier[-3])

    if (fichier[-1] == "0"):
        logging.debug ("vertion du fichier (0) correcte")
    
    elif (fichier[-1] == "1"):
        logging.debug ("Vertion du fichier (1) correcte")
        
    else:
        print ("Attention : votre fichier a une version différente de celle de ce générateur.")
        print ("Les vertion suporté sont : v0, v1")
        print ("La vertion du fichier est : " + fichier[-1])

        print ("Appuiller sur Entée pour continuer et Q pour quitter")

        ouvrir_un_fichier_avec_mauvaise_vertion=input("")

        if ouvrir_un_fichier_avec_mauvaise_vertion == "":
            print ("Le fichier sera ouvert, mais il y a des risques de dysfonctionnement...")
        
        elif ouvrir_un_fichier_avec_mauvaise_vertion == "Q" or ouvrir_un_fichier_avec_mauvaise_vertion == "q":
            annuler_ouverture=True

        else:
            print ("commande inconue")

    fond = {"Grille" : bool(int(fichier[-2])), "couleur_de_l'arière_plant" : fichier[-3]}

    logging.debug("contenue dictionaire fond : " + str(fond))

    annuler_ouverture=False

    while not (len(fichier) == caractèrelecture + 1):

        if annuler_ouverture == True:
            print ("Louverture a était anuler, vous pouver ouvrir un nouveau fichier...")
            break

        logging.debug("caractère en cours de lecture : " + fichier[caractèrelecture])

        if fichier[caractèrelecture] == "1": # détéction d'un point
            caractèrelecture = caractèrelecture + 1
            caractèrelecture = point(caractèrelecture)

            tracer_point()

            information_sur_point = {"couleur":"0", "coord_x":"0", "coord_y": "0", "taille": "0"} #réinisialisation du dicionaire point

        elif fichier[caractèrelecture] == "2": # détéction d'un cercle
            caractèrelecture = caractèrelecture + 1

            caractèrelecture = cercle(caractèrelecture)

            tracer_cercle()

            information_sur_cercle = {"couleur fond":"0", "couleur contour":"0", "coord_x":"0", "coord_y": "0", "taille": "0"} #réinisialisation du dicionaire cercle

        elif fichier[caractèrelecture] == "3": # détéction d'un rectangle
            caractèrelecture = caractèrelecture + 1

            caractèrelecture = rectangle(caractèrelecture)

            tracer_rectangle()

            information_sur_rectangle = {"couleur fond":"0", "couleur contour":"0", "coord_x":"0", "coord_y": "0", "taille": "0"} #réinisialisation du dicionaire rectangle

        elif fichier[caractèrelecture] == "4": # détéction d'un triangle
            caractèrelecture = caractèrelecture + 1

            caractèrelecture = triangle(caractèrelecture)

            tracer_triangle()

            information_sur_triangle = {"couleur fond":"0", "couleur contour":"0", "coord_x":"0", "coord_y": "0", "taille": "0"} #réinisialisation du dicionaire triangle

        elif fichier[caractèrelecture] == "5": # détéction d'un carré
            caractèrelecture = caractèrelecture + 1

            caractèrelecture = carré(caractèrelecture)

            tracer_carré()

            information_sur_carré = {"couleur fond":"0", "couleur contour":"0", "coord_x":"0", "coord_y": "0", "taille": "0"} #réinisialisation du dicionaire carré
        
        elif fichier[caractèrelecture] == "6": # fin du fichier
            
            fênetre_ouverture_en_cours_barre_de_progresion.destroy()
            break

        elif fichier[caractèrelecture] == "7": #remplisage
            
            caractèrelecture = caractèrelecture + 1                    
            caractèrelecture = remplisage(caractèrelecture)

            tracer_remplisage()

            information_sur_remplisage = {"couleur":"0", "coord_x":"0", "coord_y": "0"}

            logging.debug("caractèrelecture : " + str(caractèrelecture))
            logging.debug("caractère en cours de lecture : " + fichier[caractèrelecture])

        else:      # erreur : arrêt du programme
            
            print ("Votre fichier contient une erreur majeur (un élément inconue a était détecter)")
            print ("Votre fichier est peut-être d'une version plus récente que celle de cette aplication.")
            varibale_pour_validation=input("Appuiller sur Entrée pour quiter")

            break

        
        caractèrelecture = caractèrelecture + 1
    
image_pour_afficher=None

def fin_de_fichier():
    # fond de l'image :


    if fond["Grille"]==True:
        grille()

    if not(fond["couleur_de_l'arière_plant"]=="0"):     # détéction d'un fond non coloré
        if fond["couleur_de_l'arière_plant"]=="1":
            couleur_du_fond(couleur=(0, 0, 0, 255))

        elif fond["couleur_de_l'arière_plant"]=="2":
            couleur_du_fond(couleur=(255, 255, 255, 255))

        elif fond["couleur_de_l'arière_plant"]=="3":
            couleur_du_fond(couleur=(255, 0, 233, 255))

        elif fond["couleur_de_l'arière_plant"]=="4":
            couleur_du_fond(couleur=(253, 255, 0, 255))

        elif fond["couleur_de_l'arière_plant"]=="5":
            couleur_du_fond(couleur=(255, 144, 0, 255))
        
        elif fond["couleur_de_l'arière_plant"]=="6":
            couleur_du_fond(couleur=(255, 0, 0, 255))
        
        elif fond["couleur_de_l'arière_plant"]=="7":
            couleur_du_fond(couleur=(56, 158, 255, 255))

        elif fond["couleur_de_l'arière_plant"]=="8":
            couleur_du_fond(couleur=(255, 144, 210, 255))
        
        elif fond["couleur_de_l'arière_plant"]=="9":
            couleur_du_fond(couleur=(0, 255, 32, 255))

    global fênetre_ouverture_en_cours_barre_de_progresion
    
    ouverture_terminé()
    global image_point

    image_point.paste(imageforme, (0,0), imageforme)      # Fusionner les images

    if not(fond["couleur_de_l'arière_plant"]=="0"):
        image_fond.paste(image_point, (0,0), image_point)
        image_fond = image_fond.transpose(Image.FLIP_TOP_BOTTOM) #invertion de l'image, car l'image est dans le mauvais sens
        image_fond.save(chemain_d_accer_fichier_enregistrer)
    
    image_point = image_point.transpose(Image.FLIP_TOP_BOTTOM) #invertion de l'image, car l'image est dans le mauvais sens
    image_point.save(chemain_d_accer_fichier_enregistrer)
    
    global image_pour_afficher
    image_pour_afficher = Image.open(chemain_d_accer_fichier_enregistrer)

    enregistrement_réussit()
    
    
menu_principal()


logging.debug("fin programme")