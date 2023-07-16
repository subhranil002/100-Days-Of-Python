import time
from plyer import notification

title = "Water reminder"
message = "Drink Water"
delay = int(input("Set the minutes of Delay to Drink Water : "))


while (True):
    time.sleep(60 * delay)
    notification.notify(title=title, message=message)
