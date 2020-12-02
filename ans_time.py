import sys, select
#Chosing a default buzzer or answer if answer is not provided within 10 sec
def buzzer(inte):
     if(inte == 0):
         print "You have ten seconds to press!"

         i, o, e = select.select( [sys.stdin], [], [], 10 )

         if (i):
             return sys.stdin.readline().strip()
         else:
             return "b"
     else:
        print "You have ten seconds to answer!"

        i, o, e = select.select( [sys.stdin], [], [], 10 )

        if (i):
            return sys.stdin.readline().strip()
        else:
            return "5000"
