# 列印空心三角形
# 輸入整數 n，輸出一個 n 層的空心三角形

def print_hollow_triangle(side_length: str) -> None:
    # error handling
    try:
        side_length = int(side_length)
    except ValueError:
        print('Please enter a valid integer')
        return

    if side_length < 2:
        try:
            raise ValueError('Side length must be greater than 1')
        except ValueError as e:
            print(e)
            return

    # 實作
    width = 2 * side_length - 1  # 3 -> 5*5, 4 -> 7*7, 5 -> 9*9

    for i in range(side_length):
        for j in range(width):
            if i == side_length - 1:  # 最後一行
                if j % 2 == 0:  # 間隔印星號
                    print('*', end='')
                else:
                    print(' ', end='')
            elif j == side_length - 1 - i or j == side_length - 1 + i:
                print('*', end='')
            else:
                print(' ', end='')
        print()  # 換行


if __name__ == '__main__':
    user_input_side_length = input('Please enter the side length of the triangle: ')
    print_hollow_triangle(user_input_side_length)
