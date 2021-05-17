#-*-coding:utf-8-*-

import curses


class Window:
    # 初始化高度和宽度
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.window = None

    # 创建窗口并设置参数
    def init(self):
        # 高度多出3（2边界+1分数），宽度多出2（2边界）
        self.window = curses.newwin(self.height + 3, self.width + 2)
        self.window.keypad(True)
        self.window.timeout(100)

    # 窗口内部区域的最小y坐标
    def min_y(self):
        return 1

    # 窗口内部区域的最大y坐标
    def max_y(self):
        return self.height

    # 窗口内部区域的最小x坐标
    def min_x(self):
        return 1

    # 窗口内部区域的最大x坐标
    def max_x(self):
        return self.width

    # 清空窗口内容并绘制边界
    def clear(self):
        self.window.clear()
        self.window.box()

    # 在指定位置绘制字符
    def draw(self, y, x, ch):
        self.window.addstr(y, x, ch)

    # 在窗口左下角显示消息
    def show(self, msg):
        self.window.addstr(self.height + 1, 1, msg)

    # 刷新窗口内容
    def refresh(self):
        self.window.refresh()

    # 获取键盘按键
    def key(self):
        return self.window.getch()
