#Nonebot plugin
#AutoWhiteList
#__init__.py
#Author:dixiatielu

from mcrcon import MCRcon

#服务器地址
HOST = ''
#Rcon的端口
PORT = 25564
#Rcon的密码
RCON_PWD = ''

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