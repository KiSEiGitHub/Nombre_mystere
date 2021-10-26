import random

print('ceci est ub test')

class game:
    def __init__(self, vie, nb_vie):
        self.user = ''
        self.nb_vie = nb_vie
        self.vie = vie
        self.nb_mystere = random.randint(1, 100)
        self.lie = random.randint(1, 4)
        self.lie_or_no = 0
        self.tryy = 0
        self.help = random.randint(1, 2)

    def classic(self):
        print('Nombre mystère entre 1 et 100')
        while True:
            if self.vie == 'oui':
                print(f'Il vous reste {self.nb_vie} vies')

            self.user = int(input('>> '))

            if self.user == self.nb_mystere:
                print('Bravo, vous avez trouvé le nombre mystère')
                print(f'vous trouvé en {self.tryy} essaies')
                break

            elif self.user < self.nb_mystere:
                if self.vie == 'oui':
                    self.nb_vie -= 1
                    if self.nb_vie <= 0:
                        print('Vous avez perdu !')
                        print(f'Le nombre mystère était {self.nb_mystere}')
                        break
                    else:
                        print("C'est plus !")
                        self.tryy += 1
                elif self.vie == 'non':
                    print("C'est plus !")
                    self.tryy += 1

            elif self.user > self.nb_mystere:
                if self.vie == 'oui':
                    self.nb_vie -= 1
                    if self.nb_vie <= 0:
                        print('Vous avez perdu !')
                        print(f'Le nombre mystère était {self.nb_mystere}')
                        break
                    else:
                        print("C'est moins !")
                        self.tryy += 1
                elif self.vie == 'non':
                    print("C'est moins !")
                    self.tryy += 1

            print('-' * 50)

    def niveau_2(self):
        print('Nombre mystère entre 1 et 100')
        while True:
            if self.vie == 'oui':
                print(f'Il vous reste {self.nb_vie} vies')

            self.lie = random.randint(1, 4)
            self.help = random.randint(1, 2)
            self.user = int(input('>> '))

            if self.user == self.nb_mystere:
                print('Bravo, vous avez trouvé le nombre mystère')
                print(f"L'ordinateur a menti {self.lie_or_no} fois")
                print(f'Vous avez trouvé en {self.tryy} essaies')
                break

            elif self.user < self.nb_mystere:
                if self.vie == 'oui':
                    self.nb_vie -= 1
                    if self.nb_vie <= 0:
                        print('Vous avez perdu !')
                        print(f'Le nombre mystère était {self.nb_mystere}')
                        print(f"L'ordinateur a menti {self.lie_or_no} fois")
                        break
                    else:
                        if self.lie == 1:
                            if self.help == 1:
                                print("L'ordinateur a peut-être menti..")
                            print("C'est moins !")
                            self.lie_or_no += 1
                        else:
                            print("C'est plus !")
                        self.tryy += 1

                elif self.vie == 'non':
                    if self.lie == 1:
                        if self.help == 1:
                            print("L'ordinateur a peut-être menti..")
                        print("C'est moins !")
                        self.lie_or_no += 1
                    else:
                        print("C'est plus !")
                    self.tryy += 1

            elif self.user > self.nb_mystere:
                if self.vie == 'oui':
                    self.nb_vie -= 1
                    if self.nb_vie <= 0:
                        print('Vous avez perdu !')
                        print(f'Le nombre mystère était {self.nb_mystere}')
                        print(f"L'ordinateur a menti {self.lie_or_no} fois")
                        break
                    else:
                        if self.lie == 1:
                            if self.help == 1:
                                print("L'ordinateur a peut-être menti..")
                            print("C'est plus !")
                            self.lie_or_no += 1
                        else:
                            print("C'est moins !")
                        self.tryy += 1

                elif self.vie == 'non':
                    if self.lie == 1:
                        if self.help == 1:
                            print("L'ordinateur a peut-être menti..")
                        print("C'est plus !")
                        self.lie_or_no += 1
                    else:
                        print("C'est moins !")
                    self.tryy += 1

            print('-' * 50)



def main():
    print('Voulez-vous avoir un nombre de vie ? (oui / non)')
    vie = ""
    while vie not in ['oui', 'non']:
        vie = input('>> ')

    if vie == 'oui':
        nb_vie = int(input('Combien de vie: '))
        jeu = game(vie, nb_vie)
        print("Jeu classique : 1 | l'ordinateur ment : 2")
        c = ""
        while c not in ['1', '2']:
            c = input('>> ')

        if c == '1':
            jeu.classic()
        elif c == '2':
            jeu.niveau_2()

    elif vie == 'non':
        nb_vie = 0
        jeu = game(vie, nb_vie)
        print("Jeu classique : 1 | l'ordinateur ment : 2")
        c = ""
        while c not in ['1', '2']:
            c = input('>> ')

        if c == '1':
            jeu.classic()
        elif c == '2':
            jeu.niveau_2()


if __name__ == '__main__':
    main()