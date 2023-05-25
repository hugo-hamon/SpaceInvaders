from godot import exposed, export
from godot import *
import random

@exposed
class Spaceship(KinematicBody2D):

	velocity = export(int, 300)
	direction = export(Vector2, Vector2(0, 0))
	time = export(float, 0.5)
	score = export(int, 0)
	sprite_size = Vector2(0, 0)

	def _ready(self):
		self.screen_size = self.get_viewport().size
		self.sprite = self.get_node("AnimatedSprite")
		self.sprite_size = self.get_sprite_size()

		self.projectile_scene = ResourceLoader.load("res://scenes/Projectile.tscn")

		self.set_position(Vector2(self.screen_size.x / 2, self.screen_size.y - self.sprite_size.y))
		self.projectile_timer = self.get_node("ProjectileTimer")
		self.projectile_timer.start()

	def get_sprite_size(self):
		sprite_size = self.sprite.get_sprite_frames().get_frame("Idle", 0).get_size()
		scale = self.sprite.get_transform().get_scale()
		return Vector2(sprite_size.x * scale.x, sprite_size.y * scale.y)

	def _physics_process(self, delta):
		self.direction = Vector2(0, 0)

		self.process_input()
		self.check_screen_colision()
		
		self.direction = self.move_and_slide(self.direction, Vector2.UP)

	def process_input(self) -> None:
		if Input.is_action_pressed("right"):
			self.direction.x = self.velocity
		if Input.is_action_pressed("left"):
			self.direction.x = -self.velocity
		if Input.is_action_pressed("up"):
			self.direction.y = -self.velocity
		if Input.is_action_pressed("down"):
			self.direction.y = self.velocity
		if Input.is_action_pressed("shoot"):
			if self.projectile_timer.is_stopped():
				self.shoot()
				self.projectile_timer.start(self.time)

	def check_screen_colision(self) -> None:
		if self.get_position().x > self.screen_size.x - self.sprite_size.x / 2:
			self.set_position(Vector2(self.screen_size.x - self.sprite_size.x / 2, self.get_position().y))
		if self.get_position().x < self.sprite_size.x / 2:
			self.set_position(Vector2(self.sprite_size.x / 2, self.get_position().y))
		if self.get_position().y > self.screen_size.y - self.sprite_size.y / 2:
			self.set_position(Vector2(self.get_position().x, self.screen_size.y - self.sprite_size.y / 2))
		if self.get_position().y < self.sprite_size.y / 2:
			self.set_position(Vector2(self.get_position().x, self.sprite_size.y / 2))

	def shoot(self):
		b = self.projectile_scene.instance()
		self.owner.add_child(b)
		b.set_position(self.get_position() + Vector2(0, -40))
