from faker import Faker

def rep_user(mot_a_trouver):
    mot_donner = input()
    if len(mot_donner) != 6:
        print("\033[0mCe n'est pas un mot de six lettres...")
    else:
        mot_donner = mot_donner
        verif(mot_a_trouver, mot_donner)
        return mot_donner

def verif(mot_a_trouver, mot_donner):
    for i in range(len(mot_a_trouver)):
        if mot_a_trouver[i] == mot_donner[i]:
            print(f"\033[1;37;41m{mot_donner[i]}", end='')
        elif mot_donner[i] in mot_a_trouver:
            print(f"\033[1;37;43m{mot_donner[i]}", end='')
        else:
            print(f"\033[1;37;44m{mot_donner[i]}", end='')
    print("\033[0m")
    
def mot_hasard():
    fake = Faker(locale="fr_FR")
    mot = " "
    while len(mot) != 6:
        mot = fake.word()
    return mot
    
def jeu(mot_a_trouver):
    compteur = 0
    mot_donner = " "
    while mot_a_trouver != mot_donner and compteur != 6:
        print(f"\n\033[0mVeuillez entrer un mot de six lettres (tu es a {compteur} essais sur 6) :")
        mot_donner = rep_user(mot_a_trouver)
        compteur = compteur + 1
    if compteur == 6:
        print(f"Tu as perdu... Le mot était : {mot_a_trouver}")
    else:
        print(f"Bravo ! Tu as gagné ! Tu as réussi en {compteur} essais")
        
def Motus():
    mot = mot_hasard()
    jeu(mot)
    
Motus()


