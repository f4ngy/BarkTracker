"""setup file"""
#template taken from https://wiki.python.org/moin/Distutils/Tutorial

from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
#files = ["things/*"]

setup(
    name = "BarkTracker",
    version = "0.1.0",
    author = "Lindsey Ellis and Joseph Prezioso",
    author_email = "lle6138@gmail.com and joeprezioso@comcast.net",
    url = "https://github.com/lle6138/BarkTracker",
    license =  'GNU Affero GPL Version 3',
<<<<<<< HEAD
    description = "Bark Tracker monitors and notifies you if your dog is barking while you are away.",
    long_description ="""Bark Tracker is an application designed for home owners, pet-owners, and
=======
    #requirements.txt file should have version info for packaging purposes
    install_requires =
    [
        "numpy",        #numpy 1.9
        "pyaudio",      #PyAudio 0.2.7
        "SoundAnalyse"  #SoundAnalyse 0.1.1
    ],
      
    long_description = """Bark Tracker is an application designed for home owners, pet-owners, and
>>>>>>> 0aa551f53d420509f6f467a44c721d9ba6c8cfea
    others who want to monitor the noise level in their homes while they are away. Bark Tracker works by
    detecting noises above a certain threshold (determined by the user) through a microphone connected to
    the user's Raspberry Pi, Desktop, or Laptop. If your dog (or cat, bird, baby, rowdy brother-in-law, etc.)
    makes noise above a certain level of decibels, Bark Tracker sends you an email alerting you to that fact.

    To avoid spamming the user with countless emails over the course of a day, Bark Tracker waits 15 minutes
    (or some other amount of time, determined by the user) between emails to alert the user.
    """,
    #requirements.txt file should have version info for packaging purposes
    install_requires=
    [
        "numpy",        #numpy 1.9
        "pyaudio",      #PyAudio 0.2.7
        "SoundAnalyse"  #SoundAnalyse 0.1.1
    ],
      
    
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    #packages = ['package'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    #package_data = {'package' : files },
    #'runner' is in the root.
    #scripts = ["runner"],
    #long_description = """Really long text here.""" 
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
) 
