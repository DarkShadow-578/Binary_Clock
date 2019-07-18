#Importing the library`s for this project
import time
import datetime
from gpiozero import LED

#Function to change denery to binary
def DTB(num):
    binary = "{0:b}".format(num)
    return binary

#Gets the current time and converts it into binary and returns the values
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

#Lights up the LED`s that corrispond to the Correct time
def hours_1(binary,led_h1,led_h2):
    if binary[len(binary)-1] == "1":
        led_h2.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_h2.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_h1.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_h1.off()
            print("0")

    print("\n")

def hours_2(binary,led_h3,led_h4,led_h5,led_h6):
    if binary[len(binary)-1] == "1":
        led_h6.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_h6.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_h5.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_h5.off()
            print("0")
        if len(binary)>= 3:
            if binary[len(binary)-3] == "1":
                led_h4.on()
                print("1")
            if binary[len(binary)-3] == "0":
                led_h4.off()
                print("0")
            if len(binary)>= 4:
                if binary[len(binary)-4] == "1":
                    led_h3.on()
                    print("1")
                if binary[len(binary)-4] == "0":
                    led_h3.off()
                    print("0")
    print(":")
    
def mins_1(binary,led_m1,led_m2,led_m3):
    if binary[len(binary)-1] == "1":
        led_m3.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_m3.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_m2.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_m2.off()
            print("0")
        if len(binary)>= 3:
            if binary[len(binary)-3] == "1":
                led_m1.on()
                print("1")
            if binary[len(binary)-3] == "0":
                led_m1.off()
                print("0")

    print("\n")

def mins_2(binary,led_m4,led_m5,led_m6,led_m7):
    if binary[len(binary)-1] == "1":
        led_m7.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_m7.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_m6.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_m6.off()
            print("0")
        if len(binary)>= 3:
            if binary[len(binary)-3] == "1":
                led_m5.on()
                print("1")
            if binary[len(binary)-3] == "0":
                led_m5.off()
                print("0")
            if len(binary)>= 4:
                if binary[len(binary)-4] == "1":
                    led_m4.on()
                    print("1")
                if binary[len(binary)-4] == "0":
                    led_m4.off()
                    print("0")
    print(":")
    
def secs_1(binary,led_s1,led_s2,led_s3):
    if binary[len(binary)-1] == "1":
        led_s3.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_s3.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_s2.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_s2.off()
            print("0")
        if len(binary)>= 3:
            if binary[len(binary)-3] == "1":
                led_s1.on()
                print("1")
            if binary[len(binary)-3] == "0":
                led_s1.off()
                print("0")

    print("\n")

def secs_2(binary,led_s4,led_s5,led_s6,led_s7):
    if binary[len(binary)-1] == "1":
        led_s7.on()
        print("1")
    if binary[len(binary)-1] == "0":
        led_s7.off()
        print("0")
    if len(binary)>= 2:
        if binary[len(binary)-2] == "1":
            led_s6.on()
            print("1")
        if binary[len(binary)-2] == "0":
            led_s6.off()
            print("0")
        if len(binary)>= 3:
            if binary[len(binary)-3] == "1":
                led_s5.on()
                print("1")
            if binary[len(binary)-3] == "0":
                led_s5.off()
                print("0")
            if len(binary)>= 4:
                if binary[len(binary)-4] == "1":
                    led_s4.on()
                    print("1")
                if binary[len(binary)-4] == "0":
                    led_s4.off()
                    print("0")

#Main function to run the program
def main():
    
#Setting LED varibles

    led_h1 = LED(21)
    led_h2 = LED(20)
    led_h3 = LED(13)
    led_h4 = LED(19)
    led_h5 = LED(16)
    led_h6 = LED(26)
    led_m1 = LED(5)
    led_m2 = LED(6)
    led_m3 = LED(12)
    led_m4 = LED(8)
    led_m5 = LED(25)
    led_m6 = LED(24)
    led_m7 = LED(23)
    led_s1 = LED(18)
    led_s2 = LED(22)
    led_s3 = LED(27)
    led_s4 = LED(17)
    led_s5 = LED(4)
    led_s6 = LED(3)
    led_s7 = LED(2)
    
#while loop run T/F
    run = 1

#Turning all LED`s off
    led_h1.off()
    led_h2.off()
    led_h3.off()
    led_h4.off()
    led_h5.off()
    led_h6.off()
    led_m1.off()
    led_m2.off()
    led_m3.off()
    led_m4.off()
    led_m5.off()
    led_m6.off()
    led_m7.off()
    led_s1.off()
    led_s2.off()
    led_s3.off()
    led_s4.off()
    led_s5.off()
    led_s6.off()
    led_s7.off()
#While loop to continually run the program
    try:
        while run == 1:
            binary_H1,binary_H2,binary_M1,binary_M2,binary_S1,binary_S2=clock()
            old_H1=binary_H1
            old_H2=binary_H2
            old_H2=binary_M2
            old_H2=binary_M2
            old_H2=binary_S1
            hours_1(binary_H1,led_h1,led_h2)
            hours_2(binary_H2,led_h3,led_h4,led_h5,led_h6)
            mins_1(binary_M1,led_m1,led_m2,led_m3)
            mins_2(binary_M2,led_m4,led_m5,led_m6,led_m7)
            secs_1(binary_S1,led_s1,led_s2,led_s3)
            secs_2(binary_S2,led_s4,led_s5,led_s6,led_s7)
            time.sleep(1)
            if binary_H1 != old_H1 :
                    led_h1.off()
                    led_h2.off()
            if binary_H2 != old_H2 :
                    led_h3.off()
                    led_h4.off()
                    led_h5.off()
                    led_h6.off()
            if binary_M1 != old_M1 :
                    led_m1.off()
                    led_m2.off()
                    led_m3.off()
            if binary_M2 != old_M2 :
                    led_m4.off()
                    led_m5.off()
                    led_m6.off()
                    led_m7.off()
            if binary_S1 != old_S1 :
                    led_s1.off()
                    led_s2.off()
                    led_s3.off()
    except:
    #Turn all the LED`s On
        led_h1.on()
        led_h2.on()
        led_h3.on()
        led_h4.on()
        led_h5.on()
        led_h6.on()
        led_m1.on()
        led_m2.on()
        led_m3.on()
        led_m4.on()
        led_m5.on()
        led_m6.on()
        led_m7.on()
        led_s1.on()
        led_s2.on()
        led_s3.on()
        led_s4.on()
        led_s5.on()
        led_s6.on()
        led_s7.on()
        led_s4.on()
        led_s5.on()
        led_s6.on()
        led_s7.on()
        time.sleep(1)
    #Turn all LED`s Off
        led_h1.off()
        led_h2.off()
        led_h3.off()
        led_h4.off()
        led_h5.off()
        led_h6.off()
        led_m1.off()
        led_m2.off()
        led_m3.off()
        led_m4.off()
        led_m5.off()
        led_m6.off()
        led_m7.off()
        led_s1.off()
        led_s2.off()
        led_s3.off()
        led_s4.off()
        led_s5.off()
        led_s6.off()
        led_s7.off()
        
        







#Calling the main function
main()
