import serial

# arduino_port = "/Device/USBSER000"
baud = 9600
fileName = "data.csv"
samples = 10
print_lables = False

# ser = serial.Serial(arduino_port, baud)
# print("Connected to Arduino port:"+ arduino_port)
file = open(fileName, "a")
print("created File")


line = 0

while line <= samples:
    if print_lables:
        if line == 0:
            print("Printing Column Headers")
        else:
            print("Line " +str(line ) +"...")
        # getData= str(ser.readline())
        # data = getData[0:][:-2]
        # print(data)

        # file = open(fileName, "w")
        # file.write(data +"\n")
        line = line +1


print("data Collection complete")

# port = serial.tools.list_ports.comports()
# serialInst = serial.Serial()

# portlist = []

# for onePort in port:
#  portlist.append(str(onePort))
# print(str(onePort))


