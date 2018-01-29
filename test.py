import serial
import os
import time
import datetime

deliminater="\r\n"

def showScreen(sp):
    for line in sp:
        print line

def resetLora():
    os.system("sh ./reset-lora.sh")

def setLora(sp, sf="7", ownid="7777", dstid="FFFF"):
    deliminater="\r\n"

    sp.write("1"+deliminater)
    showScreen(sp)

    sp.write("c"+deliminater)
    showScreen(sp)
    sp.write(sf+deliminater)
    showScreen(sp)

    sp.write("f"+deliminater)
    showScreen(sp)
    sp.write(ownid+deliminater)
    showScreen(sp)

    sp.write("g"+deliminater)
    showScreen(sp)
    sp.write(dstid+deliminater)
    showScreen(sp)

    sp.write("y"+deliminater)
    showScreen(sp)

def setLora2(sp, sf="7", ownid="7777", dstid="FFFF"):
    deliminater="\r\n"

    sp.write("1"+deliminater)

    sp.write("c"+deliminater)
    sp.write(sf+deliminater)

    sp.write("f"+deliminater)
    sp.write(ownid+deliminater)

    sp.write("g"+deliminater)
    sp.write(dstid+deliminater)

    sp.write("z"+deliminater)

    print "ready"

def sendTime(sp):
    while True:
        time.sleep(5)
        sp.write(str(datetime.datetime.now()))


#シリアルポートを開く
sp = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=1.2, stopbits=serial.STOPBITS_ONE)
