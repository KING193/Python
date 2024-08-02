import smtplib

conn = smtplib.SMTP("smtp.gmail.com", 587)# servant gmail & Running out servant
conn.ehlo()# contact
conn.starttls()# Data encryption
conn.login("iS7ee7@gmail.com", "cqiiwrhvrrgzxrxl")# Login Mail, pass
conn.sendmail("iS7ee7@gmail.com", "iS7ee7@gmail.com","Subject: Lion \n\nHi,I am you from 2024\nHow are you?")# Send: form & to & message
conn.quit()# Finsh