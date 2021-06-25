from string import ascii_lowercase, ascii_uppercase

class FST:
    """Finite State Machine"""
    def __init__(self, name: str) -> None:
        self.name = name
        self.new_name = ''
        self.k = 0

    def q0(self):
        char = self.name[self.k]

        if char in ascii_lowercase:
            self.new_name += char.upper()
        else:
            self.new_name += char
            
        self.k += 1
        self.q1()
    
    def q1(self):
        while self.k < len(self.name):
            char = self.name[self.k]
            self.k += 1
            if char in ascii_uppercase:
                self.new_name += char.lower()
            elif char == ' ':
                self.new_name += char
                self.q0()
            else:
                self.new_name += char

class FormatName:
    def __init__(self, name: str) -> None:
        self.name = FST(name.strip())

    def title(self):
        self.name.q0()
        return self.name.new_name
