<div align="center">
    <h1> HoloCure Fishing Bot</h1>
    <h3></h3>
</div>

# Summary

This is a bot written to play the fishing minigame that is featured in HoloCure.
I got the idea after seeing a [reddit post](https://www.reddit.com/r/holocure/comments/15vhz6l/so_i_wrote_a_bot_that_plays_the_fishing_minigame/) of a bot that does the same thing in action, but the code wasn't available (◞‸ ◟ ；), so I decided to try and do it as a way to learn Computer Vision and other topics.

# Instructions


I only tested this out on windows, but if the demand is high I'll look into making it compatible for linux or macos.

## Pre-requeriments:

- Python
- The game must be windowed
  
## Setup:

- Download the files either through the release or git clone
- If you downloaded it, extract into a folder
- Execute "pip install -r requirements.txt" with a terminal in the extracted folder
- Edit the "# settings" part of main.py with your keybindings (if you're not sure what to type, take a look [here](https://pyautogui.readthedocs.io/en/latest/keyboard.html) or google)
- Open the Game
- Go to Holohouse
- Go near lake
- run "python main.py"

The script will automatically move the window of the game to the top left corner of your screen (because that's the easiest way to make it slightly universal) and will start spamming your action key to start the fishing minigame, after that it should do the rest on its own untill you stop the script with ctrl + c in the terminal.

Be careful of doing anything that isnt stopping the script because ***IT WILL KEEP SENDING KEYSTROKES***

Any problems feel free to contact me, ill try to respond but I don't promise anything.

# Attribution
- Thank you to [Kay (@holocuredev)](https://twitter.com/holocuredev) and the team for making the game
- Thank you to [u/flightsin](https://www.reddit.com/r/holocure/comments/15vhz6l/so_i_wrote_a_bot_that_plays_the_fishing_minigame) for posting the original showcase
