import socketio

# standard Python
sio = socketio.Client()

sio.connect('http://localhost:8080')

sio.emit('ping', {'message': 'bar', 'room': 123})

flag = False

while not flag:
    message = input()
    sio.emit('ping', { 'data': message })
    if message == "exit":
        flag = True