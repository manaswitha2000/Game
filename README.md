# Game
In python
Open four terminal windows and connect the server with three clients to start the game.
Run the following commands in each window separately -python2 server.py, python2 client.py, python2 client2.py and python2 client3.py
Server sends a question to all the clients. 
To answer press “a” (Buzzer) within ten seconds.
To skip press “b”. If nothing is pressed within ten seconds “b” is taken as default.
Client who pressed buzzer first will be asked to answer within the next ten seconds.
Please wait for the message on the window - “Type in the answer”, enter answer only after receiving this message.
Answers are to be entered as numbers (ex- 1, 33)
If no one presses the buzzer, Server moves on to the next question.
While one client is answering others are asked to wait.
Correct answer increases total score by 1.
 Wrong answer or answering after time limit decreases total score by 0.5.
When one of the clients score 5 points, he is declared as the winner and game terminates.
Game continues till all the 35 questions are asked.
