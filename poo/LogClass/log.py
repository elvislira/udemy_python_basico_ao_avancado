class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log.')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Success: {msg}')
