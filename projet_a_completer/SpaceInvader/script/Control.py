from godot import exposed, export
from godot import *


@exposed
class Control(Control):

	def _ready(self):
		pass

	def _on_QuitButton_pressed(self):
		self.get_tree().quit()

	def _on_PlayButton_pressed(self):
		self.get_tree().change_scene("res://scenes/Level.tscn")
