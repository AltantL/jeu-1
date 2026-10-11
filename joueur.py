class player:
    def __init__(self):
        self.name = "player"
        self.vieMax = 10
        self.vie = 10
        self.attaque = 1
        self.niveau = 1
        self.experience = 1
        self.inventaire = []
        self.equipements = ["casque","plastron","jambiere","botte","épée_basique","bouclier"]

    def nomJoueur(self):
        self.name = input("Nom du joueur (par défaut : player): ")

    def attaque(self):
        print("attaque : " + self.attaque)

    def levelUP(self):
        if (self.experience >= self.niveau * 10):
            self.experience = self.experience - self.niveau * 10
            self.niveau += 1
            self.attaque += 1
            self.vieMax += 5
            self.vie += 5


    def degat(self, attaque):
        self.vie -= attaque
        if self.vie <= 0:
            self.mort()

    def soin(self, heal):
        self.vie += heal

    def mort(self):
        print("vous êtes mort")