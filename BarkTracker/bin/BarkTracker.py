import numpy
import time
import pyaudio
import analyse
import smtplib # for emailing people
import datetime

gmailUser = 'barktracker@gmail.com'
gmailPassword = 'BarkBarkBark'
recipient = 'lle6138@rit.edu'
subject = 'Noisy dog'
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
    
while True:
    #read raw mic data
    rawsamps = stream.read(1024)
    #convert to NumPy array
    samps = numpy.fromstring(rawsamps, dtype = numpy.int16)
    
    if analyse.loudness(samps) >= -15:
        currentTime = datetime.datetime.utcnow  
        if(emailSentAt != None):
            timeDifference = currentTime - emailSentAt 
        else:
        	timeDifference = datetime.timedelta(minutes=100)
            
		if(timeDifference > datetime.timedelta(minutes=30)):
			print ("Sending email about dog!")
			emailSentAt = currentTime
			#Dog noisy at hour, minute, second, AM/PM
			text = "Your dog is being noisy at " + time.strftime("%I:%M%S%p")
			#prepare actual message
			message = """\
			From: %s
			To: %s
			Subject %s
	
			%s
			"""%(gmailUser, ", ".join([recipient]), subject, text)
			mailServer = smtplib.SMTP('smtp.gmail.com', 587)
			mailServer.ehlo()
			mailServer.starttls()
			mailServer.ehlo()
			mailServer.login(gmailUser, gmailPassword)
			mailServer.sendmail(gmailUser, recipient, message)
			mailServer.close()
		else:
			print ("Dog is noisy but email has already been sent")
    #elif analyse.loudness(samps) <  -15:
        #print ("Normal Ambient Sound")  
