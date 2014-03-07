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
