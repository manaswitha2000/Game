import socket
import random

#Chosing a random question from "questions.txt" and sending it to clients
questions = 0
max = 35
l = []
Asked = []
for i in range (max):
       l.append(i+1)

def question():
    file = open("questions.txt",'r',0)
    global questions
    global l
    global Asked
    k = random.choice(l)
    Asked.append(k)
    l.remove(k)#to avoid repetition for questions
    for s in file:
              if k<10:
                  if(s[0] == str(k)):
                      questions += 1
                      return str(s)

              else:
                  if(s[0] == str((k/10)) and s[1] == str((k%10))):
                      questions += 1
                      return str(s)
  
