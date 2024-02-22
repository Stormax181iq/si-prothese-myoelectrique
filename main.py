from microbit import *

# Initialisation du servomoteur (pin0):
position = 50
pin0.set_analog_period_microseconds(20000)
pin0.write_analog(position)

# Initialisation du capteur de force (pin1):
forceMaxN = 5 # en Newton
forceMax = int(forceMaxN * 51.15) # en sortie analogique

while True:
    forceLecture = pin1.read_analog() # valeur entre 0 et 1023

    if forceLecture <= forceMax:
        position += 5
        pin0.write_analog(position)
        sleep(100) # Pause le servomoteur pour éviter un effort excessif

    else:
        pass # Arrêt du servomoteur
