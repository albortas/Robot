from log import Logger

log = Logger().configurar_logger('Sistema') #Configura el logger con el nombre del sistema


class Singleton(type): #Clase Singleton para instanciar una sola vez la clase General
    _instancia = {} #Diccionario para almacenar las instancias

    def __call__(cls, *args, **kwargs): #Metodo que se ejecuta al instanciar la clase
        if cls not in cls._instancia: #Si la clase no esta en el diccionario
            cls._instancia[cls] = super(Singleton, cls).__call__(*args, **kwargs) #Se crea una instancia de la clase
        return cls._instancia[cls]


class General(metaclass=Singleton): #Clase General que se instancia una sola vez

    def __init__(self): #Metodo que se ejecuta al instanciar la clase

        try:
            log.debug('Cargando general...')

        except Exception as e:
            log.error('Problema al cargar el singleton general', e)

    def maprange(self, a, b, s): #Función que mapea un rango a otro
        (a1, a2), (b1, b2) = a, b 
        return b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

if __name__ == '__main__':
    general = General() #Instancia la clase General
    print(general.maprange((0, 100), (0, 1), 50)) #Imprime el resultado de la función maprange
    print(general.maprange((0, 100), (0, 1), 100)) #Imprime el resultado de la función maprange