# 推荐架构

[English](./ARCHITECTURE.md)

## 设计原则

第一版实现应坚持 Python 优先、可视化优先。

这意味着：

- 先保证分析质量，再考虑 UI 打磨
- 先保证本地数据稳定，再考虑部署
- 先用可解释规则，再考虑复杂模型

## 推荐技术栈

- 语言：Python
- 数据处理：pandas、numpy
- 存储：SQLite
- 可视化：plotly、matplotlib 或 pyecharts
- 原型与验证：Jupyter
- 后续本地应用：Streamlit

## 逻辑模块

### 1. 数据采集层

职责：

- 获取个股基础信息
- 获取个股日线行情
- 获取跟踪指数行情

建议输出：

- 规范化后的原始表，存入 SQLite

### 2. 数据存储层

职责：

- 设计数据表结构
- 约束主键
- 保持更新历史一致

建议的核心表：

- `stocks`
- `indices`
- `daily_prices`
- `index_prices`

### 3. 分析引擎

职责：

- 计算指数多窗口收益率
- 计算指数均线结构
- 计算个股均线
- 计算相对强弱
- 生成趋势标签

建议输出：

- 分析结果表
- 可缓存的中间指标

### 4. 可视化层

职责：

- 绘制指数趋势图
- 绘制个股趋势图
- 导出可阅读结果

可接受形式：

- notebook 图表
- 保存为 html 的交互图
- png 静态图片

## 推荐项目结构

```text
Quant for CN_A/
├── README.md
├── README.zh-CN.md
├── docs/
│   ├── MVP.md
│   ├── MVP.zh-CN.md
│   ├── ROADMAP.md
│   ├── ROADMAP.zh-CN.md
│   ├── ARCHITECTURE.md
│   ├── ARCHITECTURE.zh-CN.md
│   ├── TASKS_PHASE1.md
│   └── TASKS_PHASE1.zh-CN.md
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
├── src/
│   ├── data/
│   ├── analysis/
│   ├── visualization/
│   └── utils/
├── outputs/
│   ├── charts/
│   └── reports/
└── tests/
```

## 后续扩展方向

等第一版稳定后，这套架构可以继续扩展到：

- 板块和行业分析
- 回测
- 自选股
- 预警
- 云端部署
- 更高级的因子模型

关键是从一开始就把数据、分析、可视化分开。
