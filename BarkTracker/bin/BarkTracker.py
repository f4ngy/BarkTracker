import numpy
import time
import pyaudio
import analyse
import smtplib # for emailing people
#SERVER = "localhost"


pyaud = pyaudio.PyAudio()

gmailUser = 'barktracker@gmail.com'
gmailPassword = 'BarkBarkBark'
recipient = 'lle6138@rit.edu'

#open input stream 
stream = pyaud.open(
	format = pyaudio.paInt16, #16 bit
	channels = 2, #1 = mono; 2 = stereo; I have no idea what 3+ are...
	rate = 44100, #at 44100 Hz
	input_device_index = 1, #whichever USB port the microphone is plugged in to
	input = True)
	
while True:
	#read raw mic data
	rawsamps = stream.read(1024)
	#convert to NumPy array
	samps = numpy.fromstring(rawsamps, dtype = numpy.int16)
	#output to user
	#print analyse.loudness(samps), analyse.musical_detect_pitch(samps)
	
	if analyse.loudness(samps) > -25:
		print ("Too Loud!")
		
		#Setup email stuff
		FROM = gmailUser

		TO = [recipient] #must be a list
		
		SUBJECT = "Noisy dog"
		
		#Dog noisy at hour, minute, second, AM/PM
		TEXT = "Your dog is being noisy at " + time.strftime("%I:%M%S%p")
		
		#prepare actual message
		message = """\
		From: %s
		To: %s
		Subject %s
		
		%s
		"""%(FROM, ", ".join(TO), SUBJECT, TEXT)
		
		#send mail
		#server = smtplib.SMTP('')
		#server.sendmail(FROM, TO, message)
		#server.quit()
		
		mailServer = smtplib.SMTP('smtp.gmail.com', 587)
  		mailServer.ehlo()
  		mailServer.starttls()
  		mailServer.ehlo()
  		mailServer.login(gmailUser, gmailPassword)
  		mailServer.sendmail(gmailUser, recipient, message)
  		mailServer.close()
	
	elif analyse.loudness(samps) > -30:
		print ("Normal Ambient Sound")	
