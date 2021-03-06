from game import Game
import pygame
from constantes import *

pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption(nom)
screen = pygame.display.set_mode(taille_ecran)
icone = pygame.image.load(icon).convert_alpha()
pygame.display.set_icon(icone)

# importer de charger l'arriere plan de notre jeu
background = pygame.image.load(fond).convert()
screen.blit(background, (0, 0))

# initialiser le jeu
game = Game()

running = True

# Possitionnement initial de la pomme
game.coller_pomme()

# boucle tant que cette condition est vrai
while running:

    pygame.time.Clock().tick(15)

    game.changer_direction()

    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                # quelle touche a été utilisée
                if event.key == pygame.K_RIGHT:
                    game.tourner("right")
                    break
                elif event.key == pygame.K_LEFT:
                    game.tourner("left")
                    break
                elif event.key == pygame.K_DOWN:
                    game.tourner("down")
                    break
                elif event.key == pygame.K_UP:
                    game.tourner('up')
                    break
    except:
        break

    # Le serpent bouge à chaque fois même quand on n'appuie sur aucun bouton
    for i in range(len(game.player)):
        game.avancer(i)

    # C'est quand il a mangé la pomme
    if game.player[0].rect == game.apple.rect:
        game.coller_pomme()
        game.score += 1
        print(f"Le score est de {game.score}")

    # Quand il mange une pomme le serpent grandit
    if game.score > game.AncienScore:
        game.grandir()

    # appliquer l'arriere plan de notre jeu
    try:
        screen.blit(background, (0, 0))
    except:
        print("Fermeture du programme")
        continue

    # appliquer le serpent
    for partie in game.player:
        screen.blit(partie.image, partie.rect)

    # appliquer la pomme
    screen.blit(game.apple.image, game.apple.rect)
    pygame.display.flip()
