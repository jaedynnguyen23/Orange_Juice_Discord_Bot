import os
import discord
import time
import random

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('You have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="truth or dare with you <3"))


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'ello {member.name}, you better like orange juice.'
    )

truthlist = []
darelist = []
emptylist = []


@client.event
async def on_message(message):
    # clears list
    truthlist.clear()
    with open(r'Text file location of Truth.txt', 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]
            # add current item to the list
            truthlist.append(x)

    # clears list
    darelist.clear()
    with open(rText file location of Dare.txt', 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]
            # add current item to the list
            darelist.append(x)

    if message.author == client.user:
        return

    message_content = message.content
    message_content2 = message_content.lower()

    if "i like apple juice" in message_content2:
        time.sleep(0.15)
        await message.channel.send('ur opinion isn't valid')
    elif "i love apple juice" in message_content2:
        time.sleep(0.15)
        await message.channel.send('how dare you love such a thing')
    elif "apple juice>" in message_content2:
        time.sleep(0.15)
        await message.channel.send('u like apple juice? u must also like the taste of dirt too')
    elif "apple juice" in message_content2:
        time.sleep(0.15)
        await message.channel.send('ewww how dare u mention such a disgusting thing')
    elif "apple" in message_content2:
        time.sleep(0.15)
        await message.channel.send('ur funny')

    if message.content.startswith('!rock'):
        rockanswer = random.randint(1, 3)
        print(rockanswer)
        if rockanswer == 1:
            await message.channel.send('how sad we tied')
        if rockanswer == 2:
            await message.channel.send('haha i had paper you loose L')
        if rockanswer == 3:
            await message.channel.send('dang i had scissors')

    if message.content.startswith('!paper'):
        paperanswer = random.randint(1, 3)
        print(paperanswer)
        if paperanswer == 1:
            await message.channel.send('how sad we tied')
        if paperanswer == 2:
            await message.channel.send('dang i had rock')
        if paperanswer == 3:
            await message.channel.send('haha i had scissors you loose L')

    if message.content.startswith('!scissors'):
        scissorsanswer = random.randint(1, 3)
        print(scissorsanswer)
        if scissorsanswer == 1:
            await message.channel.send('how sad we tied')
        if scissorsanswer == 2:
            await message.channel.send('haha i had rock you loose L')
        if scissorsanswer == 3:
            await message.channel.send('dang i had paper')

    if message_content2.startswith('!addtruth'):
        try:
            wholething = message.content
            tobedeleted = '!addtruth '
            endedtruth = wholething.replace(tobedeleted, "")
            truthlist.append(endedtruth)
            with open(r'Text file location of Truth.txt', 'w') as fp:
                for item in emptylist:
                    # write each item on a new line
                    fp.write("%s\n" % item)
            print(truthlist)
            # open file in write mode
            with open(r'Text file location of Truth.txt', 'a') as fp:
                for item in truthlist:
                    # write each item on a new line
                    fp.write("%s\n" % item)
            await message.channel.send("your truth has been added")
        except (RuntimeError, TypeError, NameError, UnicodeEncodeError):
            await message.channel.send("sorry i do not support emojis plz try again")

    if message_content2.startswith('!adddare'):
        try:
            wholething = message.content
            tobedeleted = '!adddare '
            endeddare = wholething.replace(tobedeleted, "")
            darelist.append(endeddare)
            with open(r'Text file location of Dare.txt', 'w') as fp:
                for item in emptylist:
                    # write each item on a new line
                    fp.write("%s\n" % item)
            print(darelist)
            # open file in write mode
            with open(r'Text file location of Dare.txt', 'a') as fp:
                for item in darelist:
                    # write each item on a new line
                    fp.write("%s\n" % item)
            await message.channel.send("your dare has been added")
        except (RuntimeError, TypeError, NameError, UnicodeEncodeError):
            await message.channel.send("sorry i do not support emojis plz try again")

    if message_content2.startswith('!truth'):
        truthanswer1 = random.choice(truthlist)
        truthanswer2 = "your truth is: " + truthanswer1
        await message.channel.send(truthanswer2)

    if message_content2.startswith('!dare'):
        dareanswer1 = random.choice(darelist)
        dareanswer2 = "your dare is: " + dareanswer1
        await message.channel.send(dareanswer2)

client.run('INSERT DISCORD BOT KEY HERE')

