import logging


def get_logger(name,filename,mode='a',encoding='utf-8',fmt=None,debug=False):

    # name:文件名字
    # filename:文件路径
    # mode:读写模式，默认追加
    # encoding:编码格式，默认utf-8
    # fmt:日志格式，默认None，即使用默认格式
    # debug:是否开启debug模式，默认False

    # 创建日志对象
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if debug:
        file_level = logging.DEBUG
        console_level = logging.DEBUG
    else:
        file_level = logging.WARNING
        console_level = logging.INFO

    if fmt is None:
        fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s'

    # 写入文件的日志处理器
    file_handler = logging.FileHandler(filename,mode=mode,encoding=encoding)
    file_handler.setLevel(file_level)

    # 写入控制台的日志处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)

    # 创建格式化器并添加日志处理器
    formatter = logging.Formatter(fmt)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 添加日志处理器到日志对象中
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == '__main__':
    logger = get_logger('py','../logs/py.log',debug=True)
    logger.info('我是普通信息')