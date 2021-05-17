#-*-coding:utf-8-*-

import curses
import time
import sys
import os


import window
import player
import obstacle


class Game:
    # 三种不同难度的关卡配置，以(0.2, 1.0)为例，表示弹幕的填充密度是整个窗口面积的20%，每7次循环下落1行
    level_cfg = [(0.2, 7), (0.25, 5), (0.3, 3)]

    # 初始化窗口和难度等级
    def __init__(self, height, width, level):
        self.window = window.Window(height, width)
        self.level = level
        self.player = None
        self.obstacles = []

    # 创建窗口、玩家、障碍物列表并开启游戏主循环
    def run(self):
        # 初始化窗口系统
        curses.initscr()
        curses.noecho()
        curses.curs_set(0)

        self.window.init()

        # 创建玩家
        center_x = (self.window.min_x() + self.window.max_x()) // 2

        self.player = player.Player(self.window.max_y(), center_x, '*', self.window)

        # 初始化分数
        obstacle.Obstacle.score = 0

        # 根据难度等级生成障碍物列表
        obstacle_num = int(self.window.width * self.window.height * Game.level_cfg[self.level - 1][0])

        self.obstacles = [obstacle.Obstacle('-', self.window) for _ in range(0, obstacle_num)]

        # 初始化循环计数器
        loop_cnt = Game.level_cfg[self.level - 1][1]
        loop_index = 0

        hit = False

        # 游戏主循环
        while True:
            self.window.clear()

            # 绘制障碍物
            for obs in self.obstacles:
                obs.draw()

            # 绘制玩家
            self.player.draw()

            # 显示分数
            self.window.show('Score: ' + str(obstacle.Obstacle.score))

            # 如果之前玩家已被击中，则跳出游戏主循环
            if hit:
                self.window.refresh()
                break

            # 获取键盘输入
            key = self.window.key()

            # 如果是ESC键，则退出游戏
            if 27 == key:
                break

            # 更新玩家位置
            self.player.move(key)

            # 判断障碍物是否与玩家发生碰撞
            for obs in self.obstacles:
                if obs.get_y() == self.player.get_y() and obs.get_x() == self.player.get_x():
                    hit = True
                    self.player.set_sym('X')

                    break

            # 若无碰撞发生，更新障碍物位置
            if not hit:
                loop_index += 1
                if loop_index >= loop_cnt:
                    loop_index = 0

                    for obs in self.obstacles:
                        obs.move()

        # 跳出主循环后，3秒后关闭窗口
        time.sleep(3.0)

        curses.endwin()
