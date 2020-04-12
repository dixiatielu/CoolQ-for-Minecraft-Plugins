# CoolQ for Minecraft Plugins
 基于Nonebot和CoolQ的Minecraft自动白名单插件

## 依赖
1. Python3
2. nonebot
```
pip install nonebot
```
3. mcrcon
```
pip install mcrcon
```
## 使用方法
1. Clone本仓库到一台Windows操作系统的电脑上
2. 确认已安装上述依赖
3. 把/data/app/io.github.richardchien.coolqhttpapi/config/把此文件改名成机器人的QQ号.json重命名为`机器人QQ号.json`，如`2031043256.json`
4. 运行CQA.exe 并输入机器人账户密码
5. 应用管理->启用CQHTTP插件
6. 打开\nonebot\config.py按照注释配置各种常量（确保服务端已启用rcon）
7. 到\nonebot目录下命令行执行`python bot.py`，运行nonebot
8. 私聊bot，发送`wl 你的ID`即可添加白名单（wl有别名`白名`，`白名单`，`加个白名单`等）
9. 在群聊发送消息找bot加白名单即可直接执行加白名单指令，如`腐竹 加个白名单 dixiatielu`或者`bot给我加个白名单吧qwq`等都是可行的。注意后一种说法暂时不能识别消息中的游戏id，所以只能发送消息后再发一次游戏id
## 官方文档
[这里是官方文档](https://nonebot.cqp.moe/guide/)
## 对于Linux用户
请参考官方文档`安装`部分关于如何在Linux配置nonebot的操作（不是指你的Minecraft服务器运行在Linux下，Minecraft服务器和机器人可以在不同环境和机子跑的）