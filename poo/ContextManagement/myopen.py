class MyOpen:
    def __init__(self, caminho, modo):
        self._caminho = caminho
        self._modo = modo
        self._arquivo = None

    def __enter__(self):
        self._arquivo = open(self._caminho, self._modo, encoding='utf8')

        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        self._arquivo.close()