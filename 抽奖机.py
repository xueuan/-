# 创建三个数字列表
num_list1 = ['0', '1', '0', '1', '1', '0', '1', '0', '1', '0']
num_list2 = ['0', '1', '1', '1', '0', '0', '1', '0', '0', '1']
num_list3 = ['1', '0', '1', '1', '0', '1', '1', '0', '1', '1']

# 获取输入的三位数信息，并赋值给 num
num = input('如要抽奖，请输入000-999之间任意三位数：')

# 提取三位数中的百位数
hundreds_digit = num_list1[int(num[0])]
# 提取三位数中的十位数
tens_digit = num_list2[int(num[1])]
# 提取三位数中的个位数
ones_digit = num_list3[int(num[2])]

# 分别从三个数字列表中提取值，并拼接得到兑换码 code
code = (str(hundreds_digit)+str(tens_digit)+str(ones_digit))

# 如果兑换码是 111 或 000，打印兑换码以及"恭喜您中奖了！"
if code == '111' or '000':
    print('恭喜您，中奖了')
else:
    print('很遗憾，你没有中奖')


# 否则，打印兑换码以及"很遗憾您没有中奖。"


