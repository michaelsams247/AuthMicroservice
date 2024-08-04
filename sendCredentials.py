import zmq

email = 'Email: Michaelsams24@gmail.com'
password = 'Password: Testing123'

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:21219")

socket.send_string(email)
socket.recv()
socket.send_string(password)


response = socket.recv().decode()
print(response)
if response != "Failed":
    pass