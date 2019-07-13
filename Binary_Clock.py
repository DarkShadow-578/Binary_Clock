import time
import datetime
from gpiozero import LED

def DTB(num):
    binary = "{0:b}".format(num)
    return binary

def clock():
    date_time = str(datetime.datetime.now())
    hours=int(date_time[11]),int(date_time[12])
    mins=int(date_time[14]),int(date_time[15])
    secs=int(date_time[17]),int(date_time[18])
    print(hours[0],hours[1],":",mins[0],mins[1],":",secs[0],secs[1])
    binary_H1 = DTB(hours[0])
    binary_H2 = DTB(hours[1])
    binary_M1 = DTB(mins[0])
    binary_M2 = DTB(mins[1])
    binary_S1 = DTB(secs[0])
    binary_S2 = DTB(secs[1])
    return binary_H1,binary_H2,binary_M1,binary_M2,binary_S1,binary_S2

def hours_1(binary,led_1,led_2):
    if binary[len(binary)-1] == "1":
        led_1.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_1.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_2.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_2.off()
            print("0")

    print("\n")

def hours_2(binary,led_1,led_2,led_4,led_8):
    if binary[len(binary)-1] == "1":
        led_1.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_1.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_2.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_2.off()
            print("0")
        if len(binary)>= 3:
            if binary[len(binary)-3] == "1":
                led_4.on()
                print("1")
            if binary[len(binary)-3] == "0":
                led_4.off()
                print("0")
            if len(binary)>= 4:
                if binary[len(binary)-4] == "1":
                    led_8.on()
                    print("1")
                if binary[len(binary)-4] == "0":
                    led_8.off()
                    print("0")
    print(":")
    
def mins_1(binary,led_1,led_2,led_4):
    if binary[len(binary)-1] == "1":
        led_1.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_1.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_2.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_2.off()
            print("0")
        if len(binary)>= 3:
            if binary[len(binary)-3] == "1":
                led_4.on()
                print("1")
            if binary[len(binary)-3] == "0":
                led_4.off()
                print("0")

    print("\n")

def mins_2(binary,led_1,led_2,led_4,led_8):
    if binary[len(binary)-1] == "1":
        led_1.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_1.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_2.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_2.off()
            print("0")
        if len(binary)>= 3:
            if binary[len(binary)-3] == "1":
                led_4.on()
                print("1")
            if binary[len(binary)-3] == "0":
                led_4.off()
                print("0")
            if len(binary)>= 4:
                if binary[len(binary)-4] == "1":
                    led_8.on()
                    print("1")
                if binary[len(binary)-4] == "0":
                    led_8.off()
                    print("0")
    print(":")
    
def secs_1(binary,led_1,led_2,led_4):
    if binary[len(binary)-1] == "1":
        led_1.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_1.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_2.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_2.off()
            print("0")
        if len(binary)>= 3:
            if binary[len(binary)-3] == "1":
                led_4.on()
                print("1")
            if binary[len(binary)-3] == "0":
                led_4.off()
                print("0")

    print("\n")

def secs_2(binary,led_1,led_2,led_4,led_8):
    if binary[len(binary)-1] == "1":
        led_1.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_1.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_2.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_2.off()
            print("0")
        if len(binary)>= 3:
            if binary[len(binary)-3] == "1":
                led_4.on()
                print("1")
            if binary[len(binary)-3] == "0":
                led_4.off()
                print("0")
            if len(binary)>= 4:
                if binary[len(binary)-4] == "1":
                    led_8.on()
                    print("1")
                if binary[len(binary)-4] == "0":
                    led_8.off()
                    print("0")
    
def main():
    led_h1_2 =LED()
    led_h1_1 =LED()
    led_h2_8 =LED()
    led_h2_4 =LED()
    led_h2_2 =LED()
    led_h2_1 =LED()
    led_m1_4 =LED()
    led_m1_2 =LED()
    led_m1_1 =LED()
    led_m2_8 =LED()
    led_m2_4 =LED()
    led_m2_2 =LED()
    led_m2_1 =LED()
    led_s1_4 =LED()
    led_s1_2 =LED()
    led_s1_1 =LED()
    led_s2_8 =LED()
    led_s2_4 =LED()
    led_s2_2 =LED()
    led_s2_1 =LED()
    run = 1
    while run == 1:
        binary_H1,binary_H2,binary_M1,binary_M2,binary_S1,binary_S2=clock()
        hours_1(binary_H1,led_h1_1,led_h1_2)
        hours_2(binary_H2,led_h2_1,led_h2_2,led_h2_4,led_h2_8)
        mins_1(binary_M1,led_m1_1,led_m1_2,led_m1_4)
        mins_2(binary_M2,led_m2_1,led_m2_2,led_m2_4,led_m2_8)
        secs_1(binary_S1,led_s1_1,led_s1_2,led_s1_4)
        secs_2(binary_S2,led_s2_1,led_s2_2,led_s2_4,led_s2_8)
        time.sleep(1)
        led_h1_2.off()
        led_h1_1.off()
        led_h2_8.off()
        led_h2_4.off()
        led_h2_2.off()
        led_h2_1.off()
        led_m1_4.off()
        led_m1_2.off()
        led_m1_1.off()
        led_m2_8.off()
        led_m2_4.off()
        led_m2_2.off()
        led_m2_1.off()
        led_s1_4.off()
        led_s1_2.off()
        led_s1_1.off()
        led_s2_8.off()
        led_s2_4.off()
        led_s2_2.off()
        led_s2_1.off()
        
        








main()
