# Export PNG Scratch Draw

Ce programme écrit en Python vous permet d'exporter en PNG un fichier créé par le programme Scratch [Scratch Draw](https://scratch.mit.edu/projects/782765473/)
Pour exécuter le script, vous devez le télécharger. Vérifiez aussi que les librairies sont installées (voir [Librairies utilisées](#librairies-utilisées))


## Ouvrir et exporter une image

Pour ouvrir une image, cliquez sur "Ouvrir et exporter un fichier", dans le menu principal.

Ensuite, cliquez sur "Ouvrir un fichier en le collant avec le presse-papiers".
Collez le fichier Scratch Draw dans la saisie de texte, puis cliquez sur "Valider".
L'ouverture s'effectuera, quand elle sera terminée, cliquez sur "Enregistrer l'image", et sélectionnez le répertoire dans lequel vous voulez enregistrer votre image.
Une fois votre image enregistrée, l'export est terminé.


## Librairies utilisées

Ce programme utilise des librairies :

- Tkinter
- PIL

Vérifiez si ces librairies sont bien installées sur votre ordinateur. Si cela n'est pas le cas, vous ne pourrez pas exécuter le script.

## Paramétrage du log

Ce programme a un log permettant d'aider la correction de bug. Si vous n'avez pas besoin du log, vous pouvez, à la ligne 38, changer le niveau du log :
```python
logging.basicConfig(level=logging.DEBUG)
```