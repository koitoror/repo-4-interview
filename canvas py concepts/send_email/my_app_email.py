# Python code to illustrate Sending mail  
# to multiple users  
# from your Gmail account  
import smtplib
  
# list of email_id to send the mail 
li = ["kamarster@gmail.com", "koitoror@gmail.com"] 
  
for i in range(len(li)): 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("atsilikam@gmail.com", "eldoret18") 
    message = "Email message straight from my python application"
    s.sendmail("atsilikam@gmail.com", li[i], message) 
    s.quit()