from random import randint, choice

def make_number(selected_number: set[int], unselected_number: set[int]) -> int:
    """
    がちゃがちゃ
    selected_numberはすでに発表された数字
    unselected_numberはまだ発表されていない数字
    まだ発表されていない数字のうちランダムに数字1つが発表される
    """
    x = choice(list(selected_number))
    unselected_number.add(x)
    selected_number.remove(x)
    return x

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

def make_red(new_number: int) -> None:
    # <span>を加えて赤色にする
    pass

if __name__=="__main__":
    ind_to_num, num_to_ind = make_bingo()
    selected_number = set(i for i in range(1, 101))
    unselected_number = set()
    new_number = make_number(selected_number, unselected_number)
