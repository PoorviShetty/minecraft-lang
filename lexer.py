from rply import LexerGenerator
lg = LexerGenerator()

# data types
lg.add("NUMBER", r"\d+")
lg.add("BLOCKTYPE", r'["\']([^"\']+)["\']')

# commands
lg.add("START", r"(?i)\bpunchtree\b")
lg.add("END", r"(?i)\bfallinlava\b")
lg.add("INC", r"(?i)\bmine\b")
lg.add("DEC", r"(?i)\bthrow\b")
lg.add("ADD", r"(?i)\bcombine\b")
lg.add("SUB", r"(?i)\bconsume\b")
lg.add("SET", r"(?i)\bsetitem\b")
lg.add("GET", r"(?i)\bgetitem\b")
lg.add("SHOW", r"(?i)\bshowinventory\b")

lg.ignore(r"\s+") # ignore whitespace
lg.ignore(r"(?s)#.*") # ignore comments

lexer = lg.build()