# Export PNG Scratch Draw

Ce programme écrit en Python vous permet d'exporter en PNG un fichier créé par le programme Scratch [Scratch Draw](https://scratch.mit.edu/projects/782765473/).
Pour exécuter le script, vous devez le télécharger. Vérifiez aussi que les librairies sont installées (voir [Librairies utilisées](#librairies-utilisées)).

## Ouvrir et exporter une image

Pour ouvrir une image, cliquez sur "Ouvrir et exporter un fichier", dans le menu principal.

### Ouverture
Vous avez deux possibilités pour ouvrir votre fichier :
- [Ouverture par le presse-papiers](#ouverture-par-le-presse-papiers)
- [Ouverture d'un fichier en texte brut](#ouverture-dun-fichier-en-texte-brut)
#### Ouverture par le presse-papiers
Cliquez sur "Ouvrir un fichier en le collant avec le presse-papiers".
Collez le fichier Scratch Draw dans la saisie de texte, puis cliquez sur "Valider".

#### Ouverture d'un fichier en texte brut
Cliquez sur "Ouvrir un fichier en texte brut", puis sur "Ouvrir le fichier".
Vous devez sélectionner le fichier que vous voulez ouvrir, attention : il doit être en texte brut.

### Ouverture terminée
L'ouverture s'effectuera, quand elle sera terminée, cliquez sur "Enregistrer l'image", et sélectionnez le répertoire dans lequel vous voulez enregistrer votre image.
Une fois votre image enregistrée, l'export est terminé.
Vous pouvez retourner au menu principal, ou cliquer sur "Afficher dans l'explorateur de fichiers".

## Librairies utilisées

Ce programme utilise des librairies :

- Tkinter
- PIL
- Logging
- os
- platform
- subprocess
- pathlib

Vérifiez si ces librairies sont bien installées sur votre ordinateur. Si ce n'est pas le cas, vous ne pourrez pas exécuter le script.

## Paramétrage

Vous pouvez paramétrer cette application.
Notez que les paramétrages sont enregistrés dans le fichier "Réglage.txt". Si vous modifiez / supprimez / déplacez ce fichier, il peut y avoir des dysfonctionnements. Notez que ce fichier doit être dans le même répertoire que le script main.py.

### Réglage de la langue
Vous pouvez choisir français ou anglais pour la langue.
### Réglage du log
Vous pouvez choisir le niveau du log :
- Debug
- Info
- Warning
- Error
- Fatal

Si vous souhaitez modifier le script, mettez le log à Debug pour avoir des informations sur l'utilisation, alors que si vous voulez uniquement utiliser cette application, réglez le log sur Error par exemple.