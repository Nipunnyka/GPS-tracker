########################################################################################
# If we are hacker then this file will go to our server that has a static ip address

# importing socket so that we can connect two computer
import socket
# importing PySerial and time
# import serial
import time
# import motor_ibt2

###################ARDUINO SERIAL OBJECT#################################################
# serialPortMac = '/dev/tty.usbmodem14101'
# serialPortPi = '/dev/ttyACM0'
# arduinoSerial = serial.Serial(serialPortMac, 9600, timeout = 1)

mode = 0;
motorspeed1 = 0
motorspeed2 = 0
# forward_left_motor = motor_ibt2.motor1_ibt2(13, 19)
# forward_right_motor = motor_ibt2.motor1_ibt2(20, 21)


######################################################################################################################
########## Function to Create a Socket ( socket connect two computers)
######################################################################################################################
def create_socket():
    try:
        # Creating following 3 global variables
        global host
        global port
        global s  # This is socket variable which is named s

        # Assigning values to these 3 global variables
        host = ""
        port = 9999
        s = socket.socket()  # Creating a socket and assigning it to s

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


######################################################################################################################
########## # Binding the socket and listening for connections:
# Before accepting connection we listen for connections after binding host and port with the socket
######################################################################################################################
def bind_socket():
    try:
        # Declaring them again so that we can use the above global variable
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


######################################################################################################################
###########   Establish connection with a client (socket must be listening)
######################################################################################################################
def socket_accept():
    # s.accept retuens : conn: object of a conversation and address is a list of IP adress and a port
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    # read_commands(conn)  # A function defined below to send command to client
    conn.close()  # whenever the connection has been establised, at the end we want to close the connection


######################################################################################################################
###########  # Send commands to client
######################################################################################################################
def send_commands(conn, data):
    conn.send(str.encode(data))


######################################################################################################################
###########  # Send commands to client
######################################################################################################################

def strToInt(string):
    if (len(string) == 0):
        print('string length 0')
        return 0;
    x = 0
    flag = 0
    if (string[0] == '-'):
        flag = 1

    for i in range(0, len(string)):
        if string[i].isdigit():
            x += int(string[i]) * 10 ** int(len(string) - i - 1)
            print('In strToInt', i, x)
    if (flag == 1):
        return (-1) * x
    else:
        return x


def read_commands(conn):
    global mode, motorspeed1, motorspeed2, forward_left_motor, forward_right_motor
    while True:
        dataFromBase = str(conn.recv(1024), "utf-8")
        print("\n" + dataFromBase)
        print('lengthOfData', len(dataFromBase))
        if (len(dataFromBase) > 3):
            send_commands(conn, 'YES')
            index1 = dataFromBase.index(',')
            mode = dataFromBase[0:index1]

            print('At index1+1 of dataFromBase', dataFromBase[index1 + 1])

            index2 = dataFromBase.index(',', index1 + 1)
            print('At index2+1 of dataFromBase', dataFromBase[index2 + 1])

            motorspeed = dataFromBase[index1 + 1:index2]
            a = strToInt(motorspeed)
            motorspeed1 = a
            motorspeed2 = a
            # motorspeed.strip()
            print('motorspeed1', motorspeed1)
            #   motorspeed1=strToInt(motorspeed)

            # print(motorspeed)
            # index3 = dataFromBase.index(',',index2)
            motorspeed = dataFromBase[index2 + 1:]

            print(motorspeed)
            # motorspeed.strip()
            b = strToInt(motorspeed)

            motorspeed1 -= b
            motorspeed2 += b
            if (motorspeed1 > 100):
                motorspeed1 = 100
            elif (motorspeed1 < -100):
                motorspeed1 = -100

            if (motorspeed2 > 100):
                motorspeed2 = 100
            elif (motorspeed2 < -100):
                motorspeed2 = -100
            print('motorspeed1', motorspeed1)
            print('motorspeed2', motorspeed2)

            forward_left_motor.moveMotor(motorspeed1)
            forward_right_motor.moveMotor(motorspeed2)
        else:
            send_commands(conn, 'NO')


######################################################################################################################
###########  # Process Data from raspberrypi to Arduino
######################################################################################################################
# def processDataToArduino(data):
#   arduinoSerial.write(str(data).encode())

#####################################################################################################################
###########  # Remove b'' and\r\n from the string
######################################################################################################################
def makeDataWhatArduinoSent(data):
    return data[2:len(data) - 5]


######################################################################################################################
###########  # MAIN
######################################################################################################################
def main():
    create_socket()
    bind_socket()
    socket_accept()


############################################################
# Sending fake data
#    processDataToArduino('1,1001,1002,1003,1004,1005,1006');
#    time.sleep(2)
#    processDataToArduino('0,0,0,0,0,0,0');
############################################################

main()
