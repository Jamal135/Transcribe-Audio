# Python Transcribe Audio Files

***
# About:
---
So long story that I can't be bothered to type, this is a repository that transcribes audio files into text. It is that simple. It uses Google services to do this, it currently breaks with large files. Splitting up audio files is more complicated. 


Creation Date: 02/10/2022

***
# Setup:
---
So if you are using VSCode as an IDE and nothing has broken, then you can just run the setup.py file to automatically create a virtualenv and install all packages. There is a good chance this setup.py file won't work for you, if that is the case just install the requirements.txt like a normal person and hope Python won't do any of the annoying things it usually does when trying to install dependencies...

As far as usage, just run the transcribe.py file and enter a valid filename (such as 'audio.mp3') and ensure that this file is present within the Files folder. If the extension is bad or the file is not in that folder, you will have a fun time with this code not working.

***
# Future:
---
Look this isn't the best code ever... but it worked. In the future I will probably add the ability to split up and thus process larger audio files. Additionally, I will at some point make text be saved to a text file rather than just being printed.

***
# License:
---
MIT License.