class Automate:
    def __init__(self):
        self.nbr_symboles = []
        self.nbr_etats = []
        self.alphabet = []
        self.etats = []
        self.etats_initiaux = []
        self.etats_finaux = []
        self.transitions = []


def lire_automate_sur_fichier(nom_fichier: str):
    with open('G2-' + nom_fichier + '.txt', 'r') as f:

        liste = f.readlines()

        a = Automate()

        # On ajoute les caractéristiques de l'automate dans les listes de la classe Automate
        a.nbr_symboles = liste.pop(0)
        a.nbr_etats = liste.pop(0)
        a.alphabet = liste.pop(0).split(',')
        a.alphabet[-1] = a.alphabet[-1].strip('\n')
        a.etats = liste.pop(0).split(',')
        a.etats[-1] = a.etats[-1].strip('\n')
        a.etats_initiaux = liste.pop(0).split(',')
        a.etats_initiaux[-1] = a.etats_initiaux[-1].strip('\n')
        a.etats_finaux = liste.pop(0).split(',')
        a.etats_finaux[-1] = a.etats_finaux[-1].strip('\n')
        a.transitions = liste

        for i in range(0, len(a.transitions)):
            a.transitions[i] = a.transitions[i].strip('\n')

    return a


def afficher_automate(a: Automate):
    print("")
    print("Nombre de symboles : ", end='')
    print(a.nbr_symboles[0])

    print("Nombre d'états : ", end='')
    print(a.nbr_etats)

    print("Alphabet :", end=' ')
    for lettre in a.alphabet:
        print(lettre + ' ', end=' ')

    print("")
    print("")

    print("Etats :")
    for etat in a.etats:
        print(etat, end=' ')

    print("")
    print("")

    print("Etats Initiaux :")
    for etat in a.etats_initiaux:
        print(etat, end=' ')

    print("")
    print("")

    print("Etats Finaux :")
    for etat in a.etats_finaux:
        print(etat, end=' ')

    print("")
    print("")

    print("Transitions :")
    for transition in a.transitions:
        print(transition)

    print("")

    if int(a.nbr_symboles[0]) != 0:
        print("Table de transitions :")
        table(a)
        return 1
    else:
        print("L'alphabet est vide, l'automate n'est pas traitable")
        return 0


def table(a: Automate):

    # Nombre de lignes = 1 + Nombre d'états et Nombre de colonnnes = 2 + Nombre de symboles
    row = 1 + int(a.nbr_etats[0])
    col = 2 + int(a.nbr_symboles[0])

    # Initialisation du tableau avec des '-' partouts
    A = []
    for i in range(row):
        A.append(['-']*col)
        for j in range(col):
            A[i][j] = '-'

    # Ajout des lettres dans le tableau
    i = 2
    for lettre in a.alphabet:
        A[0][i] = lettre
        i += 1

    # Ajouts des états dans le tableau
    i = 1
    for etat in a.etats:
        A[i][1] = etat
        i += 1

    # Ajouts des transitions
    for i in range(1, int(a.nbr_etats[0])+1):
        for j in range(2, int(a.nbr_symboles[0])+2):
            for transition in a.transitions:
                if transition.split(",")[0] in A[i][1] and transition.split(",")[1] in A[0][j]:
                    if A[i][j] == '-':
                        A[i][j] = transition.split(",")[2]
                    else:
                        if transition.split(",")[2] not in A[i][j]:
                            A[i][j] += '+' + transition.split(",")[2]

    # On spécifie si l'état est une entrée ou une sortie ou les deux
    for i in range(1, int(a.nbr_etats[0])+1):
        for etat in a.etats_initiaux:
            if A[i][1] == etat:
                A[i][0] = 'E'
        for etat in a.etats_finaux:
            if A[i][1] == etat:
                if A[i][0] == 'E':
                    A[i][0] = 'E+S'
                else:
                    A[i][0] = 'S'

    # Affichage du tableau
    for i in range(row):
        for j in range(col):
            if j != col-1:
                print(A[i][j] + "", end='  ')
            else:
                print(A[i][j] + "  ")
    return A


def table_sans_print(a: Automate):

    # Fonction qui servira pour savoir si un automate est complet
    row = 1 + int(a.nbr_etats[0])
    col = 2 + int(a.nbr_symboles[0])

    A = []
    for i in range(row):
        A.append(['-']*col)
        for j in range(col):
            A[i][j] = '-'
    i = 2
    for lettre in a.alphabet:
        A[0][i] = lettre
        i += 1

    i = 1
    for etat in a.etats:
        A[i][1] = etat
        i += 1

    for i in range(1, int(a.nbr_etats[0])+1):
        for j in range(2, int(a.nbr_symboles[0])+2):
            for transition in a.transitions:
                if transition.split(",")[0] in A[i][1] and transition.split(",")[1] in A[0][j]:
                    if A[i][j] == '-':
                        A[i][j] = transition.split(",")[2]
                    else:
                        if transition.split(",")[2] not in A[i][j]:
                            A[i][j] += '+' + transition.split(",")[2]

    for i in range(1, int(a.nbr_etats[0])+1):
        for etat in a.etats_initiaux:
            if A[i][1] == etat:
                A[i][0] = 'E'
        for etat in a.etats_finaux:
            if A[i][1] == etat:
                if A[i][0] == 'E':
                    A[i][0] = 'E+S'
                else:
                    A[i][0] = 'S'
    return A


def est_un_automate_asynchrone(a: Automate):
    truc_a_retourner = 0
    epsilon = []

    # On rajoute chacune des transitions epsilon dans le tableau epsilon
    for transition in a.transitions:
        if transition.split(',')[1] == 'epsilon':
            epsilon.append(transition)
            truc_a_retourner = 1

    if truc_a_retourner == 0:
        print("L'automate est synchrone")

    if truc_a_retourner == 1:
        print("L'automate est asynchrone")
        print("Transitions Epsilon : ", end='')
        print(epsilon)

    return truc_a_retourner


def est_un_automate_deterministe(a: Automate):
    truc_a_retourner = 1
    test = 0

    # Si la longueur de la liste d'états initiaux est supérieur à 1 , alors il y a plusieurs entrées
    if len(a.etats_initiaux) > 1:
        print("L'automate n'est pas déterministe car il a plusieurs entrées")
        truc_a_retourner = 0

    # Si dans les transitions, il y en a deux différentes avec le même premier état et la même lettre
    # Alors cet état utilise deux fois la même transition
    for transition in a.transitions:
        for transition2 in a.transitions:
            if transition2.split(",")[0] == transition.split(",")[0] and transition2.split(",")[1] == transition.split(",")[1] and transition2 != transition:
                truc_a_retourner = 0
                test = 1

    if test == 1:
        print("L'automate n'est pas déterministe car un état utilise deux fois la même transition")

    if truc_a_retourner == 1:
        print("L'automate est déterministe")

    return truc_a_retourner


def est_un_automate_complet(a: Automate):
    A = table_sans_print(a)
    truc_a_retourner = 1

    # Si dans la table de transition il y a des '-', alors l'automate n'est pas complet
    for i in range(1, int(a.nbr_etats[0]) + 1):
        for j in range(2, int(a.nbr_symboles[0]) + 2):
            if A[i][j] == '-':
                truc_a_retourner = 0

    if truc_a_retourner == 0:
        print("L'automate n'est pas complet car certaines transitions ne sont pas utilisée")

    if truc_a_retourner == 1:
        print("L'automate est complet")

    return truc_a_retourner


def determinisation(a: Automate):
    b = Automate()
    b.nbr_symboles = a.nbr_symboles
    b.alphabet = a.alphabet

    # Si l'automate a plusieurs états initiaux, on les additionne pour en faire qu'un seul état initial
    if len(a.etats_initiaux) > 1:
        b.etats_initiaux.insert(0, a.etats_initiaux[0])
        b.etats.insert(0, a.etats_initiaux[0])
        for i in range(1, len(a.etats_initiaux)):
            b.etats_initiaux[0] += "+" + a.etats_initiaux[i]
            b.etats[0] += "+" + a.etats_initiaux[i]
    else:
        b.etats_initiaux.insert(0, a.etats_initiaux[0])
        b.etats.insert(0, a.etats_initiaux[0])

    row = 1    # On ajoutera une ligne à chaque nouvel état
    col = 2 + int(b.nbr_symboles[0])

    # Initialisation du tableau
    A = []
    for i in range(row):
        A.append(['-']*col)
        for j in range(col):
            A[i][j] = "-"

    # Initialisation des lettres
    i = 2
    for lettre in a.alphabet:
        A[0][i] = lettre
        i += 1

    # Pour chaque état, on rajoute une ligne et pour chaque colonne
    # Si le premier etat de la transition = l'etat de la boucle et la lettre de la transition = la lettre de la colonne
    # Alors on rajoute le deuxième état de la transition aux coordonnées de la colonne et de la ligne
    # Si il y a déjà un état, on crée un nouvel état en additionnant les deux états pour n'en laisser qu'un seul
    i = 1
    for etat in b.etats:
        A.append(['-'] * col)
        A[i][1] = etat
        i += 1
        for j in range(2, int(b.nbr_symboles[0]) + 2):
            for transition in a.transitions:
                if transition.split(",")[0] in A[i-1][1] and transition.split(",")[1] in A[0][j]:
                    if A[i-1][j] == '-':
                        A[i-1][j] = transition.split(",")[2]
                    else:
                        if transition.split(",")[2] not in A[i-1][j]:
                            b.etats.remove(A[i-1][j])
                            A[i-1][j] += '+' + transition.split(",")[2]

                if A[i-1][j] != '-' and A[i-1][j] not in b.etats:
                    b.etats.insert(i, A[i-1][j])

    # Un fois la boucle terminée, on ajoute le nombre d'états
    b.nbr_etats = str(len(b.etats))

    # On détermine les états finaux
    i = 0
    for etat in a.etats_finaux:
        for etat2 in b.etats:
            if etat in etat2:
                b.etats_finaux.insert(i, etat2)
                i += 1

    # Enfin on rajoute les transitions du tableau
    for j in range(2, int(b.nbr_symboles[0]) + 2):
        for i in range(1, int(b.nbr_etats[0]) + 1):
            if A[i][1] != '-' and A[0][j] != '-' and A[i][j] != '-':
                b.transitions.append(A[i][1] + ',' + A[0][j] + ',' + A[i][j])

    return b


def completion(a: Automate):

    # On recrée le tableau
    row = 1 + int(a.nbr_etats[0])
    col = 2 + int(a.nbr_symboles[0])

    A = []
    for i in range(row):
        A.append(['-'] * col)
        for j in range(col):
            A[i][j] = '-'
    i = 2
    for lettre in a.alphabet:
        A[0][i] = lettre
        i += 1

    # On veut rajouter l'etat P, mais ça ne marche pas
    """"
    a.etats.append('P')
    temp = []
    temp.append(str(int(a.nbr_etats[0]) + 1))
    a.nbr_etats = temp
    """""

    i = 1
    for etat in a.etats:
        A[i][1] = etat
        i += 1

    # Pour chaque ligne et chaque colonne, et pour chaques transitions
    # Si le premier état de la transition = l'état de la ligne et la lettre de la transition = la lettre de la colonne
    # Alors on rajoute le deuxième état de la transition aux coordonnées de la colonne et de la ligne
    # Si il y a déjà un état, on crée un nouvel état en additionnant les deux états pour n'en laisser qu'un seul
    # Une fois la boucle de transitions finis, on met des 'P' à la place des '-'
    for i in range(1, int(a.nbr_etats[0]) + 1):
        for j in range(2, int(a.nbr_symboles[0]) + 2):
            for transition in a.transitions:
                if transition.split(",")[0] in A[i][1] and transition.split(",")[1] in A[0][j]:
                    if A[i][j] == '-':
                        A[i][j] = transition.split(",")[2]
                    else:
                        if transition.split(",")[2] not in A[i][j]:
                            A[i][j] += '+' + transition.split(",")[2]

            if A[i][j] == '-':
                A[i][j] = 'P'

    # On recrée le tableau de transition en fonction du tableau
    a.transitions.clear()
    for j in range(2, int(a.nbr_symboles[0]) + 2):
        for i in range(1, int(a.nbr_etats[0]) + 1):
            if A[0][j] != '-' and A[i][j] != 'P':
                a.transitions.append(A[1][i] + ',' + A[0][j] + ',' + A[i][j])

    # On rajoute la transition de l'état P
    for j in range(2, int(a.nbr_symboles[0]) + 2):
        if A[0][j] != '-':
            a.transitions.append('P' + ',' + A[0][j] + ',' + 'P')

    return a


def synchronisation(a: Automate):
    epsilon = []
    sans_epsilon = []

    # On sépare les transitions epsilon d'un coté et les transitions sans epsilon de l'autre
    for transition in a.transitions:
        if transition.split(',')[1] == 'epsilon':
            epsilon.append(transition)
        else:
            sans_epsilon.append(transition)

    # On rajoute dans les etats finaux, les états relié à des états finaux par une transition epsilon
    for etat in a.etats_finaux:
        for e in epsilon:
            if e.split(",")[2] == etat:
                a.etats_finaux.append(e.split(",")[0])

    epsilon.reverse()

    # Pour chaque transition sans epsilon et pour chaque transition avec epsilon,
    # Si le deuixème état de la transition epsilon = le premier état de la transition sans epsilon
    # Alors on rajoute dans la liste sans epsilon, le premier état de la transition epsilon
    # Puis la lettre et le deuxième état de la transition sans epsilon
    for san in sans_epsilon:
        for e in epsilon:
            if e.split(",")[2] == san.split(",")[0]:
                sans_epsilon.append(e.split(",")[0] + ',' + san.split(",")[1] + ',' + san.split(",")[2])

    # Les transitions de l'automate deviennent la liste de transitions sans epsilon
    a.transitions.clear()
    a.transitions = sans_epsilon

    # On enlève epsilon de l'alphabet de l'automate et on réduit de 1 le nombre de symboles
    a.alphabet.remove('epsilon')

    temp = []
    temp.append(str(int(a.nbr_symboles[0]) - 1))
    a.nbr_symboles = temp

    return a


def determinisation_et_completion_automate_asynchrone(a: Automate):
    test = 0

    print("")
    print("######################")
    print("Automate Synchronisé :")
    b = synchronisation(a)
    afficher_automate(b)

    if est_un_automate_deterministe(b) == 0:
        print("")
        print("######################")
        print("Automate Déterminisé :")
        c = determinisation(b)
        afficher_automate(c)
        test = 1

        if est_un_automate_complet(c) == 0:
            print("")
            print("######################")
            print("Automate Complet :")
            d = completion(c)
            test = 2

    if test == 0:
        return b
    else:
        if test == 1:
            return c
        else:
            if test == 2:
                return d


def determinisation_et_completion_automate_synchrone(a: Automate):
    test = 0

    print("")
    print("######################")
    print("Automate Déterminisé :")
    b = determinisation(a)
    afficher_automate(b)

    if est_un_automate_complet(b) == 0:
        print("")
        print("######################")
        print("Automate Complet :")
        c = completion(b)
        test = 1

    if test == 0:
        return b
    else:
        if test == 1:
            return c


def main():
    nom_fichier = input("quel automate voulez-vous utiliser ? ")

    AF = lire_automate_sur_fichier(nom_fichier)
    if afficher_automate(AF) == 1:
        if est_un_automate_asynchrone(AF) == 1:
            AFDC = determinisation_et_completion_automate_asynchrone(AF)
        else:
            if est_un_automate_deterministe(AF) == 1:
                if est_un_automate_complet(AF) == 1:
                    AFCD = AF
                else:
                    print("")
                    print("######################")
                    print("Automate Complet :")
                    AFCD = completion(AF)
            else:
                AFCD = determinisation_et_completion_automate_synchrone(AF)
        afficher_automate(AFCD)