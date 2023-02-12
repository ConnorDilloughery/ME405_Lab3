'''!
Connor Dilloughery
Lab 0x01: Reading CSV Files 
ME 405
'''
import matplotlib.pyplot as plt
import serial

def main():
    '''! The purpose of this code is to receive information regarding
         the time and position of the encoder. It spits out a list of
         the two values
         
    '''
    try:
        ## List to contain information about the time1
        time_list1 = []
        ## List to contain information about the time2
        time_list2 = []
        ## List to contain information about the position1
        count_list1 = []
        ## List to contain information about the position2
        count_list2 = []
        with serial.Serial ('/dev/tty.usbmodem142103', 115200) as s_port:
            s_port.write (b'd')      # Write bytes, not a string
            while True:
                ## reads the information on the serial port
                x = str(s_port.readline())
                print(x)
                ## adds information regarding count1
                if 'CountOne' in x:
                    count1 = int(''.join(c for c in x if c.isdigit() or c =='.' or c =='-'))
                    count_list1.append(count1)
                ## adds information regarding time1
                elif 'TimeOne' in x:
                    time1 = int(''.join(t for t in x if t.isdigit() or t =='.' or t =='-'))
                    time_list1.append(time1)
                ## adds information regarding count2
                elif 'CountTwo' in x:
                    count2 = int(''.join(c2 for c2 in x if c2.isdigit() or c2 =='.' or c2 =='-'))
                    count_list2.append(count2)
                ## adds information regarding time2
                elif 'TimeTwo' in x:
                    time2 = int(''.join(t2 for t2 in x if t2.isdigit() or t2 =='.' or t2 =='-'))
                    time_list2.append(time2)
                ## checks to see if the code is done
                else:
                    print('Break')
                    break
            print(time_list1)
            print(count_list1)
            print(time_list2)
            print(count_list2)
        ## prints the motor time versus encoder position using pyplot
        plt.plot(time_list1, count_list1)
        plt.ylabel('Position, Encoder')
        plt.xlabel('Times, ms')
        plt.show()
        plt.plot(time_list2, count_list2)
        plt.ylabel('Position, Encoder')
        plt.xlabel('Times, ms')
        plt.show()
        

    ## prevents code from crashing if serial is bugging
    except serial.SerialException:
        serial.Serial('/dev/tty.usbmodem142103', 115200).close()
        serial.Serial('/dev/tty.usbmodem142103', 115200)

         
if __name__ == '__main__':
    main()
