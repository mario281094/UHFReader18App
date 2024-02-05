import ctypes

dll = ctypes.CDLL("D:\\TRABAJO\RFID\\I+D+I\\UHFReader18App\\UHFReader18App\\dlls\UHFReader18.dll")

OpenNetPort = dll.OpenNetPort # Abre el puerto de comunicación por TCP
CloseNetPort = dll.CloseNetPort #Cierra el puerto de comunicación
GetReaderInformation = dll.GetReaderInformation
Inventory_G2 = dll.Inventory_G2
ReadCard_G2 = dll.ReadCard_G2

# Establecer el prototipo y los parámetros de la función
# - OpenNetPort
OpenNetPort.argtypes = [ctypes.c_int, #Port
                        ctypes.c_char_p, #IPaddr
                        ctypes.POINTER(ctypes.c_ubyte), #ComAdr
                        ctypes.POINTER(ctypes.c_long)] #FrmHandle
OpenNetPort.restype = ctypes.c_long
GetWorkModeParameter = dll.GetWorkModeParameter #0 si es exitoso, no cero si hay un error

# - GetReaderInformation
GetReaderInformation.argtypes = [ctypes.POINTER(ctypes.c_ubyte), 
                                 ctypes.POINTER(ctypes.c_ubyte), 
                                 ctypes.POINTER(ctypes.c_ubyte), 
                                 ctypes.POINTER(ctypes.c_ubyte), 
                                 ctypes.POINTER(ctypes.c_ubyte), 
                                 ctypes.POINTER(ctypes.c_ubyte), 
                                 ctypes.POINTER(ctypes.c_ubyte), 
                                 ctypes.POINTER(ctypes.c_ubyte), 
                                 ctypes.c_long]
GetReaderInformation.restype = ctypes.c_long

# - Inventory_G2
Inventory_G2.argtypes = [ctypes.POINTER(ctypes.c_ubyte), 
                         ctypes.c_ubyte, ctypes.c_ubyte, 
                         ctypes.c_ubyte, 
                         ctypes.POINTER(ctypes.c_ubyte), 
                         ctypes.POINTER(ctypes.c_long), 
                         ctypes.POINTER(ctypes.c_long), 
                         ctypes.c_long]
Inventory_G2.restype = ctypes.c_long

# - GetWorkModeParameter
GetWorkModeParameter.argtypes = [ctypes.POINTER(ctypes.c_ubyte), 
                                 ctypes.POINTER(ctypes.c_ubyte), 
                                 ctypes.c_long]
GetWorkModeParameter.restype = ctypes.c_long

# - CloseNetPort 
CloseNetPort.argtypes = [ctypes.c_long]
CloseNetPort.restype = ctypes.c_long

# - ReadCard_G2
ReadCard_G2.argtypes = [ctypes.POINTER(ctypes.c_ubyte), 
                        ctypes.POINTER(ctypes.c_ubyte), 
                        ctypes.c_ubyte, ctypes.c_ubyte, 
                        ctypes.c_ubyte, 
                        ctypes.POINTER(ctypes.c_ubyte), 
                        ctypes.c_ubyte, 
                        ctypes.c_ubyte, 
                        ctypes.c_ubyte, 
                        ctypes.POINTER(ctypes.c_ubyte), 
                        ctypes.c_ubyte, 
                        ctypes.POINTER(ctypes.c_ubyte), 
                        ctypes.c_long]
ReadCard_G2.restype = ctypes.c_long