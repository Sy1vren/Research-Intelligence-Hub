---
resource_id: "08-001"
title: "NumPy 官方文档与学习资源"
module: "08-AI与编程"
category: "科学计算/数值数组"
source_type: "官方文档与教程"
maintainer: "NumPy Project"
source_url: "https://numpy.org/doc/stable/"
learning_url: "https://numpy.org/learn/"
version: "Stable documentation; consult release notes for installed version"
status: "REVIEWED"
review_date: "2026-11-15"
license_status: "待单独核对具体文档与代码示例的许可及引用要求"
---

# NumPy 官方文档与学习资源

## 资源定位
NumPy 是 Python 科学计算的基础数组库，适合处理向量、矩阵、多维数组及批量数值运算。官方学习入口提供 Quickstart、教程和用户指南。

## 核心能力
- ndarray、多维数组与数据类型
- 数组索引、切片、形状变换
- 广播机制与向量化运算
- 聚合统计、随机数与线性代数
- FFT 相关数组计算接口
- 与 SciPy、Pandas、Matplotlib 等科学计算库协作

## 对道路桥梁科研的用途
- 读取并组织传感器采集的多通道时程数组
- 进行单位换算、基线数值运算和批量计算
- 组织试验工况、测点、时间步和响应矩阵
- 为滤波、频谱分析、统计特征提取和机器学习准备数值数据

## 推荐学习顺序
1. Quickstart：数组创建、索引、运算
2. Broadcasting：理解不同形状数组如何运算
3. Copies and Views：避免误修改原始数据
4. 随机数与统计函数
5. 线性代数与 FFT 基础
6. 结合 SciPy 处理真实时程数据

## 使用注意
- 数组运算前检查形状、数据类型、单位和缺失值。
- 不要把数组计算结果自动视为工程结论；关键结果应与理论算例或独立软件核对。
- 注意 float 精度、溢出、NaN/Inf 和内存占用。
- NumPy 的 FFT 接口不替代对采样频率、窗函数、频率分辨率和混叠问题的专业判断。

## 核验记录
已检查 NumPy 官方主页、官方学习入口和稳定版文档入口；确认其定位为 Python 数值计算基础库。尚未逐项运行全部教程示例，未核验每个示例的独立许可条款。

## 来源
- 官方文档：https://numpy.org/doc/stable/
- 官方学习入口：https://numpy.org/learn/
- 官方主页：https://numpy.org/
