
# pysnowball
> 雪球APP Python API

## 快速指引

安装


示例

```python
>>> import pysnowball as ball
>>> ball.set_token()
>>> ball.cash_flow('SH600000')
```


## APIs

### 实时行情

获取某支股票的行情数据

```python
import pysnowball as ball
ball.quotec('SZ002027')
```

结果显示：

```json
{
    "data": {
        "market": {
            "region": "CN",/*地区*/
            "status": "交易中",
            "status_id": 5,
            "time_zone": "Asia/Shanghai",
            "time_zone_desc": null
        },
        "others": {
            "cyb_switch": true,
            "pankou_ratio": -24.62/*委比*/
        },
        "quote": {
            "amount": 1062973468.0,/*成交额*/
            "amplitude": 3.79,/*振幅，高低位的价差*/
            "avg_price": 11.136,
            "chg": -0.15,/*股价变动*/
            "code": "002027",
            "currency": "CNY",
            "current": 11.19,/*当前股价*/
            "current_year_percent": 13.37,
            "delayed": 0,
            "exchange": "SZ",
            "float_market_capital": 164245480333.0,
            "float_shares": 14677880280,
            "high": 11.33,/*今日最高价*/
            "issue_date": 1091548800000,/*发行日期*/
            "last_close": 11.34,/*昨收*/
            "lock_set": null,
            "lot_size": 100,
            "low": 10.9,/*最低*/
            "market_capital": 164245480333.0,
            "name": "分众传媒",
            "open": 11.2,/*今开*/
            "percent": -1.32,/*当前涨跌幅*/
            "status": 1,
            "sub_type": "2",
            "symbol": "SZ002027",
            "tick_size": 0.01,
            "time": 1610428086000,
            "timestamp": 1610428086000,
            "total_shares": 14677880280,
            "turnover_rate": 0.65,/*换手率*/
            "type": 11,
            "volume": 95458021/*成交量*/
        },
        "tags": [
            {
                "description": "深股通",
                "value": 3
            },
            {
                "description": "融",
                "value": 6
            },
            {
                "description": "空",
                "value": 7
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 实时分笔

获取实时分笔数据，可以实时取得股票当前报价和成交信息

- 关于分笔数据和逐笔数据，可以参考[这里](https://www.cnblogs.com/chuncn/archive/2009/03/13/1410144.html)
- 总结，分笔数据没啥用

```python
import pysnowball as ball
ball.pankou('SZ002027')
```

结果显示：

```json
{
    "data": {
        "ask1_order_list": null,
        "bc1": 53529,
        "bc10": null,
        "bc2": 362000,
        "bc3": 35900,
        "bc4": 137400,
        "bc5": 18200,
        "bc6": null,
        "bc7": null,
        "bc8": null,
        "bc9": null,
        "bid1_order_list": null,
        "bn1": null,
        "bn10": null,
        "bn2": null,
        "bn3": null,
        "bn4": null,
        "bn5": null,
        "bn6": null,
        "bn7": null,
        "bn8": null,
        "bn9": null,
        "bp1": 11.29,
        "bp10": null,
        "bp2": 11.28,
        "bp3": 11.27,
        "bp4": 11.26,
        "bp5": 11.25,
        "bp6": null,
        "bp7": null,
        "bp8": null,
        "bp9": null,
        "buypct": 34.51,
        "current": 11.29,
        "diff": -545053,
        "level": 1,
        "ratio": -30.98,
        "sc1": 139641,
        "sc10": null,
        "sc2": 477761,
        "sc3": 152300,
        "sc4": 227260,
        "sc5": 155120,
        "sc6": null,
        "sc7": null,
        "sc8": null,
        "sc9": null,
        "sellpct": 65.49,
        "sn1": null,
        "sn10": null,
        "sn2": null,
        "sn3": null,
        "sn4": null,
        "sn5": null,
        "sn6": null,
        "sn7": null,
        "sn8": null,
        "sn9": null,
        "sp1": 11.3,
        "sp10": null,
        "sp2": 11.31,
        "sp3": 11.32,
        "sp4": 11.33,
        "sp5": 11.34,
        "sp6": null,
        "sp7": null,
        "sp8": null,
        "sp9": null,
        "symbol": "SZ002027",
        "timestamp": 1610435043000
    },
    "error_code": 0,
    "error_description": null
}
```

### 业绩预告

按年度获取业绩预告数据

关于返回值的参数指标可以参考 [一文教你看四个指标PE/PB/ROE/股息率](https://zhuanlan.zhihu.com/p/61254326)

```python
import pysnowball as ball
ball.earningforecast('SZ002027')
```

结果显示：

```json
{
    "list": [
        {
            "eps": 0.26,
            "forecast_year": "2020",
            "pb": null,
            "pe": 42.0,
            "roe": null
        },
        {
            "eps": 0.36,
            "forecast_year": "2021",
            "pb": null,
            "pe": 30.0,
            "roe": null
        },
        {
            "eps": 0.44,
            "forecast_year": "2022",
            "pb": null,
            "pe": 25.0,
            "roe": null
        }
    ]
}
```

### 机构评级

获取机构评级数据

```python
import pysnowball as ball
ball.report('SZ002027')
```

结果显示：

```json
{
    "list": [
        {
            "like_count": 6,
            "liked": false,
            "pub_date": 1608566400000,
            "rating_desc": "买入",
            "reply_count": 1,
            "retweet_count": 1,
            "rpt_comp": "中原证券",
            "status_id": 166374866,
            "target_price_max": null,
            "target_price_min": null,
            "title": "全年净利润高增 梯媒广告景气度持续"
        },
        {
            "like_count": 3,
            "liked": false,
            "pub_date": 1608566400000,
            "rating_desc": "买入",
            "reply_count": 0,
            "retweet_count": 0,
            "rpt_comp": "西南证券",
            "status_id": 166355133,
            "target_price_max": null,
            "target_price_min": null,
            "title": "2020年度业绩预告点评：复苏的需求和成本的改善"
        },
        {
            "like_count": 0,
            "liked": false,
            "pub_date": 1608480000000,
            "rating_desc": "买入",
            "reply_count": 0,
            "retweet_count": 0,
            "rpt_comp": "新时代证券",
            "status_id": 166288944,
            "target_price_max": null,
            "target_price_min": null,
            "title": "2020年业绩预告：2020Q4净利同比增长222%-300% 新周期内营收净利有望再创新高"
        }
        ......
    ]
}
```

### 资金流向趋势

获取当日资金流入流出数据，每分钟数据

```python
import pysnowball as ball
ball.capital_flow('SZ002027')
```

结果显示：

```json
{
    "data": {
        "symbol": "SZ002027",
        "items": [
            {
                "timestamp": 1541467800000,
                "amount": -12323447,
                "type": null
            },
            {
                "timestamp": 1541467860000,
                "amount": -12940471,
                "type": null
            },
            {
                "timestamp": 1541467920000,
                "amount": -18710425,
                "type": null
            },
            ...
    ]
}
```

### 资金流向历史

获取历史资金流如流出数据，每日数据，共20个交易日

```python
import pysnowball as ball
ball.capital_history('SZ002027')
```

结果显示：

```json
{
    "data": {
        "items": [
            {
                "amount": 118088050.04999995,
                "timestamp": 1607961600000
            },
            {
                "amount": -152300443.07000005,
                "timestamp": 1608048000000
            },
            {
                "amount": -167809104.43999994,
                "timestamp": 1608134400000
            },
            {
                "amount": 343081418.17999935,
                "timestamp": 1608220800000
            },
            {
                "amount": -261495255.15999985,
                "timestamp": 1608480000000
            },
            {
                "amount": -99425858.97000015,
                "timestamp": 1608566400000
            },
            {
                "amount": 2577557.910000026,
                "timestamp": 1608652800000
            },
            {
                "amount": -39723597.56999999,
                "timestamp": 1608739200000
            },
            {
                "amount": -90937658.67000002,
                "timestamp": 1608825600000
            },
            {
                "amount": 35322662.31,
                "timestamp": 1609084800000
            },
            {
                "amount": -33591085.29999995,
                "timestamp": 1609171200000
            },
            {
                "amount": 21511088.75000003,
                "timestamp": 1609257600000
            },
            {
                "amount": 38125173.20999998,
                "timestamp": 1609344000000
            },
            {
                "amount": 9456633.149999976,
                "timestamp": 1609689600000
            },
            {
                "amount": -107577766.71000004,
                "timestamp": 1609776000000
            },
            {
                "amount": 152165408.3800001,
                "timestamp": 1609862400000
            },
            {
                "amount": 39433181.360000014,
                "timestamp": 1609948800000
            },
            {
                "amount": 15231418.50999999,
                "timestamp": 1610035200000
            },
            {
                "amount": 193131879.3399999,
                "timestamp": 1610294400000
            },
            {
                "amount": -43202581.09000003,
                "timestamp": 1610380800000
            }
        ],
        "sum10": 284683349.6,
        "sum20": -27938879.8300007,
        "sum3": 165160716.75999987,
        "sum5": 356759306.5
    },
    "error_code": 0,
    "error_description": ""
}
```

### 资金成交分布

获取资金成交分布数据

```python
import pysnowball as ball
ball.capital_assort('SZ002027')
```

结果显示：

```json
{
    "data": {
        "buy_large": 195478110.0,
        "buy_medium": 633629590.0,
        "buy_small": 258461911.0,
        "buy_total": 1087569611.0,
        "buy_xlarge": null,
        "created_at": null,
        "sell_large": 158589853.0,
        "sell_medium": 537169632.0,
        "sell_small": 186491982.0,
        "sell_total": 882251467.0,
        "sell_xlarge": null,
        "timestamp": 1610380800000,
        "updated_at": null
    },
    "error_code": 0,
    "error_description": ""
}
```

### 大宗交易

大宗交易数据

```python
import pysnowball as ball
ball.blocktrans('SZ002027')
```

结果显示：

```json
{
    "data": {
        "items": [
            {
                "buy_branch_org_name": "机构专用",
                "premium_rat": 0.0,/*溢价率*/
                "sell_branch_org_name": "机构专用",
                "td_date": 1610380800000,/*成交日期*/
                "trans_amt": 45160000.0,/*成交量*/
                "trans_price": 11.29,/*成交价格*/
                "vol": 4000000.0
            },
            {
                "buy_branch_org_name": "机构专用",
                "premium_rat": 0.0,
                "sell_branch_org_name": "机构专用",
                "td_date": 1610380800000,
                "trans_amt": 19870400.0,
                "trans_price": 11.29,
                "vol": 1760000.0
            },
           ......
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 融资融券

融资融券数据

```python
import pysnowball as ball
ball.margin('SZ002027')
```

结果显示：

```json
{
    "data": {
        "items": [
            {
                "margin_trading_amt_balance": 960745756,
                "short_selling_amt_balance": 2888439,
                "margin_trading_balance": 957857317,
                "td_date": 1541347200000
            },
            {
                "margin_trading_amt_balance": 948660728,
                "short_selling_amt_balance": 2767982,
                "margin_trading_balance": 945892746,
                "td_date": 1541088000000
            },
            ...
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 业绩指标

按年度、季度获取业绩报表数据。

```python
import pysnowball as ball
ball.indicator('SZ002027')
# or
ball.indicator(symbol='SZ002027',is_annals=1,count=10)
```

输入参数：

* symbol -> 股票代码
* is_annals -> 只获取年报,默认为1
* count -> 返回数据数量,默认5条

结果显示：

```json
{
    "data": {
        "currency": "CNY",
        "currency_name": "人民币",
        "last_report_name": "2020三季报",
        "list": [
            {
                "avg_roe": [
                    13.76,
                    -0.7067348678601876
                ],
                "basic_eps": [
                    0.13,
                    -0.675
                ],
                "capital_reserve": [
                    0.0264,
                    1.078740157480315
                ],
                "ctime": 1587995194000,
                "gross_selling_rate": [
                    45.2074,
                    -0.3172397440370201
                ],
                "net_interest_of_total_assets": [
                    9.839,
                    -0.7063353251234173
                ],
                "np_per_share": [
                    0.9387,
                    -0.029767441860465167
                ],
                "operate_cash_flow_ps": [
                    0.2337,
                    -0.09313154831199066
                ],
                "report_date": 1577721600000,
                "report_name": "2019年报",
                "undistri_profit_ps": [
                    0.9915,
                    0.021954236239950627
                ]
            },
            {
                "avg_roe": [
                    46.92,
                    -0.30643015521064304
                ],
                "basic_eps": [
                    0.4,
                    -0.18367346938775503
                ],
                "capital_reserve": [
                    0.0127,
                    -0.16447368421052636
                ],
                "ctime": 1587994241000,
                "gross_selling_rate": [
                    66.2127,
                    -0.08954316758955348
                ],
                "net_interest_of_total_assets": [
                    33.5042,
                    -0.22362570009755603
                ],
                "np_per_share": [
                    0.9675,
                    0.1409198113207548
                ],
                "operate_cash_flow_ps": [
                    0.2577,
                    -0.2416127133608005
                ],
                "report_date": 1546185600000,
                "report_name": "2018年报",
                "undistri_profit_ps": [
                    0.9702,
                    0.22515469124889492
                ]
            },
            {
                "avg_roe": [
                    67.65,
                    -0.04354587869362361
                ],
                "basic_eps": [
                    0.49,
                    -0.057692307692307744
                ],
                "capital_reserve": [
                    0.0152,
                    -0.27272727272727265
                ],
                "ctime": 1556096007000,
                "gross_selling_rate": [
                    72.7247,
                    0.03244935334118891
                ],
                "net_interest_of_total_assets": [
                    43.1547,
                    0.19488153548397802
                ],
                "np_per_share": [
                    0.848,
                    -0.0728187185654931
                ],
                "operate_cash_flow_ps": [
                    0.3398,
                    -0.3815070986530761
                ],
                "report_date": 1514649600000,
                "report_name": "2017年报",
                "undistri_profit_ps": [
                    0.7919,
                    -0.05036575128912331
                ]
            },
            {
                "avg_roe": [
                    70.73,
                    -0.033743169398907084
                ],
                "basic_eps": [
                    0.52,
                    -0.9311258278145694
                ],
                "capital_reserve": [
                    0.0209,
                    -0.5743380855397149
                ],
                "ctime": 1524557046000,
                "gross_selling_rate": [
                    70.439,
                    -0.0017389036828762475
                ],
                "net_interest_of_total_assets": [
                    36.1163,
                    -0.3017091703563349
                ],
                "np_per_share": [
                    0.9146,
                    -0.18141949342164146
                ],
                "operate_cash_flow_ps": [
                    0.5494,
                    -0.14035362228133313
                ],
                "report_date": 1483113600000,
                "report_name": "2016年报",
                "undistri_profit_ps": [
                    0.8339,
                    -0.14322408301654174
                ]
            },
            {
                "avg_roe": [
                    73.2,
                    53.62686567164179
                ],
                "basic_eps": [
                    7.55,
                    376.5
                ],
                "capital_reserve": [
                    0.0491,
                    -0.7753888380603843
                ],
                "ctime": 1493281784000,
                "gross_selling_rate": [
                    70.5617,
                    5.896920114554927
                ],
                "net_interest_of_total_assets": [
                    51.721,
                    49.00580102484772
                ],
                "np_per_share": [
                    1.1173,
                    -0.31813743439521547
                ],
                "operate_cash_flow_ps": [
                    0.6391,
                    32.286458333333336
                ],
                "report_date": 1451491200000,
                "report_name": "2015年报",
                "undistri_profit_ps": [
                    0.9733,
                    2.752120277563608
                ]
            },
            {
                "avg_roe": [
                    1.34,
                    1.0596616206589493
                ],
                "basic_eps": [
                    0.02,
                    1.048780487804878
                ],
                "capital_reserve": [
                    0.2186,
                    0.0
                ],
                "ctime": 1461226570000,
                "gross_selling_rate": [
                    10.2309,
                    5.709226834546528
                ],
                "net_interest_of_total_assets": [
                    1.0343,
                    1.0651683552598417
                ],
                "np_per_share": [
                    1.6386,
                    0.013483424047501262
                ],
                "operate_cash_flow_ps": [
                    0.0192,
                    -0.8579881656804734
                ],
                "report_date": 1419955200000,
                "report_name": "2014年报",
                "undistri_profit_ps": [
                    0.2594,
                    0.0917508417508418
                ]
            },
            {
                "avg_roe": [
                    -22.46,
                    -17.637037037037036
                ],
                "basic_eps": [
                    -0.41,
                    -14.666666666666666
                ],
                "capital_reserve": [
                    0.2186,
                    0.0
                ],
                "ctime": 1429096126000,
                "gross_selling_rate": [
                    1.5249,
                    -0.8076151546118618
                ],
                "net_interest_of_total_assets": [
                    -15.8712,
                    -22.277919292130314
                ],
                "np_per_share": [
                    1.6168,
                    -0.20201372094171066
                ],
                "operate_cash_flow_ps": [
                    0.1352,
                    10.013333333333334
                ],
                "report_date": 1388419200000,
                "report_name": "2013年报",
                "undistri_profit_ps": [
                    0.2376,
                    -0.6325394370553664
                ]
            },
            {
                "avg_roe": [
                    1.35,
                    1.1557093425605536
                ],
                "basic_eps": [
                    0.03,
                    1.1666666666666667
                ],
                "capital_reserve": [
                    0.2186,
                    0.0
                ],
                "ctime": 1398591535000,
                "gross_selling_rate": [
                    7.9263,
                    0.11268179010612621
                ],
                "net_interest_of_total_assets": [
                    0.7459,
                    1.1336690441202824
                ],
                "np_per_share": [
                    2.0261,
                    0.013050000000000006
                ],
                "operate_cash_flow_ps": [
                    -0.015,
                    0.625
                ],
                "report_date": 1356883200000,
                "report_name": "2012年报",
                "undistri_profit_ps": [
                    0.6466,
                    0.04374495560936223
                ]
            },
            {
                "avg_roe": [
                    -8.67,
                    -6.818791946308725
                ],
                "basic_eps": [
                    -0.18,
                    -7.0
                ],
                "capital_reserve": [
                    0.2186,
                    -0.000914076782449752
                ],
                "ctime": 1366735234000,
                "gross_selling_rate": [
                    7.1236,
                    0.02710652286752404
                ],
                "net_interest_of_total_assets": [
                    -5.5802,
                    -7.043756092277699
                ],
                "np_per_share": [
                    2.0,
                    -0.08256880733944962
                ],
                "operate_cash_flow_ps": [
                    -0.04,
                    -1.3636363636363635
                ],
                "report_date": 1325260800000,
                "report_name": "2011年报",
                "undistri_profit_ps": [
                    0.6195,
                    -0.22630198576245775
                ]
            },
            {
                "avg_roe": [
                    1.49,
                    1.148554336989033
                ],
                "basic_eps": [
                    0.03,
                    1.1304347826086956
                ],
                "capital_reserve": [
                    0.2188,
                    0.0
                ],
                "ctime": 1335277353000,
                "gross_selling_rate": [
                    6.9356,
                    1.510715320011584
                ],
                "net_interest_of_total_assets": [
                    0.9233,
                    1.1375575453285858
                ],
                "np_per_share": [
                    2.18,
                    0.018691588785046745
                ],
                "operate_cash_flow_ps": [
                    0.11,
                    -0.75
                ],
                "report_date": 1293724800000,
                "report_name": "2010年报",
                "undistri_profit_ps": [
                    0.8007,
                    0.041764246682279495
                ]
            }
        ],
        "org_type": 1,
        "quote_name": "分众传媒",
        "statuses": null
    },
    "error_code": 0,
    "error_description": ""
}
```

### 利润表

```python
import pysnowball as ball
ball.income('SZ300251')
# or
ball.income(symbol='SZ300251',is_annals=1,count=10)
```

输入参数：

* symbol -> 股票代码
* is_annals -> 只获取年报,默认为1
* count -> 返回数据数量,默认5条

结果显示：

```json
{
    "data": {
        "quote_name": "光线传媒",
        "currency_name": "人民币",
        "org_type": 1,
        "last_report_name": "2018三季报",
        "currency": "CNY",
        "list": [
            {
                "report_date": 1514649600000,
                "report_name": "2017年报",
                "net_profit": [
                    815156857.46,
                    0.10020849906436384
                ],
                "net_profit_atsopc": [
                    815156857.46,
                    0.10020849906436384
                ],
                "total_revenue": [
                    1843452761.05,
                    0.06477235336668148
                ],
                "op": [
                    672007490.01,
                    -0.1544941646451226
                ]
            },
            {
                "report_date": 1483113600000,
                "report_name": "2016年报",
                "net_profit": [
                    740911252.87,
                    0.8426691031822198
                ],
                "net_profit_atsopc": [
                    740911252.87,
                    0.8426691031822198
                ],
                "total_revenue": [
                    1731311632.22,
                    0.13655725191234208
                ],
                "op": [
                    794799351.95,
                    0.8342603099386635
                ]
            },
            ...
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 资产负债表

```python
import pysnowball as ball
ball.balance('SZ300251')
# or
ball.balance(symbol='SZ300251',is_annals=1,count=10)
```

输入参数：

* symbol -> 股票代码
* is_annals -> 只获取年报,默认为1
* count -> 返回数据数量,默认5条

结果显示：

```json
{
    "data": {
        "quote_name": "光线传媒",
        "currency_name": "人民币",
        "org_type": 1,
        "last_report_name": "2018三季报",
        "currency": "CNY",
        "list": [
            {
                "report_date": 1514649600000,
                "report_name": "2017年报",
                "total_assets": [
                    11884462717.67,
                    0.2989175670473065
                ],
                "total_liab": [
                    3429697781.5,
                    0.6877450604731051
                ],
                "asset_liab_ratio": [
                    0.288586691967208,
                    0.2993473206384294
                ]
            },
            {
                "report_date": 1483113600000,
                "report_name": "2016年报",
                "total_assets": [
                    9149512655.13,
                    0.11726415171002368
                ],
                "total_liab": [
                    2032118393.84,
                    0.6680466814500612
                ],
                "asset_liab_ratio": [
                    0.2221012714486624,
                    0.49297431488967003
                ]
            },
            ...
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 现金流量表

```python
import pysnowball as ball
ball.cash_flow('SZ300251')
# or
ball.cash_flow(symbol='SZ300251',is_annals=1,count=10)
```

输入参数：

* symbol -> 股票代码
* is_annals -> 只获取年报,默认为1
* count -> 返回数据数量,默认5条

结果显示：

```json
{
    "data": {
        "quote_name": "光线传媒",
        "currency_name": "人民币",
        "org_type": 1,
        "last_report_name": "2018三季报",
        "currency": "CNY",
        "list": [
            {
                "report_date": 1538236800000,
                "report_name": "2018三季报",
                "ncf_from_oa": [
                    -299512204.39,
                    -15.69337270939856
                ],
                "ncf_from_ia": [
                    701876463.13,
                    2.493053545204141
                ],
                "ncf_from_fa": [
                    -1605703920.9,
                    -10.364167402276724
                ]
            },
            {
                "report_date": 1530288000000,
                "report_name": "2018中报",
                "ncf_from_oa": [
                    -181196373.81,
                    -1.7290892286108568
                ],
                "ncf_from_ia": [
                    2347407590.16,
                    3.905172712067323
                ],
                "ncf_from_fa": [
                    -586721686.4,
                    -4.271754192732585
                ]
            },
            ...
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 主营业务构成

```python
import pysnowball as ball
ball.business('SZ300251')
# or
ball.business(symbol='SZ300251',count=10)
```

输入参数：

* symbol -> 股票代码
* count -> 返回数据数量,默认5条

结果显示：

```json
{
    "data": {
        "quote_name": "光线传媒",
        "currency": "CNY",
        "list": [
            {
                "report_date": 1530288000000,
                "report_name": "2018中报",
                "class_list": [
                    {
                        "class_standard": 2,
                        "business_list": [
                            {
                                "project_announced_name": "电影及衍生品",
                                "prime_operating_income": 472496159.52,
                                "income_ratio": 0.6554,
                                "gross_profit_rate": 0.4880141511292849
                            },
                            {
                                "project_announced_name": "电视剧",
                                "prime_operating_income": 235946734.18,
                                "income_ratio": 0.3273,
                                "gross_profit_rate": 0.41673913085394504
                            },
                            {
                                "project_announced_name": "游戏及其他",
                                "prime_operating_income": 12491524.81,
                                "income_ratio": 0.0173,
                                "gross_profit_rate": 0.34024031450488706
                            }
                        ]
                    }
                ]
            },
            {
                "report_date": 1514649600000,
                "report_name": "2017年报",
                "class_list": [
                    {
                        "class_standard": 1,
                        "business_list": [
                            {
                                "project_announced_name": "传媒",
                                "prime_operating_income": 1843452761.05,
                                "income_ratio": 1,
                                "gross_profit_rate": 0.4127651986897655
                            }
                        ]
                    },
                    {
                        "class_standard": 2,
                        "business_list": [
                            {
                                "project_announced_name": "电影及衍生品",
                                "prime_operating_income": 1238167750.17,
                                "income_ratio": 0.6717,
                                "gross_profit_rate": 0.44010894038807064
                            },
                            {
                                "project_announced_name": "视频直播",
                                "prime_operating_income": 491462820.98,
                                "income_ratio": 0.2666,
                                "gross_profit_rate": 0.33240443566869143
                            },
                            {
                                "project_announced_name": "游戏及其他",
                                "prime_operating_income": 63316334.3,
                                "income_ratio": 0.0343,
                                "gross_profit_rate": null
                            },
                            {
                                "project_announced_name": "电视剧",
                                "prime_operating_income": 50505855.6,
                                "income_ratio": 0.0274,
                                "gross_profit_rate": null
                            }
                        ]
                    },
                    {
                        "class_standard": 3,
                        "business_list": [
                            {
                                "project_announced_name": "华北地区",
                                "prime_operating_income": 1649889742.63,
                                "income_ratio": 0.895,
                                "gross_profit_rate": 0.5114414396715438
                            },
                            {
                                "project_announced_name": "华东地区",
                                "prime_operating_income": 71027506.05,
                                "income_ratio": 0.0385,
                                "gross_profit_rate": null
                            },
                            {
                                "project_announced_name": "华南地区",
                                "prime_operating_income": 62321110.18,
                                "income_ratio": 0.0338,
                                "gross_profit_rate": null
                            },
                            {
                                "project_announced_name": "其他收入之和",
                                "prime_operating_income": 60214402.19,
                                "income_ratio": 0.0327,
                                "gross_profit_rate": null
                            }
                        ]
                    }
                ]
            },
            ...
        ],
        "currency_code": "人民币"
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 十大股东

```python
import pysnowball as ball
ball.top_holders('SZ300251')
# or
ball.top_holders(symbol='SZ300251',circula=0)
```

输入参数：

* symbol -> 股票代码
* circula -> 只获取流通股,默认为1

结果显示：

```json
{
    "data": {
        "times": [
            {
                "name": "2018三季报",
                "value": 1538236800000
            },
            {
                "name": "2018中报",
                "value": 1530288000000
            },
            {
                "name": "2018一季报",
                "value": 1522425600000
            },
            {
                "name": "2017年报",
                "value": 1514649600000
            }
        ],
        "items": [
            {
                "chg": 133.92,
                "held_num": 763106985,
                "held_ratio": 10.96,
                "holder_name": "香港中央结算有限公司"
            },
            {
                "chg": 0,
                "held_num": 406609165,
                "held_ratio": 5.84,
                "holder_name": "Power Star Holdings(Hong Kong)Limited"
            },
            {
                "chg": -0.74,
                "held_num": 367792435,
                "held_ratio": 5.28,
                "holder_name": "Glossy City(HK)Limited"
            },
            {
                "chg": 0,
                "held_num": 259994273,
                "held_ratio": 3.73,
                "holder_name": "关玉婵"
            },
            {
                "chg": 0,
                "held_num": 247236384,
                "held_ratio": 3.55,
                "holder_name": "Gio2 Hong Kong Holdings Limited"
            },
            {
                "chg": 0,
                "held_num": 150837758,
                "held_ratio": 2.17,
                "holder_name": "Giovanna Investment Hong Kong Limited"
            },
            {
                "chg": -48.51,
                "held_num": 89849744,
                "held_ratio": 1.29,
                "holder_name": "易贤忠"
            },
            {
                "chg": -17.67,
                "held_num": 83437464,
                "held_ratio": 1.2,
                "holder_name": "全国社保基金四一三组合"
            },
            {
                "chg": null,
                "held_num": 72810935,
                "held_ratio": 1.05,
                "holder_name": "全国社保基金四一四组合"
            },
            {
                "chg": null,
                "held_num": 57580177,
                "held_ratio": 0.83,
                "holder_name": "挪威中央银行-自有资金"
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 主要指标

```python
import pysnowball as ball
ball.main_indicator('SZ300251')
```

输入参数：

* symbol -> 股票代码

结果显示：

```json
{
    "data": {
        "items": [
            {
                "asset_liab_ratio": 25.8594,
                "net_profit_atsopc_yoy": 22.8065,
                "operating_income_yoy": 24.5947,
                "basic_eps": 0.3277,
                "net_selling_rate": 44.0267,
                "avg_roe": 40.2459,
                "gross_selling_rate": 69.2402,
                "float_shares": 6964888862,
                "pb": 6.826,
                "np_per_share": 0.9217,
                "float_market_capital": 43739502053,
                "total_revenue": 10876591720.34,
                "market_capital": 92177088158,
                "pe_ttm": 13.363,
                "dividend": 0.083,
                "currency": "CNY",
                "dividend_yield": 1.322,
                "net_profit_atsopc": 4809760827.29,
                "total_shares": 14677880280,
                "report_date": "2018三季报"
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 股东人数

```python
import pysnowball as ball
ball.holders('SZ002027')
```

输入参数：

* symbol -> 股票代码

结果显示：

```json
{
    "data": {
        "items": [
            {
                "chg": 70.34,
                "price": 8.51,
                "ashare_holder": 134296,
                "timestamp": 1538236800000
            },
            {
                "chg": 12.68,
                "price": 9.57,
                "ashare_holder": 78838,
                "timestamp": 1530288000000
            },
            {
                "chg": 26.9,
                "price": 10.6423,
                "ashare_holder": 69964,
                "timestamp": 1522425600000
            },
            {
                "chg": -0.69,
                "price": 11.6248,
                "ashare_holder": 55132,
                "timestamp": 1514649600000
            },
            {
                "chg": -5.17,
                "price": 8.2976,
                "ashare_holder": 55515,
                "timestamp": 1506700800000
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 机构持仓

```python
import pysnowball as ball
ball.org_holding_change('SZ002027')
```

输入参数：

* symbol -> 股票代码

结果显示：

```json
{
    "data": {
        "items": [
            {
                "chg_date": "2018三季报",
                "institution_num": "202",
                "chg": -8.55,
                "held_ratio": 46.7108,
                "price": 8.51,
                "timestamp": 1538236800000
            },
            {
                "chg_date": "2018中报",
                "institution_num": "726",
                "chg": 5.68,
                "held_ratio": 55.2636,
                "price": 9.57,
                "timestamp": 1530288000000
            },
            {
                "chg_date": "2018一季报",
                "institution_num": "257",
                "chg": -12.08,
                "held_ratio": 49.5791,
                "price": 10.6423,
                "timestamp": 1522425600000
            },
            {
                "chg_date": "2017年报",
                "institution_num": "631",
                "chg": 4.75,
                "held_ratio": 61.6559,
                "price": 11.6248,
                "timestamp": 1514649600000
            },
            {
                "chg_date": "2017三季报",
                "institution_num": "119",
                "chg": -10.52,
                "held_ratio": 56.9054,
                "price": 8.2976,
                "timestamp": 1506700800000
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 分红融资

```python
import pysnowball as ball
ball.bonus('SZ002027')
```

输入参数：

* symbol -> 股票代码
* page -> 第几页 默认1
* size -> 每页含有多少数据 默认10

结果显示：

```json
{
    "data": {
        "addtions": [
            {
                "actual_issue_vol": 252525252,
                "actual_issue_price": 19.8,
                "listing_ad": 1460563200000,
                "actual_rc_net_amt": 4860797464
            },
            {
                "actual_issue_vol": 3813556382,
                "actual_issue_price": 10.46,
                "listing_ad": 1451232000000,
                "actual_rc_net_amt": 39889800000
            }
        ],
        "allots": [],
        "items": [
            {
                "dividend_year": "2018中报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2017年报",
                "ashare_ex_dividend_date": 1530201600000,
                "plan_explain": "10转2股派1元(含税)",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2017中报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2016年报",
                "ashare_ex_dividend_date": 1499270400000,
                "plan_explain": "10转4股派4.08元(含税)",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2016中报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2015年报",
                "ashare_ex_dividend_date": 1467216000000,
                "plan_explain": "10转10股派2.5元(含税)",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2015中报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2014年报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2014中报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2013年报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 行业对比

```python
import pysnowball as ball
ball.industry_compare('SZ002027')
```

输入参数：

* symbol -> 股票代码

结果显示：

```json
{
    "data": {
        "ind_name": "营销服务",
        "quote_time": 1541487843000,
        "avg": {
            "pe_ttm": 18.075806451612905,
            "basic_eps": 0.14168064516129034,
            "avg_roe": 5.092969999999999,
            "gross_selling_rate": 19.05175483870968,
            "total_revenue": 3573300766.253226,
            "net_profit_atsopc": 266114972.18451613,
            "np_per_share": 4.066348387096774,
            "operate_cash_flow_ps": 0.0033032258064516146,
            "total_assets": 5442324297.112904,
            "total_shares": 1270069773.387097
        },
        "min": {
            "pe_ttm": -72.467,
            "basic_eps": -1.68,
            "avg_roe": -14.8514,
            "gross_selling_rate": -73.3425,
            "total_revenue": 105006980.06,
            "net_profit_atsopc": -497734761.09,
            "np_per_share": -1.6479,
            "operate_cash_flow_ps": -1.6162,
            "total_assets": 571320095.1,
            "total_shares": 93338000
        },
        "max": {
            "pe_ttm": 90.347,
            "basic_eps": 0.53,
            "avg_roe": 40.2459,
            "gross_selling_rate": 69.2402,
            "total_revenue": 17002184291.88,
            "net_profit_atsopc": 4809760827.29,
            "np_per_share": 10.3348,
            "operate_cash_flow_ps": 0.7028,
            "total_assets": 18485532791.55,
            "total_shares": 14677880280
        },
        "count": 1,
        "ind_code": "S720201",
        "ind_class": "SW2014",
        "report_name": "2018三季报",
        "items": [
            {
                "symbol": "SZ002027",
                "name": "分众传媒",
                "basic_eps": 0.3277,
                "total_revenue": 10876591720.34,
                "gross_selling_rate": 69.2402,
                "net_profit_atsopc": 4809760827.29,
                "np_per_share": 0.9217,
                "avg_roe": 40.2459,
                "pe_ttm": 13.363,
                "total_assets": 18485532791.55,
                "operate_cash_flow_ps": 0.1063,
                "total_shares": 14677880280
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```
