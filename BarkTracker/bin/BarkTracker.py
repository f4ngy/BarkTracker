import numpy
import pyaudio
import analyse

pyaud = pyaudio.PyAudio()

#open input stream 
stream = pyaud.open(
	format = pyaudio.paInt16, #16 bit
	channels = 1, #mono
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
	
	if analyse.loudness(samps) > -10:
		print "Too Loud!"
	
	else if analyse.loudness(samps) > -30:
		print "Normal Ambient Sound"	
