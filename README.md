# discord-buttsbot

Simple Discord bot that will randomly replace up to 5 words in amessage with the word "butt"

## Requirements
* Python 3.4 or higher
* pip
* discord.py
* A valid Discord account with an App registered (and Bot account created for said app)

## Install
1. Clone or download this repo to an easy to remember spot on your server.
2. Copy `example_config.cfg` to `config.cfg` and fill it out in a text editor.
3. Turn on Dev Mode in Discord to get the proper ID's (User Settings -> Appearance -> Developer Mode, then right click items to get their ID).
3. `bot_channel_id` should be set to a channel in your server that it can spam in occasionally (currently just posts when it starts up).
4. `owner_id` should be your discord user ID and `admin_id` should the the ID of one other user (for now) that you trust to admin the bot (neither are used in this bot currently, I just included them from another bot I wrote).
5. If you havent already, invite your bot to your server by going to `https://discordapp.com/oauth2/authorize?client_id=REPLACE_WITH_CLIENT_ID&scope=bot&permissions=0` (replacing REPLACE_WITH_CLIENT_ID with your bots client ID)
6. Run the bot by navigating to the folder you put the files in using the command line of your server/computer and run `python3.4 buttsbot.py`, replacing `python3.4` with the name of your python >= 3.4 binary
7. The bot should have posted "This isn't a butt..." in your bot channel if it worked

## Optional supervisord setup
1. If you want the bot to be able to autostart with the server and after any disconnects/crashes, install supervisord
2. Copy `extras/supervisord_discord-buttsbot.conf` to `/etc/supervisor/conf.d/discord-buttsbot.conf`
3. Edit directory, home, user, and command to suit where you placed the files and the user you want it to run as
4. Create the folder for specified for the logs (default location requires root/sudo)
4. Restart or reload supervisord

## Usage
Buttsbot will randomly replace up to 5 words (decided randomly for chosen messages) in a message to the word "butt", or up to 5 words in any message that mentioned the bot


## Invite link:
If you want to invite my particular copy of the bot to your server, use the link below. Note that I accept no responsibility for it's actions, stability, or availability.
https://discordapp.com/oauth2/authorize?client_id=302981775083438091&scope=bot&permissions=0