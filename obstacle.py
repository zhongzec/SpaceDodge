#-*-coding:utf-8-*-

import random
import curses


class Obstacle:
    score = 0

    # 初始化障碍物的表示符号并生成随机位置
    def __init__(self, sym, window):
        self.sym = sym
        self.window = window

        # y坐标随机在窗口最上方以上
        self.y = random.randint(-self.window.max_y(), -1)

        # x坐标随机在最左和最右之间
        self.x = random.randint(self.window.min_x(), self.window.max_x())

    def set_sym(self, sym):
        self.sym = sym

    def get_y(self):
        return int(round(self.y))

    def get_x(self):
        return int(round(self.x))

    # 更新位置
    def move(self):
        in_range_before = self.window.min_y() <= self.y <= self.window.max_y()

        self.y += 1

        in_range_after = self.window.min_y() <= self.y <= self.window.max_y()

        # 如果障碍物从窗口区域离开
        if in_range_before and not in_range_after:
            # 分数加1
            Obstacle.score += 1

            # y坐标重新回到窗口最上方以上
            self.y -= self.window.max_y()

            # x坐标重新随机在最左和最右之间
            self.x = random.randint(self.window.min_x(), self.window.max_x())

    def draw(self):
        # 只有障碍物在窗口范围以内的时候才绘制其表示符号
        if self.window.min_y() <= self.y <= self.window.max_y():
            self.window.draw(self.y, self.x, self.sym)
