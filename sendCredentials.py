import zmq

email = 'TEST_USER'
password = 'TEST_PASSWORD'
sendString = '/'.join([email, password])

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:21219")
socket.send_string(sendString)

response = socket.recv().decode()
print(response)
    