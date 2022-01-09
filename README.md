# Discord Notification Bot

## Run locally

DISCORD_API_TOKENは<https://discord.com/developers/applications/929710548399042583/bot>で取得。

```sh
export DISCORD_API_TOKEN=<token>
python main.py
```

## Deploy to Heroku

```sh
heroku login
heroku git:remote -a stathack-discord-notification
git push heroku master
```

動かない時は再起動

```sh
heroku restart --app stathack-discord-notification
```

## Reference

実装の参考：<https://tech-cci.io/archives/6412>
