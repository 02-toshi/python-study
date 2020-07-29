import os
import sys

args = sys.argv

ERROR_MESSAGE = "エラー：0以上の数を指定してください！"

def make_square(size):
    """
    与えられた引数のサイズの正方形を描き、文字列として返却する

    Parameters
    ----------
    size : int
        1辺のサイズ
    Returns
    ----------
    square : string
        正方形の文字列
    """
    if size < 0:
        return ERROR_MESSAGE
    elif size == 0:
        square = ""
    elif size == 1:
        square = "*"
    else:
        square_area_str = "*"
        square_space = " "
        line_break = os.linesep
        square = ""
        square += square_area_str * size + line_break
        for i in range (size - 2):
            square += square_area_str + (square_space * (size - 2)) + square_area_str + line_break
        square += (square_area_str * size)
    return square


def main():
    size = int(args[1])
    print(make_square(size))
    print("サイズ：" + str(size))

expected_2 = """**
**
""".strip()

expected_5 = """
*****
*   *
*   *
*   *
*****
""".strip()

if __name__ == '__main__':
    actual = make_square(1)
    assert actual == "*"
    actual = make_square(2)
    assert actual == expected_2
    actual = make_square(5)
    assert actual == expected_5, f"{actual}{expected_5}"
    actual = make_square(-1)
    assert actual == ERROR_MESSAGE
    main()
