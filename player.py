#-*-coding:utf-8-*-

import curses


class Player:
    # 初始化玩家位置和表示符号
    def __init__(self, y, x, sym, window):
        self.y = y
        self.x = x
        self.sym = sym
        self.window = window

    # 设置表现符号
    def set_sym(self, sym):
        self.sym = sym

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x

    # 根据按键更新位置
    def move(self, key):
        # 向上移动
        if ord('w') == key or ord('W') == key or curses.KEY_UP == key:
            if self.y > self.window.min_y():
                self.y -= 1
        # 向下移动
        elif ord('s') == key or ord('S') == key or curses.KEY_DOWN == key:
            if self.y < self.window.max_y():
                self.y += 1

        # 向左移动
        if ord('a') == key or ord('A') == key or curses.KEY_LEFT == key:
            if self.x > self.window.min_x():
                self.x -= 1
        # 向右移动
        elif ord('d') == key or ord('D') == key or curses.KEY_RIGHT == key:
            if self.x < self.window.max_x():
                self.x += 1

    # 在玩家当前位置绘制表示玩家的符号
    def draw(self):
        self.window.draw(self.y, self.x, self.sym)
