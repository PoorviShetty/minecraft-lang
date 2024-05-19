from rply import ParserGenerator
from boxes import (
    ValueBox, 
    TypeBox, 
    SlotBox, 
    StartBox, 
    EndBox, 
    CommandsBox, 
    CommandTypeBox, 
    CommandBox, 
    MainBox
)
from lexer import lexer

pg = ParserGenerator([
        "NUMBER",
        "BLOCKTYPE", 
        "START",
        "END", 
        "INC", 
        "DEC", 
        "ADD", 
        "SUB", 
        "SET", 
        "GET",
        "SHOW"
    ])


@pg.production("main : start commands end")
def main(p):
    return MainBox(p[0], p[1], p[2])


@pg.production("commands : commands command")
def commands(p):
    return CommandsBox(p[0], p[1])


@pg.production("commands : ")
def empty_commands(p):
    return CommandsBox()


@pg.production("command : ADD number number")
def add_command(p):
    return CommandBox(CommandTypeBox(p[0]), p[1], p[2])


@pg.production("command : SUB number number")
def sub_command(p):
    return CommandBox(CommandTypeBox(p[0]), p[1], p[2])


@pg.production("command : INC number")
def inc_command(p):
    return CommandBox(CommandTypeBox(p[0]), p[1])


@pg.production("command : DEC number")
def dec_command(p):
    return CommandBox(CommandTypeBox(p[0]), p[1])


@pg.production("command : SET number blocktype number")
def sub_command(p):
    return CommandBox(CommandTypeBox(p[0]), p[1], p[2], p[3])


@pg.production("command : GET number")
def dec_command(p):
    return CommandBox(CommandTypeBox(p[0]), p[1])


@pg.production("command : SHOW")
def dec_command(p):
    return CommandBox(CommandTypeBox(p[0]))


@pg.production("number : NUMBER")
def number(p):
    return ValueBox(p[0])


@pg.production("blocktype : BLOCKTYPE")
def blocktype(p):
    return TypeBox(p[0])


@pg.production("start : START")
def start(p):
    return StartBox(p[0])


@pg.production("end : END")
def end(p):
    return EndBox(p[0])


parser = pg.build()
