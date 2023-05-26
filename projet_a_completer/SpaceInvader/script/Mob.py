from godot import exposed, export
from typing import Tuple
from godot import *


@exposed
class Mob(RigidBody2D):

	def _ready(self):
		pass

	def _process(self, delta):
		"""Fonction appelée à chaque frame"""
		pass

	def is_collide(self) -> bool:
		"""Retourne si le mob est en collision"""
		return bool(self.get_colliding_bodies())

	def get_position(self) -> Tuple[int, int]:
		"""Retourne la position du mob"""
		return self.position.x, self.position.y
