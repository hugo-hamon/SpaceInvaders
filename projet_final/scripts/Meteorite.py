from godot import exposed, export
from godot import *


@exposed
class Meteorite(RigidBody2D):
						
	def _ready(self):
		pass
						
	def _process(self, delta):
		"""Fonction appelée à chaque frame"""
		if collision := self.get_colliding_bodies() or self.position.y > 1000:
			self.get_parent().game_over()
			self.queue_free()
