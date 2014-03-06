import numpy
import time
import pyaudio
import analyse
import smtplib # for emailing people
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from multiprocessing import Process

#The following four lines should probably be editable by the user
gmailUser = "someGmailHere@gmail.com"   #pick an email
gmailPassword = "gmailPasswordHere"     #enter password (shouldn't be a problem if you're using your own email address)
recipient = "recipientEmailHere"
subject = "Noisy dog"


emailSentAt = None
pyaud = pyaudio.PyAudio()

#open input stream 
stream = pyaud.open(
	format = pyaudio.paInt16, #16 bit
	channels = 2, #1 = mono; 2 = stereo; I have no idea what 3+ are...
	#rate = 44100, #at 44100 Hz
	rate = 48000, #at 48000 Hz
	input_device_index = 2, #whichever USB port the microphone is plugged in to
	input = True)
	
def sendEmail():
	
	#Dog noisy at hour, minute, second, AM/PM
	text = "Your dog is being noisy at " + currentTime.strftime("%Y-%m-%d %H:%M:%S")        #This is what shows up in the content of the email
	message = MIMEMultipart()
	message['Subject'] = subject    #This...should be self-explanatory: it's the subject of the email
	message['From'] = gmailUser     #Where its being sent from (chosen by user)
	message['To'] = recipient       #Who gets the email (or which of your multiple email addresses this is being sent to)
	mimeText = MIMEText(text, 'plain')
	message.attach(mimeText)
	
	mailServer = smtplib.SMTP('smtp.gmail.com', 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(gmailUser, gmailPassword)                              #logs into email address (entered above) using password (also entered above)
	mailServer.sendmail(gmailUser, recipient, message.as_string())          #send the email to the recipient
	mailServer.close()                                                      #Stop doing things with the mail server
	
print("Starting BarkTracker")
	
while True:
	#read raw mic data
	rawsamps = stream.read(1024)
	#convert to NumPy array
	samps = numpy.fromstring(rawsamps, dtype = numpy.int16)

	#send email if the loudness exceeds -15 db
	if analyse.loudness(samps) >= -15:
                #This is the time at which the sound was detected
		currentTime = datetime.datetime.now()   

                #Check to see when the last email was sent
		if(emailSentAt != None):
			timeDifference = currentTime - emailSentAt 
		else:
			timeDifference = datetime.timedelta(minutes=100)

		#Only send an email to the user if it has been less than 30 minutes since the last email
			#We may want to allow the user to change this to suit his/her needs
		if(timeDifference > datetime.timedelta(minutes=30)):
			print ("Sending email about dog!")      
			emailSentAt = currentTime
			p = Process(target=sendEmail)   #sending the email is in a process so that it won't...cause things to crash
			p.start()                       #actually start the process

		else:
			print ("Dog is noisy but email has already been sent")
	#elif analyse.loudness(samps) <	 -15:
		#print ("Normal Ambient Sound")	 
	
