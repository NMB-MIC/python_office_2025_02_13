from report_sale_amount import report_daily
import time 

if __name__ == "__main__": # if run file main then execute below program
    try:
        print("start create report")
        report_daily() #create report
        print("create report is success")
        time.sleep(5) # delay time 5 sec
    except Exception as e:
        print(e)
        time.sleep(5) # delay time 5 sec