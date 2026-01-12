from settings import *
from functools import reduce
from typing import Callable
from random import choice, uniform
from pygame import Vector2

pipe = lambda *funcs: lambda arg: reduce( lambda g, f: f(g), funcs, arg )

get_random_vector: Callable[ [], Vector2 ] = lambda: pygame.Vector2( choice([1, -1]), uniform(0.2, 0.8) * choice([1, -1]) )