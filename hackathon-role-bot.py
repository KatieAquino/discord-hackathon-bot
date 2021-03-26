import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Hackathon bot online.")


@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id

    if message_id == 825070772682620948:
        guild = await client.fetch_guild(payload.guild_id)

        role = False

        if payload.emoji.name == 'adahacker':
            role = discord.utils.get(guild.roles, name='hackathons')
            print('role is: ', role)

        
        if payload.emoji.name == 'cloud_lightning':
            role = discord.utils.get(guild.roles, name='athena')
            print('role is: ', role)

        
        if role != False:
            member = guild.get_member(payload.user_id)
            guild_member = discord.utils.get(guild.roles, name="Guild Member")
            pending = discord.utils.get(guild.roles, name="Roles Pending")

            if member != None:
                print('adding role')
                await member.add_roles(guild_member)
                print('Completed')


client.run(os.environ['DISCORD_TOKEN'])