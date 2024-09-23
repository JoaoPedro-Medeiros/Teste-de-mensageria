import stomp, signal
import time
from threading import Thread, Event

class Listenner(stomp.ConnectionListener):
    def on_message(self, msg):
        print(f"RECEIVED: {msg.body}\n--> ", end='')

def timeout(signum, frame):
    raise KeyboardInterrupt

def send_message(conn: Listenner, stop_event: Event):
    signal.signal(signal.SIGABRT, timeout)
    try:
        while not stop_event.is_set():
            input("--> ")
    except KeyboardInterrupt:
        pass

conn = stomp.Connection([('10.1.4.98', 61613)])
conn.connect('','',wait=True)
conn.set_listener('UPE-Listenner', Listenner())
conn.subscribe('UPE-JP', 1)

stop_event = Event()
thread = Thread(target=send_message, args=(conn, stop_event), daemon=True)
thread.start()

conn.start()

time.sleep(120)
stop_event.set()

conn.disconnect()