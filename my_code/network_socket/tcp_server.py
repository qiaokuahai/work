import socket
import threading


IP = "127.0.0.1"
PORT = 6999


global_socks = []


def send_data():
    while True:
        for s in global_socks:
            try:
                data = s.recv(1024)
            except:
                global_socks.remove(s)
                continue
            if not data:
                global_socks.remove(s)
                continue
            new_data = data.decode("utf-8")
            new_data += ", curr_socks_length is %s" % len(global_socks)
            print(new_data)
            s.send(new_data.encode("utf-8"))


def tcp_server():
    # 建立一个服务端
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))  # 绑定要监听的端口
    server.listen(5)  # 开始监听 表示可以使用五个链接排队
    print("server start success")
    while True:
        conn, addr = server.accept()
        global_socks.append(conn)
        t1 = threading.Thread(target=send_data)
        t1.start()


if __name__ == "__main__":
    tcp_server()
