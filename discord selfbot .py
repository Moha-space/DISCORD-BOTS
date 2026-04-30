import discord
from discord.ext import commands                  
import asyncio

bot = commands.Bot(
    command_prefix='.',  
    self_bot=True,
    help_command=None                             
)

@bot.event
async def on_ready():
    print(f" 🙋 : {bot.user} ON TOP")
    print("Bot is ready!")

@bot.event 
async def on_connect():        
await asyncio.sleep(2)              
await bot.change_presence(
        status=discord.Status.idle,# online,idle,dnd
  activity=discord.Game(name=" ")       # STATUS 
)                                                
print("Status set ")



@bot.command()                                     
async def ping(ctx):                       
await ctx.send(f"pong! `{round(bot.latency * 1000)}ms`")


bot.run("Token")


# under work 
                                                                                                                                               

