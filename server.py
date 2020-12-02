import socket
from over import *
from question import *
import time
from answer_check import *

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
game_on = True
winner =  0
score1 = score2 = score3 = 0


while game_on:#this while loop keeps the connection alive
    if winner!= 0:#Stop the connection when winner is decleared
        break
    conn1, addr1 = serv.accept()
    conn2, addr2 = serv.accept()
    conn3, addr3 = serv.accept()
    print "All connected"
    while game_on:
        winner = win(score1,score2,score3)
        print len(Asked), " - No.of.questions Asked"
        
        #Game Termination
        if winner != 0:#Stop the game when winner is decleared
           break
        if len(Asked) == 35:#If all the questions are asked stop game
           game_on = False
           break
           
        q = question()#Taking question
        print "Took Question",q
        
        buz = q + "\nTo Answer - Press 'a'\nTo Skip - Press 'b'\n"
        conn1.send(buz)
        conn2.send(buz)
        conn3.send(buz)
        
        #Time taken to press the Buzzer
        print ("I am at receiving data1")
        data1 = conn1.recv(40)
        print ("I am at receiving data2")
        data2 = conn2.recv(40)
        print ("I am at receiving data3")
        data3 = conn3.recv(40)
        
        print int(data1),"Time client1"
        print int(data2),"Time client2"
        print int(data3),"Time client3"
        
        
        #Taking answer from client which Pressed the buzzer first
        if(int(data1)<int(data2) and int(data1)<int(data3) and int(data1)<=10):
           conn1.send("Type in the answer")
           conn2.send("Please wait")
           conn3.send("Please wait")
           print Asked[questions-1],"q"
           answer = conn1.recv(40)
           print answer
           score1 = score1+Ans_check(answer,Asked[questions-1])
           print score1,"score1 ",score2,"score2 ",score3,"score3 "
        elif(int(data2)<int(data1) and int(data2)<int(data3) and int(data2)<=10):
           conn2.send("Type in the answer")
           conn1.send("Please wait")
           conn3.send("Please wait")
           answer = conn2.recv(40)
           print Asked[questions-1],"q"
           print answer
           score2 = score2+Ans_check(answer,Asked[questions-1])
           print score1,"score1 ",score2,"score2 ",score3,"socre3 "
        elif(int(data3)<int(data2) and int(data1)>int(data3) and int(data3)<=10):
           conn3.send("Type in the answer")
           conn2.send("Please wait")
           conn1.send("Please wait")
           answer = conn3.recv(40)
           print Asked[questions-1],"q"
           print answer
           score3 = score3+Ans_check(answer,Asked[questions-1])
           print score1,"score1 ",score2,"score2 ",score3,"socre3 "
        else:#skip the question if no one presses the buzzer
           msg = "Moving to next question"
           print(msg)
           conn3.send(msg)
           conn2.send(msg)
           conn1.send(msg)
        
        
           
        
        
 #Result Declearation
if winner == -1 or len(Asked) == 21:
   conn1.send("U lost")
   conn2.send("U lost")
   conn3.send("U lost")
elif winner == 1:
   conn1.send("U Won")
   conn2.send("U lost")
   conn3.send("U lost")
elif winner == 2:
   conn1.send("U lost")
   conn2.send("U Won")
   conn3.send("U lost")
elif winner == 3:
   conn1.send("U lost")
   conn2.send("U lost")
   conn3.send("U Won")
   
   


