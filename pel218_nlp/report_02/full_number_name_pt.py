

NUMBER_DICT = {
    'centena': {
        '1': 'cento',
        '100': 'cem',
        '2': 'duzentos',
        '3': 'trezentos',
        '4': 'quatrocentos',
        '5': 'quinhentos',
        '6': 'seicentos',
        '7': 'setecentos',
        '8': 'oitocentos',
        '9': 'novecentos'
    },
    'dezena': {
        '10': 'dez',
        '11': 'onze',
        '12': 'doze',
        '13': 'treze',
        '14': 'catorze',
        '15': 'quinze',
        '16': 'dezesseis',
        '17': 'dezessete',
        '18': 'dezoito',
        '19': 'dezenove',
        '2': 'vinte',
        '3': 'trinta',
        '4': 'quarenta',
        '5': 'cinquenta',
        '6': 'sessenta',
        '7': 'setenta',
        '8': 'oitenta',
        '9': 'noventa'
    },
    'unidade': {
        '0': 'zero',
        '1': 'um',
        '2': 'dois',
        '3': 'tres',
        '4': 'quatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'sete',
        '8': 'oito',
        '9': 'nove'
    }
}
CONJ = " e "

class FST:
    """Finite State Machine"""
    def __init__(self, number: str) -> None:
        self.number = number
        self.name = ''
        self.digits = len(self.number) 
        
    def q0(self):
        """identify if number is hundred, dozen or units"""
        if self.digits == 3:
            self.q1()
        elif self.digits == 2:
            self.q2()
        else:
            self.q3()

    def q1(self):
        """handle hundred"""
        if self.number == '100':
            self.name += NUMBER_DICT['centena'][self.number]
        else:
            self.name += NUMBER_DICT['centena'][self.number[0]] + CONJ
            self.digits -= 1
            self.q2()

    def q2(self):
        """handle dozen"""
        if self.number[-self.digits] == '1':
            self.name += NUMBER_DICT['dezena'][self.number[-self.digits:]]
        else:
            self.name += NUMBER_DICT['dezena'][self.number[-self.digits]] + CONJ
            self.digits -= 1
            self.q3()

    def q3(self):
        """handle unit"""
        self.name += NUMBER_DICT['unidade'][self.number[-self.digits]]
        
class WriteNumber:
    def __init__(self, number: int) -> None:
        n = str(number)
        self.number = FST(n)

    def get_number_name(self) -> str:
        """return number full name in portuguese"""
        self.number.q0()
        return self.number.name
