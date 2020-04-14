"""
作者：Escape
功能：52周存钱挑战
版本：5.0
日期：2020-04-20
"""

import math
import datetime


def get_end_date(begin_date, week):
    """
    根据开始日期和时长，计算结束日期
    """
    if type(begin_date) is str:
        begin_date = datetime.datetime.strptime(begin_date, '%Y/%m/%d')
    end_date = begin_date + datetime.timedelta(days=week*7)
    return end_date

def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    """
    计算 n 周内的存款金额
    """
    money_list = []         # 记录每周存款数的列表
    saved_money_list = []   # 每周的账户累计

    for i in range(total_week):
        # 存钱操作
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)

        # 更新下一周的存钱金额
        money_per_week += increase_money
    return saved_money_list

def main():
    """
    主函数
    """
    money_per_week = int(input('请输入每周存入的金额: '))
    increase_money = float(input('请输入每周的递增金额: '))
    total_week = int(input('请输入总共的周数: '))

    # 调用函数
    saved_money_list = save_money_in_n_weeks(money_per_week, increase_money, total_week)

    # 输出第几周（从2020年的第一周开始）
    input_date_str = input('请输入日期(yyyy/mm/dd): ')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')

    week_num = input_date.isocalendar()[1]
    print('第{}周的存款：{}元'.format(week_num, saved_money_list[week_num-1]))


# if __name__ == "__main__":
#     main()
