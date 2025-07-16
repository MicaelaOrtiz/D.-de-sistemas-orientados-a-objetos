class Reloj:
    __instancia_unica = None

    def __new__(cls, *args, **kwargs):
        if kwargs.get("singleton", False):
            if cls.__instancia_unica is None:
                cls.__instancia_unica = super(Reloj, cls).__new__(cls)
            return cls.__instancia_unica
        return super(Reloj, cls).__new__(cls)

    def __init__(self, hora: int, minuto: int, segundo: int):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, valor):
        self.__hora = valor

    @property
    def minuto(self):
        return self.__minuto

    @minuto.setter
    def minuto(self, valor):
        self.__minuto = valor

    @property
    def segundo(self):
        return self.__segundo

    @segundo.setter
    def segundo(self, valor):
        self.__segundo = valor

    def __str__(self):
        return f"{self.__hora:02}:{self.__minuto:02}:{self.__segundo:02}"

    def adelantar_minuto(self):
        self.__minuto += 1
        if self.__minuto >= 60:
            self.__minuto = 0
            self.__hora += 1
            if self.__hora >= 24:
                self.__hora = 0

    def update_hora(self, h, m, s):
        self.__hora = h
        self.__minuto = m
        self.__segundo = s

    def __eq__(self, otro):
        return (
            self.__hora == otro.hora and
            self.__minuto == otro.minuto and
            self.__segundo == otro.segundo
        )
