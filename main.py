import ctypes

from src.UHF_functions import *

#Variables
port = ctypes.c_int(6000) # El puerto de red del lector
ipaddr = ctypes.c_char_p(b"192.168.68.253") # La dirección IP del lector
comadr = ctypes.c_ubyte(0) # La dirección del lector
frmhandle = ctypes.c_long(0) # El manejador del puerto de comunicación

versioninfo = ctypes.c_ubyte(0) # La información de la versión del firmware
readertype = ctypes.c_ubyte(0) # El tipo de lector
trtype = ctypes.c_ubyte(0) # El tipo de protocolo soportado
dmaxfre = ctypes.c_ubyte(0) # La frecuencia máxima de trabajo
dminfre = ctypes.c_ubyte(0) # La frecuencia mínima de trabajo
powerdbm = ctypes.c_ubyte(0) # La potencia de salida del lector
scantime = ctypes.c_ubyte(0) # El tiempo límite para el comando de inventario
parameter = (ctypes.c_ubyte*10)(0) # El parámetro de modo de trabajo

adrtid = ctypes.c_ubyte(0) # La dirección de inicio del TID
lentid = ctypes.c_ubyte(0) # El número de palabras del TID
tidflag = ctypes.c_ubyte(0) # El flag del TID (0 para EPC, 1 para TID)
epclenandepc = (ctypes.c_ubyte*100)(0) # El array que almacena el resultado del inventario
totallen = ctypes.c_long(0) # El número de bytes del array
cardnum = ctypes.c_long(0) # El número de etiquetas detectadas

EPC = (ctypes.c_ubyte)(0) # El valor EPC de la etiqueta
Mem = ctypes.c_ubyte(0) # El área de memoria a leer
WordPtr = ctypes.c_ubyte(0) # La dirección de los datos de la etiqueta a leer
Num = ctypes.c_ubyte(12) # El número de palabras a leer
Password = (ctypes.c_ubyte)(0) # La contraseña de acceso de la etiqueta
maskadr = ctypes.c_ubyte(0) # La dirección de inicio de la máscara EPC
maskLen = ctypes.c_ubyte(1) # Los bytes de la máscara
maskFlag = ctypes.c_ubyte(0) # La bandera de la máscara EPC
Data = (ctypes.c_ubyte)(0) # El array de los datos leídos de la etiqueta
EPClength = ctypes.c_ubyte(1) # La longitud en bytes de EPC
errorcode = ctypes.c_ubyte(0) # El código de error

#main
result = OpenNetPort(port, 
            ipaddr, 
            comadr,
            ctypes.byref(frmhandle))
if result == 0:
    print("Puerto abierto con éxito")

GetReaderInformation(comadr,
                     ctypes.byref(versioninfo),
                     ctypes.byref(readertype),
                     ctypes.byref(trtype),
                     ctypes.byref(dmaxfre), 
                     ctypes.byref(dminfre),
                     ctypes.byref(powerdbm),
                     ctypes.byref(scantime),
                     frmhandle)

GetWorkModeParameter(comadr, 
                     parameter, 
                     frmhandle)

res_inventory = Inventory_G2(ctypes.byref(comadr), 
                      adrtid, 
                      lentid, 
                      tidflag, 
                      epclenandepc, 
                      ctypes.byref(totallen), 
                      ctypes.byref(cardnum), 
                      frmhandle)

read_result = ReadCard_G2(ctypes.byref(comadr), 
                            EPC, 
                            Mem, 
                            WordPtr, 
                            Num, 
                            Password, 
                            maskadr, 
                            maskLen, 
                            maskFlag, 
                            Data, 
                            EPClength, 
                            ctypes.byref(errorcode), 
                            frmhandle)

# Cerrar el puerto de comunicacion
result = CloseNetPort(frmhandle)

# -Declaración de funciones
def print_res_inventory(res_inventory):
    if res_inventory == 0: 
        print("Inventario realizado con éxito")
    elif res_inventory == 1:
        print("Retorno antes de final de inventario")
    elif res_inventory == 2:
        print(" Tiempo de escaneo de inventario agotado.")
    elif res_inventory == 3:
        print("Más datos")
    elif res_inventory == 4:
        print("El MCU del módulo lector está lleno")
    else:
        print("Error de inventario")

# Imprimir el resultado
print(f"""
Parámetros del lector:
comadr: {comadr.value}
Version info: {versioninfo.value}
readertype: {readertype.value}
trtype: {trtype.value}
dmaxfre: {dmaxfre.value}
dminfre: {dminfre.value}
powerdbm: {powerdbm.value}
scantime: {scantime.value}
parameters:  
    '-> Wg_mode: {parameter[0]}'
    '-> Wg_Data_Inteval: {parameter[1]}'
    '-> Wg_Pulse_Width: {parameter[2]}'
    '-> Wg_Pulse_Inteval: {parameter[3]}'
    '-> Read_mode: {parameter[4]}'
    '-> Mode_state: {parameter[5]}'
    '-> Mem_Inven: {parameter[6]}'
    '-> First_Adr: {parameter[7]}'
    '-> Word_Num: {parameter[8]}'
    '-> Tag_Time: {parameter[9]}'
""") 

# Imprimir el resultado
if result == 0:
    print("Puerto cerrado con éxito")
print(f"""
Etiquetas detectadas: {cardnum.value}
totallen: {totallen.value}
""")

print_res_inventory(res_inventory)
print(f"readresult es {hex(read_result)}")
print(f"errorcode: {hex(errorcode.value)}")

def process_cards(n, data):
    cards = []
    pos = 0
    for i in range(n):
        lenght = data[pos]
        epc = data[pos+1:pos+lenght+1]
        pos = pos + lenght + 1
        cards.append("".join(str(format(x, "02X")) for x in epc))
    return cards

cards = process_cards(cardnum.value, epclenandepc)

print("\nLas etiquietas son:")
for card in cards:
    print(card)
