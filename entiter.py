class player:
    def __init__(self):
        self.name = ""
        self.vieMax = 10
        self.vie = 10
        self.attaque = 1
        self.defence = 1
        self.niveau = 1
        self.experience = 1
        self.inventaire = []
        self.equipements = {"casque": "",
                            "plastron" : "",
                            "jambiere" : "",
                            "botte" : "",
                            "epee" : "",
                            "bouclier" : ""}

        self.coordonee = [0,0]
        self.futurCoordonee = [0,0]

    def stuffBassique(self):
        self.inventaire.append("potion")
        self.inventaire.append("potion")

        self.equipements["casque"] = "casque_basique"
        self.equipements["plastron"] = "plastron_basique"
        self.equipements["jambiere"] = "jambiere_basique"
        self.equipements["botte"] = "botte_basique"
        self.equipements["epee"] = "epee_basique"
        self.equipements["bouclier"] = "bouclier_basique"

    def nomJoueur(self):
        self.name = input("Nom du joueur (par défaut : player): \n\n\n")
        if self.name == "":
            self.name = "player"

    def attaque(self):
        return self.attaque

    def levelUP(self):
        if self.experience >= self.niveau * 10:
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
        return round(self.niveau * 1.5) + 1

    def vie(self):
        return self.vie

    def map_player(self,carte):
        x,y = self.coordonee
        carte[x][y] = "A"
        # attention, cette action grave "A" dans la map
        # il faut trouver une alternative
        for ligne in carte:
            print(ligne)
        print("\n\n")

    def inventaireVue(self):

        print("coordonnée : ")
        print(self.coordonee)
        print("\n"+"futurCoordonée : ")
        print(self.futurCoordonee)


        #for i in self.inventaire:
        #    print(i)

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
        self.coordonee = [x,y]
        self.futurCoordonee = [x,y]

    def autreCotee(self):
        #faut aussi faire en sorte que quand ce moment arrive, la carte change
        #plusieurs choix (un return pour dire que y a eu un changement ou une map des différentes map)
        #faut juste que ce soit pas dans le joueur
        tCarte = 49

        if self.futurCoordonee[0] < 0:
            self.futurCoordonee[0] = tCarte
        if self.futurCoordonee[1] < 0:
            self.futurCoordonee[1] = tCarte
        if self.futurCoordonee[0] > tCarte:
            self.futurCoordonee[0] = 0
        if self.futurCoordonee[1] > tCarte:
            self.futurCoordonee[1] = 0

    def mouvement_haut(self,carte):
        self.futurCoordonee[0] -= 1
        self.autreCotee()
        if carte[self.futurCoordonee[0]][self.futurCoordonee[1]] != "0":
            self.coordonee = self.futurCoordonee
        else:
            self.futurCoordonee[0] += 1


    def mouvement_bas(self,carte):
        self.futurCoordonee[0] += 1
        self.autreCotee()
        if carte[self.futurCoordonee[0]][self.futurCoordonee[1]] != "0":
            self.coordonee = self.futurCoordonee
        else:
            self.futurCoordonee[0] -= 1

    def mouvement_droit(self,carte):
        self.futurCoordonee[1] += 1
        self.autreCotee()
        if carte[self.futurCoordonee[0]][self.futurCoordonee[1]] != "0":
            self.coordonee = self.futurCoordonee
        else:
            self.futurCoordonee[1] -= 1

    def mouvement_gauche(self,carte):
        self.futurCoordonee[1] -= 1
        self.autreCotee()
        if carte[self.futurCoordonee[0]][self.futurCoordonee[1]] != "0":
            self.coordonee = self.futurCoordonee
        else:
            self.futurCoordonee[1] += 1

