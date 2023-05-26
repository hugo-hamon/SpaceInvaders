from collections import deque
from typing import Tuple
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Interface:

    def __init__(self, planer) -> None:
        self.planer = planer

    def move_spaceship(self, direction: Direction) -> None:
        """Déplace le vaisseau dans la direction donnée (up, down, left, right)"""
        self.planer.move_spaceship(direction)

    def shoot(self) -> None:
        """Tire un projectile"""
        self.planer.shoot()

    def get_spaceship_position(self) -> Tuple[int, int]:
        """Retourne la position du vaisseau"""
        return self.planer.get_spaceship_position()

    def get_spaceship_size(self) -> Tuple[int, int]:
        """Retourne la taille du vaisseau"""
        return self.planer.get_spaceship_size()

    def get_spaceship_speed(self) -> int:
        """Retourne la vitesse du vaisseau"""
        return self.planer.get_spaceship_speed()

    def get_screen_size(self) -> Tuple[int, int]:
        """Retourne la taille de l'écran"""
        return self.planer.get_screen_size()

    def is_input_pressed(self, direction: Direction) -> bool:
        """Retourne True si la touche direction est pressée, False sinon"""
        return self.planer.is_input_pressed(direction)

    def get_score(self) -> int:
        """Retourne le score actuel"""
        return self.planer.get_score()

    def increase_score(self) -> None:
        """Augmente le score de 1"""
        self.planer.increase_score()

    def spaceship_collides(self) -> bool:
        """Retourne True si le vaisseau est en collision avec un ennemi, False sinon"""
        return self.planer.spaceship_collides()
