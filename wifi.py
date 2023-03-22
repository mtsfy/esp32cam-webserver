import network
import config
class Wifi:
    def connect():
        sta = network.WLAN(network.AP_IF)
        sta.active(True)
        sta.config(essid='ESP-CAM',authmode=network.AUTH_WPA_WPA2_PSK, password='esp1234Cam')
        print("Config:", sta.ifconfig())