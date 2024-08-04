# AuthMicroservice

## Overview
This microservice recieves a username and password and checks a CSV file called users.csv that is located in the same directory. It will then send back True or False if the credentials match the CSV file. 

This microservice will communicate through socket 21219 using ZeroMQ.

This microservice is designed to be used by Christian Duvals ablum tracker to validate their users. 

## Communication Contract


### Requesting Data from the Microservice Example
```
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
```

### Recieving Data from the Microservice Example

```
response = 'True'  # if credentials are correct
response = 'False' # if credentials are not correct
```


## UML Sequence
![UML_Sequence](https://github.com/user-attachments/assets/5c607876-3fe2-4bc5-9dd1-c55543023e23)
