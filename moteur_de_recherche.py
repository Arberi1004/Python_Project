
#Préparation des données 

#Importation des modules nécessaires à la manipulation des fonctions
import pandas as pd

#Lecture des fichiers utiles csv en dataframe
chemin3 = input("Entrez le chemin allant de la source à Final database.csv")
spotify = pd.read_csv(chemin3,sep=",", low_memory=False)

chemin4 = input("Entrez le chemin allant de la source à Database to Calculate popularity.csv")
popu = pd.read_csv(chemin4, sep=",")

#Merge des deux dataframes
#On crée une nouvelle dataframe, nommée dop qui va conserver certaines colonnes
dop=pd.DataFrame(spotify)
dop.drop(dop.iloc[:,15:147],1,inplace=True) #je garde que jusqu'à popu_max pour pouvoir l'utiliser

#Renommer les colonnes, par souci de majuscules/miniscules
popu.rename(columns={"uri": "Uri"}, inplace=True)
popu.rename(columns={"country": "Country"}, inplace=True)

#On merge sur la gauche les deux dataframes
output2 = pd.merge(popu, dop,  
                   on=['Country','Uri'],  
                   how='left') 

#On garde que les derniers chiffres pour la date
output2['date']=output2['date'].str[-4:]



#quete1 
def quete1(titre,artiste): 
    
    if titre in list(output2.Title) and artiste in list(output2.Artist): #Si le titre au final est classé dans la base de données
        quete1=output2.loc[(output2['Title']==titre) & (output2['Artist']==artiste)] #On localise dans la dataframe
        quete1=quete1.sort_values(by=['Popu_max'], ascending=[True]) #On trie par popularité maximum
        quete1=quete1.drop(columns=['Unnamed: 0','Uri','track','Album/Single','Explicit','Genre','Top10_dummy','Top50_dummy','Cluster','danceability','energy','Release_date'])
        #a1 = position la plus haute dans le classement
        a1= list(quete1['Popu_max'])[0] #Popumax: The top position reached by a track in the 1401 days we have data for
        
        pays_top_position = []
        for i in range(0, len(list(quete1['Popu_max']))):
            if list(quete1['Popu_max'])[i] == a1:
                pays_top_position.append(list(quete1['Country'])[i])
        
        #enlevons les doublons:
        pays_top_position2 = []
        for element in pays_top_position:
            if element not in pays_top_position2:
                pays_top_position2.append(element)
                
        pays_top_position2 = str(pays_top_position2).strip('[]')
        
        pays = list(quete1['Country']) #on crée la liste pays à partir de la colonne Country
        country = []
        for i in pays:
            if i not in country:
                country.append(i)
        country.sort()
        pays_de_classement = str(country).strip('[]') #on met ici les pays où la chanson a été classée en enlevant les "[]" de la liste

        if 'Global' in country:
            return "La position la plus haute du titre dans les classements {} et il atteint cette position dans les pays suivants \n :{}".format(a1, pays_top_position2), "\n \n La chanson a été classée dans les pays suivants: {}".format(pays_de_classement), "\n \n La chanson a été classée mondialement"

        else: 
            return "La position la plus haute du titre dans les classements {} et il atteint cette position dans les pays suivants \n :{}".format(a1, pays_top_position2), "\n \n La chanson a été classée dans les pays suivants: {}".format(pays_de_classement), "\n \n La chanson na pas été classée mondialement"
        
    else: 
        return "La quête n'est pas disponible dans la base de données"
    




#quete 2 
def quete2(artiste,pays,date):
    
    if artiste in list(output2.Artist) and pays in list(output2.Country) and date in list(output2.date): 
        #on crée "quete2" qui localise l'artiste, le pays et la date souhaités (les lignes qui sont à l'intersection des 3):
        quete2=output2.loc[(output2['Artist']==artiste) & (output2['Country']==pays) &(output2['date']==date)] 
        quete2=quete2.sort_values(by=['Popularity'], ascending=[False])
        title = list(quete2['Title'])
        titre = []
        for i in title:
            if i not in titre:
                titre.append(i)
        if len(titre) == 1 : #on differencie selon s'il y a un ou plusieurs titres dans la liste de chansons classées
            a = "{} des chansons de l'artiste a été classée dans ce pays en {}".format(len(titre), date) #on indique le nombre de chansons classées
            b = "La chanson qui a été classée est la suivante : " +str(titre).strip('[]') #on affiche les chansons classées en enlevant les [] et en convertissant la liste en str
        else: 
            a = "{} des chansons de l'artiste ont été classées dans ce pays en {}".format(len(titre), date)
            b = "La liste des chansons qui ont été classées est la suivante : " +str(titre).strip('[]')
        mycolumns = ['Title','Album/Single','Popularity']
        
        return a, b
    
    else: 
        return "La quête n'est pas disponible dans la base de données"




#quete 3 
def quete3(genre,pays,annee):

    
    if genre in list(output2.Genre) and pays in list(output2.Country) and annee in list(output2.date):
        quete3=output2.loc[(output2['Genre']==genre) & (output2['Country']==pays) & (output2['date']==annee)]
        quete3=quete3.sort_values(by=['Popularity'], ascending=[False])
        quete3=quete3.drop_duplicates(subset="Title") #suppression des doublons 
        mycolumns=["position","title","artist"]
        a1 = "Les 10 chansons les plus populaires pour le genre " + genre +  " lors de l'année " + str(annee) + " sont les suivants: \n" 
        a2= list(quete3[mycolumns]['title'])[0:10]
        a6 = []
        for element in a2:
            a6.append(element)
            a6.append("\n")

        
        quete3pt2=quete3.sort_values(by=['Popularity'], ascending=[False])
        quete3pt2=quete3pt2.drop_duplicates(subset="Artist")
        mycolumn=["Artist","Artist_followers"]
        a3 = "Les 10 artistes les plus populaires pour le genre " + genre + " lors de l'année " + str(annee) + " sont les suivants: \n"
        a4 = list(quete3pt2[mycolumn]['Artist'])[0:10]
        a5 = [] #enlver si ne marche pas de meme pour les 3 lignes suivantes
        for element in a4:
            a5.append(element)
            a5.append("\n") #on fait cela pour que l'affichage sur l'interface soit plus aéré: on passe à la ligne après chaque element de la liste (c'est pas terrible dans la console mais bon sur l'interface)
                
        return a1, a6, a3, a5
        
    else: 
        return "La quête n'est pas disponible dans la base de données"





#quete 4
def quete4(artiste):
    
    dot_quete4=spotify['Album/Single']=='album' #dot_quete4 est une colonne qui retourne des False ou True selon si la condition est réalisée ou pas
    doti_quete4 = spotify[dot_quete4]

    #transformation des artistes en une liste (utile pour la fonction plus tard
    
    dotii_quete4=doti_quete4['Country']== 'Global' #doti_quete4 a 93703 lignes 
    dotiii_quete4 = doti_quete4[dotii_quete4] #dotiii_quete4 a 3288 lignes car on a gardé que les Global
    
    
    #On vire les singles qui compliquent tout et on teste d'abord only sur Global
    
    dofi = dotiii_quete4.groupby(['Album']).sum().reset_index()
    #on fait la somme des popu pour chaque album
    
    dofi = dofi.sort_values(by=['Popularity'], ascending=[False])
    #on trie par popularité 
    
    dofi.rename(columns={'Popularity': 'Somme des popularités'}, inplace=True)
    
    #on renomme la colonne popularité par son vrai nom : somme des popu'
    
    dopalo = pd.DataFrame(dofi)
    dopalo.drop(dopalo.iloc[:,2:150],1,inplace=True)
    
    #on vire les colonnes inutiles çad tt le reste à part somme des popu et album
    
    output4 = pd.merge(dotiii_quete4, dopalo,  
                       on=['Album'],  
                       how='left') 
      
    output4 = output4.sort_values(by=['Popularity'], ascending=[False])


    if artiste in list(output4.Artist):
        mycolumns = ['Album','Somme des popularités']
        quete4=output4.loc[(output4['Artist']==artiste)]
        #print(quete4[mycolumns]) : indices + 2 colonnes : 1 pour album et et 1 pour somme des popularités
        album_lpp = list(quete4[mycolumns]['Album'])[1]  
        
        chansons = []
        for i in range (0, len(list(output4['Title']))):
            if list(output4['Album'])[i] == str(album_lpp):  #on parcourt la list des albums et quand on rencontre l'album le plus populaire....: cf ligne suivante
                chansons.append(list(output4['Title'])[i])  #on ajoute dans la liste "chansons" les chansons qui sont dans l'album le plus populaire
            else:
                pass
    
        les_3_chansons_lpp = chansons[0:3]
        a = "L'album le plus populaire de {} est {}".format(artiste, album_lpp)
        b = "Les 3 chansons les plus populaire de cet album sont: {}, {} et {}.".format(les_3_chansons_lpp[0], les_3_chansons_lpp[1], les_3_chansons_lpp[2])
        return a, b
        
    else:
        return "L'artiste n'est pas dans la base de donnÃ©e."







#extension quete 4
def quete4bis(artiste, pays):

    les_pays = list(spotify['Country'])
    Pays = []
    for i in les_pays:
        if i not in Pays:
            Pays.append(i)
    
    artistes = list(spotify['Artist'])
    artist = []
    for i in artistes:
        if i not in artist:
            artist.append(i)
        
    artist_minuscules = []
    for i in range(0, len(artist)): #parcourt les artistes
        artist_minuscules.append(artist[i].lower())


    #on transforme ce qui est saisi en minuscules
    artiste_min = artiste.lower()
    if artiste_min in artist_minuscules and pays in Pays:
        dot_quete4=spotify['Album/Single']=='album' #dot_quete4 est une colonne qui retourne des False ou True selon si la condition est réalisée ou pas
        doti_quete4 = spotify[dot_quete4]
        dotii_quete4=doti_quete4['Country']== pays #on sélectionne les lignes correspondants au pays que l'on souhaite
        dotiii_quete4 = doti_quete4[dotii_quete4] 
        
        dofi = dotiii_quete4.groupby(['Album']).sum().reset_index() 
            #on fait la somme des popu pour chaque album
            
        dofi = dofi.sort_values(by=['Popularity'], ascending=[False])
            #on trie par popularitÃ© 
            
        dofi.rename(columns={'Popularity': 'Somme des popularitÃ©s'}, inplace=True)
            #on renomme la colonne popularitÃ© par son vrai nom : somme des popu'
            
        dopalo = pd.DataFrame(dofi)
        dopalo.drop(dopalo.iloc[:,2:150],1,inplace=True)
            #on vire les colonnes inutiles Ã§ad tt le reste Ã  part somme des popu et album
            
        output4 = pd.merge(dotiii_quete4, dopalo,  
                               on=['Album'],  
                               how='left') 
            
        output4 = output4.sort_values(by=['Popularity'], ascending=[False])
            
        
        mycolumns = ['Album', 'Somme des popularitÃ©s']
        
        #on doit mettre output4['Artist'] en minuscule pour pouvoir tester la condition avant la ligne album_lpp
        
        for i in range(0, len(output4['Artist'])): 
            output4['Artist'][i] = output4['Artist'][i].lower()

        
        quete4=output4.loc[(output4['Artist']==artiste_min) & (output4['Country']==pays)] 
        #print(quete4[mycolumns]) #: indices + 3 colonnes : 1 pour album, 1 pour pays et 1 pour somme des popularitÃ©s
        album_lpp = list(quete4[mycolumns]['Album'])[0]
        chansons = []
        for i in range (0, len(list(output4['Title']))):
            if list(output4['Album'])[i] == album_lpp: 
                chansons.append(list(output4['Title'])[i]) 
            else:
                pass
    
        les_3_chansons_lpp = chansons[0:3]
        a = "Dans ce pays, l'album le plus populaire de {} est {}".format(artiste, album_lpp)
        b = "Les 3 chansons les plus populaire de cet album sont: {}, {} et {}.".format(les_3_chansons_lpp[0], les_3_chansons_lpp[1], les_3_chansons_lpp[2])
        return a, b
        
    else:
        return "L'artiste et/ou le pays n'est pas dans la base de donnée."



#quete bonus
def quetebonus(releasedate):
    output2['Release_date']=output2['Release_date'].str[:4] #on ne conserve que l'année

    if releasedate in list(output2.Release_date):
        quetebonus=output2.loc[(output2['Release_date']==releasedate)]
        quetebonus=quetebonus.sort_values(by=['Popularity'], ascending=[False])
        mycols = ['title','artist','Popu_max','Country']
        queteebonus = quetebonus[mycols].drop_duplicates()
        return queteebonus.head(5)
              
    else:
        return "Aucun titre publié le jour de votre anniversaire n'a été classé dans notre classement :/"



