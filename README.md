# Organisateur de table de donnée CSV

## Résumé du programme

ce programme permet d'organiser des fichiers de type csv par l'entremise du tableur excel. placez simplement le ou les fichiers désiré dans le dossier nommé input_csv_file_here et roulez le programme. Suivez ensuite les instructions, cela lira automatiquement le fichier et ouvrira excell pour que vous puissiez organiser les donnés comme vous le désirez.

lorsque vouz aurez terminé, suivez les instructions de nouveau, excell se fermera automatiquement et votre fichier organisé se trouvera dans le dossier output_organised_csv_here.

si vous le voulez, il est possible en même temps de recevoir le fichier en version tableau markdown, indiquez le simplement au programme lorsque demandé, le tableau markdown sera ensuite déposé dans le dossier output_organised_markdown_here 

## entrée
les fichiers à traiter doivent obligatoirement être déposés dans le dossier "input_csv_file_here".
### important : les fichiers csv ne seront lus que si ils terminent par ".csv" exactement, pas de ".CSV" ou autres extentions étranges! 

## Sortie
les fichiers organisés sont déposés dans le dossier "output_organised_csv_here".

les fichiers markdown du csv organisé sont déposés dans le dossier "output_organised_markdown_here".

## Dépendances
- ### pandas
  nécésaire afin de lire/écrire correctement les fichiers 
- ### rich
  pas réellement nécésaire mais cela ajoute de la couleur dans le terminal et rend le tout plus claire, sans cela, les messages seront moins lisibles car ils seront tous de la meme couleur et surtout, remplis de codes de changement de couleur et de style qui ne serait pas visible avec rich. Donc fortement recommendé
- ### openpyxl (for xlsx read/write)
  nécésaire afin de lire/écrire des xlsx

#### Installation des dépendances
```
pip install pandas rich openpyxl
```
## crédit (acknowledgements)
- code : Antoine D-C
- avec l'aide de: Philippe Gauthier, Google.com, reddit.com et perplexity.ai