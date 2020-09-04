import time, threading
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP

port = input('Enter a Port:')

server_socket.bind(('0.0.0.0', int(port)))
server_socket.listen(128)
print('server listening on port {}...'.format(port))

while True:

    client_socket,client_addr = server_socket.accept()#

    data = client_socket.recv(1024).decode('utf8')
    print('————————————————————————————————————————————————————————————')
    print('current time is',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print('请求头data =', data) # 就是请求头信息相关
    print('type data =', type(data))
    niubi = ''
    try:
        bzp = data.splitlines()[0]
        print('bzp =', bzp)
        niubi = bzp.split(' ')[1]
    except Exception as e:
        print('e =', e)
        print("User IP:{}".format(client_addr))
    else:
        print('the path you requested:', niubi)
        print("User IP:{}".format(client_addr))
        print('————————————————————')
        client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
        client_socket.send('content-type:text/html\n'.encode('utf8'))

        client_socket.send('\n'.encode('utf8'))

        client_socket.send(r'<meta charset="UTF-8">'.encode('utf8'))
        client_socket.send('您请求的路径{}<br>'.format(niubi).encode('utf8'))
        client_socket.send('您的公网IP：{}\n'.format(client_addr).encode('utf8'))
