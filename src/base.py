import ctypes

from . import uhf_functions, results

# Crear una clase Comunicacion que representa la comunicación entre el programa y el lector RFID
class Comunication:
    # Inicializar la instancia con el puerto y la dirección de comunicación
    def __init__(self, ipAddr, port=6000):
        self.ipAddr = ipAddr
        self.port = port
        self.comPort = comPort # El puerto de comunicación que usa el lector
        self.comAdr = comAdr # La dirección de comunicación del lector
        self.frmHandle = 0 # El identificador del puerto de comunicación del lector

    # Definir un método para abrir el puerto de red especificado y devolver el frmHandle
    def openNetPort(self):
        port = ctypes.c_int(self.port)
        ipAddr = ctypes.c_char_p((self.ipAddr.encode('utf-8')))
        comAdr = ctypes.c_ubyte(self.comAdr)
        frmHandle = ctypes.c_long(0)
        try:
            result = OpenNetPort(port, ipAddr, comAdr, ctypes.byref(frmHandle))
            if result == 0:
                self.frmHandle = frmHandle
            if result in results_dict:
                raise ComunicacionError(results_dict[result])
            return result    
        except ComunicacionError:
            # Lanzar una excepción personalizada con el mensaje de error
            raise ComunicacionError(f"Error al abrir el puerto de red {port} con la dirección IP {ipAddr}")

    # Definir un método para cerrar el puerto de red
    def closeNetPort(self):
        frmhandle = ctypes.c_long(self.frmHandle)
        try:
            result = CloseNetPort(frmhandle)
            if result in results_dict:
                raise ComunicacionError(results_dict[result])
        except ComunicacionFail:
            raise ComunicacionError(f"Error al intentar cerrar el puerto", result)

    def openComPort(self, comPort):
    # Definir un método para abrir el puerto de comunicación especificado y devolver el frmHandle  
        pass

    def autoOpenComPort(self):
    # Definir un método para abrir automáticamente el puerto de comunicación y devolver el comPort y el frmHandle
        pass

    def closeComPort(self):
    # Definir un método para cerrar el puerto de comunicación
        pass
    
    def closeSpecComPort(self, comPort):
    # Definir un método para cerrar el puerto de comunicación especificado
        pass





# Crear una clase LectorRFID que representa un lector RFID que se comunica con las etiquetas
class LectorRFID:
    # Inicializar la instancia con una instancia de la clase Comunicacion que gestiona la comunicación con el lector
    def __init__(self, comunicacion):
        self.comunicacion = comunicacion # Una instancia de la clase Comunicacion
        self.readerInfo = {} # Un diccionario que almacena la información del lector
        self.workMode = None # El modo de trabajo del lector
        self.workModeParams = {} # Un diccionario que almacena los parámetros del modo de trabajo
        self.wg

class ComunicacionError(Exception):
    # Inicializar la instancia con el mensaje de error
    def __init__(self, mensaje):
        # Llamar al método __init__ de la clase base
        super().__init__(mensaje)
        # Almacenar el mensaje de error como un atributo
        self.mensaje = mensaje


