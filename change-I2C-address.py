# !/usr/bin/env python
# coding: latin-1
# Autor:   Ingmar Stapel
# Datum:   20170723
# Version:   1.0
# Homepage:   http://custom-build-robots.com

# Mit diesem Programm kann die Adresse des MaxBotix I2CXL MaxSonar
# Ultraschall  Sensors geaendert werden.

# Hier wird die smbus Python Bibliothek importiert.
import smbus
import time
import subprocess
import os

# Hier wird das Objekt dev fuer den I2C Bus 1 angelegt.
dev = smbus.SMBus(1)

# es wird der Bildschirm in der Konsole geloescht.
os.system('clear')
 
# Ausgabe einer Statusanzeige was das Programm gerade macht.
print '---------------------------------------------------------'
print 'Searching for i2c devices...'
time.sleep(0.5)
print 'This are the devices which are available:'
print '---------------------------------------------------------'
# Hier wird die Ausgabe des Aufrufes i2cdetect -y 1 via Python
# in dem Terminal-Fenster ausgegeben.
output = subprocess.check_output("i2cdetect -y 1", shell=True)
print output


# Dem Anwender wird angezeigt, dass jetzt die alte und neue Adresse 
# des Sensors eingegeben werden muss.
print '---------------------------------------------------------'
print 'Now you could change the sensor I2C address.'
print '---------------------------------------------------------'

try:
   addressOld = raw_input("The actual sensor address (e. g. 0x70):")
   addressNew = raw_input("The new sensor address (0x70 to 0x77):") 
except ValueError: 
   sys.exit()

print '---------------------------------------------------------'
print 'Checking if the new address could be used (0x70 to 0x77)'

# Die eingegebenen Adressen werden in Integer Werte umgewandelt.
addressOld = int(addressOld, 16)
addressNew = int(addressNew, 16)

# Pruefen ob die neue Adresse zulaessig ist und im vorgegebenen
# Intervall liegt.
# Um die Preufung zu deaktivieren muss hier die IF Abfrage 
# ausgebaut werden.

if addressNew in range(111, 120):

   time.sleep(0.5)
   print 'Changing the sensor I2C address...'
   print '---------------------------------------------------------'

   # Die neue Adresse wird geändert dazu erfolgt ein Bitshift 
   # nach links der Adresse (z. B. 0x73 << 1 = 0xE6)
   addressNew = addressNew << 1

   # Die Sequenz zum Aendern der Adresse wird an den Sensor 
   # geschickt.
   dev.write_block_data(addressOld, 0xe0, [0xAA, 0xA5, addressNew])
   time.sleep(1)
   os.system('clear')

   # Ausgabe einer Statusanzeige was das Programm gerade macht.
   print '---------------------------------------------------------'
   print 'Searching for i2c devices...'
   time.sleep(0.5)
   print 'This are the devices which are available:'
   print '---------------------------------------------------------'
   
   # Hier wird die Ausgabe des Aufrufes i2cdetect -y 1 via Python
   # in dem Terminal-Fenster ausgegeben.
   output = subprocess.check_output("i2cdetect -y 1", shell=True)
   print output
else:
   os.system('clear')
   print '---------------------------------------------------------'
   print"The new address is not vailid."
   print '---------------------------------------------------------'
# Ende des Programmes
