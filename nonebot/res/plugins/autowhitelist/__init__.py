#Nonebot plugin
#AutoWhiteList
#__init__.py
#Author:dixiatielu

from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

from .data_source import get_whitelist

@on_command('wl', aliases=('白名', '白名单', '加白名单', '添加白名单', '加个白名单'))
async def wl(session: CommandSession):

    uid = session.get('uid', prompt='您在LittleSkin注册的角色的ID是？')

    ress = await get_whitelist(uid, session.bot.config.RCON_HOST, session.bot.config.RCON_PORT, session.bot.config.RCON_PWD)

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
# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'白名', 'whitelist'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'wl')
