from umqtt.simple import MQTTClient


class MqttManager:
    """A simple MQTT manager for connecting to an MQTT broker and publishing messages.
    Usage:
        with MqttManager(client_id, mqtt_server, mqtt_user, mqtt_pass) as mqtt:
            mqtt.publish(topic, payload)
        # Automatically disconnects from MQTT broker when exiting the block"""
    def __init__(self, client_id, mqtt_server, mqtt_user, mqtt_pass, port=1883):
        self.mqtt_server = mqtt_server
        self.mqtt_user = mqtt_user
        self.mqtt_pass = mqtt_pass
        self.client_id = client_id
        self.client = MQTTClient(self.client_id, self.mqtt_server, user=self.mqtt_user, password=self.mqtt_pass, port=port)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()
    
    def publish(self, topic, payload):
        self.client.publish(topic, payload)
        print(f'Published to {topic}: {payload}')

    def connect(self):
        self.client.connect()
        print(f'Connected to {self.mqtt_server} MQTT broker, client ID: {self.client_id}')
    
    def disconnect(self):
        self.client.disconnect()
        print(f'Disconnected from {self.mqtt_server} MQTT broker, client ID: {self.client_id}')
