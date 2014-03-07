import numpy
import time
import pyaudio
import analyse
import smtplib # for emailing people
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from multiprocessing import Process

#The following variables should be customized by the user
gmailUser = "someGmailHere@gmail.com"   # sender e-mail
gmailPassword = "gmailPasswordHere"     # sender password
recipient = "recipientEmailHere"        # recipient e-mail
subject = "Noisy dog"                   # e-mail subject line
streamChunk = 1024                      # chunk used for the audio input stream
sampleRate = 48000                      # the sample rate of the user's mic
input_device_index = 2                  # device index for the user's mic
numChannels = 2                         # number of channels for the user's mic
audio_format = pyaudio.paInt16          # the audio format
ambient_db = -15                        # the ambience noise level in db
email_timer = 15                        # number of minutes between e-mails

emailSentAt = None
pyaud = pyaudio.PyAudio()

#open input stream 
stream = pyaud.open(
	format = audio_format,
	channels = numChannels, 
	rate = sampleRate, 
	input_device_index = input_device_index, #whichever USB port the microphone is plugged in to
	input = True)
	
def sendEmail():
	
	#Dog noisy at hour, minute, second, AM/PM
	text = "Your dog is being noisy at " + currentTime.strftime("%Y-%m-%d %H:%M:%S")        #This is what shows up in the content of the email
	message = MIMEMultipart()
	message['Subject'] = subject    # The subject of the email
	message['From'] = gmailUser     # Where its being sent from (chosen by user)
	message['To'] = recipient       # Who gets the e-mail
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
	rawsamps = stream.read(streamChunk)
	#convert to NumPy array
	samps = numpy.fromstring(rawsamps, dtype = numpy.int16)

	#send email if the loudness exceeds ambient noise
	if analyse.loudness(samps) >= ambient_db:
                #This is the time at which the sound was detected
		currentTime = datetime.datetime.now()   

                #Check to see when the last email was sent
		if(emailSentAt != None):
			timeDifference = currentTime - emailSentAt 
		else:
			timeDifference = datetime.timedelta(minutes=email_timer + 1)

		#Only send an email to the user if one hasn't been sent recently
		if(timeDifference > datetime.timedelta(minutes=email_timer)):
			print ("Sending email about dog!")      
			emailSentAt = currentTime
			p = Process(target=sendEmail)   #sending the email is in a process so that it won't...cause things to crash
			p.start()                       #actually start the process

		else:
			print ("Dog is noisy but email has already been sent")
	#elif analyse.loudness(samps) <	 ambient_db:
		#print ("Normal Ambient Sound")	 
	
