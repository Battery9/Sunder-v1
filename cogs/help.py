import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        class mainmenu(discord.ui.View):
            @discord.ui.button(label="Tournaments & Scrims", style=discord.ButtonStyle.success)
            async def button1(self, interaction: discord.Integration, button: discord.ui.Button):
                await interaction.response.edit_message(content ="Success", embed=None)
            @discord.ui.button(label="Tournaments & Scrims", style=discord.ButtonStyle.success)
            async def button2(self, interaction: discord.Integration, button: discord.ui.Button):
                await interaction.response.send_message("Success")
            @discord.ui.button(label="Tournaments & Scrims", style=discord.ButtonStyle.success)
            async def button3(self, interaction: discord.Integration, button: discord.ui.Button):
                await interaction.response.send_message("Success")
            @discord.ui.button(label="Tournaments & Scrims", style=discord.ButtonStyle.success)
            async def button4(self, interaction: discord.Integration, button: discord.ui.Button):
                await interaction.response.send_message("Success")

        view = mainmenu()
        userid = ctx.message.author.id
        embed = discord.Embed(title="❏ **__HELP MENU__**", description=f"Hey <@{userid}>, this is Sunder, available here 24/7 to help you. I pride myself on having a faster typing speed than any other moderator on this server, so I am confident that I can help you find what you're looking for. Why not give me a try before tagging those lazy folks? \n **Ohh Btw, how may i help you?**", color=0x52f3ff)
        embed.set_thumbnail(url="https://i.ibb.co/LC96Nb1/ezgif-com-gif-maker.gif")
        await ctx.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Help(bot))
