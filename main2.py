import time
import stomp

class Listenner(stomp.ConnectionListener):
    def on_message(self, msg):
        print(f"Message: {msg.body}")

conn = stomp.Connection([("10.1.4.98", 61613)])
conn.connect('','', wait=True)

conn.set_listener('UPE-Listenner', Listenner())

conn.subscribe('UPE-JP', 1)

time.sleep(120)

conn.disconnect()