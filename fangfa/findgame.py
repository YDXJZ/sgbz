import win32gui
import re

def get_game_window(title_pattern):
    """
    通过窗口标题模糊匹配获取游戏窗口位置
    :param title_pattern: 窗口标题的正则表达式（如".*我的游戏.*"）
    :return: (left, top, width, height)
    """

    def callback(hwnd, hwnd_list):
        if win32gui.IsWindowVisible(hwnd) and re.match(title_pattern, win32gui.GetWindowText(hwnd)):
            rect = win32gui.GetWindowRect(hwnd)
            hwnd_list.append(rect)
        return True

    hwnd_list = []
    win32gui.EnumWindows(callback, hwnd_list)

    if hwnd_list:
        left, top, right, bottom = hwnd_list[0]
        return (left, top, right - left, bottom - top)
    return None
