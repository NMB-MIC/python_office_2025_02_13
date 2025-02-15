from report_sale_amount import report_daily
from send_email import send_to_gmail
import time 
from dotenv import load_dotenv
import os 

if __name__ == "__main__": # if run file main then execute below program
    try:
        load_dotenv()
        username = os.getenv("user")
        password = os.getenv("password")
        print(username,password)
        print("start create report")
        file_name = report_daily() #create report
        print("create report is success")
        
        print("start send email")
        send_to_gmail(file_name,username,password) #send to gmail
        print("send email success")
        time.sleep(5) # delay time 5 sec
    except Exception as e:
        print(e)
        time.sleep(5) # delay time 5 sec