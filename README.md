# Bot to get users/chats IDs in Telegram

<a href="https://hub.docker.com/r/groosha/my-id-bot"><img src="https://img.shields.io/badge/my--id--bot-docker%20hub-blue"></a>
<a href="https://t.me/my_id_bot"><img src="https://img.shields.io/badge/Telegram-@my__id__bot-0c5161"></a>   
Demo: [@my_id_bot in Telegram](https://t.me/my_id_bot).  

This is a simple bot written with [aiogram 3.x](https://github.com/aiogram/aiogram) framework to show some IDs, like:

* Your user ID (when asked in inline mode or in private chat with any message);  
* Group/supergroup ID (when added to that group or with /id command);  
* Channel ID (when message forwarded from channel to one-to-one chat with bot);  
* Sticker ID (they can be re-used with any bot);
* Group to supergroup migrate information (both old and new ID).

## Requirements:
* Python 3.9 and newer;  
* Linux (should work on Windows, but not tested);   
* Systemd init system (optional).  
* Docker (optional).

## Installation:

### Just to test (not recommended)
1. Clone this repo;
2. `cd` to cloned directory and initialize Python virtual environment (venv);
3. Activate the venv and install all dependencies from `requirements.txt` file;
4. Copy `env_example` to `.env` (with the leading dot), open `.env` and edit the variables;
5. In the activated venv: `python -m bot`

### Systemd 
1. Perform steps 1-4 from "just to test" option above;
2. Copy `my-id-bot.example.service` to `my-id-bot.service` (or whatever your prefer), open it and edit `WorkingDirectory` 
and `ExecStart` directives;
3. Copy (or symlink) that service file to `/etc/systemd/system/` directory;
4. Enable your service `sudo systemctl enable my-id-bot --now`;
5. Check that service is running: `systemctcl status my-id-bot` (can be used without root privileges).

### Docker + Docker Compose
1. Get `docker-compose.example.yml` file and rename it as `docker-compose.yml`;
2. Get `env_example` file, rename it as `.env` (with the leading dot), open it and edit the variables;
3. Run the bot: `docker compose up -d`;
4. Check that container is up and running: `docker compose ps`
