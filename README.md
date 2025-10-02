# README #

This README would normally document whatever steps are necessary to get your application up and running.

### How to setup ###

#### Then prepare python environment ####
`./script/install_requirements.sh`

##### Enjoy! #####

`./script/run_tests.sh`

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines
# Mesurer avec COSMIC
> Tiré du Manuel de mesurage COSMIC v5 Partie 1-2020-06-15b
> https://cosmic-sizing.org/measurement-manual/
## 1 Présentation
La méthode COSMIC consiste à appliquer un ensemble de modèles, principes, règles et
processus pour mesurer les exigences fonctionnelles des utilisateurs (ou « EFU ») d'un logiciel
donné.
Le résultat est une « valeur d'une quantité » (telle que définie par l'ISO) représentant la taille
fonctionnelle du logiciel selon la méthode COSMIC adoptée comme étant ISO/IEC 19761: 2011.
La valeur numérique est sur un ratio selon les échelles de mesure : par conséquent, des
opérations mathématiques valides peuvent être effectuées en utilisant ces valeurs.
La méthode COSMIC adopte la définition des exigences fonctionnelles des utilisateurs telles que
définies par l'ISO.
## Les 17 principes de la méthode COSMIC.
La méthode COSMIC est basée sur 17 principes d'ingénierie du logiciel classés en deux modèles :
> 1. Le modèle contextuel du logiciel COSMIC. Ce modèle contient les principes relatifs à
l'identification de la nature et de la structure du logiciel à mesurer tel que requis par la
méthode COSMIC, conduisant à l'identification de son EFU.
> 2. Le modèle générique d’un logiciel. Ce modèle contient les principes à appliquer de l’EFU afin d'extraire et de mesurer les éléments qui contribuent à la taille fonctionnelle à l'aide de la méthode COSMIC.
Les principes sont écrits en utilisant la terminologie de la méthode COSMIC.

## PROCESSUS DE MESURAGE COSMIC
Le processus de mesurage COSMIC comprend trois phases - voir figure 2.1 :
> 1. La phase de la stratégie de mesurage, dans laquelle le but et la portée du MTF sont définis.
Le modèle de contexte logiciel est ensuite appliqué afin que le logiciel à mesurer et la
mesure requise soient définis sans ambiguïté - voir la section 3.
> 2. La phase de mise en correspondance au cours de laquelle le modèle de logiciel générique
est appliqué aux EFU du logiciel à mesurer pour produire le modèle COSMIC du logiciel
qui peut être mesuré - voir la section 4.
> 3. La phase de mesurage, dans laquelle les tailles réelles sont affectées - voir la section 5.
Les règles régissant l'enregistrement des mesures sont décrites à la section 6.
La relation entre les trois phases de la méthode COSMIC est illustrée à la figure 2.1.

Le projet d'automatisation vise la phase 2, c.-à-d. la mise en correspondance, les règles 10 à 

## 3 PHASE 1 – STRATÉGIE DE MESURAGE.
Cette section décrit les paramètres clés qui doivent être pris en compte dans la phase de stratégie de mesurage avant de commencer réellement à mesurer.

### RÈGLE 1 : Activités de mesurage.
La détermination de la taille fonctionnelle COSMIC doit impliquer toutes les activités et règles décrites aux sections 3.2 à 3.6.

### RÈGLE 2 : Raison d’être et périmètre.
La raison d’être et le périmètre du MTF doivent être déterminés avant de commencer un exercice de mesurage particulier.

### RÈGLE 3 : Identification de l’EFU.
L’EFU identifiée comme étant dans le champ d'application du MTF doit être utilisée comme source exclusive à partir de laquelle la taille fonctionnelle du logiciel doit être mesurée.

### RÈGLE 4 : Si nécessaire aux fins de l'exercice de mesurage, chacune de ces couches doit être identifiée.

### RÈGLE 5 : Un seul logiciel à mesurer ne doit pas avoir son périmètre défini pour s'étendre sur plus d'une couche.

### RÈGLE 6 : Caractéristiques des couches.
Les couches identifiées dans le cadre du MTF doivent avoir les caractéristiques suivantes:
> a) Le logiciel de chaque couche doit fournir des fonctionnalités à ses utilisateurs fonctionnels.
> b) Les logiciels d'une couche subordonnée doivent fournir des services fonctionnels aux
logiciels d'une couche utilisant ses services.
> c) Les logiciels qui partagent des données avec d'autres logiciels ne seront pas considérés
comme étant dans des couches différentes s'ils interprètent de manière identique les
attributs de données qu'ils partagent.

### RÈGLE 7 : Utilisateurs fonctionnels.
Tous les utilisateurs fonctionnels qui déclenchent, fournissent des informations ou reçoivent des
informations de processus fonctionnels dans l’EFU du logiciel dans le cadre du MTF doivent être identifiés.

### RÈGLE 8 : Identification des frontières.
La frontière de chaque logiciel à l'intérieur de chaque couche et dans le périmètre du MTF doit être identifiée.

### RÈGLE 9 : Allocation de chaque EFU à une frontière.
Une fois les frontières identifiées, chaque EFU dans le champ d'application du MTF doit être allouée à un logiciel spécifique.

## 4 PHASE 2 – MISE EN CORRESPONDANCE.

### RÈGLE 10 : Identification des processus fonctionnels.
Chaque processus fonctionnel identifié dans le champ d'application du MTF doit:
a) Dériver d'au moins une EFU identifiable;
b) Être initié par un mouvement de saisie de données d'un utilisateur fonctionnel informant le
processus fonctionnel qu'il a détecté un événement déclencheur;
c) Comprendre au moins deux mouvements de données, à savoir toujours une Entrée plus
une Sortie ou une éCriture;
d) Appartient à une et une seule couche;
e) Être complet lorsqu'un point de synchronisation asynchrone doit être atteint conformément à son EFU.

### RÈGLE 11 : Identification des groupes de données.
Chaque groupe de données identifié dans le champ d'application du MTF doit :
a) Être unique et se distinguer par sa collection unique d'attributs de données,
b) Être directement lié à un objet d'intérêt décrit dans l’EFU du logiciel.

### RÈGLE 12 : Identification des mouvements de données.
Chaque processus fonctionnel identifié doit être partitionné en ses mouvements de données qui le composent.

### RÈGLE 13 : Processus fonctionnel - Entrée de déclenchement unique.
Pour tout processus fonctionnel, un seul mouvement de données d'Entrée de déclenchement doit être identifié et comptabilisé pour l'Entrée de toutes les données décrivant un seul objet d'intérêt que l’EFU doit être entré, à moins que l’EFU exige explicitement des données décrivant le même objet d'intérêt unique pour être entré plusieurs fois dans le même processus fonctionnel.
### RÈGLE 14 : Processus fonctionnel - Sortie, Lecture ou éCriture unique.
De même, un mouvement de données de Sortie, de Lecture ou d'éCriture unique doit être identifié
et comptabilisé pour le mouvement de toutes les données décrivant un seul objet d'intérêt que
l’EFU requiert de ce type (par exemple, Sortie, Lecture ou éCcriture, respectivement), sauf si l’EFU
exige explicitement que les données décrivant le même objet d'intérêt soient déplacées plusieurs
fois dans le même processus fonctionnel par un mouvement de données du même type (par
exemple, Sortie, Lecture ou éCriture, respectivement).
### RÈGLE 15 : Processus fonctionnel - Occurrences.
Si un mouvement de données d'un type particulier (Entrée, Sortie, Lecture ou éCriture) se produit plusieurs fois avec différentes valeurs de données lorsqu'un processus fonctionnel est exécuté, un seul mouvement de données de ce type doit être identifié et compté dans ce processus fonctionnel [pour un même groupe de données].

### RÈGLE 16 : Entrée.
Une Entrée doit :
a) Recevoir un seul groupe de données provenant du côté de l'utilisateur fonctionnel de la
frontière;
b) Tenir compte de toutes les manipulations de formatage et de présentation requises ainsi
que de toutes les validations associées des attributs de données saisis, dans la mesure
où ces manipulations de données n'impliquent pas un autre type de mouvement de
données.
REMARQUE : Une Entrée rend compte de toutes les manipulations qui pourraient être
nécessaires pour valider certains codes saisis ou pour obtenir certaines descriptions
associées.
Cependant, si une ou plusieurs Lectures sont requises dans le cadre du processus de
validation, celles-ci sont identifiées et comptabilisées comme des mouvements de
données de Lecture distincts.
c) Inclure toute fonctionnalité de « demande de réception des données d’entrée », où il n’est
pas nécessaire de spécifier les données à saisir.
### RÈGLE 17 : Sortie.
Une Sortie doit :
a) Envoyer des attributs de données à partir d'un seul groupe de données vers le côté de
l'utilisateur fonctionnel de la frontière;
b) Tenir compte de toutes les manipulations de formatage et de présentation des données
requises, y compris le traitement requis pour envoyer les attributs de données à l'utilisateur
fonctionnel, dans la mesure où ces manipulations n'impliquent pas un autre type de
mouvement de données.

### RÈGLE 18 : Lecture.
Une Lecture doit :
a) Récupérer un seul groupe de données du stockage persistant;
b) Prendre en compte tous les traitements logiques et / ou calculs mathématiques
nécessaires à la lecture des données, dans la mesure où ces manipulations n'impliquent
pas un autre type de mouvement de données;
c) Inclure toute fonctionnalité de « demande de Lecture ».

### RÈGLE 19 : éCriture.
Une éCriture doit :
a) Déplacer les attributs de données d'un groupe de données unique vers un stockage
persistant;
b) Prendre en compte tout le traitement logique et / ou le calcul mathématique pour créer les
attributs de données à éCrire, dans la mesure où ces manipulations n'impliquent pas un
autre type de mouvement de données.
### RÈGLE 20 : éCriture – Suppression.
Une exigence pour supprimer un groupe de données du stockage persistant sera un seul mouvement d'éCriture de données.

## PHASE 3 – MESURAGE.

### RÈGLE 21 : Taille d'un mouvement de données.
Une unité de mesure, 1 PFC, doit être affectée à chaque mouvement de données (Entrée, Sortie,
Lecture ou éCriture) identifié dans chaque processus fonctionnel.

### RÈGLE 22 : Taille d'un processus fonctionnel.
Les résultats de 5.2, appliqués à tous les mouvements de données identifiés au sein du processus
fonctionnel identifié, doivent être agrégés en une seule valeur de taille fonctionnelle pour ce
processus fonctionnel :
a) Multiplier le nombre de mouvements de données de chaque type par sa taille unitaire;
b) Additionner les tailles de l'étape a) pour chacun des types de mouvement de données dans le processus fonctionnel.
Taille (processus fonctionnel) = Σ taille (Entrées) + Σ taille (Sorties) + Σ taille (Lectures) + Σ taille (éCriture).

### RÈGLE 23 : Taille fonctionnelle de l’EFU identifiée de chaque logiciel à mesurer.

La taille de chaque logiciel à mesurer dans une couche doit être obtenue en agrégeant la taille des processus fonctionnels au sein de l’EFU identifiée pour chaque logiciel.
REMARQUE : Au sein de chaque couche identifiée, la fonction d'agrégation peut être entièrement
mise à l’échelle. Par conséquent, un sous-total peut être généré pour des processus fonctionnels
individuels, des éléments logiciels individuels ou pour la couche entière, selon l'objectif et le
périmètre du MTF.
### RÈGLE 24 : Taille fonctionnelle des modifications apportées à l’EFU.
Au sein de chaque couche identifiée, la taille fonctionnelle des modifications apportées à l’EFU au sein de chaque logiciel dans le cadre du MTF doit être calculée en agrégeant les tailles du mouvement de données d'impact correspondant selon la formule suivante:
Taille (modifications apportées à un logiciel) = Σ taille (ajout de mouvements de données) + Σ taille (mouvements de données modifiés) + Σ taille (mouvements de données supprimés) 
résumé sur tous les processus fonctionnels pour le logiciel.

### RÈGLE 25 : Étiquetage.
Un résultat de mesurage COSMIC sur l’EFU pour un logiciel conforme aux règles obligatoires de l'ISO 19761 doit être étiqueté selon la convention suivante :
x CFP (ISO⁄IEC 19761: 2011) [ou en français : x PFC (ISO/IEC 19761: 2011)]

### RÈGLE 26 : Documentation des résultats de mesure.
La documentation des résultats des mesures COSMIC doit comprendre les informations suivantes:
a) Identification de chaque logiciel dans le cadre du MTF (nom, identification de version ou identification de configuration).
b) Une description de l'objectif et du périmètre de mesurage.
c) Une description de la relation de chaque logiciel dans le cadre du MTF avec ses utilisateurs fonctionnels, à la fois d'égal à égal et entre les couches.
d) La taille fonctionnelle de chaque logiciel dans le cadre du MTF, calculée selon 5.2 et rapportée selon 6.

COSMIC MM – Partie 1 : Principes Définitions & Règles – MPC v1 – Copyright © 2020

### Who do I talk to? ###

* lapointe.alexandra@gmail.com