from nonebot import on_command, CommandSession
from mcrcon import MCRcon

__plugin_name__ = '重载MinecraftQQ'
__plugin_usage__ = '重载MinecraftQQ'

@on_command('qreload', aliases=('重载', 'MCQQ重载', 'MinecraftQQ重载', 'minecraftqq重载', 'mcqqreload'))
async def qreload(session: CommandSession):
    with MCRcon(host = session.bot.config.RCON_HOST, port = session.bot.config.RCON_PORT, password = session.bot.config.RCON_PWD) as rcon:
        res = rcon.command('qq reload socket')
    await session.send(res)