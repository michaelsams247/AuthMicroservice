import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:21219")

userName= None
password = None

while True:
    message = socket.recv().decode()
    userName, password = message.split('/')
    valid = False
    with open('./users.csv', mode ='r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            lineData = line[:-1].split(',')
            if lineData[0] == userName and lineData[1] == password:
                valid = True
                break
    
    socket.send_string(str(valid))
    userName, password = None, None
    


