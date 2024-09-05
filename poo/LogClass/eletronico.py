from logprintmixin import LogPrintMixin


class Eletronico(LogPrintMixin):
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado is not True:
            self._ligado = True
            self.log_sucess(f'{self._nome} está ligado.')
        else:
            self.log_error(f'{self._nome} já está ligado.')
    
    def desligar(self):
        if self._ligado:
            self._ligado = False
            self.log_sucess(f'{self._nome} foi desligado.')
        else:
            self.log_error(f'{self._nome} já está desligado.')