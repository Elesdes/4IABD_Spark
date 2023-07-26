# Projet de Génération et d'Analyse de Données de Fréquence Cardiaque

 Ce projet utilise Apache Spark pour générer, streamer et analyser des données de fréquence cardiaque simulées. Les données générées sont conçues pour simuler les mesures de fréquence cardiaque pendant l'activité sportive. Le projet est composé de cinq scripts Scala qui sont exécutés séquentiellement.

## Installation
Vous devrez installer les logiciels suivants :
- [Apache Spark](https://spark.apache.org/docs/latest/spark-standalone.html)
- [Scala](https://www.scala-lang.org/download/)

Configurer POM :
 Indique à Maven ce dont il a besoin pour construire et exécuter notre projet.

Les balises `<groupId>`, `<artifactId>` et `<version>` donnent un identifiant unique à votre projet. C'est un peu comme le nom et l'adresse de votre projet dans le monde de la programmation.

Dans la section `<properties>`, on définit des valeurs que l'on veut réutiliser à plusieurs endroits dans le fichier. Ici, par exemple, on a défini la version de Scala que l'on va utiliser.

La section `<dependencies>` est comme la liste des ingrédients de la recette. Elle énumère toutes les choses dont votre projet a besoin pour fonctionner. Ici, on a besoin de la bibliothèque standard de Scala, de certains outils pour tester notre code (JUnit et ScalaTest), et d'Apache Spark pour le traitement des données.

Ensuite, la section `<build>` décrit comment assembler tous ces ingrédients. Elle indique où trouver le code source et comment compiler le code et exécuter les tests.

Dans votre cas, ce fichier POM est utilisé pour configurer tout ce qui est nécessaire pour exécuter vos scripts Scala. Il définit tout ce dont vous avez besoin pour votre projet, comme Apache Spark pour le traitement des données et des outils pour tester votre code.




## Scripts
Voici une description de chaque script :
1. Move.scala : Ce script génère une série de messages et les envoie à un sujet spécifique. Ces messages sont utilisés pour simuler un flux de données en temps réel qui sera ensuite consommé par les scripts Spark Streaming suivants.

2. SparkStreamingJson.scala : Ce script utilise Spark Streaming pour lire les messages en tant que flux de données, créant un nouvel ensemble de données toutes les 5 secondes. Chaque ensemble de données est converti en un DataFrame Spark SQL et sauvegardé en format CSV.

3. SparkStreamingTab2.scala : Ce script est similaire au précédent, mais il ajoute une colonne "SportBPM" au DataFrame avant de l'écrire en CSV. La valeur de "SportBPM" est générée aléatoirement pour chaque ligne, simulant une fréquence cardiaque en battements par minute.

4. SparkStreamingGroupe.scala : Ce script ajoute une étape de traitement pour regrouper les données par la valeur de "SportBPM" et compter le nombre d'occurrences de chaque valeur. Cela donne une idée de la distribution des valeurs de fréquence cardiaque simulées.

5. SparkStreamingGroupe2.scala : Après le regroupement des données et le comptage des occurrences, ce script ajoute une étape de filtrage pour ne conserver que les groupes ayant plus de 5 occurrences. Cela permet de se concentrer sur les valeurs de fréquence cardiaque les plus couramment observées.

## Utilisation
Pour utiliser ces scripts, vous devrez exécuter les scripts dans l'ordre indiqué ci-dessus. Vous pouvez exécuter un script Scala à partir de la ligne de commande comme suit :

Lancer en premier  Move pour stimuler une entrée de données en streaming après move il faut lancer (2) SparkStreamingJson qui va commencer le traitement en stream suite a ca lancer (3) SparkStreamingTab2 puis lancer (4) SparkStreamingGroupe et (5) SparkStreamingGroupe2 qui feront les traitements nécessaires 
Assurez-vous de remplacer le chemin de sortie des fichiers CSV dans chaque script par le chemin où vous souhaitez que les fichiers soient sauvegardés.

## Analyse des Résultats

Les fichiers CSV produits par ces scripts peuvent être utilisés pour analyser les données de fréquence cardiaque simulées. 

Les données en sortie seront utiliser dans la partie visualisation Python 
main et main2 
