# Dummy comment

#Job01
class Personne():
    "Personne"
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        print('Salut! mon  Nom: ', self.nom, 'Prénom: ', self.prenom)


#Job 02.718

class Auteur(Personne):
    "Auteur"
    def __init__(self, nom, prenom= None):
        super().__init__(nom, prenom)
        self.oeuvre= []
    def listerOeuvre(self):
        print('Les oeuvres dans cette liste: ')
        for item in self.oeuvre:
            print(item)
        return self.oeuvre
    def ecrireUnLivre(self, inp_titre):
        liv= Livre(inp_titre, self)
        #liv.titre= inp_titre
        self.oeuvre.append(liv.titre)



#print(A_1.nom, A_1.oeuvres)
class Livre():
    "Livre"
    def __init__(self, titre, auteur):
        self.titre= titre
        self.auteur= auteur
    def show_title(self):
        print('Titre: ', self.titre)
    def __str__(self):
        return self.titre
    def __repr__(self):
        return self.titre



#Job 07.389
class Bibliotheque():
    "Bibliotheque"
    def __init__(self, nom):
        self.nom= nom
        self.catalogue={}
    def acheter_livre(self, o_auteur, tit_livre, nb_livre):
        if tit_livre in o_auteur.listerOeuvre():
            self.catalogue[tit_livre]=nb_livre
    def inventaire(self):
        for key in self.catalogue:
            print('Titre: ', key, ', quantité: ', self.catalogue[key])
    def louer(self, o_client, tit_liv):
        #print('tit_liv is: ', type(tit_liv))
        #print('self.catalogue: ', type(list(self.catalogue.keys())[0]))
        #print(tit_liv in list(self.catalogue.keys()))
        if tit_liv in list(self.catalogue.keys()):
            print('!!!!!!!!!I entered louer!')
            o_client.collection.append(tit_liv)
            self.catalogue[tit_liv]-=1

    def rendre(self, o_client):
        for item in o_client.collection:
            if item in list(self.catalogue.keys()):
                self.catalogue[item]+=1
            else:
                self.catalogue[item]=1





class Client(Personne):
    "Client"
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)

        self.collection= []
    def list_collections(self):
        print('Titres: ')
        for item in self.collection:
            print(item)

#Job 20.085
import pandas as pd
class Board():
    "Board"
    def __init__(self, i, j):
        self.i= i
        self.j= j
        my_dict= {}
        for item in range(j):
            my_dict[item]= i*['O']
        df= pd.DataFrame(data= my_dict)
        self.tab= df
    def play(self, n, s):
        #n= column in which the player throw his coin
        #s= colour of the coin red or yellow
        df= self.tab
        for k in range(self.i-1, -1,-1):
            if df[n][k]=='O':
                df[n][k]=s
                break
        #print('Player using colour', s, ' chose column: ', n)
        self.tab= df
    def print_tab(self):
        print(self.tab)
    #def winner(self):
