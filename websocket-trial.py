import asyncio
import websockets
import serial
import syslog
import time

port = '/dev/ttyUSB1'
ard = serial.Serial(port,9600,timeout=5)

import asyncio
import websockets

async def echo(websocket, path):
    while True:
        try:
            # print("here")
            b = ard.readline()  # read a byte string
            string_n = b.decode()  # decode byte string into Unicode
            string = string_n.rstrip()  # remove \n and \r
            readings = string.split(",")
            if len(readings[0]) != 19:
                continue
            # print(readings)
            await websocket.send(readings[0])
        except websockets.ConnectionClosed:
            print("connection broken")
            break

asyncio.get_event_loop().run_until_complete(
websockets.serve(echo, '0.0.0.0', 8765))
asyncio.get_event_loop().run_forever()
