import time
import winsound
from winotify import Notification

def water_reminder():
    reminder_count = 0
    while True:  
        reminder_count += 1
        print(f"Reminder {reminder_count}: Time to drink water!") 
        
        
        toast = Notification(
            app_id='Water Reminder',
            title='Drink Water',
            msg='Time to drink water!',
            duration='short'
        )
        toast.show()
        

        winsound.Beep(1000, 1000)  

        time.sleep(3600) 


water_reminder()