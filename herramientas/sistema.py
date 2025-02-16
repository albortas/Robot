import os
from log import Logger

log = Logger().configurar_logger('Sistema')


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Sistema(metaclass=Singleton):

    def __init__(self):

        try:
            log.debug('Cargando sistema...')

        except Exception as e:
            log.error('Problema al cargar el archivo sistema', e)

    def temperatura(self):
        try:
            temp = os.popen("vcgencmd measure_temp").readline() # Comando para obtener la temperatura del sistema
            # log.debug("System temperature: " + temp.replace("temp=", "")[:-5])
            return temp.replace("temp=", "")[:-5]
        except:
            return '000'

if __name__ == '__main__':
    sistema = Sistema()
    print(sistema.temperatura())