import pygame


class graphiqueMap:
    def __init__(self,taille):
        self.tailleBloc = 10 # taille de chaque bloc en pixel
        self.taille = taille
        self.longeurTotal = self.tailleBloc * self.taille
        self.init = pygame.init()
        self.screen = pygame.display.set_mode((self.longeurTotal, self.longeurTotal))
        self.clock = pygame.time.Clock()


    def generateMapGraph(self, carte):

        self.screen.fill("purple")
        for y, ligne in enumerate(carte):
            for x, element in enumerate(ligne):
                if element == "_":
                    pygame.draw.rect(self.screen, "gray",(x * self.tailleBloc, y * self.tailleBloc, self.tailleBloc, self.tailleBloc))
                elif element == "F":
                    pygame.draw.rect(self.screen,"green", (x * self.tailleBloc, y * self.tailleBloc, self.tailleBloc,self.tailleBloc))
                elif element == "0":
                    pygame.draw.rect(self.screen, "black",(x * self.tailleBloc, y * self.tailleBloc, self.tailleBloc, self.tailleBloc))
                else:
                    pygame.draw.rect(self.screen, "brown",(x * self.tailleBloc, y * self.tailleBloc, self.tailleBloc, self.tailleBloc))
                #self.screen.blit("lienImg", [x * self.tailleBloc, y * self.tailleBloc])


        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_z]:
             #player_pos.y -= self.tailleBloc * self.dt
        #if keys[pygame.K_s]:
            #player_pos.y += self.tailleBloc * self.dt
        #if keys[pygame.K_q]:
            #player_pos.x -= self.tailleBloc * self.dt
        #if keys[pygame.K_d]:
            #player_pos.x += self.tailleBloc * self.dt




    def drawEntity(self,playerCoo):
        pygame.draw.rect(self.screen, "pink",(playerCoo[1] * self.tailleBloc, playerCoo[0] * self.tailleBloc, self.tailleBloc, self.tailleBloc))


    def flip(self):
        pygame.display.flip()
