# from logfilemixin import LogFileMixin
# from logprintmixin import LogPrintMixin


# lf = LogFileMixin()
# lf.log_error('Erro ao tentar estabelecer conexão.')
# lf.log_sucess('Conexão estabelecida')

# lp = LogPrintMixin()
# lp.log_error('Erro ao tentar estabelecer conexão.')
# lp.log_sucess('Conexão estabelecida')

from smartphone import Smartphone


iphone = Smartphone('iPhone')
iphone.ligar()
motorola = Smartphone('Motorola')
motorola.desligar()
