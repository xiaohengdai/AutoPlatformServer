from enum import Enum

class MainTonalValue(Enum):
    red="RED"   #红色
    orange="ORANGE"   #橙色
    yellow="YELLOW"   #黄色
    green="GREEN"     #绿色
    blue="BLUE"       #蓝色
    violet="VIOLET"   #紫色
    black="BLACK"     #黑色
    white="WHITE"     #白色
    orange_red="ORANGE_RED"  #桔红色
    dark_red = "DARK_RED" # 暗红色
    rice_yellow='RICE_YELLOW'   #米黄色

    #相应的颜色RGB值，可以在这个网站上查RGB对应的颜色，http://tools.jb51.net/static/colorpicker/
    # colors = dict((
    #     ((196, 2, 51), MainTonalValue.red.value),
    #     ((255, 165, 0), MainTonalValue.orange.value),
    #     ((255, 69, 0), "orange_red"),
    #     ((255, 205, 0), MainTonalValue.yellow.value),
    #     ((0, 128, 0), MainTonalValue.green.value),
    #     ((0, 0, 255), MainTonalValue.blue.value),
    #     ((127, 0, 255), MainTonalValue.violet.value),
    #     ((0, 0, 0), MainTonalValue.black.value),
    #     ((255, 255, 255), MainTonalValue.white.value),))
    #   ((255, 229, 153), MainTonalValue.rice_yellow.value),
    #   ((213, 90, 95), MainTonalValue.dark_red.value)
