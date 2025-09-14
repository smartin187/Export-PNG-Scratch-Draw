""" Je génère des fichiers image grâce à Scratch
 Voici la structure d'un fichier image
 j'ai défini des types de forme
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
J'ai donné l'extension .sdrw à ces fichiers"""

import logging
logging.basicConfig(level=logging.DEBUG)

from PIL import Image, ImageDraw, Image

#inicialisation des dicionaire pour les information des élément ------------------
information_sur_point = {"couleur":"0", "coord_x":"0", "coord_y": "0", "taille": "0"}

information_sur_cercle = {"couleur fond":"0", "couleur contour":"0", "coord_x":"0", "coord_y": "0", "taille": "0"}

information_sur_rectangle = {"couleur fond":"0", "couleur contour":"0", "coord_x":"0", "coord_y": "0", "taille": "0"}

information_sur_triangle = {"couleur fond":"0", "couleur contour":"0", "coord_x":"0", "coord_y": "0", "taille": "0"}

information_sur_carré = {"couleur fond":"0", "couleur contour":"0", "coord_x":"0", "coord_y": "0", "taille": "0"}

information_sur_remplisage = {"couleur":"0", "coord_x":"0", "coord_y": "0"}

#inicialisation des couleurs :
baige=(255, 205, 127, 255)
jaune=(255, 247, 0, 255)
marron=(150, 84, 38, 255)
vert_clair=(143, 255, 139, 255)
vert_foncé=(5, 158, 0, 255)
bleu_clair=(127, 192, 255, 255)
bleu_foncé=(0, 69, 255, 255)
orange=(255, 125, 0, 255)
blanc=(255, 255, 255, 255)
girs_clair=(128, 128, 128, 255)
rose=(255, 165, 236, 255)
violet=(230, 0, 163, 255)
rouge=(255, 0, 0, 255)
noir=(0, 0, 0, 255)
gris_foncé=(82, 82, 82, 255)
transparence=(0, 0, 0, 0)

#fin inicialisation --------------------

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
        #raise Exception("erreur de structure pour le triangle, pour la couleur du contour")
        print("erreur de structure pour le triangle, pour la couleur du contour")
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

    ImageDraw.floodfill(image, (int(information_sur_remplisage["coord_x"]), int(information_sur_remplisage["coord_y"])), couleur_temporaire_contour, thresh=0)

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

#démarage du programme pour l'utilisateur

print ("Bienvenu")
print ("ce logiciel vous permet d'exporter les fichier de ce programme Scratch https://scratch.mit.edu/projects/782765473/ en .png")
print ("___________________________")
print ("")

global annuler_ouverture
annuler_ouverture=False

ecriture_menue_principal=True
commande_menu=""

while True: #boucle principale du programme

    if ecriture_menue_principal==True:

        annuler_ouverture=False

        print ("")
        print ("----  MENU PRINCIPAL  ----")
        print ("")

        print ("Commandes :")
        print ("   Appuiller sur Entée pour ouvrir un fichier")
        print ("   Ecriver Q pour quitter")

        commande_menu=input("")

        if commande_menu=="":
            fichier = input("Coller les chiffres de scratch draw : ")
            ouverture_fichier=True
        
        elif commande_menu=="Q" or commande_menu=="q":
            break

        ecriture_menue_principal=False

        

    if ouverture_fichier==True:

        #try:
            ouverture_fichier=False

            image = Image.new('RGBA', (480, 360), color = (255, 255, 255, 0))
            d = ImageDraw.Draw(image)

            imageforme = Image.new('RGBA', (480, 360), color = (255, 255, 255, 0))
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
                    logging.debug("fin du fichier")

                    print("le fichier a étais ouvert avec succé.")

                    varibale_pour_validation=input("Appuiller sur Entrée pour retouvner au menu principal.")
                    print("")

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


            image.paste(imageforme, (0,0), imageforme)      # Fusionner les images

            if not(fond["couleur_de_l'arière_plant"]=="0"):
                image_fond.paste(image, (0,0), image)
                image_fond = image_fond.transpose(Image.FLIP_TOP_BOTTOM) #invertion de l'image, car l'image est dans le mauvais sens
                image_fond.save('image_générer.png')
            
            image = image.transpose(Image.FLIP_TOP_BOTTOM) #invertion de l'image, car l'image est dans le mauvais sens
            image.save('image_générer.png')
            
            ecriture_menue_principal=True

        #except:
            #print("erreur")
            #try:
            #    print("Une erreur est survenue.")
            #    print("Vouler vous enregistrer votre image ?")
            #    print("L'ouverture sera incomplet, mais une partit de l'image pourrait être ouvert.")
            #    print("appuiller sur Entrée pour enregistrer votre image, et Q pour quiter.")
            #    variable_pour_comande_erreur=input("")
            #    if variable_pour_comande_erreur=="Q" or variable_pour_comande_erreur=="q":
            #        quit()
            #    elif variable_pour_comande_erreur=="":
            #        print("Esser de sovegarder votre image...")
            #        image.save('image_générer.png')
            #        quit()
            #    else:
            #        quit()

            #except:
            #    print("Erreur majeur")
            #    sleep(5)
            #    quit()

logging.debug("fin programme")