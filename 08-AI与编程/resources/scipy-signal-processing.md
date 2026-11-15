---
resource_id: "08-002"
title: "SciPy 官方科学计算与信号处理指南"
module: "08-AI与编程"
category: "信号处理/频谱分析/数值算法"
source_type: "官方文档与用户指南"
maintainer: "SciPy Project"
source_url: "https://docs.scipy.org/doc/scipy/tutorial/"
signal_url: "https://docs.scipy.org/doc/scipy/reference/signal.html"
version: "Stable documentation; check release notes for version-specific behavior"
status: "REVIEWED"
review_date: "2026-11-15"
license_status: "待单独核对具体文档与代码示例的许可及引用要求"
---

# SciPy 官方科学计算与信号处理指南

## 资源定位
SciPy 建立在 NumPy 之上，提供优化、统计、插值、积分、线性代数、FFT 和信号处理等科学算法。本卡重点关注 `scipy.signal` 与 `scipy.fft`。

## 核心能力
- 滤波器设计与滤波：低通、高通、带通、陷波等
- 信号去趋势、峰值检测和相关分析
- 功率谱密度与频谱分析
- 快速傅里叶变换（FFT）
- 插值、优化、统计和数值求解

## 对桥梁振动研究的用途
- 对加速度、位移或应变时程进行预处理
- 分析主频、频带能量和谱峰
- 比较不同工况下的频谱变化
- 提取时域与频域特征，供后续统计分析或机器学习使用

## 推荐工作流
1. 明确传感器量纲、采样频率、采样时长和测点方向。
2. 检查时间戳、缺测、饱和、异常尖峰和趋势项。
3. 根据研究目的选择去趋势、滤波或重采样方法，并记录参数。
4. 使用 FFT 或功率谱密度分析频率成分。
5. 检查频率分辨率、Nyquist 频率、窗函数和边界效应。
6. 将处理前后信号与参数、图表一并保存，确保可复现。

## 重要边界
- 滤波可能改变幅值、相位和瞬态特征；应说明滤波器类型、阶数、截止频率和相位处理方式。
- 频谱峰值不必然等于结构固有频率，需结合测量布置、激励特性和结构动力学解释。
- 采样频率不足会导致混叠，后处理不能恢复未采集到的信息。
- 不应为获得“更好看”的曲线而任意选择滤波参数。

## 核验记录
已检查 SciPy 官方用户指南及信号处理参考入口，确认其涵盖 FFT、信号处理、优化、统计等子模块。未对所有算法示例逐项运行，也未对具体项目数据开展验证。

## 来源
- SciPy 用户指南：https://docs.scipy.org/doc/scipy/tutorial/
- Signal reference：https://docs.scipy.org/doc/scipy/reference/signal.html
- SciPy Getting Started：https://new.scipy.org/getting-started.html
