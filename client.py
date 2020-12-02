import socket
from buz_first import *
from datetime import datetime
from ans_time import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))

while True:
    from_server = client.recv(4096)
    
    #Game termination when "U Lost" or "U Won" is received
    if(from_server[0]=="U"):
         break
         
    print from_server
    #To calculate the time taken by client to press the buzzer
    #Sending the time taken to server
    #Server receives time taken from three clients
    #and decides upon whom to chose for answering
    now = datetime.now()
    before_time = now.strftime("%S")
    if (type(from_server) == str):
       buzz = buzzer(0)
       ans_in = buz_first(before_time,buzz)
       client.send(str(ans_in))

    #Command to type/wait forothers to type in the answer
    from_server = client.recv(4096)
    print from_server
    
    #If the command is to "Type the answer"
    #Then sending the answer
    if (from_server[0]=='T'):
        answer = buzzer(1)
        client.send(answer)
   
client.close()
print from_server
