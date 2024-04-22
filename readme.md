## Simple timer that resets on a keybooard press
* I built this to add a timer for family games.
* Running the script will ask you to set a timer of up to 20 seconds.
    * It will then give you 10 seconds to get ready, before starting the timer.
* Players can reset the timer by tapping any button on the keyboard, with the exception of the Tab key, which will stop the script.
* The script will also end (whilst playing a 'game over' sound) when the countdown reaches 0.

## Extending the timer beyond 20 seconds
You can download wav files for up to 100 seconds from [here](https://evolution.voxeo.com/library/audio/prompts/numbers/index.jsp). Just move the files into the /sounds/ folder and the script will ensure you have added consecutive numbers and let you set the timer you want, up to the value of 'seconds' wav files you have added. (Feel free to submit a PR to add more .wav files.)

## Getting up and running
* To clone this repository, run `git clone https://github.com/learkonas/countdown-timer`
* Run `pip install -r requirements.txt` to install dependencies.
* Run `python timer.py`