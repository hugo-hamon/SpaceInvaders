from godot import exposed, export
from godot import *
import random

@exposed
class Level(Node):

	def _ready(self):
		self.mob_scene = ResourceLoader.load("res://scenes/Meteorite.tscn")
		self.score_label = self.get_node("ScoreLabel")
		self.player = self.get_node("Spaceship")
		print(self.player)
		self.screen_size = self.get_viewport().size
		self.spawn_timer = self.get_node("MeteoriteTimer")
		self.spawn_timer.connect("timeout", self, "_on_spawn_timer_timeout")
		self.spawn_timer.start()

	def _process(self, delta):
		self.score_label.set_text(f"Score: {self.player.score}")

	def _on_spawn_timer_timeout(self) -> None:
		self.spawn_mob()
		new_time = max(0.5, -1 / 50 * self.player.score + 2)
		self.spawn_timer.set_wait_time(random.uniform(new_time, new_time + 0.25))

	def spawn_mob(self) -> None:
		mob = self.mob_scene.instance()
		self.add_child(mob)
		position = Vector2(random.uniform(50, self.screen_size.x - 50), -100)
		mob.set_position(position)
		mob.set_linear_velocity(Vector2(0, random.randint(150, 200)))

	def game_over(self) -> None:
		# stop the spawn timer
		self.spawn_timer.stop()
		# delete all mobs
		for mob in self.get_children():
			if str(mob.get_name()) == "Meteorite" or str(mob.get_name()).startswith("@Meteorite"):
				mob.queue_free()
		# resete the score
		self.player.score = 0
		# move the player back to the start position
		self.player.set_position(Vector2(self.screen_size.x / 2, self.screen_size.y - 100))
		# start the spawn timer
		self.spawn_timer.start()
