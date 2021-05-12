# This application is  Developed to help needy people to book the vaccine. Not for commercial purpose.
# Share it to others or make a better version which can reach public , so that everyone can benefitted. 





import json,ast
import time
import requests

# mention 18 , If the preferred age category is less than 45 (or) mention 45 , If the preferre age is greated than 45
agefromGUI=45

#Replace with your hospital location pincode in India
pincodeFromGUI='6xxxxx'

#preferable date for booking
datefromGUI='12-05-2021'

#mention today date
TodayDate='12-05-2021'

#Format 'DD-MM-YYYY'


#Mail Content

# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
msg['Subject'] = "message "

message = "Vaccine Slot Opened  https://selfregistration.cowin.gov.in/ " 
 
 
# setup the parameters of the message
#mention you new gmal account password inside the brakets
password = "your new Gmail account password"

#mention you new gmal account  inside the brackets
msg['From'] = "Mentionyournewgmailaccount@gmail.com"
msg['To'] = "Mention receiver Mail Account"


# Mail function #

def sendMail_function():
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
 
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
 
    server.starttls()
 
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
 
 
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
 
    server.quit()
 
    print ('successfully sent email to %s:' % (msg['To']))






url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='
url=url+pincodeFromGUI +'&date='+ TodayDate
print(url)

headers = {
    'User-Agent': 'My User Agent 1.0',
    
}

while(1):
    
    response=requests.get(url,headers=headers)
    parsedJSONformat=response.json()
    print('parsedJSONformat')
    print(parsedJSONformat)
    print('parsing..........................')
    print(len(parsedJSONformat['centers']))
    for i in range(len(parsedJSONformat['centers'])):
        print(parsedJSONformat['centers'][i]['center_id'])
        for j in range(len(parsedJSONformat['centers'][i]['sessions'])):
            if( parsedJSONformat['centers'][i]['sessions'][j]['min_age_limit'] == agefromGUI and parsedJSONformat['centers'][i]['sessions'][j]['date'] == datefromGUI):
                if(parsedJSONformat['centers'][i]['sessions'][j]['available_capacity'] > 0):
                    print('vaccine available')
                    print(parsedJSONformat['centers'][i]['sessions'][j]['vaccine'])
                    msg['Subject'] = "message " + parsedJSONformat['centers'][i]['sessions'][j]['vaccine']
                    sendMail_function()
                else:
                    print('Vaccine Not Available')
                    print(parsedJSONformat['centers'][i]['sessions'][j]['vaccine'])
        
            
    time.sleep(4)
    #Dont change the time sleep=4 to lesser value. As per Govt OpenAPI rule , I have given a shortes delay for quick notification , lesser than this will violate the rule and your ip will be blocked for further notification
                
                
                
                
            
     
        
     


