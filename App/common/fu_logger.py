import os
import datetime
from loguru import logger


class Logger:
    __instance = None
    DATE = datetime.datetime.now().strftime("%Y-%m-%d")
    # 项目路径下创建log目录保存日志文件
    logpath = os.path.join(os.path.dirname(os.getcwd()), "logs")  # 拼接指定路径
    # 判断目录是否存在，不存在则创建新的目录
    if not os.path.isdir(logpath): os.makedirs(logpath)
    logger.add('%s/%s.log' % (logpath, DATE),  # 指定文件
               format="{time:YYYY-MM-DD HH:mm:ss}  | {level}> {elapsed} | {name}  |{message}",
               encoding='utf-8',
               # retention='30 days',  # 设置历史保留时长
               colorize=True,  # 终端颜色
               backtrace=True,  # 回溯
               diagnose=True,  # 诊断
               enqueue=True,  # 异步写入
               catch=True,
               # rotation="5kb",  # 切割，设置文件大小，rotation="12:00"，rotation="1 week"
               # filter="my_module"  # 过滤模块
               # compression="zip"   # 文件压缩
               )

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def info(self, msg, *args, **kwargs):
        return logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        return logger.debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        return logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        return logger.exception(msg, *args, exc_info=True, **kwargs)
