from main import *

'''A_1= Auteur()
A_1.nom= 'Cohello'
A_1.prenom= 'Paulo'
L_1= Livre()
L_1.titre= 'Alchimiste'
L_1.auteur= A_1
A_1.ecrireUnLivre('Zahir')
L_1.show_title()
A_1.listerOeuvre()

bib= Bibliotheque()
print(bib.__doc__)
'''
#catalogue= {livre: 1}
print('Bienvenue au jeu de puissance 4!')
i= int(input('Entrer le nombre de lignes de votre board: '))
j= int(input('Entrer le nombre de colonnes de votre board: '))
my_board=Board(i, j)
print(my_board.tab)
for l in range(21):
    n1= int(input('*Joueur1*  Choisisser une colonne: '))
    #s1= input('*Joueur1*  Choisisser une couleur: ')
    my_board.play(n1, 'R')
    print(my_board.tab)
    n2=  int(input('*Joueur2*  Choisisser une colonne: '))
    #s2= input('*Joueur2*  Choisisser une couleur: ')
    my_board.play(n2, 'J')
    print(my_board.tab)
print('just to make a change')
