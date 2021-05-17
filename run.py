#!/usr/bin/env python
#-*-coding:utf-8-*-

import getopt
import sys
import os

import game


def main(argv):
    # 判断参数是否缺失
    try:
        opts, _ = getopt.getopt(argv, 'h:w:d:', ['canvas_height=', 'canvas_width=', 'diff_level='])
    except getopt.GetoptError:
        print('run.py -h <canvas_height> -w <canvas_width> -d <diff_level>')
        sys.exit()

    # 默认参数
    width = 20
    height = 50
    level = 1

    # 解析参数
    for opt, arg in opts:
        if opt in ('-h', '--canvas_height'):
            height = int(arg)
        elif opt in ('-w', '--canvas_width'):
            width = int(arg)
        elif opt in ('-d', '--diff_level'):
            level = int(arg)

    # 获取控制台尺寸
    rows, cols = os.popen('stty size', 'r').read().split()

    rows = int(rows)
    cols = int(cols)

    # 如果输入参数大于最大可用尺寸（去除边界），提示最大可用尺寸
    if height > rows - 3 or width > cols - 2:
        print('current max height available: ', rows - 3)
        print('current max width available: ', cols - 2)
        print('Please input a valid size for game board to fit in the Window')
        sys.exit()

    # 使用参数创建游戏
    the_game = game.Game(height, width, level)
    the_game.run()


if __name__ == "__main__":
    main(sys.argv[1:])
