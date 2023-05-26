from godot import exposed, export
from godot import *


@exposed
class Bullet(Area2D):

	speed = export(int, 500)

	def _ready(self):
		self.planer = self.get_parent().get_node("Planer")

	def _physics_process(self, delta):
		self.position += Vector2(0, -self.speed * delta)
		if self.position.y < 0:
			self.queue_free()

	def _process(self, delta):
		# Check collision
		for body in self.get_overlapping_bodies():
			if body.is_in_group("Enemy"):
				self.planer.score += 1
				self.queue_free()
				body.queue_free()
				break
