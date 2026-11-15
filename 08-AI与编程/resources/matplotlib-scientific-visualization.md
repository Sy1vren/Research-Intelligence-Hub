---
resource_id: "08-004"
title: "Matplotlib 官方绘图教程"
module: "08-AI与编程"
category: "科学绘图/结果表达"
source_type: "官方文档与教程"
maintainer: "Matplotlib Project"
source_url: "https://matplotlib.org/stable/tutorials/"
version: "Stable documentation; consult release notes for installed version"
status: "REVIEWED"
review_date: "2026-11-15"
license_status: "待单独核对具体文档与代码示例的许可及引用要求"
---

# Matplotlib 官方绘图教程

## 资源定位
Matplotlib 是 Python 科学绘图的基础工具，适合制作可复现的二维图表，并可支持部分三维可视化。

## 核心能力
- 折线图、散点图、柱状图、直方图和箱线图
- 多子图布局、坐标轴和图例控制
- 误差棒、注释、颜色映射和色标
- 数学公式、中文字体与出版级图片导出
- 与 NumPy、Pandas、SciPy 工作流集成

## 对道路桥梁科研的用途
- 绘制桥梁振动时程曲线
- 对比滤波前后的信号
- 展示 FFT 幅值谱或功率谱密度
- 绘制不同工况、测点和模型预测结果的对比图
- 生成论文、竞赛答辩和技术报告中的规范图表

## 推荐学习顺序
1. Pyplot tutorial：快速掌握基础绘图
2. Figure/Axes：理解面向对象绘图结构
3. Labels、legends、ticks：规范图表标注
4. Subplots：组织多图对比
5. Annotations 和 error bars：表达关键结果与不确定性
6. Savefig：控制尺寸、分辨率和输出格式

## 图表质量检查
- 每个坐标轴标明物理量和单位。
- 图例、线型和颜色应便于区分且不造成误读。
- 频谱图应标明频率单位和幅值/功率定义。
- 不得通过截断坐标轴或选择性展示误导读者。
- 导出后检查字体、符号、图例遮挡和分辨率。

## 核验记录
已检查 Matplotlib 官方稳定版教程入口及 SciPy 生态官方入门页面对其用途的介绍。未逐项运行所有示例，也未核对每个示例的独立许可要求。

## 来源
- 官方教程：https://matplotlib.org/stable/tutorials/
- 官方文档：https://matplotlib.org/stable/
