# Bridge Vibration Intelligence
# 桥梁振动智能分析工具箱（第一版）

本项目是科研代码模板，当前实现**单通道振动时程**的基础分析流程：

CSV 数据 → 数据质量检查 → 去趋势 → 可选带通滤波 → Welch 功率谱密度 → 时域/频域特征 → 图表与结果导出。

> 当前版本是可复现的教学与科研起步模板，不是经过工程认证的结构健康监测系统，也不直接给出吊索风致振动安全结论。请先用合成演示数据熟悉流程，再接入经过授权的真实数据。

## 1. 目录结构

```text
bridge-vibration-analysis/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/          # 原始数据（不要覆盖）
│   └── processed/    # 程序输出
├── results/          # 图表、频谱和摘要
├── scripts/
│   └── generate_demo.py
├── src/
│   └── analyze.py
└── tests/
    └── test_analyze.py
```

## 2. 环境准备

建议使用 Python 3.10 或更高版本，并在独立虚拟环境中安装依赖。

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

python -m pip install -r requirements.txt
```

## 3. 输入数据格式

默认读取 CSV，至少包含两列：

| time_s | acceleration_m_s2 |
|---:|---:|
| 0.000 | 0.012 |
| 0.010 | 0.018 |
| 0.020 | -0.004 |

- 时间列单位为秒，必须严格递增且近似等间隔。
- 响应列应为数值型，例如加速度、位移或应变；单位由使用者明确记录。
- 不允许将不同单位或不同测点的数据混在同一列。
- 原始文件应保留不变，分析程序只读取原始文件并写出新结果。

## 4. 先运行合成演示

```bash
python scripts/generate_demo.py --output data/raw/demo_synthetic.csv
python src/analyze.py --input data/raw/demo_synthetic.csv \
  --time-column time_s \
  --signal-column acceleration_m_s2 \
  --output-dir results
```

演示信号由脚本人工合成，含有已知频率成分与随机噪声，**不是实测桥梁数据**。可以用它检查频谱流程是否能识别预设频率。

## 5. 分析真实 CSV

```bash
python src/analyze.py --input data/raw/your_measurement.csv \
  --time-column time_s \
  --signal-column acceleration_m_s2 \
  --output-dir results
```

可选带通滤波示例（截止频率必须低于 Nyquist 频率）：

```bash
python src/analyze.py --input data/raw/your_measurement.csv \
  --time-column time_s \
  --signal-column acceleration_m_s2 \
  --output-dir results \
  --lowcut 0.2 --highcut 20 --filter-order 4
```

滤波频率仅为命令格式示例，不是桥梁或吊索的推荐参数。必须依据采样率、结构特性、传感器性能和研究目的选择。

## 6. 输出内容

程序在输出目录中生成：
- `processed_signal.csv`：时间、原始信号、去趋势信号和（若启用）滤波信号。
- `power_spectral_density.csv`：Welch 功率谱密度。
- `summary.json`：采样率、采样点数、时域特征和主频估计。
- `time_history.png`：时程图。
- `power_spectral_density.png`：功率谱密度图。

## 7. 当前计算定义

- 采样频率：由时间列相邻差值的中位数估计。
- 去趋势：线性去趋势。
- 滤波：可选 Butterworth 带通滤波，采用二阶节（SOS）表示和前后向滤波。
- 频谱：Welch 方法估计功率谱密度。
- 时域特征：均值、标准差、RMS、峰值绝对值、峰峰值、峰值因子。
- 主频估计：在非零频率范围内取 PSD 最大值对应的频率。

## 8. 重要科研边界

1. 频谱峰值只是信号的主导频率成分，不自动等于结构固有频率。
2. Welch 参数、窗函数、分段长度和重叠率会影响频率分辨率及谱估计。
3. 滤波可能改变信号幅值和边界行为；必须保存滤波参数并比较处理前后结果。
4. 不规则采样、缺失采样、传感器饱和或时间戳错误必须先处理，不能直接假设数据合格。
5. 单通道分析不能替代多测点模态识别、风场分析或流固耦合研究。
6. 后续机器学习必须按时间或试验批次划分训练/测试数据，避免相邻窗口泄漏。
7. 不得将合成演示数据用于支持真实工程结论。

## 9. 测试

```bash
python -m unittest discover -s tests -v
```

## 10. 后续路线

- v0.2：多通道数据、批量文件处理、测点元数据。
- v0.3：滑动窗口与时域/频域特征表。
- v0.4：按试验批次或时间分组的机器学习基线。
- v0.5：模型解释、泛化评估和可复现实验报告。

每个版本都应保留测试记录、参数配置和已知限制。
