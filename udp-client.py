import socket

# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)

prev_delay = 0.1
while True:
    message = b'This is the message. It will be repeated.'
    delay = prev_delay

    try:
        # send the message
        print('sending {!r}'.format(message))
        sent = sock.sendto(message, server_address)

        # receive the response
        print('waiting to receive')
        sock.settimeout(delay)
        data, server = sock.recvfrom(4096)
        print('received {!r}'.format(data))

    except socket.timeout:
        # wait longer for the next request
        delay *= 2
        if delay > 2.0:
            print('I think the server is down')
            break
    except Exception as e:
        # handle the exception here
        print("An error occurred:", e)
        # re-throw the exception
        raise
    else:
        # save the value of delay for the next iteration
        prev_delay = delay

print('closing socket')
sock.close()
