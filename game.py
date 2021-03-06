import pygame
from player import Bloc, Apple
from random import randrange
from constantes import *


class Game:  # Je modifie la classe pour crée
    def __init__(self):
        self.player = [Bloc(100, 250)]
        self.direction = ["right" for i in range(len(self.player))]

        self.apple = Apple()

        # Les variables pour les scores
        self.score = 0
        self.AncienScore = 0

        self.coordonnée = [] # Prepare le grandir du serpent en gardant les coordonnées des pommes

    def changer_direction(self):
        """
        Quand le serpent bouge il faut assingner les changements directions.
        """
        if not len(self.player) == 1:
            for i in range(len(self.player) - 1, -1, -1):
                if i > 0:  # Pour pas modifier en compte le premier element
                    self.direction[i] = self.direction[i - 1]

    def coller_pomme(self):
        """
        Cette fonction doit choisir l'emplacement du fruit wumpa de façon aléatoires
        """
        # Ces variables serviront à éviter d'avoir le serpent et la pomme au même endroit
        egal_x, egal_y = True, True

        while egal_x:
            # On choisit un nombre pour le x
            x, egal_x = randrange(0, 500, 25), False

            # Cette boucle verifie si cette coordonnée est déjà assigné
            for bloc in self.player:
                if bloc.rect.x == x:
                    egal_x = True
                    break

        while egal_y:
            y, egal_y = randrange(0, 500, 25), False
            for bloc in self.player:
                if bloc.rect.y == y:
                    egal_y = True
                    break

        self.apple.rect.x, self.apple.rect.y = x, y
        self.coordonnée.append(Bloc(x, y))

    def tourner(self, direction):
        """
        Cette procedure sert à tourner le personnage par rapport à la direction ou il va déjà. Car il peut pas aller
        dans l'autre sens d'un seul coup.
        
        param direction: str, envoie la nouvelle direction voulu.
        """

        # Parcours d'un dictionnaire en prenant la cle et sa valeur
        for cle, val in direction_inverse.items():
            if direction == cle and not self.direction[0] == val:
                self.direction[0] = direction

    def teleport(self, bloc):
        """
        Quand le joueur sort du terrain, il apparait l'autre côté.
        """

        if self.player[bloc].rect.x >= 500:
            self.player[bloc].rect.x = 0

        elif self.player[bloc].rect.x <= -25:
            self.player[bloc].rect.x = 500

        elif self.player[bloc].rect.y >= 500:
            self.player[bloc].rect.y = 0

        elif self.player[bloc].rect.y <= -25:
            self.player[bloc].rect.y = 500

    def avancer(self, bloc):
        """
        Cette procédure sert à faire avancer le joueur dans toutes les directions.

        param bloc: int, indice du bloc
        """
        if self.direction[bloc] == "right":
            self.player[bloc].move_right()

        elif self.direction[bloc] == "left":
            self.player[bloc].move_left()

        elif self.direction[bloc] == "up":
            self.player[bloc].move_up()

        elif self.direction[bloc] == "down":
            self.player[bloc].move_down()

        for i in range(len(self.player)):
            if not bloc == i and self.player[bloc].rect == self.player[i].rect:
                print("Lose")
                pygame.quit()

        self.teleport(bloc)

    def grandir(self):
        """
        Quand le serpent mange une pomme il faut bien qu'il grandisse
        """
        if not self.coordonnée[0].rect in self.player:
            self.player.append(self.coordonnée.pop(0))
            self.direction.append(len(self.direction) - 1)
            self.AncienScore += 1