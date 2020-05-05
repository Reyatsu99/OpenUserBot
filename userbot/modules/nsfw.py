@bot.on(events.NewMessage(outgoing=True, pattern='.boobs'))
@bot.on(events.MessageEdited(outgoing=True, pattern='.boobs'))
async def boobs(e):
    nsfw = requests.get('http://api.oboobs.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'k.jpg')
    await bot.send_file(e.chat_id, "k.jpg")
@bot.on(events.NewMessage(outgoing=True, pattern='.butts'))
@bot.on(events.MessageEdited(outgoing=True, pattern='.butts'))
async def butts(e):
    nsfw = requests.get('http://api.obutts.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'k.jpg')
    await bot.send_file(e.chat_id, "k.jpg")
