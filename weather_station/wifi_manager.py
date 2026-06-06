import network
from time import sleep, time

class WifiManager:
    """A simple WiFi manager for connecting and disconnecting from a WiFi network.
    Usage:
        with WifiManager(ssid, password) as wifi:
            # Connected to WiFi, do something
            pass
        # Automatically disconnected from WiFi when exiting the block
    """
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)
        self.default_timeout = 10  # seconds

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

    def _connection_message(self):
        print(f"Connected to WiFi: {self.ssid}")
        print("IP:", self.wlan.ifconfig()[0])

    def connect(self, timeout=None):
        """Connect to the WiFi network."""
        if timeout is None:
            timeout = self.default_timeout

        print(f"Connecting to WiFi: {self.ssid}")
        if not self.wlan.active():
            self.wlan.active(True)

        if self.wlan.isconnected():
            self._connection_message()
            return
        
        self.wlan.connect(self.ssid, self.password)

        # retry until connected or timeout
        start_time = time()
        while not self.wlan.isconnected():
            if time() - start_time > timeout:
                raise Exception("WiFi connection timed out")
            sleep(1)
    
        self._connection_message()

    def disconnect(self):
        """Disconnect from the WiFi network."""
        if self.wlan.isconnected():
            self.wlan.disconnect()
            print("WiFi disconnected")