class ennemie:
    def __init__(self):
        self.name = "ennemie"
        self.vieMax = 10
        self.vie = 10
        self.attaque = 1
        self.defence = 1
        self.niveau = 1
        self.equipements = ["","","","","",""]

    def nomEnnemie(self):
        self.name = input("Nom de l'ennemie: ")

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
        return round(self.niveau * 1.5)