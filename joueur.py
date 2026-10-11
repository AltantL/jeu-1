import sys

class player:
    def __init__(self, map):
        self.name = "player"
        self.vieMax = 10
        self.vie = 10
        self.attaque = 1
        self.defence = 1
        self.niveau = 1
        self.experience = 1
        self.inventaire = []
        self.equipements = ["casque_basique","plastron_basique","jambiere_basique","botte_basique","épée_basique","bouclier_basique"]

        self.coordonee = 0,0

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


    def nomJoueur(self):
        self.name = input("Nom du joueur (par défaut : player): ")

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

    def mort(self):
        sys.exit("vous êtes mort")