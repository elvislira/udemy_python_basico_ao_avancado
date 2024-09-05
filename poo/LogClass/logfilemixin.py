from logabstrato import Log


FILE_NAME = 'logs.log'

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})\n'

        with open(FILE_NAME, 'a') as file:
            file.write(msg_formatada)