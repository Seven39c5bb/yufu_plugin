from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import astrbot.api.message_components as Comp
import requests
import os
import random

@register("yufu", "Seven39c5bb", "这是支持渔夫乐园开发的插件", "1.0.0")
class Yufu(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    @filter.command_group("yf")
    def yf():
        pass
    @yf.command("help")
    async def yfhelp(self, event: AstrMessageEvent):
        helpTxt='''
        渔夫bot使用帮助：
        还在开发中，有什么需求都可以提一下，看情况更新,使用/yf help进行命令查询
        1./llt 随机发送llt图
        2./yf r 随机发送渔夫图
        3./dou 斗
        4./chat 进行大模型ai聊天,模型为gemini-2.5-flash-preview-04-17
        '''
        yield event.plain_result(helpTxt)
    @yf.command("r")
    async def randomPic(self, event: AstrMessageEvent):
        plugin_root_dir = os.path.dirname(os.path.abspath(__file__))
        img_path=os.path.join(plugin_root_dir,'asset','img','yf')
        all_items = os.listdir(img_path)
        image_files = [f for f in all_items if os.path.isfile(os.path.join(img_path, f))]
        random_image_name = random.choice(image_files)
        random_image_path = os.path.join(plugin_root_dir, 'asset', 'img', 'yf',random_image_name)
        try:
            chain =[
                Comp.Image.fromFileSystem(random_image_path)
            ]
            yield event.chain_result(chain) # 发送一条纯文本消息
        except:
            yield event.plain_result(f'请求失败，可能是没找到这个图片哦qaq')

    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("llt")
    async def llt(self, event: AstrMessageEvent):
        plugin_root_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(plugin_root_dir, 'asset', 'img', 'llt')
        all_items = os.listdir(image_path)
        image_files = [f for f in all_items if os.path.isfile(os.path.join(image_path, f))]
        random_image_name = random.choice(image_files)
        random_image_path = os.path.join(plugin_root_dir, 'asset', 'img', 'llt',random_image_name)
        try:
            chain =[
                Comp.Image.fromFileSystem(random_image_path)
            ]
            yield event.chain_result(chain) # 发送一条纯文本消息
        except:
            yield event.plain_result(f'请求失败，可能是没找到这个图片哦qaq')

    @filter.command("dou")
    async def dou(self, event: AstrMessageEvent):
        chain=[
            Comp.At(qq=2214648656),
            Comp.At(qq=1484809270),
            Comp.At(qq=835326109),
            Comp.At(qq=1169462875),
            Comp.At(qq=1954300394),
            Comp.At(qq=1732967400),
            Comp.At(qq=1367809074),
            Comp.At(qq=827361754),
            Comp.Plain("斗")
        ]
        yield event.chain_result(chain)
    @filter.command("huan")
    async def huan(self, event: AstrMessageEvent):
        chain=[
            Comp.At(qq=827361754),
            Comp.At(qq=953153795),
            Comp.Plain("\n环")
        ]
        yield event.chain_result(chain)
    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
