from rply.token import BaseBox
from rply.token import Token  


class ValueBox(BaseBox):
    def __init__(self, value):
        self.value = value
    def get_number(self):
        return int(self.value.getstr())
    def is_block_type(self):
        return False


class TypeBox(BaseBox):
    def __init__(self, value):
        self.value = value
    def get_type(self):
        if self.value.getstr() != '<START>' and self.value.getstr() != '<END>' and self.value.getstr() != '<SLOT>' and self.value.getstr() != '<TYPE>' and self.value.getstr() != '<VALUE>':
            return self.value.getstr()
        return ValueError('Invalid block type')
    def is_block_type(self):
        return True


class SlotBox(BaseBox):
    def __init__(self, value):
        self.value = value
    def get_number(self):
        return int(self.value.getstr())


class StartBox(BaseBox):
    def __init__(self, value):
        self.value = '<START>'
    def get_action(self):
        return self.value


class EndBox(BaseBox):
    def __init__(self, value):
        self.value = '<END>'
    def get_action(self):
        return self.value


class CommandsBox(BaseBox):
    def __init__(self, commands=None, command=None):
        self.commands = commands
        self.command = command

    def get_list(self):
        if self.commands:
            return self.commands.get_list() + [self.command]
        return []


class CommandTypeBox(BaseBox):
    def __init__(self, value):
        self.value = value
    def get_type(self):
        if self.value.gettokentype() in ['ADD']:
            return [self.value.gettokentype(), '<SLOT>', '<SLOT>']
        elif self.value.gettokentype() in ['SUB']:
            return [self.value.gettokentype(), '<SLOT>', '<VALUE>']
        elif self.value.gettokentype() in ['INC', 'DEC']:
            return [self.value.gettokentype(), '<SLOT>']
        elif self.value.gettokentype() in ['SET']:
            return [self.value.gettokentype(), '<SLOT>', '<BLOCK>', '<VALUE>']
        elif self.value.gettokentype() in ['GET']:
            return [self.value.gettokentype(), '<SLOT>']
        elif self.value.gettokentype() in ['SHOW']:
            return [self.value.gettokentype()]
        else:
            return ValueError('Invalid command type')


class CommandBox(BaseBox):
    def __init__(self, command, arg1 = None, arg2 = None, arg3 = None):
        self.command = command
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def eval_with(self):
        command_str = ''
        a = self.arg1.get_number() if self.arg1 is not None else 'N/A'
        b = ''
        if self.arg2 is not None:
            if self.arg2.is_block_type():
                b = self.arg2.get_type()
            if not self.arg2.is_block_type():
                b = self.arg2.get_number()
        c = self.arg3.get_number() if self.arg3 is not None else 'N/A'

        # yes, I am ashamed
        if self.command.get_type()[0] == 'ADD':
            command_str += f'inventory[{a}][1] = inventory[{a}][1] + inventory[{b}][1] if (inventory[{a}][0]).lower() == (inventory[{b}][0]).lower() else (_ for _ in ()).throw(ValueError("Error: Cannot combine"))\n'
            command_str += f'inventory[{b}][1] = 0\n'
        elif self.command.get_type()[0] == 'SUB':
            command_str += f'inventory[{a}][1] = inventory[{a}][1] - inventory[{b}][1] if ((inventory[{a}][0]).lower() == (inventory[{b}][0]).lower() and (inventory[{a}][1] >= inventory[{b}][1])) else (_ for _ in ()).throw(ValueError("Error: Cannot consume"))\n'
            command_str += f'inventory[{b}][1] = 0\n'
        elif self.command.get_type()[0] == 'INC':
            command_str += f'inventory[{a}][1] = inventory[{a}][1] + 1 if (inventory[{a}][1] is not None) else (_ for _ in ()).throw(ValueError("Error: Cannot increment"))\n'
        elif self.command.get_type()[0] == 'DEC':
            command_str += f'inventory[{a}][1] = inventory[{a}][1] - 1 if (inventory[{a}][1] is not None and inventory[{a}][1] > 0) else (_ for _ in ()).throw(ValueError("Error: Cannot decrement"))\n'
        elif self.command.get_type()[0] == 'SET':
            command_str += f'inventory[{a}] = [{b}, {c}] if top < 10 else (_ for _ in ()).throw(ValueError("Inventory full!"))\n'
            command_str += f'top += 1\n'
        elif self.command.get_type()[0] == 'GET':
            prepare_str = f'Slot {a} '
            prepare_str += f'has {{}} {{}} blocks!\".format(inventory[{a}][0], inventory[{a}][1])'
            command_str += 'print("' + prepare_str + ')\n'
        elif self.command.get_type()[0] == 'SHOW':
            command_str += 'print("----------")\n'
            command_str += 'print("INVENTORY:")\n'
            command_str += 'print("----------")\n'
            command_str += 'print("\\n".join([f"Slot {i} has {item[1]} {item[0]} blocks!" for i, item in enumerate(inventory[ : top])]))\n'
        else:
            return ValueError('Invalid command arguments')
        return command_str


class MainBox(BaseBox):
    def __init__(self, start, commands, end, inventory = []):
        self.start = start
        self.commands = commands
        self.end = end
        self.inventory = inventory

    def eval(self):
        command_str = 'inventory = [None] * 10\n'
        command_str += 'top = 0\n'
        if self.start.get_action() == '<START>':
            # command_str += self.start.get_action() + '\n'
            for i in self.commands.get_list(): 
                command_str += i.eval_with()
            # command_str += self.end.get_action() 
                       
            # VERY UNSAFE
            exec(command_str)
        else:
            return 'NOT STARTED'
