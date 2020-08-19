async def get_phrase(body: str, thing: str, another: str) -> str:
    return '''　　{body}{thing}是怎么回事呢？{body}相信大家都很熟悉，但是{body}{thing}是怎么回事呢，下面就让小编带大家一起了解吧。
　　{body}{thing}，其实就是{another}，大家可能会很惊讶{body}怎么会{thing}呢？但事实就是这样，小编也感到非常惊讶。
　　这就是关于{body}{thing}的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！'''.format(body=body, thing=thing, another=another)