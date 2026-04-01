# 数据字段清单

[English](./DATA_FIELDS.md)

## 适用范围

这份字段清单只针对当前第一阶段。

跟踪指数：

- 上证指数
- 沪深300

已选定个股：

- `601318` 中国平安
- `600900` 长江电力
- `601899` 紫金矿业

主数据源：

- `efinance`

## 设计原则

下面每个字段都分成三类：

- `必须有`：第一版 MVP 不能缺
- `建议有`：如果能拿到，最好一起存
- `暂缓`：第一版先不需要

## 1. 指数基础信息

用途：

- 标识跟踪指数
- 为图表和分析结果提供标签

### 必须有

- `index_code`：指数代码
- `index_name`：指数名称
- `market`：市场或交易所标记，如果可用

### 建议有

- `publisher`：指数发布方，如果可用
- `base_date`：指数基日，如果可用

### 暂缓

- `constituent_count`：成分数量
- `index_category`：指数类别

## 2. 指数日线历史行情

用途：

- 长期趋势图
- 多窗口收益率计算
- 均线计算
- 作为个股对比基准

### 必须有

- `trade_date`：交易日期
- `index_code`：指数代码
- `open`：开盘价
- `high`：最高价
- `low`：最低价
- `close`：收盘价

### 建议有

- `volume`：成交量
- `amount`：成交额
- `change_pct`：涨跌幅
- `change_amount`：涨跌额

### 暂缓

- `turnover_rate`：换手率
- `amplitude`：振幅
- 分时字段

## 3. 个股基础信息

用途：

- 标识选定个股
- 给图表和输出结果打标签
- 支撑后续筛选和报告

### 必须有

- `stock_code`：股票代码
- `stock_name`：股票名称
- `market`：交易所标记，例如上交所或深交所

### 建议有

- `listing_date`：上市日期
- `total_market_value`：总市值
- `float_market_value`：流通市值
- `pe_ratio`：市盈率
- `pb_ratio`：市净率

### 暂缓

- `industry`：行业
- `sector`：板块
- `main_business`：主营业务
- 更细的股东结构数据

## 4. 个股日线历史行情

用途：

- 个股长期趋势图
- 均线计算
- 相对指数强弱计算
- 用成交量辅助解释走势

### 必须有

- `trade_date`：交易日期
- `stock_code`：股票代码
- `open`：开盘价
- `high`：最高价
- `low`：最低价
- `close`：收盘价

### 建议有

- `volume`：成交量
- `amount`：成交额
- `change_pct`：涨跌幅
- `change_amount`：涨跌额
- `turnover_rate`：换手率
- `adjustment_flag`：复权标记，或者至少明确当前使用的是哪种复权方式

### 暂缓

- 分时字段
- 盘口级数据
- 资金流明细

## 5. 第一版需要计算的派生指标

这些不是原始字段，但它们决定了为什么要采集上面的原始字段。

### 指数指标

- `return_20d`
- `return_60d`
- `return_120d`
- `ma_20`
- `ma_60`
- `ma_120`
- `ma_250`
- `trend_label`

### 个股指标

- `return_20d`
- `return_60d`
- `return_120d`
- `ma_20`
- `ma_60`
- `ma_120`
- `ma_250`
- `relative_strength_vs_sse`
- `relative_strength_vs_csi300`
- `trend_label`

## 6. 对 efinance 的验证清单

正式实现前，先验证下面几点：

1. 这两个跟踪指数能否稳定查询到。
2. 这三只选定个股能否稳定查询到。
3. 日期字段能否稳定返回并统一格式。
4. 价格字段是否为可直接计算的数值型。
5. 三只股票能否统一使用同一种复权方式。

## 7. 当前建议的最小数据库表

- `indices`
- `index_prices`
- `stocks`
- `daily_prices`

这 4 张表已经足够支撑当前 MVP，板块相关表以后再加即可，不会影响当前核心结构。
