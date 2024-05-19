import os

from lexer import lexer
from parser import parser

def main():
    import sys
    begin(sys.argv)
    
    
def read_file(file_name):
    if not file_name.endswith('.mine'):
        print("Error: Only files with a .mine extension are allowed.")
        quit()
    else:
        try:
            with open(file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' does not exist.")
        except IOError:
            print(f"Error: Could not read the file '{file_name}'.")
    
    
def begin(argv):
    if len(argv) > 1:
        code = read_file(argv[1])
        tokens = []
        for line in code.split('\n'):
            for token in (list(lexer.lex(line))):
                tokens.append(token)
        print(parser.parse(iter(tokens)).eval())
    else:
        print("Please provide a filename.")
   
    
if __name__ == '__main__':
    main()