class BlockStatus(Enum):
    normal = 1  # 未点击
    opened = 2  # 已点击
    mine = 3    # 地雷
    flag = 4    # 标记为地雷
    ask = 5   # 标记为问号
    bomb = 6    # 踩中地雷
    hint = 7    # 被双击的周围
    double = 8  # 正被鼠标左右键双击