#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time

col = [2, 3, 4, 14, 15, 17, 18, 27]
row = [22, 23, 24, 10, 9, 25, 11, 8]
delta_time = 0.001
led_x = 8
led_y = 8

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for r in row:
        GPIO.setup(r, GPIO.OUT)      
    for c in col:
        GPIO.setup(c, GPIO.OUT)

def light_up_point(index_row, index_col):
    GPIO.output(row[index_row], GPIO.HIGH)
    GPIO.output(col[index_col], GPIO.LOW)

def clear():
    for r in row:
        GPIO.output(r, GPIO.LOW)      
    for c in col:
        GPIO.output(c, GPIO.HIGH)

def draw_pixel(y, x):
    clear()
    light_up_point(y, x)
    time.sleep(delta_time)
    
def draw_row(y, row_pattern):
    clear()
    GPIO.output(col[y], GPIO.HIGH)
    for i in range(led_x):
        if row_pattern[1] == "1":
            GPIO.output(row[1], GPIO.LOW)

def draw_matrix(pattern):
    for x in range(led_x):
        for y in range(led_y):
            if pattern[y][x] == "1":
                draw_pixel(y,x)
