class MineBlock:
　　def open_mine(self, x, y):
        # 踩到雷了
        if self._block[y][x].value:
            self._block[y][x].status = BlockStatus.bomb
            return False

        # 先把状态改为 opened
        self._block[y][x].status = BlockStatus.opened

        around = _get_around(x, y)

        _sum = 0
        for i, j in around:
            if self._block[j][i].value:
                _sum += 1
        self._block[y][x].around_mine_count = _sum

        # 如果周围没有雷，那么将周围8个未中未点开的递归算一遍
        # 这就能实现一点出现一大片打开的效果了
        if _sum == 0:
            for i, j in around:
                if self._block[j][i].around_mine_count == -1:
                    self.open_mine(i, j)

        return True


def _get_around(x, y):
    """返回(x, y)周围的点的坐标"""
    # 这里注意，range 末尾是开区间，所以要加 1
    return [(i, j) for i in range(max(0, x - 1), min(BLOCK_WIDTH - 1, x + 1) + 1)
            for j in range(max(0, y - 1), min(BLOCK_HEIGHT - 1, y + 1) + 1) if i != x or j != y]