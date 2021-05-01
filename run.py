import os
import discord

#imports genéricos do Discord API
from discord import channel
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get
#imports adicionais para exemplos e funções específicas
import pandas as pd
import numpy as np

#Token utilizado no bot, pode ser encontrado na seção dev do discord
token = 'insira token aqui'
#prefixo do bot, comando acionador no chat do canal
BOT_PREFIXO = '*'
bot = commands.Bot(command_prefix=BOT_PREFIXO)

#Evento de inicialização 
@bot.event
async def on_ready():
    print("Logado como: " + bot.user.name + "\n")

#Primeiro Comando - Join
#Captura o canal de voz do usuário que acionou o comando e entra no canal de voz
#Só realiza essa ação caso o usuário esteja de fato em um canal de voz
@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"Bot conectado em {channel}\n")

#Segundo Comando - Leave
#Caso esteja em um canal de voz, sai dele
@bot.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Saí de {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")

#Terceiro Comando - Play
#Procura um áudio e reproduz na voz
@bot.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx):
    song_there = os.path.isfile("sample.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)

    voice.play(discord.FFmpegPCMAudio("sample.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07
    print("playing\n")

#Inicia o bot
bot.run(token)
