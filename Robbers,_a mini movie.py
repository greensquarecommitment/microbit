# Add your Python code here. E.g.
from microbit import *
msg1= "break the door"
msg2= "break your head,Quiet!"
while running_time() < 10000:
    display.show(Image.ASLEEP)
    sleep(3000)
    display.scroll(msg1)
display.show(Image.SURPRISED)
sleep(2000)
display.scroll(msg2)
sleep(1000)
display.show(Image.SWORD)
sleep(3000)
display.show(Image.TARGET)
sleep(2000)
display.show(Image.SKULL)
