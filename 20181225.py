#用户：xiangjianqun   

#日期：2018-12-25   

#时间：14:03   

#文件名称：PyCharm
import socket
import time


def beimenchuixue_client():
    client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    client.connect(('127.0.0.1' , 8000))
    while True:
        data = input("北门吹雪:")
        if not data.strip():
            continue
        client.send(data.encode('utf-8'))
        response = client.recv(1024)
        print(response.decode('utf-8'))


if __name__ == '__main__':
    print("北门吹雪: http://www.cnblogs.com/2bjiujiu/")
    while True:
        # 一个小重启
        try:
            beimenchuixue_client()
        except ConnectionResetError as e:
            time.sleep(2)