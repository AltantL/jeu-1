import sys
from os import remove


class player:
    def __init__(self):
        self.name = "player"
        self.vieMax = 10
        self.vie = 10
        self.attaque = 1
        self.defence = 1
        self.niveau = 1
        self.experience = 1
        self.inventaire = ["potion","potion"]
        self.equipements = ["casque_basique","plastron_basique","jambiere_basique","botte_basique","épée_basique","bouclier_basique"]

        self.coordonee = 0,0


    def nomJoueur(self):
        self.name = input("Nom du joueur (par défaut : player): \n\n\n")

    def attaque(self):
        return self.attaque

    def levelUP(self):
        if (self.experience >= self.niveau * 10):
            self.experience = self.experience - self.niveau * 10
            self.niveau += 1
            self.attaque += 1
            self.vieMax += 5
            self.vie += 5


    def degat(self, attaque):
        attaque = attaque - self.defence
        if attaque < 0:
            attaque = 0

        self.vie -= attaque
        if self.vie <= 0:
            self.mort()

    def soin(self, heal):
        self.vie += heal
        if self.vie >= self.vieMax:
            self.vie = self.vieMax

    def mort(self):
        sys.exit("vous êtes mort")

    def vie(self):
        return self.vie

    def map_player(self,carte):
        x,y = self.coordonee
        carte[x][y] = "A"
        for ligne in carte:
            print(ligne)
        print("\n\n")

    def inventaireVue(self):
        for i in self.inventaire:
            print(i)

    def inventaireUtilisation(self, i):
        i = int(i)
        liste = []
        with open('liste_objet', 'r', encoding='utf-8') as f:
            for line in f:
                liste.append(line.split(","))

        print(liste)

        action = liste[i][1]
        action = int(action)
        liste.remove(liste[i])
        self.soin(action)


    def tp(self,x,y):
        self.coordonee = x,y

    def coordonee(self):
        return self.coordonee

    def mouvement_haut(self):
        self.coordonee += 0,1

    def mouvement_bas(self):
        self.coordonee -= 0,1

    def mouvement_droit(self):
        self.coordonee += 1,0

    def mouvement_gauche(self):
        self.coordonee -= 1,0

