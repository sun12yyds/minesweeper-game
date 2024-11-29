class MineBlock:
    def __init__(self):
        self._block = [[Mine(i, j) for i in range(BLOCK_WIDTH)] for j in range(BLOCK_HEIGHT)]

        # ÂñÀ×
        for i in random.sample(range(BLOCK_WIDTH * BLOCK_HEIGHT), MINE_COUNT):
            self._block[i // BLOCK_WIDTH][i % BLOCK_WIDTH].value = 1