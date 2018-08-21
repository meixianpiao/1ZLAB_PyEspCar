

from machine import Pin
import time


import encoder

pin_x = Pin('X1',Pin.IN)
pin_y = Pin('X2',Pin.IN)

enc = encoder.Encoder(pin_x,pin_y,1,1)


print('test start')
data = 0
while 1:  
  if data != enc.position:
    print(enc.position)
    data = enc.position
  