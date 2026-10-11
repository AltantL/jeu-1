import joueur
import map

print("test jeu\n\n\n")

monde = map.map()
monde.generationMonde()

monde.affichageMonde()

player = joueur.player()
player.nomJoueur()

spawn = (monde.lignes // 2)-1

player.tp(spawn, spawn)

print("bienvenue dans le monde " + player.name + ",\n bon courage")

while player.vie > 0:

    player.map_player(monde.maMap())

    touche = input("haut -> 'z' \n"
                   "bas  -> 's' \n"
                   "droite -> 'd'\n"
                   "gauche -> 'q'\n"
                   "inventaire -> 'i'\n")

    if touche == "z":
        player.mouvement_haut()
    elif touche == "s":
        player.mouvement_bas()
    elif touche == "d":
        player.mouvement_droit()
    elif touche == "q":
        player.mouvement_gauche()
    elif touche == "i":
        pass