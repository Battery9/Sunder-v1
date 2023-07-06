import discord
from discord.ext import commands
import asyncio
import configparser
config = configparser.ConfigParser()

#Making a class with command name.
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Writing my command function using this commands.command decorator from discord.py
    @commands.command()
    async def help(self, ctx):
        #This a View class for creating buttons. I've used discord.ui.button decorator for defining each button. 
        #Also using discord.Interaction to define an action on button press.
        class mainmenu(discord.ui.View):
            @discord.ui.button(label="Tournaments & Scrims", style=discord.ButtonStyle.success)
            async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.edit_message(content ="Okay. Here you go...", embed=scrims_embed, view=back_view)

            @discord.ui.button(label="Discord Server", style=discord.ButtonStyle.blurple)
            async def button2(self, interaction: discord.Integration, button: discord.ui.Button):
                await interaction.response.edit_message(content = "Let me walk you through...", embed=discord_embed, view=back_view)

            @discord.ui.button(label="Need Help!", style=discord.ButtonStyle.red)
            async def button3(self, interaction: discord.Integration, button: discord.ui.Button):
                await interaction.response.edit_message(content="Get help...", embed=help_embed, view=back_view)

            @discord.ui.button(label="Fun & Utility", style=discord.ButtonStyle.gray)
            async def button4(self, interaction: discord.Integration, button: discord.ui.Button):
                await interaction.response.edit_message(content="Wie Wie!", embed=extra_embed, view=back_view)

            @discord.ui.button(label="X", style=discord.ButtonStyle.red)
            async def close(self, interaction: discord.Integration, button: discord.ui.Button):
                await interaction.message.delete()
                await interaction.response.delete()
        
        #Another View class for Back and Close buttons.
        class back(discord.ui.View):
            @discord.ui.button(label="Need More Help", style=discord.ButtonStyle.blurple)
            async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.edit_message(content="Anything Else? Choose from other options below.", embed=None, view=mainmenu())
            
            @discord.ui.button(label="Thank You!", style=discord.ButtonStyle.green)
            async def close(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.message.reply(content="You're Welcome!🥰️ Type !help and I'm here.", delete_after=7)
                await interaction.response.edit_message(view=None)
                await asyncio.sleep(60)  #Delete the response after 60sec. overides ctx.send 200sec.
                await interaction.message.delete()
                

        #All Embed to be send with responces.------------------->>>>>>>>
        ##Tourny & Scrim
        scrims_embed = discord.Embed(title="**__❑ On-going Tournaments and Scrims__**", description="**>> Please visit the below channel to learn about and join different events happening right now across different platforms of UREsports. Our only talented admin have listed all the Scrims and Tournament just for you. Unleash your talents, show off your skills and roast your opponents with your squad.\nIt’s time to have some fun and make some noise**\n\n<#1125346374737727530>", color=0x00ff00).set_footer(text="Sunder | UREsports")
        
        ##Reading the ini file inside res to use.
        config.read('res/data.ini')
        popular = config['var']['popular']
        if(popular!=''):
            scrims_embed.add_field(name="__❑ Popular: __", value=popular)

        ##Server Embed
        discord_embed = discord.Embed(title="**__❑ Discod Server Guide__**",
      description="**>> Kinda Confused? Don't rage quit yet. Save your precious Brain power and Let me be your guide for UREsports Discord server.  Get, set, click!👇\n**",
      color=0x0073ff).set_footer(text="Feel free to peek into every other channels, No one can stop youh! Sunder | UREsports")
        discord_embed.add_field(name="➤ <#1118542149772918784>", value="A good Starting point to know Unknown Rivals Esports", inline=False)
        discord_embed.add_field(name="➤ <#1118542163488284733>", value="All important updates are here.", inline=False)
        discord_embed.add_field(name="➤ <#1118542173990821948>", value="Chat with our family.", inline=False)
        discord_embed.add_field(name="➤ MUSIC ZONE & GAMES", value="Scroll Down to Hang Out with my fellow Bots.")
        discord_embed.add_field(name="➤ <#1125346374737727530>", value="Yupp. The most important one at the End.")

        ##Help Embed
        help_embed = discord.Embed(title="**__Ask for HELP__**", description="**Oh, you've uncovered my bot secrets! 🙈I can't answer(or question) everything. As an automated bot, I do have my limitations, and it seems I've reached the edge of my virtual universe. But worry not, for I've got a solution! 🤖🌟 To receive the personalized touch and expert assistance, I suggest reaching out to our delightful human team.\nSimply make use of <#1118542173990821948> and <#1118542156035014737>. __Tag those online folks, hope they are not AFK! 😅__**",color=0xccff33).set_footer(text="Happy human interaction awaits! 🎉🤝").set_thumbnail(url="https://i.ibb.co/LC96Nb1/ezgif-com-gif-maker.gif")

        ##Extra Embed
        extra_embed = discord.Embed(title="**__Extra Commands__**", description="", color=0xff66ff).set_footer(text="Talk to other bots if you wanna dance or play.")
        extra_embed.add_field(name="```shayari```", value="(coming soon)I will throw a Shayari! ✨📜 a dose of soul-stirring poetry and heartfelt emotions.", inline=False)
        extra_embed.add_field(name="invite", value="Invite Sunder bot to join your server!")

        #Creating a view object, an embed message and sending it using await ctx.reply.
        view = mainmenu()
        back_view = back()
        userid = ctx.message.author.id
        embed = discord.Embed(title="❏ **__HELP MENU __**⫸", description=f"Hey <@{userid}>, this is Sunder, available here 24/7 to help you. I pride myself on having a faster typing speed than any other moderator on this server, so I am confident that I can help you find what you're looking for. Why not give me a try before tagging those lazy folks? \n **Ohh Btw, how may i help you?**", color=0x52f3ff)
        embed.set_thumbnail(url="https://i.ibb.co/LC96Nb1/ezgif-com-gif-maker.gif")
        await ctx.reply(embed=embed, view=view, delete_after=200)
        await ctx.message.delete()

#Adding my class as a cog to be loaded in main.py.
async def setup(bot):
    await bot.add_cog(Help(bot))
