import time
from threading import Thread
import socket

class IOTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)  # Set socket timeout to 5 seconds
        while self._running:
            try:
                data = sock.recv(8192)
                print(data)  # Print received data (you can process it as needed)
            except socket.timeout:
                continue  # Continue waiting if timeout occurs
            except Exception as e:
                print(f"Error occurred: {e}")
                break  # Break the loop on any other exception
        print("Task finished")

# Example usage
c = IOTask()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Example socket creation
try:
    sock.connect(('localhost', 8192))  # Example connection
except Exception as e:
    print(f"Error connecting to server: {e}")
    sock.close()  # Close the socket
    exit()

t = Thread(target=c.run, args=(sock,))
t.start()

# Optionally, you can terminate the task after some time
time.sleep(10)  # Wait for 10 seconds
c.terminate()  # Terminate the task
t.join()  # Wait for the thread to finish
sock.close()  # Close the socket
