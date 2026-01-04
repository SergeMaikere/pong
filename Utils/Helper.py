from functools import reduce

pipe = lambda *funcs: lambda arg: reduce( lambda g, f: f(g), funcs, arg )
