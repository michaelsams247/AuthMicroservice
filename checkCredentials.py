import zmq
import csv

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:21219")

email= None
password = None

while True:
    message = socket.recv().decode()

    if message[:5] == 'Email':
        email = message[7:]
    elif message[:8]:
        password = message[10:]

    if email is not None and password is not None:

        with open('credentials.csv', mode ='r') as file:
            data = csv.reader(file)
            for line in data:
                pass
            

            
        socket.send_string('True')
        email = None
        password = None
    else:
        socket.send_string('')


