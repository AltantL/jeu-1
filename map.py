class map:
    def __init__(self):
        self.lignes = 50
        self.valeur_defaut = "F"
        # la valeur "0" signifie pas le droit de passer
        self.mapI = [[self.valeur_defaut for _ in range(self.lignes)] for _ in range(self.lignes)]
        self.map = [[self.valeur_defaut for _ in range(self.lignes)] for _ in range(self.lignes)]

        self.village_type = ([["I"],["G"]],
                             [["M"],["P"]])
        #self.village_type = ([["INN"], ["Guilde"]],
        #                     [["maison"], ["poste_de_garde"]])


    def generationMonde(self):
        mid = (len(self.map)//2)-1
        for y,ligne in enumerate(self.map):
            for x, element in enumerate(ligne):
                if x == mid or y == mid:
                    self.map[y][x] = "_"
                    self.mapI[y][x] = "_"
                if x == 0 or y == 0 or x == self.lignes-1 or y == self.lignes-1:
                    #BORDURE MAP
                    self.map[y][x] = "0"


        for y,ligne in enumerate(self.village_type):
            for x, element in enumerate(ligne):
                self.map[mid + y][mid + x] = element[0]
                self.mapI[mid + y][mid + x] = element[0]


    def affichageMonde(self):
        for ligne in self.map:
            print(ligne)
        print("\n\n")

    def maMap(self):
        return self.map

    def nettoyageMap(self):
        for y, ligne in enumerate(self.mapI):
            for x, element in enumerate(ligne):
                self.map[y][x] = element