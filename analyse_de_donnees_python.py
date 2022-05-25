#Question 1 : Analyses de données

import pandas as pd
chemin = input("Entrez le chemin allant de la source à Final database.csv : ")
dat = pd.read_csv(chemin)
dat

chemin2 = input("Entrez le chemin allant de la source à Database to calculate popularity.csv : ")
dt = pd.read_csv(chemin2)
#on crée deux dataframes dans lesquelles on enregistre nos deux bases de données 
#on demande le chemin pour atteindre les deux bases de données pour que ce
#soit réalisable sur n'importe quel ordinateur. 

datQ1=dat.sort_values(by=['Popularity'], ascending=[False])
#on trie la base de données par ordre décroissant de popularité
#ce qui va nous aider plus tard pour extraire la chanson la plus populaire

#on fait ça pour ne conserver que les 3 premiers chiffres 
#de la colonne Release_date ce qui sera pratique pour les classer 
# entre décennies : par exemple, 201 équivaut aux années 2010
#on pourra alors différencier les chansons selon leurs décennies (201,202...)
datQ1['Release_date']=datQ1['Release_date'].str[:3]
datQ1

#pour traiter la première question concernant la france, on ne conserve
#que les lignes qui concerne le classement français
datQ1_2=datQ1['Country']==str('France')
datQ1_FR = datQ1[datQ1_2]
datQ1_FR

#On va ensuite chercher la chanson la plus populaire de chaque décennie
#On commence par extraire de notre base de données datQ1_FR uniquement les chansons
#sorties durant les années 2000 : donc Release_date=200
datQ1_FR_2=datQ1_FR['Release_date']==str(200)
datQ1_FR_2000 = datQ1_FR[datQ1_FR_2]
datQ1_FR_2000

#comme la base de données a au prélable été classé par ordre décroissant de 
#popularité, la chanson la plus populaire se trouve en haut du document
#on peut alors extraire la chanson la plus populaire sortie durant les années
#2000 dans le classement français en extrayant la première ligne de 
#datQ1_FR_2000 qu'on enregistre dans une variable nommmée décennie2000FR
decennie2000FR = datQ1_FR_2000.head(1)
decennie2000FR

#On va alors faire ça pour chacune des décennies (allant de 1940 à 2020)
#On commence par les années 2010
datQ1_FR_3=datQ1_FR['Release_date']==str(201)
datQ1_FR_2010 = datQ1_FR[datQ1_FR_3]
datQ1_FR_2010

decennie2010FR = datQ1_FR_2010.head(1)
decennie2010FR

#Puis les années 2020 etc..
datQ1_FR_4=datQ1_FR['Release_date']==str(202)
datQ1_FR_2020 = datQ1_FR[datQ1_FR_4]
datQ1_FR_2020

decennie2020FR = datQ1_FR_2020.head(1)
decennie2020FR

datQ1_FR_5=datQ1_FR['Release_date']==str(199)
datQ1_FR_1990 = datQ1_FR[datQ1_FR_5]
datQ1_FR_1990

decennie1990FR = datQ1_FR_1990.head(1)
decennie1990FR

datQ1_FR_6=datQ1_FR['Release_date']==str(198)
datQ1_FR_1980 = datQ1_FR[datQ1_FR_6]
datQ1_FR_1980

decennie1980FR = datQ1_FR_1980.head(1)
decennie1980FR

datQ1_FR_7=datQ1_FR['Release_date']==str(197)
datQ1_FR_1970 = datQ1_FR[datQ1_FR_7]
datQ1_FR_1970

decennie1970FR = datQ1_FR_1970.head(1)
decennie1970FR

datQ1_FR_8=datQ1_FR['Release_date']==str(196)
datQ1_FR_1960 = datQ1_FR[datQ1_FR_8]
datQ1_FR_1960

decennie1960FR = datQ1_FR_1960.head(1)
decennie1960FR

datQ1_FR_9=datQ1_FR['Release_date']==str(195)
datQ1_FR_1950 = datQ1_FR[datQ1_FR_9]
datQ1_FR_1950

decennie1950FR = datQ1_FR_1950.head(1)
decennie1950FR

datQ1_FR_10=datQ1_FR['Release_date']==str(194)
datQ1_FR_1940 = datQ1_FR[datQ1_FR_10]
datQ1_FR_1940

decennie1940FR = datQ1_FR_1940.head(1)
decennie1940FR

#On a donc enregistré dans des variables, chacune des chansons les plus
#populaires pour chaque décennie 
#Donc, pour faire apparaitre les chansons les plus populaires pour chaque 
#décennie du classement français, il suffit de les concaténer en un seul 
#document
analysedecennieFR = pd.concat((decennie1940FR, decennie1950FR, decennie1960FR, decennie1970FR, decennie1980FR, decennie1990FR, decennie2000FR, decennie2010FR, decennie2020FR), axis=0)
analysedecennieFR
#Le document affichera donc les chansons les plus populaires 
#sorties pour chacune des différentes décennies dans le classement français
#pendant la période étudiée

analysedecennieFR['Release_date'] = analysedecennieFR['Release_date'] + '0'
analysedecennieFR
#on peut ajouter ces lignes pour avoir les vrais valeurs des décennies
#(1940,1950...) au lieu des valeurs tels que 194,195 mais cela revient au même

#On peut alors réaliser un graphique pour voir l'évolution de la popularité
#des titres les plus populaires de chaque décennie
#On va donc réaliser un diagramme par barres qui montrera l'évolution
#de la popularité du titre le plus populaire qui est sortie durant chacune
#des décennies allant de 1940 à 2020 durant notre période étudiée.
import seaborn as sns
import matplotlib.pyplot as plt
#on importe d'abord les librarys nécessaires pour cela
fig = sns.catplot(x="Release_date", y="Popularity", kind="bar", data=analysedecennieFR, palette="autumn_r")
fig.fig.get_axes()[0].set_yscale('log')
fig.set(title = "Evolution des chansons les plus populaires en France à travers les décennies")
plt.plot

#On utilisera alors le même processus pour le classement des USA ainsi que 
#le classement Global.
datQ1_3=datQ1['Country']==str('Global')
datQ1_GLOBAL = datQ1[datQ1_3]

datQ1_GLOBAL_2=datQ1_GLOBAL['Release_date']==str(202)
datQ1_GLOBAL_2020 = datQ1_GLOBAL[datQ1_GLOBAL_2]
datQ1_GLOBAL_2020

decennie2020GLOBAL = datQ1_GLOBAL_2020.head(1)
decennie2020GLOBAL

datQ1_GLOBAL_3=datQ1_GLOBAL['Release_date']==str(201)
datQ1_GLOBAL_2010 = datQ1_GLOBAL[datQ1_GLOBAL_3]
datQ1_GLOBAL_2010

decennie2010GLOBAL = datQ1_GLOBAL_2010.head(1)
decennie2010GLOBAL

datQ1_GLOBAL_4=datQ1_GLOBAL['Release_date']==str(200)
datQ1_GLOBAL_2000 = datQ1_GLOBAL[datQ1_GLOBAL_4]
datQ1_GLOBAL_2000

decennie2000GLOBAL = datQ1_GLOBAL_2000.head(1)
decennie2000GLOBAL

datQ1_GLOBAL_5=datQ1_GLOBAL['Release_date']==str(199)
datQ1_GLOBAL_1990 = datQ1_GLOBAL[datQ1_GLOBAL_5]
datQ1_GLOBAL_1990

decennie1990GLOBAL = datQ1_GLOBAL_1990.head(1)
decennie1990GLOBAL

datQ1_GLOBAL_6=datQ1_GLOBAL['Release_date']==str(198)
datQ1_GLOBAL_1980 = datQ1_GLOBAL[datQ1_GLOBAL_6]
datQ1_GLOBAL_1980

decennie1980GLOBAL = datQ1_GLOBAL_1980.head(1)
decennie1980GLOBAL

datQ1_GLOBAL_7=datQ1_GLOBAL['Release_date']==str(197)
datQ1_GLOBAL_1970 = datQ1_GLOBAL[datQ1_GLOBAL_7]
datQ1_GLOBAL_1970

decennie1970GLOBAL = datQ1_GLOBAL_1970.head(1)
decennie1970GLOBAL

datQ1_GLOBAL_8=datQ1_GLOBAL['Release_date']==str(196)
datQ1_GLOBAL_1960 = datQ1_GLOBAL[datQ1_GLOBAL_8]
datQ1_GLOBAL_1960

decennie1960GLOBAL = datQ1_GLOBAL_1960.head(1)
decennie1960GLOBAL

datQ1_GLOBAL_9=datQ1_GLOBAL['Release_date']==str(195)
datQ1_GLOBAL_1950 = datQ1_GLOBAL[datQ1_GLOBAL_9]
datQ1_GLOBAL_1950

decennie1950GLOBAL = datQ1_GLOBAL_1950.head(1)
decennie1950GLOBAL

datQ1_GLOBAL_10=datQ1_GLOBAL['Release_date']==str(194)
datQ1_GLOBAL_1940 = datQ1_GLOBAL[datQ1_GLOBAL_10]
datQ1_GLOBAL_1940

decennie1940GLOBAL = datQ1_GLOBAL_1940.head(1)
decennie1940GLOBAL

analysedecennieGLOBAL = pd.concat((decennie1940GLOBAL, decennie1950GLOBAL, decennie1960GLOBAL, decennie1970GLOBAL, decennie1980GLOBAL, decennie1990GLOBAL, decennie2000GLOBAL, decennie2010GLOBAL, decennie2020GLOBAL), axis=0)
analysedecennieGLOBAL

analysedecennieGLOBAL['Release_date'] = analysedecennieGLOBAL['Release_date'] + '0'

fig = sns.catplot(x="Release_date", y="Popularity", kind="bar", data=analysedecennieGLOBAL, palette="autumn_r")
fig.fig.get_axes()[0].set_yscale('log')
fig.set(title = "Evolution des chansons les plus populaires du classement Global à travers les décennies")
plt.plot
#On obtient alors un graphique pour le classement global

#On finit par faire cela pour le classement des USA.
datQ1_4=datQ1['Country']==str('USA')
datQ1_USA = datQ1[datQ1_4]
datQ1_USA

datQ1_USA_2=datQ1_USA['Release_date']==str(202)
datQ1_USA_2020 = datQ1_USA[datQ1_USA_2]
datQ1_USA_2020

decennie2020USA = datQ1_USA_2020.head(1)
decennie2020USA

datQ1_USA_3=datQ1_USA['Release_date']==str(201)
datQ1_USA_2010 = datQ1_USA[datQ1_USA_3]
datQ1_USA_2010

decennie2010USA = datQ1_USA_2010.head(1)
decennie2010USA

datQ1_USA_4=datQ1_USA['Release_date']==str(200)
datQ1_USA_2000 = datQ1_USA[datQ1_USA_4]
datQ1_USA_2000

decennie2000USA = datQ1_USA_2000.head(1)
decennie2000USA

datQ1_USA_5=datQ1_USA['Release_date']==str(199)
datQ1_USA_1990 = datQ1_USA[datQ1_USA_5]
datQ1_USA_1990

decennie1990USA = datQ1_USA_1990.head(1)
decennie1990USA

datQ1_USA_6=datQ1_USA['Release_date']==str(198)
datQ1_USA_1980 = datQ1_USA[datQ1_USA_6]
datQ1_USA_1980

decennie1980USA = datQ1_USA_1980.head(1)
decennie1980USA

datQ1_USA_7=datQ1_USA['Release_date']==str(197)
datQ1_USA_1970 = datQ1_USA[datQ1_USA_7]
datQ1_USA_1970

decennie1970USA = datQ1_USA_1970.head(1)
decennie1970USA

datQ1_USA_8=datQ1_USA['Release_date']==str(196)
datQ1_USA_1960 = datQ1_USA[datQ1_USA_8]
datQ1_USA_1960

decennie1960USA = datQ1_USA_1960.head(1)
decennie1960USA

datQ1_USA_9=datQ1_USA['Release_date']==str(195)
datQ1_USA_1950 = datQ1_USA[datQ1_USA_9]
datQ1_USA_1950

decennie1950USA = datQ1_USA_1950.head(1)
decennie1950USA

datQ1_USA_10=datQ1_USA['Release_date']==str(194)
datQ1_USA_1940 = datQ1_USA[datQ1_USA_10]
datQ1_USA_1940

decennie1940USA = datQ1_USA_1940.head(1)
decennie1940USA

analysedecennieUSA = pd.concat((decennie1940USA, decennie1950USA, decennie1960USA, decennie1970USA, decennie1980USA, decennie1990USA, decennie2000USA, decennie2010USA, decennie2020USA), axis=0)
analysedecennieUSA

analysedecennieUSA['Release_date'] = analysedecennieUSA['Release_date'] + '0'

fig = sns.catplot(x="Release_date", y="Popularity", kind="bar", data=analysedecennieUSA, palette="autumn_r")
fig.fig.get_axes()[0].set_yscale('log')
fig.set(title = "Evolution des chansons les plus populaires du classement des USA à travers les décennies")
plt.plot


#Question 2 : Analyse de données 


dat2 = pd.DataFrame(dat)
dat2.drop(dat2.iloc[:,10:147],1,inplace=True)
dat2
#on enlève les colonnes qui ne nous seront pas utiles pour répondre à cette question

dt.rename(columns={'uri': 'Uri'}, inplace=True)
dt.rename(columns={'country': 'Country'}, inplace=True)
dt
#on renomme ajoute des majuscules à deux de nos colonnes : en faisant cela, on prépare une jointure entre les deux
#bases de données par une clef de jointure composée à la fois de Country et Uri (ce qui n'est possible 
#que si les deux colonnes ont le même titre)

dt_dat = pd.merge(dt, dat2,  
                   on=['Country','Uri'],  
                   how='left') 
  
dt_dat
#on réalise une jointure composée ers la gauche entre nos deux bases de données en se basant sur une clef de jointure
#qui a donc pour deux composants "Uri" (pour différencier les chansons et "Country" (pour différencier les mêmes chansons
#classées dans plusieurs pays)

dt_dat2=dt_dat['position']<=10.0
filtered_dt_dat = dt_dat[dt_dat2]
filtered_dt_dat
#On élimine l'ensemble des titres qui ne sont pas dans le top10 d'un classement tous pays confondus 
#cela va nous permettre de classer les différents genres entre eux : plus un titre a de top10, plus il est populaire

filtered_dt_dat['date']=filtered_dt_dat['date'].str[6:]
filtered_dt_dat
#on modifie supprime les 6 premières valeurs de la colonne date : une fois cela fait, on pourra différencier 
#les différents titres selon les années dans lesquelles ils ont été classés

filtered_dt_dat3=filtered_dt_dat['date']==str(2017)
filtered_dt_dat2017 = filtered_dt_dat[filtered_dt_dat3]
filtered_dt_dat2017

filtered_dt_dat2=filtered_dt_dat['date']==str(2018)
filtered_dt_dat2018 = filtered_dt_dat[filtered_dt_dat2]
filtered_dt_dat2018

filtered_dt_dat4=filtered_dt_dat['date']==str(2019)
filtered_dt_dat2019 = filtered_dt_dat[filtered_dt_dat4]
filtered_dt_dat2019

filtered_dt_dat5=filtered_dt_dat['date']==str(2020)
filtered_dt_dat2020 = filtered_dt_dat[filtered_dt_dat5]
filtered_dt_dat2020
#on crée différentes dataframes dans lesquelles on enregistre respectivement toutes les chansons classées
#d'une certaine année


#On doit donc séparer chacune de ces dataframes en fonction de leur cluster
#On commence alors par l'année 2017
filtered_dt_dat2017_2=filtered_dt_dat2017['Cluster']==str('spanish speaking')
filtered_dt_dat2017_spanish_speaking = filtered_dt_dat2017[filtered_dt_dat2017_2]
filtered_dt_dat2017_spanish_speaking

filtered_dt_dat2017_3=filtered_dt_dat2017['Cluster']==str('english speaking and nordic')
filtered_dt_dat2017_english_speaking_and_nordic = filtered_dt_dat2017[filtered_dt_dat2017_3]
filtered_dt_dat2017_english_speaking_and_nordic

filtered_dt_dat2017_4=filtered_dt_dat2017['Cluster']==str('southern europe and portuguese heritage')
filtered_dt_dat2017_southern_europe_and_portuguese_heritage = filtered_dt_dat2017[filtered_dt_dat2017_4]
filtered_dt_dat2017_southern_europe_and_portuguese_heritage

filtered_dt_dat2017_5=filtered_dt_dat2017['Cluster']==str('global')
filtered_dt_dat2017_global = filtered_dt_dat2017[filtered_dt_dat2017_5]
filtered_dt_dat2017_global

spanish_speaking2017 = filtered_dt_dat2017_spanish_speaking['Genre'].value_counts().to_frame().reset_index()
english_speaking_and_nordic2017 = filtered_dt_dat2017_english_speaking_and_nordic['Genre'].value_counts().to_frame().reset_index()
southern_europe_and_portuguese_heritage2017 = filtered_dt_dat2017_southern_europe_and_portuguese_heritage['Genre'].value_counts().to_frame().reset_index()
global2017 = filtered_dt_dat2017_global['Genre'].value_counts().to_frame().reset_index()
#on enregistre alors dans de nouvelles variables le dénombrement de l'occurence de chaque genre dans chacun des documents 
#en faisant cela, on va voir quels sont les genres qui ont le plus de titres passées dans le top10 pour chaque cluster.

spanish_speaking2017.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
spanish_speaking2017.rename(columns={'index': 'Genre'}, inplace=True)
spanish_speaking2017

english_speaking_and_nordic2017.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
english_speaking_and_nordic2017.rename(columns={'index': 'Genre'}, inplace=True)
english_speaking_and_nordic2017

southern_europe_and_portuguese_heritage2017.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
southern_europe_and_portuguese_heritage2017.rename(columns={'index': 'Genre'}, inplace=True)
southern_europe_and_portuguese_heritage2017

global2017.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
global2017.rename(columns={'index': 'Genre'}, inplace=True)
global2017
#on modifie ici le nom des colonnes de sorte à avoir quelque chose de plus clair : on obtient, pour chaque genre,
#le nombre de jours passées par tous les titres de ce genre dans le top10 de tous nos classements confondus.

#on va alors modifier nos nouvelles dataframes : on ne va conserver que les 10 premières valeurs pour conserver un graphique
#lisible.
spanish_speaking2017 = spanish_speaking2017.head(10)
english_speaking_and_nordic2017 = english_speaking_and_nordic2017.head(10)
southern_europe_and_portuguese_heritage2017 = southern_europe_and_portuguese_heritage2017.head(10)
global2017 = global2017.head(10)

#on peut alors enfin passer à la réalisation de nos diagrammes circulaires pour chacun des clusters de l'année 2017

plt.pie(spanish_speaking2017['Comptabilisation du nombre de top10'], labels=spanish_speaking2017['Genre'])
plt.title('Distribution des genres du cluster "spanish speaking" en 2017')
plt.show

plt.pie(english_speaking_and_nordic2017['Comptabilisation du nombre de top10'], labels=english_speaking_and_nordic2017['Genre'])
plt.title('Distribution des genres du cluster "english speaking and nordic" en 2017')
plt.show

plt.pie(southern_europe_and_portuguese_heritage2017['Comptabilisation du nombre de top10'], labels=southern_europe_and_portuguese_heritage2017['Genre'])
plt.title('Distribution des genres du cluster "southern europe and portuguese" en 2017')
plt.show

plt.pie(global2017['Comptabilisation du nombre de top10'], labels=global2017['Genre'])
plt.title('Distribution des genres du cluster "global" en 2017')
plt.show

#On réalise alors la même chose pour toutes les autres années
#en commençant par 2018
filtered_dt_dat2=filtered_dt_dat['date']==str(2018)
filtered_dt_dat2018 = filtered_dt_dat[filtered_dt_dat2]
filtered_dt_dat2018


filtered_dt_dat2018_2=filtered_dt_dat2018['Cluster']==str('spanish speaking')
filtered_dt_dat2018_spanish_speaking = filtered_dt_dat2018[filtered_dt_dat2018_2]

filtered_dt_dat2018_3=filtered_dt_dat2018['Cluster']==str('english speaking and nordic')
filtered_dt_dat2018_english_speaking_and_nordic = filtered_dt_dat2018[filtered_dt_dat2018_3]

filtered_dt_dat2018_4=filtered_dt_dat2018['Cluster']==str('southern europe and portuguese heritage')
filtered_dt_dat2018_southern_europe_and_portuguese_heritage = filtered_dt_dat2018[filtered_dt_dat2018_4]

filtered_dt_dat2018_5=filtered_dt_dat2018['Cluster']==str('global')
filtered_dt_dat2018_global = filtered_dt_dat2018[filtered_dt_dat2018_5]
filtered_dt_dat2018_global


spanish_speaking2018 = filtered_dt_dat2018_spanish_speaking['Genre'].value_counts().to_frame().reset_index()
english_speaking_and_nordic2018 = filtered_dt_dat2018_english_speaking_and_nordic['Genre'].value_counts().to_frame().reset_index()
southern_europe_and_portuguese_heritage2018 = filtered_dt_dat2018_southern_europe_and_portuguese_heritage['Genre'].value_counts().to_frame().reset_index()
global2018 = filtered_dt_dat2018_global['Genre'].value_counts().to_frame().reset_index()
#on enregistre alors dans de nouvelles variables le dénombrement de l'occurence de chaque genre dans chacun des documents 
#en faisant cela, on va voir quels sont les genres qui ont le plus de titres passées dans le top10 pour chaque cluster.

spanish_speaking2018.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
spanish_speaking2018.rename(columns={'index': 'Genre'}, inplace=True)


english_speaking_and_nordic2018.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
english_speaking_and_nordic2018.rename(columns={'index': 'Genre'}, inplace=True)

southern_europe_and_portuguese_heritage2018.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
southern_europe_and_portuguese_heritage2018.rename(columns={'index': 'Genre'}, inplace=True)
southern_europe_and_portuguese_heritage2018

global2018.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
global2018.rename(columns={'index': 'Genre'}, inplace=True)
global2018

spanish_speaking2018 = spanish_speaking2018.head(10)
english_speaking_and_nordic2018 = english_speaking_and_nordic2018.head(10)
southern_europe_and_portuguese_heritage2018 = southern_europe_and_portuguese_heritage2018.head(10)
global2018 = global2018.head(10)


plt.pie(spanish_speaking2018['Comptabilisation du nombre de top10'], labels=spanish_speaking2018['Genre'])
plt.title('Distribution des genres du cluster "spanish speaking" en 2018')
plt.show

plt.pie(english_speaking_and_nordic2018['Comptabilisation du nombre de top10'], labels=english_speaking_and_nordic2018['Genre'])
plt.title('Distribution des genres du cluster "english speaking and nordic" en 2018')
plt.show

plt.pie(southern_europe_and_portuguese_heritage2018['Comptabilisation du nombre de top10'], labels=southern_europe_and_portuguese_heritage2018['Genre'])
plt.title('Distribution des genres du cluster "southern europe and portuguese" en 2018')
plt.show

plt.pie(global2018['Comptabilisation du nombre de top10'], labels=global2018['Genre'])
plt.title('Distribution des genres du cluster "global" en 2018')
plt.show

#Puis pour l'année 2019
filtered_dt_dat3=filtered_dt_dat['date']==str(2019)
filtered_dt_dat2019 = filtered_dt_dat[filtered_dt_dat3]
filtered_dt_dat2019

filtered_dt_dat2019_2=filtered_dt_dat2019['Cluster']==str('spanish speaking')
filtered_dt_dat2019_spanish_speaking = filtered_dt_dat2019[filtered_dt_dat2019_2]

filtered_dt_dat2019_3=filtered_dt_dat2019['Cluster']==str('english speaking and nordic')
filtered_dt_dat2019_english_speaking_and_nordic = filtered_dt_dat2019[filtered_dt_dat2019_3]

filtered_dt_dat2019_4=filtered_dt_dat2019['Cluster']==str('southern europe and portuguese heritage')
filtered_dt_dat2019_southern_europe_and_portuguese_heritage = filtered_dt_dat2019[filtered_dt_dat2019_4]

filtered_dt_dat2019_5=filtered_dt_dat2019['Cluster']==str('global')
filtered_dt_dat2019_global = filtered_dt_dat2019[filtered_dt_dat2019_5]
filtered_dt_dat2019_global

spanish_speaking2019 = filtered_dt_dat2019_spanish_speaking['Genre'].value_counts().to_frame().reset_index()
english_speaking_and_nordic2019 = filtered_dt_dat2019_english_speaking_and_nordic['Genre'].value_counts().to_frame().reset_index()
southern_europe_and_portuguese_heritage2019 = filtered_dt_dat2019_southern_europe_and_portuguese_heritage['Genre'].value_counts().to_frame().reset_index()
global2019 = filtered_dt_dat2019_global['Genre'].value_counts().to_frame().reset_index()
#on enregistre alors dans de nouvelles variables le dénombrement de l'occurence de chaque genre dans chacun des documents 
#en faisant cela, on va voir quels sont les genres qui ont le plus de titres passées dans le top10 pour chaque cluster.

spanish_speaking2019.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
spanish_speaking2019.rename(columns={'index': 'Genre'}, inplace=True)


english_speaking_and_nordic2019.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
english_speaking_and_nordic2019.rename(columns={'index': 'Genre'}, inplace=True)

southern_europe_and_portuguese_heritage2019.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
southern_europe_and_portuguese_heritage2019.rename(columns={'index': 'Genre'}, inplace=True)
southern_europe_and_portuguese_heritage2019

global2019.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
global2019.rename(columns={'index': 'Genre'}, inplace=True)
global2019

spanish_speaking2019 = spanish_speaking2019.head(10)
english_speaking_and_nordic2019 = english_speaking_and_nordic2019.head(10)
southern_europe_and_portuguese_heritage2019 = southern_europe_and_portuguese_heritage2019.head(10)
global2019 = global2019.head(10)

plt.pie(spanish_speaking2019['Comptabilisation du nombre de top10'], labels=spanish_speaking2019['Genre'])
plt.title('Distribution des genres du cluster "spanish speaking" en 2019')
plt.show

plt.pie(english_speaking_and_nordic2019['Comptabilisation du nombre de top10'], labels=english_speaking_and_nordic2019['Genre'])
plt.title('Distribution des genres du cluster "english speaking and nordic" en 2019')
plt.show

plt.pie(southern_europe_and_portuguese_heritage2019['Comptabilisation du nombre de top10'], labels=southern_europe_and_portuguese_heritage2019['Genre'])
plt.title('Distribution des genres du cluster "southern europe and portuguese" en 2019')
plt.show

plt.pie(global2019['Comptabilisation du nombre de top10'], labels=global2019['Genre'])
plt.title('Distribution des genres du cluster "global" en 2019')
plt.show

filtered_dt_dat5=filtered_dt_dat['date']==str(2020)
filtered_dt_dat2020 = filtered_dt_dat[filtered_dt_dat5]
filtered_dt_dat2020

filtered_dt_dat2020_2=filtered_dt_dat2020['Cluster']==str('spanish speaking')
filtered_dt_dat2020_spanish_speaking = filtered_dt_dat2020[filtered_dt_dat2020_2]
filtered_dt_dat2020_spanish_speaking

filtered_dt_dat2020_3=filtered_dt_dat2020['Cluster']==str('english speaking and nordic')
filtered_dt_dat2020_english_speaking_and_nordic = filtered_dt_dat2020[filtered_dt_dat2020_3]
filtered_dt_dat2020_english_speaking_and_nordic

filtered_dt_dat2020_4=filtered_dt_dat2020['Cluster']==str('southern europe and portuguese heritage')
filtered_dt_dat2020_southern_europe_and_portuguese_heritage = filtered_dt_dat2020[filtered_dt_dat2020_4]
filtered_dt_dat2020_southern_europe_and_portuguese_heritage

filtered_dt_dat2020_5=filtered_dt_dat2020['Cluster']==str('global')
filtered_dt_dat2020_global = filtered_dt_dat2020[filtered_dt_dat2020_5]
filtered_dt_dat2020_global

spanish_speaking2020 = filtered_dt_dat2020_spanish_speaking['Genre'].value_counts().to_frame().reset_index()
english_speaking_and_nordic2020 = filtered_dt_dat2020_english_speaking_and_nordic['Genre'].value_counts().to_frame().reset_index()
southern_europe_and_portuguese_heritage2020 = filtered_dt_dat2020_southern_europe_and_portuguese_heritage['Genre'].value_counts().to_frame().reset_index()
global2020 = filtered_dt_dat2020_global['Genre'].value_counts().to_frame().reset_index()
#on enregistre alors dans de nouvelles variables le dénombrement de l'occurence de chaque genre dans chacun des documents 
#en faisant cela, on va voir quels sont les genres qui ont le plus de titres passées dans le top10 pour chaque cluster.

spanish_speaking2020.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
spanish_speaking2020.rename(columns={'index': 'Genre'}, inplace=True)
spanish_speaking2020

english_speaking_and_nordic2020.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
english_speaking_and_nordic2020.rename(columns={'index': 'Genre'}, inplace=True)
english_speaking_and_nordic2020

southern_europe_and_portuguese_heritage2020.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
southern_europe_and_portuguese_heritage2020.rename(columns={'index': 'Genre'}, inplace=True)
southern_europe_and_portuguese_heritage2020

global2020.rename(columns={'Genre': 'Comptabilisation du nombre de top10'}, inplace=True)
global2020.rename(columns={'index': 'Genre'}, inplace=True)
global2020
#on modifie

global2020=global2020.head(10)
southern_europe_and_portuguese_heritage2020 = southern_europe_and_portuguese_heritage2020.head(10)
english_speaking_and_nordic2020 = english_speaking_and_nordic2020.head(10)
spanish_speaking2020 = spanish_speaking2020.head(10)


plt.pie(english_speaking_and_nordic2020['Comptabilisation du nombre de top10'], labels=english_speaking_and_nordic2020['Genre'])
plt.title('Distribution des genres du cluster "english speaking" en 2020')
plt.show

plt.pie(global2020['Comptabilisation du nombre de top10'], labels=global2020['Genre'])
plt.title('Distribution des genres du cluster "global" en 2020')
plt.show

plt.pie(southern_europe_and_portuguese_heritage2020['Comptabilisation du nombre de top10'], labels=southern_europe_and_portuguese_heritage2020['Genre'])
plt.title('Distribution des genres du cluster "southern europe and portuguese" en 2020')
plt.show

plt.pie(spanish_speaking2020['Comptabilisation du nombre de top10'], labels=spanish_speaking2020['Genre'])
plt.title('Distribution des genres du cluster "spanish speaking" en 2020')
plt.show

#Question 3 : Analyse de données
dat = dat.sort_values(by=['Popularity'], ascending=[True])
#on trie notre document par ordre décroissant pour que les titres les plus populaires soient en haut du document

#on se base sur un dot trié par popularité mais ça a aucune incidence sur le résultat final -> on peut en changer.
dat_q3=dat['Top50_dummy']==1.0
filtered_dat_bytop50 = dat[dat_q3]
filtered_dat_bytop50

dat_q3_2=dat['Top10_dummy']==1.0
filtered_dat_bytop10 = dat[dat_q3_2]
filtered_dat_bytop10
#on ne conserve que les données du document global qui ont déjà atteint le top50 puis le top10 tous classements confondus

value_count_filtered_dat_bytop50 = filtered_dat_bytop50['Artist'].value_counts()
value_count_filtered_dat_bytop10 = filtered_dat_bytop10['Artist'].value_counts()
#on enregistre dans les dataframes respectives
#le décompte du nombre d'occurences de chaque artiste dans nos documents (ce qui correspond respectivement au nombre
#titres que chaque artiste présent dans cette liste ont déjà atteint respectivement le top10 ou le top50 tous classements
#confondus)

#on peut alors faire apparaitre les 10 artistes qui dominent ces deux décomptes comme demandé
value_count_filtered_dat_bytop50.head(10)
value_count_filtered_dat_bytop10.head(10)

#On peut alors faire la même chose pour le classement français comme demandé, en filtrant la base de données initiale de 
#telle sorte à ne conserver que le classement français
dat_q3_FR=dat['Country']=='France'
filtered_dat_byFR = dat[dat_q3_FR]

dat_q3_FR=filtered_dat_byFR['Top50_dummy']==1.0
filtered_dat_bytop50_FR = filtered_dat_byFR[dat_q3_FR]

dat_q3_FR_2=filtered_dat_byFR['Top10_dummy']==1.0
filtered_dat_bytop10_FR = filtered_dat_byFR[dat_q3_FR_2]

value_count_filtered_dat_bytop50_FR = filtered_dat_bytop50_FR['Artist'].value_counts()
value_count_filtered_dat_bytop10_FR = filtered_dat_bytop10_FR['Artist'].value_counts()

value_count_filtered_dat_bytop50_FR.head(10)
value_count_filtered_dat_bytop10_FR.head(10)

#Question 4 : Analyse de données

#on va tout d'abord filtrer la base de données Databse to calculate popularity de façon à ne conserver 
#que le classement global qui nous concerne dans cette question.
dt_2=dt['Country']=='Global'
dt_global = dt[dt_2]

value_count_dt_global = dt_global['track'].value_counts()
#on dénombre ensuite le nombre d'occurences de chacune des tracks dans cette base de données : ainsi, si une chanson 
#obtiendra une valeur de 100, elle aura passé 100 jours dans le classement global vu qu'une ligne correspond à une journée
#on privilégie la colonne "track" et non "title" car plusieurs titres peuvent avoir le même titre ce qui est impossible 
#dans le cas de la colonne "track"

value_count_dt_global.head(1)
#on affiche premier de ce classement : ce sera donc la chanson qui aura placé le plus de temps dans le classement Global

##Partie Graphique

#pour réaliser le graphique, on va notre base de données qui ne contient que le classement global de telle sorte à ne 
#conserver que les classement de la chanson numéro un précédemment : shape of you de Ed Sheeran
#pour la localiser, on utilise le lien spotify qui permet d'obtenir cette chanson.
dt_global_2=dt_global['Uri']=='https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3'
dt_global_shapeofyou = dt_global[dt_global_2]
dt_global_shapeofyou

#ensuite je réalise un tri des colonnes de sorte à avoir uniquement les colonnes date et position 
#qui sont celles qui me seront nécessaires pour la réalisation de ce graphique
dt_global_shapeofyou_2 = pd.DataFrame(dt_global_shapeofyou)
dt_global_shapeofyou_2.drop(dt_global_shapeofyou_2.iloc[:,0:2],1,inplace=True)
dt_global_shapeofyou_2

dt_global_shapeofyou_3 = pd.DataFrame(dt_global_shapeofyou_2)
dt_global_shapeofyou_3.drop(dt_global_shapeofyou_3.iloc[:,2:6],1,inplace=True)
dt_global_shapeofyou_3

#on transforme tout cela en un nouveau fichier csv
dt_global_shapeofyou_3.to_csv('graphiqueQ4.csv')

#A partir de ce ficher csv nouvellement créee, on peut réaliser un basic plot 
import matplotlib.pyplot as plt
import pandas as pd

graph = pd.read_csv('graphiqueQ4.csv')

plt.figure(figsize=(20, 12))
x = range(len(graph['date']))
plt.plot(x, graph['position'])
plt.xticks(x, graph['date'])
plt.xlabel('date')
plt.ylabel('position')

#On inverse ensuite les deux axes pour avoir une évolution chronologique
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.title('Evolution de Shape of you dans le classement global durant la période')
plt.show()