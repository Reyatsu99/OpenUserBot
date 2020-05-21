# Credits to https://t.me/TheHardGamer

from telethon import events
import io
import os
import urllib
from urllib.request import urlopen
import requests
import re
from telethon.tl.types import MessageMediaPhoto
from PIL import Image

from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.boobs(?: |$)(.*)")
async def boobs(e):
    nsfw = requests.get('http://api.oboobs.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve(
        "http://media.oboobs.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'k.jpg')
    await bot.send_file(e.chat_id, "k.jpg")


@register(outgoing=True, pattern="^.butts(?: |$)(.*)")
async def butts(e):
    nsfw = requests.get('http://api.obutts.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve(
        "http://media.obutts.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'k.jpg')
    await bot.send_file(e.chat_id, "k.jpg")


CMD_HELP.update({"boobs": ".boobs\
    \nUsage: Uploads a random picture featuring women's breasts."})


CMD_HELP.update({"butts": ".butts\
    \nUsage: Uploads a random picture featuring women's butt/ass."})
