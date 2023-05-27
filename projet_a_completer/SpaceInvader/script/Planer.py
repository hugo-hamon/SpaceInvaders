from .interface import Interface, UserInput
from godot import exposed, export
from typing import Tuple, List
from .edit import run
from godot import *
import random

SPRITE_NAME = ["GreenPlaner", "RedPlaner", "YellowPlaner"]


@exposed
class Planer(KinematicBody2D):

	velocity = export(int, 300)
	direction = export(Vector2, Vector2(0, 0))
	time = export(float, 0.5)
	score = export(int, 0)
	sprite_name = export(str, "GreenPlaner")

	def _ready(self):
		self.interface = Interface(self)

		self.sprite_name = random.choice(SPRITE_NAME)
		self.screen_size = self.get_viewport().size
		self.sprite = self.get_node("AnimatedSprite")
		self.sprite_size = self.get_sprite_size()
		if self.sprite_name in ["GreenPlaner", "RedPlaner"]:
			self.sprite.set_scale(Vector2(1.25, 1.25))
		self.sprite.set_animation(self.sprite_name)

		self.bullet_scene = ResourceLoader.load("res://scenes/Bullet.tscn")

		self.set_position(Vector2(self.screen_size.x / 2,
								  self.screen_size.y - self.sprite_size.y))
		self.bullet_timer = self.get_node("BulletTimer")
		self.bullet_timer.start()

	def get_sprite_size(self):
		sprite_size = self.sprite.get_sprite_frames(
		).get_frame(self.sprite_name, 0).get_size()
		scale = self.sprite.get_transform().get_scale()
		return Vector2(sprite_size.x * scale.x, sprite_size.y * scale.y)

	def _physics_process(self, delta):
		self.direction = Vector2(0, 0)

		run(self.interface)

		self.direction = self.move_and_slide(self.direction, Vector2.UP)

	# Interface functions
	def shoot(self):
		if self.bullet_timer.is_stopped():
			b = self.bullet_scene.instance()
			self.owner.add_child(b)
			b.set_position(self.get_position() + Vector2(0, -40))
			self.bullet_timer.start(self.time)

	def move_spaceship(self, user_input: UserInput) -> None:
		"""Déplace le vaisseau dans la direction donnée (up, down, left, right)"""
		if user_input == UserInput.UP:
			self.direction.y = -self.velocity
		elif user_input == UserInput.DOWN:
			self.direction.y = self.velocity
		elif user_input == UserInput.LEFT:
			self.direction.x = -self.velocity
		elif user_input == UserInput.RIGHT:
			self.direction.x = self.velocity

	def get_spaceship_position(self) -> Tuple[int, int]:
		"""Retourne la position du vaisseau"""
		return self.get_position().x, self.get_position().y

	def get_spaceship_size(self) -> Tuple[int, int]:
		"""Retourne la taille du vaisseau"""
		return self.sprite_size.x, self.sprite_size.y

	def get_spaceship_speed(self) -> int:
		"""Retourne la vitesse du vaisseau"""
		return self.velocity

	def get_asteroid_position(self) -> List[Tuple[int, int]]:
		"""Retourne la position des astéroides"""
		return [
			(mob.get_position().x, mob.get_position().y)
			for mob in self.get_parent().get_children()
			if str(mob.get_name()) == "Mob" or str(mob.get_name()).startswith("@Mob")
		]

	def get_screen_size(self) -> Tuple[int, int]:
		"""Retourne la taille de l'écran"""
		return self.screen_size.x, self.screen_size.y

	def is_input_pressed(self, user_input: UserInput) -> bool:
		"""Retourne True si la touche direction est pressée, False sinon"""
		if user_input == UserInput.UP:
			return Input.is_action_pressed("up")
		elif user_input == UserInput.DOWN:
			return Input.is_action_pressed("down")
		elif user_input == UserInput.LEFT:
			return Input.is_action_pressed("left")
		elif user_input == UserInput.RIGHT:
			return Input.is_action_pressed("right")
		elif user_input == UserInput.SPACE:
			return Input.is_action_pressed("shoot")

	def get_score(self) -> int:
		"""Retourne le score actuel"""
		return self.score

	def increase_score(self) -> None:
		"""Augmente le score de 1"""
		self.score += 1

	def spaceship_collides(self) -> bool:
		"""Retourne True si le vaisseau est en collision avec un ennemi, False sinon"""
		#  get parent node
		parent = self.get_parent()
		return any(
			(str(mob.get_name()) == "Mob" or str(
				mob.get_name()).startswith("@Mob"))
			and mob.is_collide() for mob in parent.get_children()
		)

	def reset_game(self) -> None:
		"""Reset le jeu"""
		self.get_parent().game_over()
