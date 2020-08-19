from nonebot import on_command, CommandSession
from mcrcon import MCRcon

__plugin_name__ = 'rcon'
__plugin_usage__ = 'rcon'

@on_command('rcon', aliases=('重载', 'MCQQ重载', 'MinecraftQQ重载', 'minecraftqq重载', 'mcqqreload'), permission = SUPERUSER)
async def rcon(session: CommandSession):
    cmmd = session.get('cmmd', prompt='请输入指令')
    with MCRcon(host = session.bot.config.RCON_HOST, port = session.bot.config.RCON_PORT, password = session.bot.config.RCON_PWD) as rcon:
        res = rcon.command(cmmd)
    await session.send(res)

@weather.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['cmmd'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('指令不能为空，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg