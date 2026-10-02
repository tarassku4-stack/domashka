import inspect
import colorama
from colorama import init, Fore, Back, Style, AnsiToWin32



for name, obj in inspect.getmembers(colorama):
    if not name.startswith('_'):
        print(f"- {name}: {type(obj)}")


for name, method in inspect.getmembers(AnsiToWin32, predicate=inspect.isroutine):
    if not name.startswith('_'):
        print(f"  * {name}{inspect.signature(method)}")