import discord #importing up all the libraries 
import random #to generate random quotes 
import requests #request to use json api 
import json #access zenquotes api
import os #os is used to access .env file 
from stay_alive import stay_alive #hosting on web

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

greeting_commands = [
"A functioning and resilient infrastructure is the foundation of every successful community. Pleasent greetings to you user. Press .continue for more"  
"Environment is no one's property to destroy; it's everyone's responsibility to protect. Pleasent greetings to you user. Press .continue for more",
"There's something better than an 'excuse' for your mistake, which is 'now you know how to stop it from happening again. Pleasent greetings to you user. Press .continue for more",
"Sustainability improves the quality of our lives, protects our ecosystem and preserves natural resources for future generations. Pleasent greetings to you user. Press .continue for more ",
]
#The list of greeting commands
gif = ['https://tenor.com/view/killua-zoldyck-anime-hello-salute-cute-boy-gif-19915148', 'https://tenor.com/view/hi-excited-happy-bananafish-yay-gif-18377734',
'https://tenor.com/view/hello-there-baby-yoda-mandolorian-hello-gif-20136589',
'https://tenor.com/view/hi-hello-there-hello-sup-swag-gif-17652416',
'https://tenor.com/view/anime-life-is-great-happy-led-gif-8166652',
'https://tenor.com/view/anime-anime-girl-girl-cat-gif-18514354',
'https://tenor.com/view/eromanga-sensei-anime-yo-hi-hello-gif-17430483',
'https://tenor.com/view/kakashi-hatake-hi-naruto-hello-anime-gif-13667691',
'https://tenor.com/view/anime-hi-hello-wave-happy-gif-17215102',
'https://tenor.com/view/neko-cat-neko-hello-loli-hello-markus-hello-hi-gif-21914840',
'https://tenor.com/view/anime-waving-hello-anime-gif-21791647',
'https://tenor.com/view/viktor-yuri-on-ice-hello-gif-22450356',
'https://tenor.com/view/baby-hello-hello-there-hi-waving-gif-15692366'
]
#list of gif
@client.event 
async def on_ready():
    print("We have logged in as {0.user}".format(client))
#on ready just do stuff
@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content #creating a variable

    if msg.startswith('.hey'):
        await message.channel.send((random.choice(greeting_commands)))
    
    if msg.startswith('.inspire'):
      quote = get_quote()
      await message.channel.send(quote)
    
    if msg.startswith('.greet'):
      await message.channel.send((random.choice(gif)))
    
    if msg.startswith('.continue'):
      myEmbed = discord.Embed(title = "Commands", description = "The commands of the bot are given as", color = 0xffbb99 )
      myEmbed.add_field(name=".hey", value="New here just pressout .hey", inline = False)
      myEmbed.add_field(name=".about", value="This will tell you about the project of the bot based upon SDG goal: Industry innovation and infrastructure.", inline = False)
      myEmbed.add_field(name=".greet", value="The following command present you a warm surprise greet", inline = False)
      myEmbed.add_field(name=".inspire", value="Recieve a random quote to get your day going!!!", inline = False)
      myEmbed.add_field(name=".info", value="Get more to know about the SDG goal Industry, innovation and infrastructure.", inline = False)
      myEmbed.add_field(name=".initiate", value="Know how you can help", inline = False)
      myEmbed.add_field(name=".show", value="What is happening all around the globe in the world of innovation?", inline = False)
      myEmbed.add_field(name=".sources", value="Press .source to know about the sources of information", inline = False)
      myEmbed.set_footer(text = "Let the new adventure begin fellow usermate!!!!")
      myEmbed.set_author(name = "Saturo The SDG Bot (Mohak)")
      await message.channel.send(embed = myEmbed)
      #defining the continue statement to maintain ease 
   
    if msg.startswith('.about'):
      await message.channel.send("Economic growth, social development and climate action are heavily dependent on investments infrastructure, sustainable industrial development and technological progress. In the face of a rapidly changing global economic landscape and increasing inequalities, sustained growth must include industrialization that first of all, makes opportunities accessible to all people, and second, is supported by innovation and resilient infrastructure.")
      #about provides info about project 
    if msg.startswith('.info'):
      myEmbed2 = discord.Embed(title = "Information", description = "What does it really means about Industry innovation and infrastructure", color = 0xffbb99 )
      myEmbed2.add_field(name="Sustainable development", value="Basic infrastructure like roads, information and communication technologies, sanitation, electrical power and water remains scarce in many developing countries. In 2019, some 87 per cent of people in developed countries used the Internet, compared with just 19 per cent in the least developed countries.", inline = False)
      myEmbed2.set_footer(text = "Let the new adventure begin fellow usermate!!!!")
      myEmbed2.set_author(name = "Saturo The SDG Bot (Mohak)")
      await message.channel.send(embed = myEmbed2)
      #info command 
    if msg.startswith('.show'):
      myEmbed3 = discord.Embed(title = "Progress", description = "How far have we reached Industry innovation and infrastructure", color = 0xffbb99 )
      myEmbed3.add_field(name="Sustainable development", value="Investment in research and development globally – as well as financing for economic infrastructure in developing countries – has increased, and impressive progress has been made in mobile connectivity with almost the entire world population 97 per cent living within reach of a mobile cellular signal.", inline = False)
      myEmbed3.add_field(name = "Graph", value = "https://tenor.com/view/loading-bar-gif-19667497", inline = False)
      myEmbed3.set_footer(text = "Let the new adventure begin fellow usermate!!!!")
      myEmbed3.set_author(name = "Saturo The SDG Bot (Mohak)")
      await message.channel.send(embed = myEmbed3)
    
    if msg.startswith('.initiate'):
      myEmbed4 = discord.Embed(title = "How you can help?", description = "Know to play your initiative in ensuring sustainable goals.", color = 0xffbb99 )
      myEmbed4.add_field(name="Sustainable development", value="Establish standards and promote regulations that ensure company projects and initiatives are sustainably managed. Collaborate with NGOs and the public sector to help promote sustainable growth within developing countries. Think about how industry impacts on your life and well-being and use social media to push for policymakers to prioritize the SDGs.", inline = False)
      myEmbed4.set_footer(text = "Let the new adventure begin fellow usermate!!!!")
      myEmbed4.set_author(name = "Saturo The SDG Bot (Mohak)")
      await message.channel.send(embed = myEmbed4)
    
    if msg.startswith('.sources'):
      myEmbed5 = discord.Embed(title = "Sources of the projects", description = "The given sources are the resources used upon.", color = 0xffbb99 )
      myEmbed5.add_field(name="Tenor Library", value="https://tenor.com/", inline = False)
      myEmbed5.add_field(name="ZenQuotes Api", value="https://zenquotes.io/api/random", inline = False)
      myEmbed5.add_field(name="Sustainable development reference API", value="https://www.un.org/sustainabledevelopment/wp-content/uploads/2019/07/9_Why-It-Matters-2020.pdf", inline = False)
      myEmbed5.set_footer(text = "Let the new adventure begin fellow usermate!!!!")
      myEmbed5.set_author(name = "Saturo The SDG Bot (Mohak)")
      await message.channel.send(embed = myEmbed5)

stay_alive()  #stay alive is the file to host bot on web
client.run(os.getenv('token')) #to run the bot on host the token variable is in env file but you can simply use by client.run(bot's token)