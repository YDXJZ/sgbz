from fangfa.FindWindows import get_game_window

# 检测游戏是否运行
game_rect = get_game_window(r".*QQ三国.*|.*Genshin Impact.*")  # 支持多语言标题
if game_rect:
    zb_left, zb_top, zb_right, zb_bottom = game_rect  # 储存游戏窗口坐标
    # 计算比例
    current_width, current_height = zb_right, zb_bottom
    # 计算宽高比例
    print(game_rect)


else:
    print("未找到游戏窗口")