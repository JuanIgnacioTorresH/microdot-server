# Configuracion inicial
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

#defino función 
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect("Cooperadora Alumnos", "")
        while not sta_if.isconnected():
            print(".",end="")
    print("Network config:", sta_if.ifconfig())

do_connect()