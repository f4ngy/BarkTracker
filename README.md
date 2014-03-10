BarkTracker
===========

An application written in Python, this will alert pet owners if their dogs are being noisy while they're at work.

This script needs to be customized to work with your personal microphone and machine. All of the customizable data is stored in variables at the top of the file.  The lines that should be altered are noted in the code but we will also list them here.

- Gmail address to send from
- Gmail password for the above
- E-mail for receiving notifications
- Microphone settings
- Timer to prevent e-mails from being sent too often
- Ambient noise level

We would also like to note that right now the code uses gmail's smtp server for sending e-mails, but it should be possible to use your own if you have one hosted.  This would require modifying the code a little bit though.

This project was developed as part of the Advanced FOSS course taught at RIT during Spring 2014.

Installation
===========
- Install Python 2.7.5 (unless you are using a Raspberry Pi in which case move to the next section)
- Install python-devel
- Pip install numpy
- Pip install pyaudio, you might need to install portaudio-devel first
- Pip install SoundAnalyse
- Modify BarkTracker.py with your microphone, ambient noise level, and time between notiications settings
- Run BarkTracker.py, you should start receiving e-mails

Raspberry Pi?
===========

This application *can* be run on a Raspberry Pi but there are several requirements as of 3/10/14.

- The Pi must be connected to the internet
- You must be running Python 3 due to an issue with Linux distributions, NumPy, and Python 2.7.5
- You must follow the steps linked below to get SoundAnalyse working with Python 3 http://blenderartists.org/forum/showthread.php?151392-Using-Microphone-Input-with-the-BGE&p=2562000&viewfull=1#post2562000
- The Raspberry Pi might have issues installing numpy due to RAM, in which case you should switch to CLI and install from there.
