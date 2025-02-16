import logging #Permite configurar el registro de mensajes (logs)
from pathlib import Path # Permite trabajar con rutas de archivos

ROBOT = 'Robot' #Variable global de la clase

class Logger:
    #Constructor sin parámetros
    def __init__(self):
        #Carpeta donde se guardarán los logs
        logs_folder = 'logs/' #Carpeta donde se guardarán los logs
        Path(logs_folder).mkdir(parents=True, exist_ok=True) #Crea la carpeta si no existe

        # Crea un handler (manejador) de archivos que registra incluso mensajes de depuración
        self.logging_file_handler = logging.FileHandler(logs_folder + ROBOT + '.log') #Crea un archivo de logs
        # self.logging_file_handler.setLevel(logging.INFO)

        # Crea un handler (manejador) de consola con un nivel de registro más alto
        self.logging_stream_handler = logging.StreamHandler() # Manejador de consola
        # self.logging_stream_handler.setLevel(logging.DEBUG)

        # Crea un formateador y lo añade a los manejadores
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logging_file_handler.setFormatter(formatter)
        self.logging_stream_handler.setFormatter(formatter)

    def configurar_logger(self, nombre_logger=None): #Configura el logger
        if not nombre_logger:
            nombre_logger = ROBOT
        else:
            nombre_logger = ROBOT + ' ' + nombre_logger

        logger = logging.getLogger("{:<32}".format(nombre_logger)) #Crea un logger con el nombre del robot

        logger.setLevel(logging.INFO) #Establece el nivel de registro

        # Añade los manejadores al logger
        logger.addHandler(self.logging_file_handler)
        logger.addHandler(self.logging_stream_handler)

        return logger
    
if __name__ == '__main__':
    log = Logger().setup_logger('Sistema') #Configura el logger con el nombre del sistema
    # log.debug('Log de depuración') 
    log.info('Log de información')
    log.warning('Log de advertencia')
    log.error('Log de error')
    log.critical('Log crítico')
