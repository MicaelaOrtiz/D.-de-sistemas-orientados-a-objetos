from .reloj import Reloj

class RelojBuilder:
    def __init__(self):
        self._hora = 0
        self._minuto = 0
        self._segundo = 0

    def set_hora(self, h):
        self._hora = h
        return self

    def set_minuto(self, m):
        self._minuto = m
        return self

    def set_segundo(self, s):
        self._segundo = s
        return self

    def build(self):
        return Reloj(self._hora, self._minuto, self._segundo)
