# Saving Challenge
汇率兑换器和存钱挑战的综合应用，生成交互式数据报告, 主要利用dash, forex_python, plotly实现


程序待优化处（仍未实现）:
1. 根据日期查询累计账户金额时，目前采取重复计算saved_money_list的方式；目前我的优化思路是，在加载趋势图时，将计算得到的saved_money_list存储到caeche或另一个Div中；
2. 汇率兑换器与存钱挑战实现分页，并创建一个目录以跳转至不同板块；
