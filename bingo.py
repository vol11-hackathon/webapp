from random import randint, sample

def make_number(number_order: list[int], opened: int) -> tuple[int, int]: 
    """
    がちゃがちゃ
    まだ発表されていない数字が1つ発表される
    """
    x = number_order[opened]
    return x, opened + 1

def make_bingo() -> tuple[tuple[tuple[int]], tuple[tuple[int]]]: 
    """
    ind_to_num: bingoのインデックスに対応する番号
    num_to_ind: bingoの番号に対応するインデックス
    """
    _ind_to_num_list = [[0 for i in range(5)] for _ in range(5)]
    _num_to_ind_list = [(-1, -1) for _ in range(101)]
    bingo_num = set()
    for i in range(5):
        for j in range(5):
            x = randint(j * 20 + 1, j * 20 + 20)
            while x in bingo_num:
                x = randint(j * 20 + 1, j * 20 + 20)
            bingo_num.add(x)
            _ind_to_num_list[i][j] = x
            _num_to_ind_list[x] = (i, j)
    _ind_to_num_tuple = tuple(tuple(x for x in lis) for lis in _ind_to_num_list)
    _num_to_ind_tuple = tuple(pair for pair in _num_to_ind_list)
    return _ind_to_num_tuple, _num_to_ind_tuple

def count(new_number: int, num_to_ind: tuple[tuple[int]], cnt: list[int], cnt_to_ind: tuple[tuple[tuple[int]]]):
    """
    もしビンゴ内に数字があればカウントを増やす
    リーチ、ビンゴがあればそれを示す
    """
    i, j = num_to_ind[new_number]
    if i == -1:
        return
    cnt[i] += 1
    cnt[j + 5] += 1
    if i == j:
        cnt[10] += 1
    if i + j == 4:
        cnt[11] += 1
    print(cnt)
    for k in range(12):
        if cnt[k] == 4:
            for i, j in cnt_to_ind[k]:
                # リーチである目印(色変えるなど)
                pass
    for k in range(12):
        if cnt[k] == 5:
            for i, j in cnt_to_ind[k]:
                # ビンゴである目印(色変えるなど)
                pass

def make_red(new_number: int) -> None:
    # <span>を加えて赤色にする
    pass

if __name__=="__main__":
    ind_to_num, num_to_ind = make_bingo()

    number_order = sample([i for i in range(1, 101)], 100)
    opened = 0

    cnt = [0 for _ in range(12)]
    cnt_to_ind = (((0, 0), (0, 1), (0, 2), (0, 3), (0, 4)),
                ((1, 0), (1, 1), (1, 2), (1, 3), (1, 4)),
                ((2, 0), (2, 1), (2, 2), (2, 3), (2, 4)),
                ((3, 0), (3, 1), (3, 2), (3, 3), (3, 4)),
                ((4, 0), (4, 1), (4, 2), (4, 3), (4, 4)),
                ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0)),
                ((0, 1), (1, 1), (2, 1), (3, 1), (4, 1)),
                ((0, 2), (1, 2), (2, 2), (3, 2), (4, 2)),
                ((0, 3), (1, 3), (2, 3), (3, 3), (4, 3)),
                ((0, 4), (1, 4), (2, 4), (3, 4), (4, 4)),
                ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4)),
                ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0)))
    print(ind_to_num)
    for i in range(50):
        new_number, opened = make_number(number_order, opened)
        print(new_number)
        count(new_number, num_to_ind, cnt, cnt_to_ind)
        make_red(new_number)
