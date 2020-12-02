from datetime import datetime

#Finding the time taken to press buzzer
def buz_first(before_time,imp):
  #If buzzer is pressed
  if(imp == 'a'):
    now = datetime.now()
    after_time = now.strftime("%S")
    bt = int(before_time)
    at = int(after_time)
    ans = at-bt
    if(bt>50 and at<10):
        bt = 60-bt
        ans = bt+at
    if(ans<0):
      ans = -ans
    return ans
  #If buzzer id not pressed returning 30sec as default
  else:
    return 30
