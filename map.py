class map:
    def __init__(self):
        self.lignes = 50
        self.valeur_defaut = "F"
        # la valeur "0" signifie pas le droit de passer
        self.mapI = [[self.valeur_defaut for _ in range(self.lignes)] for _ in range(self.lignes)]
        self.map = [[self.valeur_defaut for _ in range(self.lignes)] for _ in range(self.lignes)]

        self.lignesMonde = 3
        self.mapMonde = ([["map1"],["map2"],["map3"]],
                         [["map4"],["map5"],["map6"]],
                         [["map7"],["map8"],["map9"]])
        self.coordonneeMapMonde = [2,2]

        self.village_type = ([["I"],["G"]],
                             [["M"],["P"]])
        #self.village_type = ([["INN"], ["Guilde"]],
        #                     [["maison"], ["poste_de_garde"]])


    def generationMonde(self):
        mid = (len(self.map)//2)-1
        for y,ligne in enumerate(self.map):
            for x, element in enumerate(ligne):
                if x == 0 or y == 0 or x == self.lignes-1 or y == self.lignes-1:
                # BORDURE MAP
                    self.map[y][x] = "0"
                if x == mid or y == mid:
                    self.map[y][x] = "_"
                    self.mapI[y][x] = "_"



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

    def autreCotee(self,coordonee):
        #faut aussi faire en sorte que quand ce moment arrive, la carte change
        #plusieurs choix (un return pour dire que y a eu un changement ou une map des différentes map)
        #faut juste que ce soit pas dans le joueur
        tCarte = self.lignes-1

        if coordonee[0] < 0:
            if self.deplacementGrandeMap([self.coordonneeMapMonde[0],self.coordonneeMapMonde[1]-1]):
                coordonee[0] = tCarte
                return coordonee
        if coordonee[1] < 0:
            if self.deplacementGrandeMap([self.coordonneeMapMonde[0]-1,self.coordonneeMapMonde[1]]):
                coordonee[1] = tCarte
                return coordonee
        if coordonee[0] > tCarte:
            if self.deplacementGrandeMap([self.coordonneeMapMonde[0], self.coordonneeMapMonde[1] + 1]):
                coordonee[0] = 0
                return coordonee
        if coordonee[1] > tCarte:
            if self.deplacementGrandeMap([self.coordonneeMapMonde[0]+1,self.coordonneeMapMonde[1]]):
                coordonee[1] = 0
                return coordonee
        return coordonee

    def pasMouv(self,coordonee):
        if self.map[coordonee[0]][coordonee[1]] == "0":
            return False
        return True

    def deplacementGrandeMap(self,coordonee):
        if not (0 <= coordonee[0] < self.lignesMonde-1 and 0 <= coordonee[1] < self.lignesMonde-1):
            self.coordonneeMapMonde = coordonee
            return True
        else :
            return False