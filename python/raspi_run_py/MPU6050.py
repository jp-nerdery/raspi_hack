# -*- coding: utf-8 -*-
#!/usr/bin/python

#REFERENCE 
#https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pd 
#https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf

import smbus
import math
from time import sleep
import data_function.data_control
#DEVICE Address
DEV_ADDR = 0x68
ACCEL_XOUT = 0x3b
ACCEL_YOUT = 0x3d
ACCEL_ZOUT = 0x3f
TEMP_OUT = 0x41
GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47
PWR_MGMT_1 = 0x6b
PWR_MGMT_2 = 0x6c

INTERVAL_TIME = 0.5 # IF YOU WANT FPS 30.SET 1/30 

bus = smbus.SMBus(1)
bus.write_byte_data(DEV_ADDR, PWR_MGMT_1, 0)

def read_byte(adr):
    return bus.read_byte_data(DEV_ADDR, adr) 
def read_word(adr):
    high = bus.read_byte_data(DEV_ADDR, adr)
    low = bus.read_byte_data(DEV_ADDR, adr+1)
    val = (high << 8) + low
    return val 
def read_word_sensor(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val 
def get_temp():
    temp = read_word_sensor(TEMP_OUT)
    x = temp / 340 + 36.53
    return x 
def get_gyro_data_lsb():
    x = read_word_sensor(GYRO_XOUT)
    y = read_word_sensor(GYRO_YOUT)
    z = read_word_sensor(GYRO_ZOUT)
    return [x, y, z]
def get_gyro_data_deg():
    x,y,z = get_gyro_data_lsb()
    x = x / 131.0
    y = y / 131.0
    z = z / 131.0
    return [x, y, z]
 
def get_accel_data_lsb():
    x = read_word_sensor(ACCEL_XOUT)
    y = read_word_sensor(ACCEL_YOUT)
    z = read_word_sensor(ACCEL_ZOUT)
    return [x, y, z] 
def get_accel_data_g():
    x,y,z = get_accel_data_lsb()
    x = x / 16384.0
    y = y / 16384.0
    z = z / 16384.0
    return [x, y, z]
 
while True:
    data_param = {} 
    temp = get_temp()
    gyro_x,gyro_y,gyro_z = get_gyro_data_deg()
    accel_x,accel_y,accel_z = get_accel_data_g()
    data_param['temp'] =temp
    data_param['gyro_x'] = gyro_x
    data_param['gyro_y'] = accel_y
    data_param['gyro_z'] = gyro_z
    data_param['accel_x'] = accel_x
    data_param['accel_y'] = accel_y
    data_param['accel_z'] = accel_z 
    data_function.data_control.My_pg_Access.insert_data(table_name = "insert_table_name",dataparam= data_param)
     
    sleep(INTERVAL_TIME)