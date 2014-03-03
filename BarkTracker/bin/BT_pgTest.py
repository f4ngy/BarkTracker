import numpy
import time
import pyaudio
import analyse
import smtplib # for emailing people
import datetime
import audiolab

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from multiprocessing import Process

gmailUser = "someGmailHere@gmail.com"
gmailPassword = "gmailPasswordHere"
recipient = "recipientEmailHere"
subject = "Noisy dog"
emailSentAt = None
pyaud = pyaudio.PyAudio()
#pygame.midi.init()

#open stream for pygame version
stream = pygame.midi.read()

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
	text = "Your dog is being noisy at " + currentTime.strftime("%Y-%m-%d %H:%M:%S")
	message = MIMEMultipart()
	message['Subject'] = subject
	message['From'] = gmailUser
	message['To'] = recipient

	mimeText = MIMEText(text, 'plain')
	message.attach(mimeText)

	mailServer = smtplib.SMTP('smtp.gmail.com', 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(gmailUser, gmailPassword)
	mailServer.sendmail(gmailUser, recipient, message.as_string())
	mailServer.close()

print("Starting BarkTracker")

while True:
	#read raw mic data
	rawsamps = stream.read(1024)
	#convert to NumPy array
	samps = numpy.fromstring(rawsamps, dtype = numpy.int16)
	
	if analyse.loudness(samps) >= -15:
		currentTime = datetime.datetime.now()	
		if(emailSentAt != None):
			timeDifference = currentTime - emailSentAt 
		else:
			timeDifference = datetime.timedelta(minutes=100)
			
		if(timeDifference > datetime.timedelta(minutes=30)):
			print ("Sending email about dog!")
			emailSentAt = currentTime
			p = Process(target=sendEmail)
			p.start()

		else:
			print ("Dog is noisy but email has already been sent")
	#elif analyse.loudness(samps) <	 -15:
		#print ("Normal Ambient Sound")	 
