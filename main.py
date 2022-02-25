import discord
import os
import asyncio

guild_id = 863307439348908032
msgId = 937598096148402186

bot = discord.Bot()

@bot.event
async def on_ready():
    print('연결이 완료되었습니다.')


@bot.slash_command(guild_id=[946025877324566568], description="초대코드 생성하기")
async def 초대코드(ctx):
    try:
        main_guild = bot.get_guild(guild_id)

        channel = main_guild.text_channels[9]
        invite_code = await channel.create_invite(max_age=30, max_uses=1, reason=str(ctx.author.id))
        await ctx.respond(content=f"30초 후 만료됩니다\n{invite_code}", ephemeral=True)
        print(f'{ctx.author} (이)가 초대코드를 생성했습니다')

    except:
        await ctx.respond(f"{ctx.author.mention} 예기치 못한 오류가 발생됨.", ephemeral=True)

token = os.environ['BOT_TOKEN']
bot.run(token)



