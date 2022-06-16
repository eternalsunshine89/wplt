from enum import Enum


class Action(Enum):
    CLICK = '点击'
    DOUBLECLICK = '双击'
    INPUT = '输入'


print(Action.INPUT)