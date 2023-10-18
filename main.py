import pied
import random
# from [] import []

longueur_list = len(pied.words)
# nb_choisi = input("choose number between 1 and " + str(longueur_list))
nb_choisi = random.randint(1, longueur_list)


def question2():
    nb = int(nb_choisi) - 1
    mot_a_trouver = pied.words[nb]
    guess = input("quel mot est ce que je cherche ?")

    if guess == mot_a_trouver:
        print("youhou, trop doué")
    else:
        print('pas bon. réessaye: ')
        question2()


def question():
    if "1" <= str(nb_choisi) <= str(longueur_list):
        print(nb_choisi)

        question2()
    else:
        print("invalid number, input again")
        question()


question()




# trouver mot correspondant a id choisi

