#Nonebot plugin
#autowhitelist.py
#Author:dixiatielu

from nonebot import on_command, CommandSession
from mcrcon import MCRcon

#服务器地址
HOST = ''
#Rcon的端口
PORT = 25564
#Rcon的密码
RCON_PWD = ''

@on_command('wl', aliases=('白名', '白名单', '加白名单', '添加白名单', '加个白名单'))
async def wl(session: CommandSession):

    uid = session.get('uid', prompt='您在LittleSkin注册的角色的ID是？')

    ress = await get_whitelist(uid)

    await session.send(ress)


# wl.args_parser 装饰器将函数声明为 wl 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@wl.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将ID跟在命令名后面，作为参数传入
            # 例如用户可能发送了：wl dixiatielu
            session.state['uid'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('您的ID不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的id），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def get_whitelist(uid: str) -> str:
    with MCRcon(host=HOST, port=PORT, password=RCON_PWD) as rcon:
        res = rcon.command('whitelist add '+uid)
    if res == 'Player is already whitelisted':
        tip = '您在服务器上已经有白名单了，无需再次添加'
    elif res == 'That player does not exist':
        tip = '没有找到您的角色名哦~请确认您在LittleSkin的角色管理添加了角色，并且向我发送的名字是您创建的角色名'
    else:
        tip = '添加成功，您的角色名为：' + uid
    return '服务器返回消息：' + res + '\n' + '机器人给您的回复：' + tip
