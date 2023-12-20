import math
from pathlib import Path
from typing import Tuple, List

from common.puzzle import Puzzle
from common.util import read_lines


class Module:
    def __init__(self, name):
        self.name = name
        self.outputs = []

    def get_output(self, inp: Tuple[str, bool]) -> List[Tuple[str, bool]]:
        pass

    def __repr__(self):
        return f'{self.name}: {self.outputs}'


class FlipFlop(Module):
    def __init__(self, name):
        super().__init__(name)
        self.value = False

    def get_output(self, inp):
        source, value = inp
        output = []
        if not value:
            self.value = not self.value
            for o in self.outputs:
                output.append((self.name, self.value, o))
        return output

    def __repr__(self):
        return f'{self.name}, [{self.value}], {self.outputs}'


class Conjunction(Module):
    def __init__(self, name):
        super().__init__(name)
        self.inputs = {}

    def get_output(self, inp):
        source, value = inp
        self.inputs[source] = value
        high = value
        for i in self.inputs.values():
            high &= i
        output = []
        for o in self.outputs:
            output.append((self.name, not high, o))
        return output

    def __repr__(self):
        return f'{self.name}, {self.inputs}, {self.outputs}'


class Broadcaster(Module):
    def __init__(self):
        super().__init__('broadcaster')

    def get_output(self, inp):
        output = []
        for o in self.outputs:
            output.append((self.name, False, o))
        return output


class Button(Module):
    def __init__(self):
        super().__init__('button')

    def get_output(self, inp):
        return [(self.name, False, 'broadcaster')]


class Output(Module):
    def __init__(self):
        super().__init__('output')

    def get_output(self, inp):
        return []


class Twenty(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        modules = self.read_modules(self.data)
        low = 0
        high = 0
        for n in range(1000):
            todo = modules['button'].get_output(('start', False))
            while len(todo) > 0:
                source, value, out = todo.pop(0)
                if value:
                    high += 1
                else:
                    low += 1
                todo.extend(modules[out].get_output((source, value)))
        return low * high

    def read_modules(self, data):
        modules = {}
        for line in data:
            module_name = line[0:line.index(' ')]
            if module_name.startswith('%'):
                module_name = module_name[1:]
                modules[module_name] = FlipFlop(module_name)
            elif module_name.startswith('&'):
                module_name = module_name[1:]
                modules[module_name] = Conjunction(module_name)
            else:
                modules['broadcaster'] = Broadcaster()
        modules['button'] = Button()
        modules['output'] = Output()
        for line in data:
            module_name = line[0:line.index(' ')]
            if module_name.startswith('%') or module_name.startswith('&'):
                module_name = module_name[1:]
            outputs = line[line.rfind('>') + 1:]
            splits = [x.strip() for x in outputs.split(',')]
            for s in splits:
                if s not in modules.keys():
                    s = 'output'
                modules[module_name].outputs.append(s)
                if isinstance(modules[s], Conjunction):
                    modules[s].inputs[module_name] = False
        return modules

    def part_two(self):
        modules = self.read_modules(self.data)
        mod = modules['output']
        while not isinstance(mod, Conjunction):
            mod = next(filter(lambda module: mod.name in module.outputs, modules.values()))
        inputs = [key for key in mod.inputs.keys()]
        presses = 0
        cycles = []
        while len(inputs) > 0:
            presses += 1
            todo = modules['button'].get_output(('start', False))
            while len(todo) > 0:
                source, value, out = todo.pop(0)
                if out == 'rm':
                    if value:
                        cycles.append(presses)
                        inputs.remove(source)
                todo.extend(modules[out].get_output((source, value)))
        return math.lcm(*cycles)


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = Twenty(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())