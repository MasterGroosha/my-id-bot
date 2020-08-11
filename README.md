# Bot to get users/chats IDs in Telegram

<a href="https://hub.docker.com/r/groosha/my-id-bot"><img src="https://img.shields.io/badge/my--id--bot-docker%20hub-blue"></a>  
Demo: [@my_id_bot in Telegram](https://t.me/my_id_bot).  

This is a simple bot written with [aiogram](https://github.com/aiogram/aiogram) framework to show some IDs, like:

* Your user ID (when asked in inline mode or in private chat with any message);  
* Group/supergroup ID (when added to that group or with /id command);  
* Channel ID (when message forwarded from channel to one-to-one chat with bot);  
* Sticker ID (they can be re-used with any bot);
* Group to supergroup migrate information (both old and new ID).

#### Requirements:
* Python 3.7 and above;  
* Linux (should work on Windows, but not tested);   
* Systemd init system (not necessary).  
* Docker (optional, see below).

#### Installation:  
1. Create a directory for bot: `mkdir my-id-bot`;  
2. `cd my-id-bot && python3 -m venv venv`;  
3. Put `bot.py` file to `my-id-bot` directory;  
4. `source venv/bin/python && pip install -r requirements.txt`;  
5. `chmod +x bot.py`;  
6. `BOT_TOKEN=12345:abcxyz ENABLE_STATS=0 ./bot.py`

If you want systemd support for autostart and other tasks: open `my-id-bot.service` file, change relevant options to match yours, enter correct token.  
Now copy that file to `/etc/systemd/system` enable it with `systemctl enable my-id-bot.service` and run it: `systemctl restart my-id-bot.service`. Easy!

Alternatively, you can use Docker (experimental):  
Build image: `docker build -t my-id-bot-image .`  
Run container: `docker run -e BOT_TOKEN=12345:abcxyz -e ENABLE_STATS=0 -v /path/to/logs/on/host:/logs --name my-id-bot -d --rm my-id-bot-image`.  
Or use Docker Compose as `docker-compose up -d`.
