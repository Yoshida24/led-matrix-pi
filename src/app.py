#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time
import led_matrix
import patterns

def clockward(number, pitch):
    return (number + 1) % pitch

def draw_smily():
    frame_num = 60
    led_matrix.init()
    pictures = [
        patterns.smily,
        patterns.not_smily
    ]
    frame = 0
    flip = 0
    while True:
        led_matrix.draw_matrix(pictures[flip])
        frame += 1
        if frame > frame_num:
            frame = 0
            flip = clockward(flip, len(pictures));

def nagashi():
    frame_num = 5
    led_matrix.init()
    frame = 0
    flip = 0
    start = 0
    end = 8
    while True:
        led_matrix.draw_matrix(patterns.get_eight_col(patterns.akiba, start, end))
        frame += 1
        if frame > frame_num:
            frame = 0
            start +=1
            end += 1
    
draw_smily()
# nagashi()
