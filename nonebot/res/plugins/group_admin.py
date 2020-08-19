from nonebot import on_request, RequestSession

__plugin_name__ = '自动同意加群'
__plugin_usage__ = '自动同意加群'
# 将函数注册为群请求处理器
@on_request('group')
async def _(session: RequestSession):
    await session.approve()