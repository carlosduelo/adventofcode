from collections import deque
from dataclasses import dataclass
import typing as t
# Operations
# AND
# OR
# NOT
# LSHIFT
# RSHIFT

@dataclass
class Wire:
    _value: t.Optional[int] = None

    def set_value(self, value):
        if self._value is not None:
            raise ValueError(f'Wire is already computed {self}')
        self._value = value

    @property
    def value(self):
        if self._value is not None:
            return self._value
        raise ValueError('Not computed')


@dataclass(frozen=True)
class EQUAL:
    in1: str
    out: str
    def compute(self, circuit):
        circuit[self.out].set_value((int(self.in1) if self.in1.isdigit() else circuit[self.in1].value))

@dataclass(frozen=True)
class NOT:
    in1: str
    out: str
    def compute(self, circuit):
        circuit[self.out].set_value((int(self.in1) if self.in1.isdigit() else
                                     circuit[self.in1].value) ^ 65535)

@dataclass(frozen=True)
class RS:
    in1: str
    param: int
    out: str
    def compute(self, circuit):
        circuit[self.out].set_value((int(self.in1) if self.in1.isdigit() else
                                     circuit[self.in1].value) >> self.param)

@dataclass(frozen=True)
class LS:
    in1: str
    param: int
    out: str
    def compute(self, circuit):
        circuit[self.out].set_value((int(self.in1) if self.in1.isdigit() else
                                    circuit[self.in1].value) << self.param)

@dataclass(frozen=True)
class AND:
    in1: str
    in2: str
    out: str
    def compute(self, circuit):
        circuit[self.out].set_value((int(self.in1) if self.in1.isdigit() else
                                     circuit[self.in1].value) & (int(self.in2)
                                                                 if
                                                                 self.in2.isdigit()
                                                                 else
                                                                 circuit[self.in2].value))


@dataclass(frozen=True)
class OR:
    in1: str
    in2: str
    out: str
    def compute(self, circuit):
        circuit[self.out].set_value((int(self.in1) if self.in1.isdigit() else
                                     circuit[self.in1].value) | (int(self.in2)
                                                                 if
                                                                 self.in2.isdigit()
                                                                 else
                                                                 circuit[self.in2].value))


def create_wire(wires, name):
    if name not in wires:
        wires[name] = Wire()

def parse(wires, ops, line):
    e = line.split()
    if len(e) == 3: # Provide signal to wire
        create_wire(wires, e[0])
        create_wire(wires, e[2])
        ops.append(EQUAL(e[0], e[2]))
    elif len(e) == 4: # NOT
        create_wire(wires, e[1])
        create_wire(wires, e[3])
        ops.append(NOT(e[1], e[3]))
    elif len(e) == 5: # OTHER
        if e[1] == 'OR':
            create_wire(wires, e[0])
            create_wire(wires, e[2])
            create_wire(wires, e[4])
            ops.append(OR(e[0], e[2], e[4]))
        elif e[1] == 'AND':
            create_wire(wires, e[0])
            create_wire(wires, e[2])
            create_wire(wires, e[4])
            ops.append(AND(e[0], e[2], e[4]))
        elif e[1] == 'RSHIFT':
            create_wire(wires, e[0])
            create_wire(wires, e[4])
            ops.append(RS(e[0], int(e[2]), e[4]))
        elif e[1] == 'LSHIFT':
            create_wire(wires, e[0])
            create_wire(wires, e[4])
            ops.append(LS(e[0], int(e[2]), e[4]))
        else:
            raise ValueError(f'Error parsing {line}')
    else:
        raise ValueError(f'Error parsing {line}')

def read(path, wires=None):
    wires = wires if wires else {}
    operations = deque()
    with open(path, 'r') as stream:
        for line in stream:
            parse(wires, operations, line.strip())
    return wires, operations

def compute(wires, operations):
    while operations:
        op = operations.popleft()
        try:
            op.compute(wires)
        except ValueError:
            operations.append(op)
    return wires

def sample():
    wires = compute(*read('./sample'))
    assert wires['d'].value == 72
    assert wires['e'].value == 507
    assert wires['f'].value == 492
    assert wires['g'].value == 114
    assert wires['h'].value == 65412
    assert wires['i'].value == 65079
    assert wires['x'].value == 123
    assert wires['y'].value == 456

def problem():
    wires = compute(*read('./input'))
    assert wires['a'].value == 16076
    wires = compute(*read('./input2'))
    assert wires['a'].value == 2797

sample()
problem()
