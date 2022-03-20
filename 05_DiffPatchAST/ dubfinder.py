import ast
import sys
import inspect
from textwrap import dedent
from itertools import combinations
from importlib import import_module
from difflib import SequenceMatcher

attrs = ['name', 'id', 'arg', 'attr']
result = {}


def create(module_name, module):
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            if not name.startswith('__'):
                create(module_name + '.' + name, obj)
        elif inspect.isfunction(obj) or inspect.ismethod(obj):
            tree = ast.parse(dedent(inspect.getsource(obj)))
            for node in ast.walk(tree):
                for attr in attrs:
                    if hasattr(node, attr):
                        setattr(node, attr, '_')
            result[module_name + "." + name] = ast.unparse(tree)


for module_name in sys.argv[1:]:
    module = import_module(module_name)
    create(module_name, module)


for one, two in combinations(result.items(), r=2):
    if SequenceMatcher(None, one[1], two[1]).ratio() > 0.95:
        print(one[0], ":", two[0])