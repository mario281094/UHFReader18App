import ctypes

dll = ctypes.WinDLL("dlls\\UHFReader18.dll")

# Estas funciones son WINAPI
OpenNetPort = dll.OpenNetPort # Abre el puerto de comunicación por TCP
CloseNetPort = dll.CloseNetPort # Cierra el puerto de comunicación
GetReaderInformation = dll.GetReaderInformation # Obtiene información de la configuración del lector
GetWorkModeParameter = dll.GetWorkModeParameter #btiene parámetros del modo de trabajo
Inventory_G2 = dll.Inventory_G2 # Detecta etiquetas en el área inductiva y obtiene sus valores EPC
ReadCard_G2 = dll.ReadCard_G2 # Lee parte o toda la memoria de una etiqueta

# Establecer el prototipo y los parámetros de la función
# - OpenNetPort
OpenNetPort.argtypes = [ctypes.c_int, #Port
                        ctypes.c_char_p, #IPaddr
                        ctypes.POINTER(ctypes.c_ubyte), #ComAdr
                        ctypes.POINTER(ctypes.c_long)] #FrmHandle
OpenNetPort.restype = ctypes.c_long #0 si es exitoso, no cero si hay un error


# - GetReaderInformation
GetReaderInformation.argtypes = [ctypes.POINTER(ctypes.c_ubyte), #ComAdr: Dirección del lector
                                 ctypes.POINTER(ctypes.c_ubyte), #VersionInfo Versión del firmware
                                 ctypes.POINTER(ctypes.c_ubyte), #ReaderType Tipo de lector
                                 ctypes.POINTER(ctypes.c_ubyte), #TrType Tipo de protocolo
                                 ctypes.POINTER(ctypes.c_ubyte), #dmaxfre Frecuencia máxima de trabajo
                                 ctypes.POINTER(ctypes.c_ubyte), #dminfre: Frecuencia mínima de trabajo
                                 ctypes.POINTER(ctypes.c_ubyte), #powerdBm: Potencia de salida del lector
                                 ctypes.POINTER(ctypes.c_ubyte), #ScanTime: Tiempo límite para el comando de inventario
                                 ctypes.c_long] #FrmHandle: Manejador de comunicación al que está conectado el lector. Se obtiene cuando se llama a la función OpenNetPort
GetReaderInformation.restype = ctypes.c_long #Retorno: Cero si éxito, no cero si error

# - Inventory_G2 Detecta etiquetas en el área inductiva y obtiene sus valores EPC
Inventory_G2.argtypes = [ctypes.POINTER(ctypes.c_ubyte), #ComAdr: Dirección del lector.
                         ctypes.c_ubyte, #AdrTID: Dirección de inicio de la consulta TID
                         ctypes.c_ubyte, #LenTID: Número de palabras de datos de la consulta TID
                         ctypes.c_ubyte, #TIDFlag: Bandera de la consulta TID (en 1 consulta TID, en 0 EPC)
                         ctypes.POINTER(ctypes.c_ubyte), #EPClenandEPC: Datos EPC de la etiqueta leída por el lector 
                         ctypes.POINTER(ctypes.c_long), #Totallen: Cantidad de bytes de EPClenandEPC
                         ctypes.POINTER(ctypes.c_long), #CardNum: Número de etiquetas detectadas
                         ctypes.c_long] #FrmHandle: Manejador de comunicación al que está conectado el lector.
Inventory_G2.restype = ctypes.c_long #- 0: Éxito.- 0x01: Retorno antes de que finalice el inventario.- 0x02: Tiempo de escaneo de inventario agotado. - 0x03: Más datos. - 0x04: El MCU del módulo lector está lleno. - Otros: Error.

# - GetWorkModeParameter Obtiene parámetros del modo de trabajo
GetWorkModeParameter.argtypes = [ctypes.POINTER(ctypes.c_ubyte), #ComAdr: Puntero a la dirección del lecto
                                 ctypes.POINTER(ctypes.c_ubyte), #Puntero a 10 bytes con el parámetro del modo de trabajo. Desde el primer byte hasta el undécimo, respectivamente, son: Wg_mode, Wg_Data_Inteval, Wg_Pulse_Width, Wg_Pulse_Inteval, Read_mode, Mode_state, Mem_Inven, First_Adr, Word_Num, Tag_Time, Accuracy.
                                 ctypes.c_long] #FrmHandle: Manejador de comunicación al que está conectado el lector.
GetWorkModeParameter.restype = ctypes.c_long #Retorno: Cero si éxito, no cero si error

# - CloseNetPort  Desconecta un puerto de red
CloseNetPort.argtypes = [ctypes.c_long] #FrmHandle: Manejador del puerto de red
CloseNetPort.restype = ctypes.c_long #Retorno: Cero si éxito, no cero si error

# - ReadCard_G2 Lee parte o toda la memoria de una etiqueta
ReadCard_G2.argtypes = [ctypes.POINTER(ctypes.c_ubyte), #ComAdr: Dirección del lector
                        ctypes.POINTER(ctypes.c_ubyte), #EPC: Valor EPC de la etiqueta
                        ctypes.c_ubyte, #Mem: Área de memoria a leer
                        ctypes.c_ubyte, #WordPtr: Dirección de los datos de la etiqueta a leer
                        ctypes.c_ubyte, #Num: Número de palabras a leer
                        ctypes.POINTER(ctypes.c_ubyte), #Password: Contraseña de acceso de la etiqueta
                        ctypes.c_ubyte, #maskadr: Dirección de inicio de la máscara EPC
                        ctypes.c_ubyte, #maskLen: Bytes de máscara
                        ctypes.c_ubyte, #maskFlag: Bandera de máscara EPC
                        ctypes.POINTER(ctypes.c_ubyte), #Data: Datos leídos de la etiqueta
                        ctypes.c_ubyte, #EPClength: Longitud en bytes de EPC
                        ctypes.POINTER(ctypes.c_ubyte), #errorcode: Byte de explicación cuando el valor de retorno es 0xFC
                        ctypes.c_long] #FrmHandle: Manejador del puerto de comunicación
ReadCard_G2.restype = ctypes.c_long #Retorno: Cero si éxito, no cero si error