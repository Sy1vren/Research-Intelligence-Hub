---
resource_id: "08-003"
title: "pandas 官方文档与数据分析教程"
module: "08-AI与编程"
category: "数据读取/清洗/整理"
source_type: "官方文档与教程"
maintainer: "pandas Project"
source_url: "https://pandas.pydata.org/docs/"
learning_url: "https://pandas.pydata.org/docs/getting_started/"
version: "Stable documentation; consult release notes for installed version"
status: "REVIEWED"
review_date: "2026-11-15"
license_status: "待单独核对具体文档与代码示例的许可及引用要求"
---

# pandas 官方文档与数据分析教程

## 资源定位
pandas 是 Python 中常用的表格型数据处理工具，核心对象为 Series 和 DataFrame，适合读取、清洗、筛选、合并和汇总实验及监测数据。

## 核心能力
- CSV、Excel、JSON、Parquet 等常见数据格式读写
- 缺失值、重复值和异常记录检查
- 时间序列索引、重采样与时间窗口
- 多表连接、分组统计和透视表
- 数据类型转换与数据整理

## 对工程科研的用途
- 整理桥梁监测系统导出的多测点数据
- 按时间戳对齐风速、加速度、温度等多源记录
- 按测点、工况、日期或试验批次分组
- 建立数据质量检查表和可追溯的数据处理流水线

## 推荐学习顺序
1. Getting started：Series、DataFrame
2. 读取与写出 CSV/Excel
3. 选择、筛选、排序和缺失值处理
4. merge/join 与 groupby
5. 日期时间索引、resample 和 rolling
6. 将清洗结果交给 NumPy、SciPy 和 Matplotlib

## 使用注意
- 原始数据应只读保存；清洗结果另存并记录处理步骤。
- 时间戳必须明确时区、格式、采样间隔及重复记录处理规则。
- 不要未经说明就删除异常值或填补缺失值。
- 合并多源数据前检查键是否唯一、时间是否对齐，避免重复行和数据泄漏。

## 核验记录
已检查 pandas 官方文档和 Getting Started 教程入口，确认文档覆盖数据结构、IO、缺失数据、合并及时间序列等主题。未对全部教程示例逐项运行。

## 来源
- 官方文档：https://pandas.pydata.org/docs/
- Getting started：https://pandas.pydata.org/docs/getting_started/
