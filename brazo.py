import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep

GPIO.setmode(GPIO.BCM)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(25,GPIO.OUT)    #Ponemos el pin 25 como salida
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(28, GPIO.OUT)
sm = GPIO.PWM(25,50)        #Ponemos el pin 25, 26, 27 y 28 en modo PWM y enviamos 50 pulsos por segundo
sm3= GPIO.PWM(26,50)
smp=GPIO.PWM(27,50)
smpg=GPIO.PWM(28,50)




sm.start(7.5) 
sm3.start(7.5)
smp.start(7.5) 
smpg.start(7.5)   
print("Iniciando")            #Enviamos un pulso del 7.5% para centrar el servo

try:                 
    while True:      #iniciamos un loop infinito
        opcion=input("Introduzca el caracter")


        if(opcion=="i"):
            sm3.ChangeDutyCycle(4.5)
            time.sleep(2)
            print("izquierda")

        elif (opcion=="d"):
            sm3.ChangeDutyCycle(10.5)
            time.sleep(2)
            print("derecha")

        elif (opcion=="c"):
            sm3.ChangeDutyCycle(7.5)
            time.sleep(2)
            print("centro")

        elif (opcion=="a"):
            sm.ChangeDutyCycle(10.5)
            time.sleep(2)
            print("abajo")

        elif (opcion=="s"):
            sm.ChangeDutyCycle(7.5)
            time.sleep(2)
            print("arriba subir brazo")

        elif (opcion=="g"):
            smpg.ChangeDutyCycle(10.5)
            time.sleep(2)
            print("pinza gira a 180 grados")

        elif (opcion=="o"):
            smpg.ChangeDutyCycle(4.5)
            time.sleep(2)
            print("pinza gira a 0 grados")
        
        elif (opcion=="t"):
            smp.ChangeDutyCycle(10.5)
            time.sleep(2)
            print("agarrar")

        elif (opcion=="l"):
            smp.ChangeDutyCycle(4.5)
            time.sleep(2)
            print("soltar")
except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    sm.stop()                      #Detenemos el servo
    sm3.stop()
    smp.stop()
    smpg.stop()
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script
