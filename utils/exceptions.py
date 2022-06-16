"""自定义错误类型"""
from loguru import logger as log


class BaseError(Exception):
    """异常基类"""
    pass


class ArgumentError(BaseError):
    """参数错误"""

    def __init__(self, msg='参数错误'):
        log.error(msg)


class ElementNotFoundError(BaseError):
    """元素未找到"""

    def __init__(self, ele):
        log.warning(f'没有找到元素：【{ele}】')


class WaitElementTimeout(BaseError):
    """等待元素超时错误"""

    def __init__(self, ele):
        log.warning(f'等待元素超时：【{ele}】')


class LoginError(BaseError):
    """登录错误"""

    def __init__(self, msg='登录流程发生错误'):
        log.error(msg)


class PageErrorToast(BaseError):
    """页面出现错误提示"""

    def __init__(self, msg='页面上出现错误提示'):
        log.error(msg)


class ChildError(BaseError):
    """登录错误"""

    def __init__(self, msg='内部错误'):
        log.error(msg)

