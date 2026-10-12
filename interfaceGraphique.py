import pygame

class graphique:
    def __init__(self):
        self.tailleBloc = 30 # taille de chaque bloc en pixel
        self.map = []
        self.taille = 1
        self.longeurTotal = self.tailleBloc * self.taille

    def initialisationMapGraph(self,carte):

        self.taille = len(carte) * self.tailleBloc

        self.longeurTotal = self.tailleBloc * self.taille

        for y, ligne in enumerate(carte):
            for x, element in enumerate(ligne):
                self.map[y][x] = element

    def generateMapGraph(self):

        pygame.init()
        screen = pygame.display.set_mode((self.longeurTotal, self.longeurTotal))
        screen.fill("purple")

        for y, ligne in enumerate(self.map):
            for x, element in enumerate(ligne):
                create_rectangle(x * self.tailleBloc, y * self.tailleBloc, (x + 1) * self.tailleBloc,
                                        (y + 1) * self.tailleBloc, fill="white")


    def drawMapGraph(self):
        pygame.display.set_caption("map")