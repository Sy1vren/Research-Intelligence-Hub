---
resource_id: "08-005"
title: "scikit-learn 官方机器学习用户指南"
module: "08-AI与编程"
category: "传统机器学习/模型评估"
source_type: "官方文档与示例"
maintainer: "scikit-learn Project"
source_url: "https://scikit-learn.org/stable/user_guide.html"
examples_url: "https://scikit-learn.org/stable/auto_examples/index.html"
version: "Stable documentation; check release notes and compatibility before installation"
status: "REVIEWED"
license_status: "项目主页说明软件采用 BSD license；具体文档、示例和第三方数据仍需分别核对"
---

# scikit-learn 官方机器学习用户指南

## 资源定位
scikit-learn 是基于 NumPy、SciPy 等生态构建的传统机器学习工具库，覆盖预处理、分类、回归、聚类、降维、模型选择和评价。

## 核心能力
- 数据预处理与特征变换
- 线性回归、岭回归和其他回归方法
- 决策树、随机森林、支持向量机等模型
- 聚类与主成分分析
- Pipeline、交叉验证和超参数搜索
- 回归与分类评价指标

## 对桥梁振动预测的用途
- 建立线性回归、随机森林等可解释基线模型
- 将时域、频域和工况变量组成特征矩阵
- 比较不同特征组合和算法的预测表现
- 使用交叉验证与独立测试集评估泛化能力

## 推荐学习顺序
1. Getting Started：理解 estimator、fit、predict
2. Supervised learning：回归与分类
3. Preprocessing：特征缩放和编码
4. Model selection：交叉验证与参数搜索
5. Metrics：选择符合工程目标的评价指标
6. Pipeline：将预处理与模型封装为可复现流程

## 工程时序建模的关键规范
- 按时间或试验工况划分训练集与测试集，避免相邻窗口随机拆分造成信息泄漏。
- 同一试件、同一桥梁或同一试验批次的数据可能高度相关，应设计分组验证。
- 所有标准化、特征选择和缺失值填补步骤只能在训练数据上拟合，再应用于验证/测试数据。
- 先建立简单基线模型，再评估复杂模型是否真正带来可靠提升。
- 报告 MAE、RMSE、R² 等指标时，必须说明测试集构成、目标变量单位和适用范围。
- 不得把单一数据集上的高分解释为模型具有普遍工程适用性。

## 核验记录
已检查 scikit-learn 官方稳定版主页、用户指南和安装说明。官方主页说明其提供分类、回归、聚类、降维、模型选择和预处理工具，并注明 BSD 许可；安装依赖与兼容版本应以具体版本文档为准。未运行全部示例，未在桥梁项目数据上验证模型效果。

## 来源
- 用户指南：https://scikit-learn.org/stable/user_guide.html
- 示例库：https://scikit-learn.org/stable/auto_examples/index.html
- 安装说明：https://scikit-learn.org/stable/install.html
- 官方主页：https://scikit-learn.org/
