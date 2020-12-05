# Twitch Count Bot 

## Setup Video
<a href="https://youtu.be/nW5W9JBWX5Y">
    <img src="./images/youtube_thumbnail.jpg" width="500"/>
</a>

[Youtube Video Link](https://youtu.be/nW5W9JBWX5Y)

## Setup and Run

Requires at Python `3.7.3`.

Install necessary packages (locally):

```bash
python3 -m pip install -r requirements.txt
```

Copy `.env.sample` to `.env`

```
cp .env.sample .env

```

Open `.env` and insert the following fields:

| Field        | Explaination                                                          |
|--------------|-----------------------------------------------------------------------|
| `TMI_TOKEN`  | OAuth Token with `oauth:` as a prefix                                 |
| `CLIENT_ID`  | Client ID obtained from Twitch's Developer site                       |
| `BOT_NICK`   | Twitch name of the Bot                                                | 
| `BOT_PREFIX` | Prefix for commands the bot should listen to (set to `!` per default) |
| `CHANNEL`    | The name of the your Twitch channel you want the bot to run at        |

Start Bot:

```
python3 bot.py
```

## Add the Bot to Autostart (Raspberry Pi OS)

Install necessary packages (globally):

```bash
sudo -H python3 -m pip install -r requirements.txt
```

## Credits
![K0nze Logo](./images/k_logo_30x30.png "Logo") Created by Konstantin (Konze) Lübeck

 * Discord: [discord.k0nze.gg](https://discord.k0nze.gg) 
 * Twitch: [twitch.tv/k0nze](https://twitch.tv/k0nze) 
 * Youtube: [youtube.com/k0nze](https://youtube.com/k0nze) 
 * Twitter: [twitter.com/k0nze_gg](https://twitter.com/k0nze_gg) 
 * Instagram: [instagram.com/k0nze.gg](https://instagram.com/k0nze.gg) 
