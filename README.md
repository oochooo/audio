# audio

* if file is mp3
  1. move the file to Desktop/--output folder--
* otherwise
  1. skips if the file isnt 'aiff', 'wav', or 'flac'
  2. converts to 320kbps mp3 and move to Desktop/<output>
 
* logs details at Desktop/--output folder-- upon completion
 
 directions:
 
 1. download the zipfile and extract inside the root of your library folder (please back up as this hasnt been tested extensively)
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
