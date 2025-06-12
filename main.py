from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import requests

@register("yufu", "Seven39c5bb", "这是支持渔夫乐园开发的插件", "1.0.0")
class Yufu(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("llt")
    async def llt(self, event: AstrMessageEvent):
        url="https://pics-bed.vercel.app/yufu/llt/1.jpg"
        try:
            chain =[
                Comp.Image.fromURL(url)
            ]
            yield event.chain_result(chain) # 发送一条纯文本消息
        except:
            yield event.plain_result(f'请求失败，可能是没找到这个图片哦qaq')
        

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
