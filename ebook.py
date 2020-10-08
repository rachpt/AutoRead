#!/usr/bin/env python3

'''
--说明📖--
口袋阅自动打卡，使用 adb 指令实现。

--笔记📒--
截图：adb shell screencap -p /sdcard/01.png
传图：adb pull /sdcard/01.png
'''

import os
from random import randint
from time import sleep, time

adb_path = './adb'
total_page = 320  # 阅读页数：300 页
total_time = 31  # 阅读时间：30 分钟

page_per_time = int(total_time * 60 / total_page)
page_per_time = page_per_time if page_per_time > 3 else 3
total_page = total_page + randint(3, 10)

def operator(i:int, start):
    if i == 0:
        print("口袋阅打卡📅，任务开始…… ▶️")
    elif i % 10 == 0:
        print(f"已阅读 {i:3} 页，阅读时间：{(time() - start) / 60:4.1f} 分钟")
    os.system(f"{adb_path} shell input tap {randint(450, 650)} {randint(900, 1100)}")
    sleep(randint(page_per_time - 2, page_per_time + 2))

def read():
    start = time()
    [operator(i, start) for i in range(total_page)]

    print(f"任务完成👌！总阅读页数📖：{total_page}，总阅读时间🕒：{(time() - start) / 60:.2f} 分钟")

def main():
    print("---自动操作开始🏠---")
    os.system(f"{adb_path} shell input tap 350 1170")  # 进入电子书（x：-，y：-）
    sleep(3)
    os.system(f"{adb_path} shell input keyevent 3")  # home按键
    sleep(3)
    os.system(f"{adb_path} shell input keyevent 187")  # 切换应用 qq阅读
    sleep(3)
    os.system(f"{adb_path} shell input tap 125 300")  # 第一本书位置（x：40-200，y：188-408）
    # os.system(f"{adb_path} shell input tap 360 300")  # 第二本书位置（x：278-438，y：188-408）
    sleep(2)
    read()
    print("---自动打卡😃---")
    sleep(2)
    os.system(f"{adb_path} shell input keyevent 3")  # home按键
    sleep(3)
    os.system(f"{adb_path} shell input keyevent 187")  # 切换应用 qq阅读
    sleep(3)
    os.system(f"{adb_path} shell input tap 90 100")  # 点击活动中心（+-10）
    sleep(8)
    os.system(f"{adb_path} shell input tap 350 1100")  # 点击口袋阅打卡（y：960-1240）
    sleep(8)
    os.system(f"{adb_path} shell input tap 354 1130")  # 点击口袋阅打卡-打卡（y：1090-1180）
    sleep(6)
    os.system(f"{adb_path} shell input keyevent 4")  # 返回按键
    sleep(3)
    os.system(f"{adb_path} shell input keyevent 3")  # home按键
    sleep(3)
    os.system(f"{adb_path} shell input keyevent 26")  # 🔌锁屏
    print("---打卡完成✅，自动操作结束🔚---")


if __name__ == "__main__":
    main()
