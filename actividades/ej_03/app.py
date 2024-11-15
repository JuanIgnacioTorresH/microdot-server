# Aplicacion del servidor
from microdot import Microdot
from microdot import send_file
from machine import Pin
import machine
import onewire, ds18x20
import time
import ujson

app = Microdot()
# the device is on GPIO12
dat = machine.Pin(19)
buzzer = machine.Pin(14, Pin.OUT)

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))

# scan for devices on the bus
roms = ds.scan()

setPoint = 15

@app.route('/')
async def index(request):
    return send_file("index.html")

@app.route('/<dir>/<file>')
async def static(request, dir, file):
    return send_file('/' + dir + '/' + file)

@app.route('/temp')
async def static(request):
    global setPoint
    ds.convert_temp()
    time.sleep_ms(750)
    print (roms)
    temp = ds.read_temp(roms[0])
    if temp >= setPoint:
        buzzer.value(1)
        return ujson.dumps({"temperature": temp, "buzzer":1})
    else:
        buzzer.value(0)
        return ujson.dumps({"temperature": temp, "buzzer":0})
        
@app.route('/update/ref/<int:ref>')
async def static(request, ref):
    print(ref)
    global setPoint
    setPoint = ref * 30 / 100
    return ujson.dumps({"status": 1})

app.run(port=80)