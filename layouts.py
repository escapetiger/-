import dash_core_components as dcc
import dash_html_components as html
import dash_table
import uuid



def set_layout():
    session_id = str(uuid.uuid4())
    return html.Div([

        html.Div(
            id='Header',
            children=[
                html.H1(children='欢迎参加存钱挑战',
                        style={'textAlign': 'center',
                               'color': 'black',
                               'backgroundColor': '#C1D4FE',
                               'marginBlockStart': '0em',
                               'marginBlockEnd': '0em',
                               })
            ],
        ),
        html.Div(
            id='Input_area',
            children=[
                html.Div(
                    id='Money_per_week',
                    children=[
                        html.Label('每周存入的金额:'),
                        dcc.Input(id='money_per_week', type='text', placeholder='10', value=10),
                    ]
                ),
                html.Div(
                    id='Increment_money',
                    children=[
                        html.Label('每周递增金额:'),
                        dcc.Input(id='increment_money', type='text', placeholder='10', value=10),
                    ]
                ),
                html.Div(
                    id='Begin_date',
                    children=[
                        html.Label('开始日期(yyyy/mm/dd):'),
                        dcc.Input(id='begin_date', type='text', placeholder='2020/1/1', value='2020/1/1'),
                    ]
                ),
                html.Div(
                    id='Total_week',
                    children=[
                        html.Label('总共的周数:'),
                        dcc.Input(id='total_week', type='text', placeholder='10', value=10),
                    ]
                )],
            style={'backgroundColor': '#E5EBF7'}
        ),
        html.Div(id='Graph_container',
                 children=[
                     html.Div(id='graph_area',
                              children=[
                                  html.Div(
                                      id='Total-line-title',
                                      children=[html.H3(children='累计账户金额趋势图',
                                                        style={'textAlign': 'center', 'color': 'black'})],
                                  ),
                                  dcc.Graph(id='line_graph')
                              ])
                ]
        ),
        html.Div(
            id='Query',
            children=[
                html.Div(
                    id='Query_date',
                    children=[
                        html.Label('查询的日期:'),
                        dcc.Input(id='query_date', type='text', placeholder='2020/2/1', value='2020/2/1'),
                    ]
                ),
                html.Div(
                    id='Query_answer',
                    children=[html.H4(id='query_answer')]
                )
            ],
            style={'backgroundColor': '#E5EBF7'}
        ),
        html.Div(
            id='Converter_container',
            children=[
                html.Div(
                    id='Converter_header',
                    children=[
                        html.H1(children='欢迎使用汇率兑换器',
                                style={'textAlign': 'center',
                                       'color': 'black',
                                       'backgroundColor': '#C1D4FE',
                                       'marginBlockStart': '0em',
                                       'marginBlockEnd': '0em',
                                       })
                    ]
                ),

                html.Div(
                    id='Amount',
                    children=[
                        html.Label('金额：'),
                        dcc.Input(id='amount', type='text', placeholder='100', value=100)]
                ),
                html.Div(
                    id='Base_currency',
                    children=[
                        html.Label('待兑换币种：'),
                        dcc.Input(id='base_currency', type='text', placeholder='CNY', value='CNY')]
                ),
                html.Div(
                    id='Target_currency',
                    children=[
                        html.Label('目标币种：'),
                        dcc.Input(id='target_currency', type='text', placeholder='USD', value='USD')]
                ),
                html.Div(
                    id='Convert_result',
                    children=[
                        html.Label('兑换结果：'),
                        html.Div(id='convert_result')
                    ]
                )
            ],
            style={'backgroundColor': '#E5EBF7'}
        ),

        html.Div(id='session_id', children=session_id, style={'display': 'none'}),
    ], style={'backgroundColor': '#E2E9FF'})
