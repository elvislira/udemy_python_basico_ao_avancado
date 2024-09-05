from log import Log


class LogPrintMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})\n'
        print(msg_formatada)