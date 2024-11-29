class MineBlock:
����def open_mine(self, x, y):
        # �ȵ�����
        if self._block[y][x].value:
            self._block[y][x].status = BlockStatus.bomb
            return False

        # �Ȱ�״̬��Ϊ opened
        self._block[y][x].status = BlockStatus.opened

        around = _get_around(x, y)

        _sum = 0
        for i, j in around:
            if self._block[j][i].value:
                _sum += 1
        self._block[y][x].around_mine_count = _sum

        # �����Χû���ף���ô����Χ8��δ��δ�㿪�ĵݹ���һ��
        # �����ʵ��һ�����һ��Ƭ�򿪵�Ч����
        if _sum == 0:
            for i, j in around:
                if self._block[j][i].around_mine_count == -1:
                    self.open_mine(i, j)

        return True


def _get_around(x, y):
    """����(x, y)��Χ�ĵ������"""
    # ����ע�⣬range ĩβ�ǿ����䣬����Ҫ�� 1
    return [(i, j) for i in range(max(0, x - 1), min(BLOCK_WIDTH - 1, x + 1) + 1)
            for j in range(max(0, y - 1), min(BLOCK_HEIGHT - 1, y + 1) + 1) if i != x or j != y]