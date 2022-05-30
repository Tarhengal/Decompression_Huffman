# Decompression_Huffman

## avant-propos

J’ai choisi de traiter le sujet de la décompression de Huffamn car j’avais traité la compression lors de la première partie du module. Cette première partie n’avait pas très bien été traité de ma part pour plusieurs raisons, non connaissance de GitHub, début en Java et le non rendu d’un compte rendu. Cela avait résulté d’une note plutôt mauvaise alors pour cette seconde partie il est très clair que j’ai fait tout mon possible pour avoir la meilleure note possible pour rattraper mes erreurs et m’éviter d’aller au rattrapage. Je pense donc cette fois ci avoir traité le sujet dans son entièreté, et ayant passé un certain nombre d’heure dessus espère que cela va payer.

## Description du projet 

Le sujet abordé est donc la décompression de Huffman le principe est de faire le chemin inverse de ce que nous avions effectué pour la compression. Le concept de Huffman réside dans le fait de coder les caractères avec une forte fréquence d’apparition avec un code binaire le plus léger possible et les caractères avec une fréquence d’apparition moins grande un code binaire plus lourd. Ainsi sur de long texte on arrive à atteindre un taux de compression plutôt satisfaisant. Lors de la compression nous devons aussi créer un fichier avec la fréquence de chaque caractère présent dans le texte se ficher nous permettras de décompresser notre fichier binaire lorsque nous le souhaitons en utilisant le mécanisme inverse 
Pour la décompression donc, nous avons accès a deux fichiers, un fichier .txt contenant les fréquences de chaque caractère et un fichier .bin qui est le fichier texte compressé contenant une suite d’octets. On récupère la fréquence de chaque caractère dans le fichier texte puis on construit l’arbre sur le principe présenté par Hufmman à l’aide de ces données. Une fois l’arbre construit a l’aide du code binaire convertis depuis le ficher .bin contenant les octets on parcourt l’arbre construit précédemment pour retrouver les caractères initiaux du texte 
Puis il suffit de créer un fichier texte avec le texte décompressé. On étudiera le taux de compression du fichier .bin donné initialement et le poids moyen de chaque caractère.

## le code 

se laisser guider par le main.py