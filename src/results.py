InventoryReturnEarly_G2 = 0x01
InventoryTimeOut_G2 = 0x02
InventoryMoreData_G2 = 0x03
ReadermoduleMCUFull_G2 = 0x04
AccessPasswordError = 0x05
DestroyPasswordError = 0x09
DestroyPasswordCannotZero = 0x0a
TagNotSupportCMD = 0x0b
AccessPasswordCannotZero = 0x0c
TagProtectedCannotSetAgain = 0x0d
TagNoProtectedDonotNeedUnlock = 0x0e
ByteLockedWriteFail = 0x10
CannotLock = 0x11
LockedCannotLockAgain = 0x12
ParameterSaveFailCanUseBeforeNoPower = 0x13
CannotAdjust = 0x14
InventoryReturnEarly_6B = 0x15
InventoryTimeOut_6B = 0x16
InventoryMoreData_6B = 0x17
ReadermoduleMCUFull_6B = 0x18
NotSupportCMDOrAccessPasswordCannotZero = 0x19
CMDExecuteErr = 0xF9
GetTagPoorCommunicationCannotOperation = 0xFA
NoTagOperation = 0xFB
TagReturnErrorCode = 0xFC
CMDLengthWrong = 0xFD
IllegalCMD = 0xFE
ParameterError = 0xFF
CommunicationErr = 0x30
RetCRCErr = 0x31
RetDataErr = 0x32
CommunicationBusy = 0x33
ExecuteCmdBusy = 0x34
ComPortOpened = 0x35
ComPortClose = 0x36
InvalidHandle = 0x37
InvalidPort = 0x38
RecmdErr = 0xEE

results_dict = {
    1: "Inventario terminado antes de tiempo",
    2: "Tiempo de espera de inventario excedido",
    3: "Más datos de inventario disponibles",
    4: "Módulo lector lleno",
    5: "Error de contraseña de acceso",
    9: "Error de contraseña de destrucción",
    10: "La contraseña de destrucción no puede ser cero",
    11: "La etiqueta no soporta el comando",
    12: "La contraseña de acceso no puede ser cero",
    13: "La etiqueta está protegida y no se puede configurar de nuevo",
    14: "La etiqueta no está protegida y no necesita desbloqueo",
    16: "Fallo de escritura de bloqueo de bytes",
    17: "No se puede bloquear",
    18: "Bloqueado y no se puede bloquear de nuevo",
    19: "Fallo al guardar el parámetro, se puede usar antes de que no haya energía",
    20: "No se puede ajustar",
    21: "Inventario terminado antes de tiempo (6B)",
    22: "Tiempo de espera de inventario excedido (6B)",
    23: "Más datos de inventario disponibles (6B)",
    24: "Módulo lector lleno (6B)",
    25: "Comando no soportado o contraseña de acceso no puede ser cero",
    249: "Error al ejecutar el comando",
    250: "Comunicación deficiente con la etiqueta, no se puede operar",
    251: "No hay operación de etiqueta",
    252: "La etiqueta devuelve el código de error",
    253: "Longitud del comando incorrecta",
    254: "Comando ilegal",
    255: "Error de parámetro",
    48: "Error de comunicación",
    49: "Error de CRC",
    50: "Error de datos",
    51: "Comunicación ocupada",
    52: "Ejecución de comando ocupada",
    53: "Puerto de comunicación abierto",
    54: "Puerto de comunicación cerrado",
    55: "Identificador no válido",
    56: "Puerto no válido",
    238: "Error de comando"
}
