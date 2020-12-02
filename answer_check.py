#checking if the entered answer is correct 
def Ans_check(string,num):
    file = open("answers.txt",'r',0)
    answer = str(num)+"."+string+"\n"
    for s in file:
        if num<10:
            if(s[0] == str(num)):
                if(answer == str(s)):
                    return 1
                else:
                    return -0.5

        else:
            if(s[0] == str((num/10)) and s[1] == str((num%10))):
                if(answer == str(s)):
                    return 1
                else:
                    return -0.5
