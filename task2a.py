#!/usr/bin/env python
import time
from flyt_python import api
import math

# Instance of Flyt drone navigation class
drone = api.navigation(timeout=120000)
time.sleep(3)
print('Taking off')
drone.take_off(10)


side_length = 10  # in meters

print('Going along the setpoints')
drone.position_set(0, side_length,0, relative=True)
drone.position_set(side_length * math.sqrt(3) / 2, -side_length / 2,0, relative=True)
drone.position_set(-side_length * math.sqrt(3) / 2, -side_length / 2,0, relative=True)

print('Landing')
drone.land(async=False)

# Shutdown the instance
drone.disconnect()
