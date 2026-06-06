from machine import Pin, I2C, unique_id
import ubinascii
from time import sleep

import BME280
from wifi_manager import WifiManager
from mqtt_manager import MqttManager


# Update interval for reading sensor data and printing payload
UPDATE_INTERVAL = 1 * 60  # seconds

# ESP32 - Pin assignment
# i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
# GPIO 5 is D1 (SCL), GPIO 4 is D2 (SDA)
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)
client_id = ubinascii.hexlify(unique_id())

mqtt_server = '192.168.18.72'
mqtt_user = 'home_server_broker_1'
mqtt_pass = '4367@sam'
topic_pub = f'home/weather/{client_id}'
WIFI_SSID = 'arnab_sudeshna'
WIFI_PASSWD = 'act12345'


def scan_i2c():
  """Scan for I2C devices and print their addresses."""
  print('Scanning I2C bus...')
  devices = i2c.scan()
  if devices:
    print(f'I2C devices found: {[hex(device) for device in devices]}')
  else:
    print('No I2C devices found.')


def read_bme280():
  """Read temperature, humidity, and pressure from the BME280 sensor."""
  bme = BME280.BME280(i2c=i2c)
  temp = bme.temperature
  hum = bme.humidity
  pres = bme.pressure
  return temp, hum, pres


def generate_weather_data_payload(temp, hum, pres):
  """Generate a payload dictionary containing the weather data."""
  return {
    "temperature": temp,
    "humidity": hum,
    "pressure": pres
  }


# Main loop to continuously read sensor data and print the payload
while True:
  scan_i2c()  # Scan for I2C devices before reading sensor data
  temp, hum, pres = read_bme280() # Read sensor data

  payload = generate_weather_data_payload(temp, hum, pres) # Generate payload from sensor data
  print(f'Generated payload: {payload}')
  
  with WifiManager(WIFI_SSID, WIFI_PASSWD) as wifi:
      with MqttManager(client_id, mqtt_server, mqtt_user, mqtt_pass) as mqtt:
          mqtt.publish(topic_pub, str(payload))  # Publish payload to MQTT topic
  sleep(UPDATE_INTERVAL)  # sleep for UPDATE_INTERVAL seconds
