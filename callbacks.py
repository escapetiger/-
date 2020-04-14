from save_52_weeks import save_money_in_n_weeks, get_end_date
from dash.dependencies import Input, Output
from app import cache, app
from plots import *
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError


# # # # # # Update line graph # # # # #
@app.callback(
    Output('line_graph', 'figure'),
    [Input('money_per_week', 'value'),
     Input('increment_money', 'value'),
     Input('total_week', 'value'),
     Input('begin_date', 'value')]
)
def line_graph(money_per_week, increment_money, total_week, begin_date):
    try:
        saved_money_list = save_money_in_n_weeks(int(money_per_week), float(increment_money), int(total_week))

        begin_date = datetime.datetime.strptime(begin_date, '%Y/%m/%d')
        end_date = get_end_date(begin_date, total_week)
        time = [begin_date + datetime.timedelta(days=i*7) for i in range(total_week)]

        return plot_time_series(saved_money_list, time)
    except:
        raise ValueError('请输入正确的信息！')


# # # # # # # # # # # END # # # # # # # # # #

# # # # # # Query by date # # # # #
@app.callback(
    Output('query_answer', 'children'),
    [Input('money_per_week', 'value'),
     Input('increment_money', 'value'),
     Input('total_week', 'value'),
     Input('query_date', 'value'),
     Input('begin_date', 'value')]
)
def query_by_date(money_per_week, increment_money, total_week, query_date, begin_date):
    saved_money_list = save_money_in_n_weeks(int(money_per_week), float(increment_money), int(total_week))
    try:
        begin_date = datetime.datetime.strptime(begin_date, '%Y/%m/%d')
        query_date = datetime.datetime.strptime(query_date, '%Y/%m/%d')
        end_date = get_end_date(begin_date, total_week)
        if query_date > end_date:
            return '已超出存钱挑战的日期！'
        week_num = query_date.isocalendar()[1] - begin_date.isocalendar()[1]
        return '第{}周的存款：{}元'.format(week_num, saved_money_list[week_num-1])
    except:
        return '请检查日期格式是否正确！'


# # # # # # # # # # # END # # # # # # # # # #

# # # # # # Converter # # # # #
@app.callback(
    Output('convert_result', 'children'),
    [Input('amount', 'value'),
     Input('base_currency', 'value'),
     Input('target_currency', 'value')]
)
def convert(amount, base, target):
    CRate, CCode = CurrencyRates(), CurrencyCodes()
    try:
        result = CRate.convert(base, target, float(amount))
        return "{} {}({}) is {} {}({})".format(amount, base, CCode.get_symbol(base),
                                              round(result, 2), target, CCode.get_symbol(target))
    except RatesNotAvailableError:
        return 'The base or target currency are not supported, please refer to '\
              'https://forex-python.readthedocs.io/en/latest/currencysource.html'
    except ValueError:
        return 'Please enter correct amount! Only number!'
# # # # # # # # # # # END # # # # # # # # # #



