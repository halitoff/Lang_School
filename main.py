import discord
import config
import words

bot = discord.Bot(intents=discord.Intents.all())
c = discord.commands.context.ApplicationContext
users = {}

@bot.slash_command(description="Начать игру")
async def reverse(ctx: c):
    print(ctx.user.id)
    if users.get(ctx.user.id) is None:
        users[ctx.user.id] = ["", "waiting"]

    word = words.get()
    await ctx.respond(f"Переверни слово: {word[::-1].upper()}")
    users[ctx.user.id] = [word, "game"]


@bot.event
async def on_message(message: discord.Message):
    if message.author.id in users and users[message.author.id][1] == "game":
        if message.content.lower() == users[message.author.id][0]:
            await message.channel.send("Поздравляем, вы угадали!")
        else:
            await message.channel.send(f"Не угадал, слово: {users[message.author.id][0]}")


bot.run(config.TOKEN)
