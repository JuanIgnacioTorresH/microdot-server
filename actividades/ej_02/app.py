# Aplicacion del servidor
from microdot import Microdot
from microdot import send_file
from machine import Pin
import time

app = Microdot()
ledR = Pin(32, Pin.OUT)
ledY = Pin(33, Pin.OUT)
ledG = Pin(25, Pin.OUT)

toggleR = 0
toggleY = 0
toggleG = 0

@app.route('/')
async def index(request):
    return send_file("index.html")

@app.route('/<dir>/<file>')
async def static(request, dir, file):
    return send_file('/' + dir + '/' + file)

@app.route('/led/toggle/<int:number>')
def toggleLed(request, number):
    global toggleR, toggleY, toggleG
    if number == 1:
        toggleR = 1 - toggleR
        ledR.value(toggleR)
    elif number == 2:
        toggleY = 1 - toggleY
        ledY.value(toggleY)
    elif number == 3:
        toggleG = 1 - toggleG
        ledG.value(toggleG)

app.run(port=80)
