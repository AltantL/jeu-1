import pygame
import random

import interfaceGraphique
import entiter
import map

print("test jeu\n\n\n")

monde = map.map()
monde.generationMonde()

mapGraph = interfaceGraphique.graphiqueMap(monde.lignes)
#mapGraph.generateMapGraph(monde.map)

monde.affichageMonde()

player = entiter.player()
#player.nomJoueur()


monstre = [entiter.player(), entiter.player(), entiter.player(), entiter.player(), entiter.player()]



spawn = (monde.lignes // 2)-1

player.tp(spawn, spawn)

for i in [0,1,2,3,4]:
    x = random.choice([1,2,3,4,5,6,7,8,9,10])
    y = random.choice([1,2,3,4,5,6,7,8,9,10])
    monstre[i].tp(x,y)

print("bienvenue dans le monde " + player.name + ",\n bon courage")

running = True

timePlayer = pygame.time.get_ticks()
timeMonstre = pygame.time.get_ticks()

monstre_pos = list[list[int]]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    #player.map_player(monde.map)

    if 200 < pygame.time.get_ticks() - timePlayer:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            player.mouvement_haut(monde.map)
            timePlayer = pygame.time.get_ticks()
        if keys[pygame.K_s]:
            player.mouvement_bas(monde.map)
            timePlayer = pygame.time.get_ticks()
        if keys[pygame.K_q]:
            player.mouvement_gauche(monde.map)
            timePlayer = pygame.time.get_ticks()
        if keys[pygame.K_d]:
            player.mouvement_droit(monde.map)
            timePlayer = pygame.time.get_ticks()
        if keys[pygame.K_i]:
            player.inventaireVue()
            timePlayer = pygame.time.get_ticks()


    # zone méchant mob
    if 1000 < pygame.time.get_ticks() - timeMonstre:

        for i in [0,1,2,3,4]:
            mouv = random.choice([1,2,3,4])
            if mouv == 1:
                monstre[i].mouvement_haut(monde.map)
                timeMonstre = pygame.time.get_ticks()
            if mouv == 2:
                monstre[i].mouvement_bas(monde.map)
                timeMonstre = pygame.time.get_ticks()
            if mouv == 3:
                monstre[i].mouvement_gauche(monde.map)
                timeMonstre = pygame.time.get_ticks()
            if mouv == 4:
                monstre[i].mouvement_droit(monde.map)
                timeMonstre  = pygame.time.get_ticks()


    mapGraph.generateMapGraph(monde.map)
    mapGraph.drawEntity(player.coordonee)

    for i in [0, 1, 2, 3, 4]:
        mapGraph.drawEntity(monstre[i].coordonee)
    mapGraph.flip()































    # touche = input("haut -> 'z' \n"
    #                "bas  -> 's' \n"
    #                "droite -> 'd'\n"
    #                "gauche -> 'q'\n"
    #                "inventaire -> 'i'\n\n")
    #
    # if touche == "mort":
    #     player.mort()
    #
    # if touche == "z":
    #     player.mouvement_haut()
    # elif touche == "s":
    #     player.mouvement_bas()
    # elif touche == "d":
    #     player.mouvement_droit()
    # elif touche == "q":
    #     player.mouvement_gauche()
    # elif touche == "i":
    #     while len(player.inventaire) > 0:
    #         player.inventaireVue()
    #         i = input("choisier un item ou exit pour sortir\n")
    #         if i == "exit":
    #             break
    #         if int(i) <= len(player.inventaire):
    #             player.inventaireUtilisation(i)
    # monde.nettoyageMap()
pygame.quit()