class map:
    def __init__(self):
        self.lignes = 10
        self.valeur_defaut = "F"
        self.mapI = [[self.valeur_defaut for _ in range(self.lignes)] for _ in range(self.lignes)]
        self.map = [[self.valeur_defaut for _ in range(self.lignes)] for _ in range(self.lignes)]

        self.village_type = ([["I"],["G"]],
                             [["M"],["P"]])
        #self.village_type = ([["INN"], ["Guilde"]],
        #                     [["maison"], ["poste_de_garde"]])

    def generationMonde(self):
        mid = (len(self.map)//2)-1
        #self.map[:mid][:mid] = []
        for y,ligne in enumerate(self.map):
            for x, element in enumerate(ligne):
                if x == mid or y == mid:
                    self.map[y][x] = "_"


        for y,ligne in enumerate(self.village_type):
            for x, element in enumerate(ligne):
                self.map[mid + y][mid + x] = element[0]


        for y, ligne in enumerate(self.mapI):
            for x, element in enumerate(ligne):
                if x == mid or y == mid:
                    self.mapI[y][x] = "_"

        for y, ligne in enumerate(self.village_type):
            for x, element in enumerate(ligne):
                self.mapI[mid + y][mid + x] = element[0]

    def affichageMonde(self):
        for ligne in self.map:
            print(ligne)
        print("\n\n")

    def maMap(self):
        return self.map

    def nettoyageMap(self):
        self.map = self.mapI