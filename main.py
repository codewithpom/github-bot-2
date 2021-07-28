import discord
import github_api
from discord.ext import commands
import webserver
import os
client = commands.Bot(command_prefix="?")

token = os.environ['token']

@client.event
async def on_ready():
    print('Bot online')

  
@client.event
async def on_message(message):
            ctx = message.channel
            if str(message.content).startswith("?search "):
                question = str(message.content)[len("?search "):]
                print(question)
                data = github_api.search(question)
                repos_embed = discord.Embed(title="Results repostiroes for " + question, desc="Here are the results for your query", color=0x3498db)
                for i in data:
                    title = i['title']
                    description = i['des']
                    language = i['lang']
                    href = "https://github.com" + i['href']
                    repos_embed.add_field(name=title, value=f"The name of the repository is {title}. Its description is {description}. The language it is programmed in is {language}. The link to it is {href}")
                try:
                    await ctx.send(embed=repos_embed)

                except Exception as e:
                    await ctx.send("Message too long cannot send it.Sorry 😞😞😞😞")
            
webserver.keep_alive()
client.run(token)

