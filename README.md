
*i wrote this to clean up my morbidly unorganised Rekordbox hard drive that had been exported by different computers over the years*

* cleans up any duplicates checking the size, extension, and the first letter of the file name. if all these match, it deletes any extra copies (max copy ==1)
  * (you can uncheck the option to match the first letter at the start of the script)

* if file is mp3
  1. move the file to Desktop/--output folder--
* otherwise
  1. skips if the file isnt 'aiff', 'wav', or 'flac'
  2. converts to 320kbps mp3 and move to Desktop/<output>
 
* logs details at Desktop/--output folder-- upon completion
 
 directions:
 
 1. download the zipfile and extract inside the root of your library folder, cd into it (please back up as this hasnt been tested extensively)
 2. [create python3 virtual environment] (https://docs.python.org/3/library/venv.html)
 ```
 python3 -m venv venv
 ```

 3. [install pydub dependencies via homebrew] (https://github.com/jiaaro/pydub)
 ```
 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
 brew install ffmpeg
 ```
 4. activate the virtual environment
 ```
 source venv/bin/activate
 ```
 5. install python dependencies
 ```
 pip install -r requirements.txt
 ```

 
 6. run
 
 ```
 python audio.py
 ```
