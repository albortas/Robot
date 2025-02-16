import json  # Módulo para trabajar con archivos JSON
import sys #Módulo que provee acceso a algunas variables usadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete
import os # Módulo que provee una forma portable de usar la funcionalidad dependiente del sistema operativo
from log import Logger
import jmespath  # http://jmespath.org/tutorial.html para hacer consultas en archivos JSON
import shutil # Módulo que permite copiar archivos
from pathlib import Path # Módulo que permite trabajar con rutas de archivos y directorios

log = Logger().configurar_logger('Configuracion')


class Singleton(type): # Clase que permite que solo se pueda instanciar una vez la clase
    _instancia = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancia:
            cls._instancia[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instancia[cls]


class Config(metaclass=Singleton):
    CONTROL_DESHABILITAR_GPIO_PORT = 'control_deshabilitar[0].gpio_port'
    PANTALLA_LCD_CONTROL_I2C_DIRECCION = 'pantalla_lcd_control[0].pantalla_lcd[0].direccion'
    DISPOSITIVO_CONTROL_REMOTO = 'dispositivo_control_remoto[0].control_remoto[0].dispositivo'

    PLACA_CONTROL_MOVIMIENTO_PCA9685_DIRECCION = 'control_movimiento[*].placa[*].pca9685[*].direccion | [0] | [0] | [0]'
    PLACA_CONTROL_MOVIMIENTO_PCA9685_VELOCIDAD_CLOCK_REFENRENCIA = 'control_movimiento[*].placa[*].pca9685_1[*].velocidad_clock_referencia | [0] | [0] | [0]'
    PLACA_CONTROL_MOVIMIENTO_PCA9685_FRECUENCIA = 'control_movimiento[*].placa[*].pca9685_1[*].frecuencia | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_HOMBRO_IZQUIERDO_PCA9685 = 'control_movimiento[*].servos[*].hombro_posterior_izquierdo[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_HOMBRO_IZQUIERDO_CANAL = 'control_movimiento[*].servos[*].hombro_posterior_izquierdo[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_HOMBRO_IZQUIERDO_MIN_PULSO = 'control_movimiento[*].servos[*].hombro_posterior_izquierdo[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_HOMBRO_IZQUIERDO_MAX_PULSO = 'control_movimiento[*].servos[*].hombro_posterior_izquierdo[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_HOMBRO_IZQUIERDO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].hombro_posterior_izquierdo[*].angulo_reposo | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_BRAZO_IZQUIERDO_PCA9685 = 'control_movimiento[*].servos[*].brazo_posterior_izquierdo[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_BRAZO_IZQUIERDO_CANAL = 'control_movimiento[*].servos[*].brazo_posterior_izquierdo[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_BRAZO_IZQUIERDO_MIN_PULSO = 'control_movimiento[*].servos[*].brazo_posterior_izquierdo[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_BRAZO_IZQUIERDO_MAX_PULSO = 'control_movimiento[*].servos[*].brazo_posterior_izquierdo[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_BRAZO_IZQUIERDO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].brazo_posterior_izquierdo[*].angulo_reposo | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_PIE_IZQUIERDO_PCA9685 = 'control_movimiento[*].servos[*].pie_posterior_izquierdo[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_PIE_IZQUIERDO_CANAL = 'control_movimiento[*].servos[*].pie_posterior_izquierdo[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_PIE_IZQUIERDO_MIN_PULSO = 'control_movimiento[*].servos[*].pie_posterior_izquierdo[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_PIE_IZQUIERDO_MAX_PULSO = 'control_movimiento[*].servos[*].pie_posterior_izquierdo[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_PIE_IZQUIERDO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].pie_posterior_izquierdo[*].angulo_reposo | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_HOMBRO_DERECHO_PCA9685 = 'control_movimiento[*].servos[*].hombro_posterior_derecho[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_HOMBRO_DERECHO_CANAL = 'control_movimiento[*].servos[*].hombro_posterior_derecho[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_HOMBRO_DERECHO_MIN_PULSO = 'control_movimiento[*].servos[*].hombro_posterior_derecho[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_HOMBRO_DERECHO_MAX_PULSO = 'control_movimiento[*].servos[*].hombro_posterior_derecho[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_HOMBRO_DERECHO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].hombro_posterior_derecho[*].angulo_reposo | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_BRAZO_DERECHO_PCA9685 = 'control_movimiento[*].servos[*].brazo_posterior_derecho[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_BRAZO_DERECHO_CANAL = 'control_movimiento[*].servos[*].brazo_posterior_derecho[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_BRAZO_DERECHO_MIN_PULSO = 'control_movimiento[*].servos[*].brazo_posterior_derecho[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_BRAZO_DERECHO_MAX_PULSO = 'control_movimiento[*].servos[*].brazo_posterior_derecho[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_BRAZO_DERECHO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].brazo_posterior_derecho[*].angulo_reposo | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_PIE_DERECHO_PCA9685 = 'control_movimiento[*].servos[*].pie_posterior_derecho[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_PIE_DERECHO_CANAL = 'control_movimiento[*].servos[*].pie_posterior_derecho[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_PIE_DERECHO_MIN_PULSO = 'control_movimiento[*].servos[*].pie_posterior_derecho[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_PIE_DERECHO_MAX_PULSO = 'control_movimiento[*].servos[*].pie_posterior_derecho[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_POSTERIOR_PIE_DERECHO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].pie_posterior_derecho[*].angulo_reposo | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_HOMBRO_IZQUIERDO_PCA9685 = 'control_movimiento[*].servos[*].hombro_anterior_izquiero[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_HOMBRO_IZQUIERDO_CANAL = 'control_movimiento[*].servos[*].hombro_anterior_izquiero[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_HOMBRO_IZQUIERDO_MIN_PULSO = 'control_movimiento[*].servos[*].hombro_anterior_izquiero[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_HOMBRO_IZQUIERDO_MAX_PULSO = 'control_movimiento[*].servos[*].hombro_anterior_izquiero[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_HOMBRO_IZQUIERDO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].hombro_anterior_izquiero[*].angulo_reposo | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_BRAZO_IZQUIERDO_PCA9685 = 'control_movimiento[*].servos[*].brazo_anterior_izquierdo[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_BRAZO_IZQUIERDO_CANAL = 'control_movimiento[*].servos[*].brazo_anterior_izquierdo[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_BRAZO_IZQUIERDO_MIN_PULSO = 'control_movimiento[*].servos[*].brazo_anterior_izquierdo[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_BRAZO_IZQUIERDO_MAX_PULSO = 'control_movimiento[*].servos[*].brazo_anterior_izquierdo[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_BRAZO_IZQUIERDO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].brazo_anterior_izquierdo[*].angulo_reposo | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_PIE_IZQUIERDO_PCA9685 = 'control_movimiento[*].servos[*].pie_anterior_izquierdo[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_PIE_IZQUIERDO_CANAL = 'control_movimiento[*].servos[*].pie_anterior_izquierdo[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_PIE_IZQUIERDO_MIN_PULSO = 'control_movimiento[*].servos[*].pie_anterior_izquierdo[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_PIE_IZQUIERDO_MAX_PULSO = 'control_movimiento[*].servos[*].pie_anterior_izquierdo[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_PIE_IZQUIERDO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].pie_anterior_izquierdo[*].angulo_reposo | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_HOMBRO_DERECHO_PCA9685 = 'control_movimiento[*].servos[*].hombro_anterior_derecho[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_HOMBRO_DERECHO_CANAL = 'control_movimiento[*].servos[*].hombro_anterior_derecho[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_HOMBRO_DERECHO_MIN_PULSO = 'control_movimiento[*].servos[*].hombro_anterior_derecho[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_HOMBRO_DERECHO_MAX_PULSO = 'control_movimiento[*].servos[*].hombro_anterior_derecho[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_HOMBRO_DERECHO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].hombro_anterior_derecho[*].angulo_reposo | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_BRAZO_DERECHO_PCA9685 = 'control_movimiento[*].servos[*].brazo_anterior_derecho[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_BRAZO_DERECHO_CANAL = 'control_movimiento[*].servos[*].brazo_anterior_derecho[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_BRAZO_DERECHO_MIN_PULSO = 'control_movimiento[*].servos[*].brazo_anterior_derecho[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_BRAZO_DERECHO_MAX_PULSO = 'control_movimiento[*].servos[*].brazo_anterior_derecho[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_BRAZO_DERECHO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].brazo_anterior_derecho[*].angulo_reposo | [0] | [0] | [0]'

    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_PIE_DERECHO_PCA9685 = 'control_movimiento[*].servos[*].pie_anterior_derecho[*].pca9685 | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_PIE_DERECHO_CANAL = 'control_movimiento[*].servos[*].pie_anterior_derecho[*].canal | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_PIE_DERECHO_MIN_PULSO = 'control_movimiento[*].servos[*].pie_anterior_derecho[*].min_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_PIE_DERECHO_MAX_PULSO = 'control_movimiento[*].servos[*].pie_anterior_derecho[*].max_pulso | [0] | [0] | [0]'
    CONTROL_MOVIMIENTO_SERVO_ANTERIOR_PIE_DERECHO_ANGULO_REPOSO = 'control_movimiento[*].servos[*].pie_anterior_derecho[*].angulo_reposo | [0] | [0] | [0]'

    valores = {} # Diccionario que almacena los valores del archivo de configuración

    def __init__(self): # Método constructor de la clase

        try:
            log.debug('Cargando configuraciones...')

            self.cargar_configuracion()
            self.lista_modulos()

        except Exception as e:
            log.error('Problema al cargar el archivo de configuracion', e)

    def cargar_configuracion(self):
        try:
            if not os.path.exists(str(Path.home()) + '/robot.json'): # Si no existe el archivo de configuración
                shutil.copyfile(str(Path.home()) + '/robot/robot.default', # Copia el archivo de configuración por defecto
                                str(Path.home()) + '/robot.json') # En la ruta del usuario

            with open(str(Path.home()) + '/robot.json') as json_file: # Abre el archivo de configuración
                self.valores = json.load(json_file) # Carga los valores del archivo de configuración en el diccionario
                # log.debug(json.dumps(self.valores, indent=4, sort_keys=True)) # Imprime el diccionario con formato

        except Exception as e:
            log.error("El archivo de configuracion no existe o no es un json valido, se cancelara.")
            sys.exit(1)

    def lista_modulos(self): # Método que lista los módulos
        log.info('Configuracion detectada para los modulos: ' + ', '.join(self.valores.keys())) # Imprime los módulos

    def guardar_configuracion(self): # Método que guarda la configuración
        try:
            with open('~/robot.json', 'w') as outfile: # Abre el archivo de configuración en modo escritura
                json.dump(self.valores, outfile) # Guarda los valores del archivo de configuración en el diccionario
        except Exception as e:
            log.error("Problema al guardar el archivo de configuracion", e)

    def obtener(self, buscar_patron): # Método que obtiene un valor del archivo de configuración
        log.debug(buscar_patron + ': ' + str(jmespath.search(buscar_patron, self.valores))) # Imprime el valor del archivo de configuración
        return jmespath.search(buscar_patron, self.valores) # Retorna el valor del archivo de configuración

    def obtener_nombre_seccion(self, buscar_patron): # Método que obtiene un valor del archivo de configuración

        PCA9685 = 'control_movimiento[*].servos[*].' + str(buscar_patron) + '[*].pca9685 | [0] | [0] | [0]'
        CANAL = 'control_movimiento[*].servos[*].' + str(buscar_patron) + '[*].canal | [0] | [0] | [0]'
        MIN_PULSO = 'control_movimiento[*].servos[*].' + str(buscar_patron) + '[*].min_pulso | [0] | [0] | [0]'
        MAX_PULSO = 'control_movimiento[*].servos[*].' + str(buscar_patron) + '[*].max_pulso | [0] | [0] | [0]'
        ANGULO_REPOSO = 'control_movimiento[*].servos[*].' + str(buscar_patron) + '[*].angulo_reposo | [0] | [0] | [0]'

        PCA9685 = jmespath.search(PCA9685, self.valores) # Imprime el valor del archivo de configuración

        PCA9685_DIRECCION = 'control_movimiento[*].placa[*].pca9685' + str(PCA9685) + '[*].direccion | [0] | [0] | [0]'
        PCA9685_VELOCIDAD_CLOCK_REFERENCIA = 'control_movimiento[*].placa[*].pca9685' + str(PCA9685) + '[*].velocidad_clock_referencia | [0] | [0] | [0]'
        PCA9685_FRECUENCIA = 'control_movimiento[*].placa[*].pca9685' + str(PCA9685) + '[*].frecuencia | [0] | [0] | [0]'

        log.info('PCA9685_DIRECCION: ' + str(jmespath.search(PCA9685_DIRECCION, self.valores)))
        log.info('PCA9685_VELOCIDAD_CLOCK_REFERENCIA: ' + str(jmespath.search(PCA9685_VELOCIDAD_CLOCK_REFERENCIA, self.valores)))
        log.info('PCA9685_FRECUENCIA: ' + str(jmespath.search(PCA9685_FRECUENCIA, self.valores)))
        log.info('CANAL: ' + str(jmespath.search(CANAL, self.valores)))
        log.info('MIN_PULSO: ' + str(jmespath.search(MIN_PULSO, self.valores)))
        log.info('MAX_PULSO: ' + str(jmespath.search(MAX_PULSO, self.valores)))
        log.info('ANGULO_REPOSO: ' + str(jmespath.search(ANGULO_REPOSO, self.valores)))

        return jmespath.search(PCA9685_DIRECCION, self.valores), jmespath.search(PCA9685_VELOCIDAD_CLOCK_REFERENCIA, self.valores), jmespath.search(PCA9685_FRECUENCIA, self.valores), jmespath.search(CANAL, self.valores), jmespath.search(MIN_PULSO, self.valores), jmespath.search(MAX_PULSO, self.valores), jmespath.search(ANGULO_REPOSO, self.valores)


if __name__ == "__main__":
    configuracion = Config() # Instancia la clase Config
    print(configuracion.obtener('control_deshabilitar[0].gpio_port')) # Imprime el valor del archivo de configuración
    print(configuracion.obtener('pantalla_lcd_control[0].pantalla_lcd[0].direccion')) # Imprime el valor del archivo de configuración
    print(configuracion.obtener('dispositivo_control_remoto[0].control_remoto[0].dispositivo')) # Imprime el valor del archivo de configuración
    print(configuracion.obtener('control_movimiento[*].placa[*].pca9685[*].direccion | [0] | [0] | [0]')) # Imprime el valor del archivo de configuración
    print(configuracion.obtener('control_movimiento[*].placa[*].pca9685[*].velocidad_clock_referencia | [0] | [0] | [0]')) # Imprime el valor del archivo de configuración
    print(configuracion.obtener('control_movimiento[*].placa[*].pca9685[*].frecuencia | [0] | [0] | [0]')) # Imprime el valor del archivo de configuración
    print(configuracion.obtener('control_movimiento[*].servos[*].hombro_posterior_izquierdo[*].pca9685 | [0] | [0] | [0]')) # Imprime el valor del archivo de configuración
    print(configuracion.obtener('control_movimiento[*].servos[*].hombro_posterior_izquierdo[*].canal | [0] | [0] | [0]')) # Imprime el valor del archivo de configuración
    print(configuracion.obtener('control_movimiento[*].servos[*].hombro_posterior_izquierdo[*].min_pulso | [0] | [0] | [0]')) # Imprime el valor del archivo de configuración
    print(configuracion.obtener('control_movimiento[*].servos[*].hombro_posterior_izquierdo[*].max_pulso | [0] | [0] | [0]')) # Imprime el valor del archivo de configuración
    print(configuracion.obtener('control_movimiento[*].servos[*].hombro_posterior_izquierdo[*].angulo_reposo | [0] | [0] | [0]')) # Imprime el valor del archivo de configuración