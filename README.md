# DiscordLC
 
## Installation

### Mod

To install this mod, go to your DDLC `game` folder, and replace your current `scripts.rpa` file with the one provided. Be sure to add `logo.png` to the aforementioned folder, too.

Go to your `characters` folder and drag in `path.txt`.

In any location, create a new text file. This is your message file and is how Discord communicates with DDLC. Name it however you want, but write down the location of the file. (i.e. `C:\MyFolder\textfile.txt`.)

Edit `path.txt` in your `characters` folder and paste in the directory of your message file.

### Bot

**Make sure you have Python 3.6+ installed or else this won't work**

Go to https://discord.com/developers/applications

Create an application.

Click on the application name, and click "Bot"

Click "Add Bot"

From the bot tab of your application, click "Reveal Token."

Copy that token with Ctrl+C or the equivalent combination.

Open `bot/config.txt`

Replace "INSERT BOT TOKEN HERE" with your token.

Replace "INSERT PATH TO TEXT FILE HERE" with the path to your message file.

Run `bot.py`

* You might have to type `python3 ` (note the space) into a Terminal window and then drag `bot.py` into the window if you're on a Mac.

## Commands

`!d charname "quote"`: Makes a certain character say something, e.g. `!d sayori "Hello!"`

`!d charname pose "quote"`: Makes a certain character say something in a certain pose, e.g. `!d sayori 4p "Not again!"`

`!d hide charname`: Hides a character, e.g. `!d hide sayori` would hide Sayori.


**Note:** `charname` can be either `sayori`, `yuri`, `natsuki`, or `monika`.
