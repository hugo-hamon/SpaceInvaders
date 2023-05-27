from .interface import Interface, UserInput


def run(interface: Interface) -> None:
    """Fonction appelée à chaque tour de boucle"""
    if interface.spaceship_collides():
        interface.reset_game()
    if interface.is_input_pressed(UserInput.UP):
        interface.move_spaceship(UserInput.UP)
    if interface.is_input_pressed(UserInput.DOWN):
        interface.move_spaceship(UserInput.DOWN)
    if interface.is_input_pressed(UserInput.LEFT):
        interface.move_spaceship(UserInput.LEFT)
    if interface.is_input_pressed(UserInput.RIGHT):
        interface.move_spaceship(UserInput.RIGHT)
    if interface.is_input_pressed(UserInput.SPACE):
        interface.shoot()
