import serial
import logging
import binascii
from time import sleep
import post_robot

org_dic = {
    "temp": 0,
    "p_x": 0,
    "p_y": 0,
    "p_z": 0,
    "v_x": 0,
    "v_y": 0,
    "v_z": 0,
    "pitch": 0,
    "roll": 0,
    "yaw": 0
}
com = None
try:
    com = serial.Serial("COM12", 256000)
    data_str = ""
    while True:
        com.reset_input_buffer()
        data_str = binascii.b2a_hex(com.readline())
        print(str(data_str), end="")
        data_str = data_str.split()

        if len(data_str) == 10:
            org_dic["temp"] = data_str[0]
            org_dic["p_x"] = data_str[1]
            org_dic["p_y"] = data_str[2]
            org_dic["p_z"] = data_str[3]
            org_dic["v_x"] = data_str[4]
            org_dic["v_y"] = data_str[5]
            org_dic["v_z"] = data_str[6]
            org_dic["pitch"] = data_str[7]
            org_dic["roll"] = data_str[8]
            org_dic["yaw"] = data_str[9]
            print(org_dic)
            post_robot.upload_pkg()

        # com.write(key.encode('gbk'))
        sleep(0.2)

except ValueError:
    print("Port config error")
except serial.serialutil.SerialException:
    print("No such device found or accessible")
except Exception as e:
    print("Unknown Error")
    logging.error("Unknown Error: %s", e)

finally:
    com.close()
    print("Hello World")
