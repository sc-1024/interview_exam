# 國泰國中的老師出了一道題目給同學們練習，同學們自己設定一串奇偶混和地亂數，
# 並將數字依照” 奇數都在偶數前面”，且”偶數升冪排序”，”奇數降冪排序”。
# 例如 ‘417324689435’ 將會變成 ‘975331244468’。
# 然而，班上有50位學生，每一個同學給出的數字長度不一，老師希望能用一段小程式來幫助他驗證答案，請你寫一個函數幫幫老師吧!


def sort_num(nums: str) -> str:
    even = []
    odd = []
    for num in nums:
        if not num.isdigit():
            raise ValueError('請檢查輸入數字是否包含非數字字元')
        if int(num) % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    # solution 2 自己排序
    '''
    for i in range(len(even)):
        for j in range(i, len(even)):
            if even[i] > even[j]:
                even[i], even[j] = even[j], even[i]

    for i in range(len(odd)):
        for j in range(i, len(odd)):
            if odd[i] < odd[j]:
                odd[i], odd[j] = odd[j], odd[i]
    return ''.join(odd + even)
    '''

    # solution 1 用python內建函數排序
    return ''.join(sorted(odd, reverse=True) + sorted(even))


# 測試
if __name__ == '__main__':
    # print(sort_num('417324689435'))  # 975331244468
    random_num = input('請輸入一串奇偶混和地亂數：')
    print(sort_num(random_num))
