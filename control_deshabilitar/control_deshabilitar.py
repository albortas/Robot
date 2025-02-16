import signal
import RPi.GPIO as GPIO
import sys
from herramientas.log import Logger
from herramientas.config import Config
import herramientas.colas as colas

log = Logger().configurar_logger('Control deshabilitar')

class ControlDeshabilitar:
    gpio_port = None

    def __init__(self, comunicacion_colas):

        try:

            log.debug('Configurar Control ...')

            signal.signal(signal.SIGINT, self.exit_gracefully) 
            signal.signal(signal.SIGTERM, self.exit_gracefully) 

            self.gpio_port = Config().get(Config.CONTROL_DESHABILITAR_GPIO_PORT) # 17

            GPIO.setmode(GPIO.BCM) # GPIO.BOARD
            GPIO.setup(self.gpio_port, GPIO.OUT) # GPIO.OUT

            self._deshabilar_colas = comunicacion_colas[colas.CONTROL_DESACTIVAR]
            self._pantalla_lcd_colas = comunicacion_colas[colas.PANTALLA_LCD_CONTROL]

            self.deshabilitar()

            self._pantalla_lcd_colas.put(colas.CONTROL_DESACTIVAR_PANTALLA_LCD_OK_ON)

        except Exception as e:
            log.error('Problema de inicializacion del controlador deshabilitar', e)
            self._pantalla_lcd_colas.put(colas.CONTROL_DESACTIVAR_PANTALLA_LCD_NOK)
            try:
                self.salir()
            finally:
                sys.exit(1)

    def salir(self, signum, frame):
        try:
            self.salir()
        finally:
            log.info('Terminado')
            sys.exit(0)

    def procesar_eventos_colas(self):

        try:
            while True:
                event = self._deshabilar_colas.get()

                if event == colas.CONTROL_DESACTIVAR_ACCION_ACTIVAR:
                    self.activar_servos()

                if event == colas.CONTROL_DESACTIVAR_ACCION_DESACTIVAR:
                    self.salir()

        except Exception as e:
            log.error('Problema desconocido al procesar la cola del controlador deshabilitar', e)
            sys.exit(1)

    def activar_servos(self):
        self._pantalla_lcd_colas.put(colas.CONTROL_DESACTIVAR_PANTALLA_LCD_OK_ON)
        GPIO.output(self.gpio_port, GPIO.LOW)

    def deshabilitar(self):
        self._pantalla_lcd_colas.put(colas.CONTROL_DESACTIVAR_PANTALLA_LCD_OK_OFF)
        GPIO.output(self.gpio_port, GPIO.HIGH)
