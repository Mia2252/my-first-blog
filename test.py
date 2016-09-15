waterfall = "hey! this is some code!        "
import time
while 1:
  time.sleep(0.1)
  waterfall=waterfall[1:]+waterfall[0]
  print(waterfall)
