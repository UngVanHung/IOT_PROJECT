
import sys
import random
import time
from Adafruit_IO import MQTTClient

AIO_FEED_IDS = ["smart-farm-ttnt.temperature", "smart-farm-ttnt.humidity"]
AIO_USERNAME = "vanhung4320"
AIO_KEY = "aio_YnPk88fXuMRQTf5PKNaj9UNC4SN4"

def  connected(client):
    print("Ket noi thanh cong...")
    for feed in AIO_FEED_IDS:
        client.subscribe(feed)

def subscribe(client,userdata,mid,granted_qos) :
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)

def  message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)
    # if isMicrobitConnected:
        # ser.write((str(payload) + "#").encode())

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

# def getPort():
#     # ports = serial.tools.list_ports.comports()
#     # N = len(ports)
#     commPort = "None"
#     for i in range(0, N):
#         port = ports[i]
#         strPort = str(port)
#         if "USB Serial Device" in strPort:
#             splitPort = strPort.split(" ")
#             commPort = (splitPort[0])
#     return commPort

# isMicrobitConnected = False
# if getPort() != "None":
#     ser = serial.Serial( port=getPort(), baudrate=115200)
#     isMicrobitConnected = True

def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    try:
        if(splitData[0]=="1"):
            if splitData[1] == "TEMP":
                client.publish("bbc-temp", splitData[2])
            elif splitData[1] == "HUMI":
                client.publish("bbc-humi", splitData[2])
        if (splitData[0] == "2"):
            if splitData[1] == "TEMP":
                client.publish("bbc-temp2", splitData[2])
            elif splitData[1] == "HUMI":
                client.publish("bbc-humi2", splitData[2])
    except:
        pass

mess = ""
# def readSerial():
#     bytesToRead = ser.inWaiting()
#     if (bytesToRead > 0):
#         global mess
#         mess = mess + ser.read(bytesToRead).decode("UTF-8")
#         while ("#" in mess) and ("!" in mess):
#             start = mess.find("!")
#             end = mess.find("#")
#             processData(mess[start:end + 1])
#             if (end == len(mess)):
#                 mess =""
#             else:
#                 mess = mess[end+1:]
while True:
    value = random.randint(0, 40)
    value1 = random.randint(20, 100)
    value2 = random.randint(0, 40)
    value3 = random.randint(20, 100)
    print("Cap nhat nhiet do 1:", value)
    client.publish("bbc-temp", value)
    print("Cap nhat do am 1:", value1)
    client.publish("bbc-humi", value1)
    print("Cap nhat nhiet do 2:", value2)
    client.publish("bbc-temp2", value2)
    print("Cap nhat do am 2:", value3)
    client.publish("bbc-humi2", value3)
    time.sleep(10)
# while True:
#         if isMicrobitConnected:
#             readSerial()
#
#         time.sleep(1)