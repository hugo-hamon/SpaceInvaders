from .interface import Interface, Direction


def run(interface: Interface) -> None:
    """Fonction appelée à chaque tour de boucle"""
    print(interface.spaceship_collides())