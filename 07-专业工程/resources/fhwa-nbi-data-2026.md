---
title: "FHWA National Bridge Inventory 2026 Data"
resource_id: "07-007"
source_url: "https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm"
publisher_or_author: "Federal Highway Administration, U.S. Department of Transportation"
version: "FHWA 2026 annual NBI page updated 2026-10-07; related U.S. DOT Data Portal catalog record updated 2026-11-02"
published_date: "2026 annual submission; page updated 2026-10-07"
verified_date: "2026-11-16"
license_or_access: "FHWA public download. Data.gov catalog metadata links to USAGov Government Works guidance; a separate U.S. DOT Data Portal NBI record lists CC0 1.0. Treat these as record-specific metadata and check the actual downloaded file and any third-party material before reuse."
primary_module: "07-专业工程"
resource_type: "桥梁基础设施公开数据集"
status: "VERIFIED"
---

# FHWA 2026 National Bridge Inventory（NBI）数据

## 1. 资源简介
美国联邦公路管理局（FHWA）发布的 2026 年国家桥梁清单数据。页面提供美国各州及地区的公路桥梁年度数据下载，包含 Excel、JSON 和 GeoJSON 等格式，并提供全量汇总下载入口。

## 2. 解决的问题
为桥梁资产统计、桥梁状态与位置分析、区域桥梁状况比较、基础设施数据可视化及数据驱动研究提供可追溯的公开数据来源。

## 3. 核心价值
- FHWA 页面列出 2026 年各州/地区数据及全量下载入口，页面更新时间为 2026-10-07。
- 全部公路桥梁汇总条目显示 624,939 座，并提供 Excel、JSON、GeoJSON 格式。
- Data.gov 将发布机构标注为 FHWA，数据集访问级别为 public，元数据修改日期为 2026-09-03。
- Data.gov 目录记录将许可证链接指向 USAGov Government Works 说明。\n- 另一个美国交通部 Data Portal 的 NBI 目录记录显示：数据和元数据最后更新于 2026-11-02，记录创建于 2026-10-14，提供方为 Office of Bridges and Structures，记录列出的 Rights 为 CC0 1.0。该记录的 Temporal Applicability 标为 2024/2025，不能仅凭目录标题将其当作 2026 年度数据文件。
- FHWA 明确说明 2026—2027 年处于旧 Coding Guide 向新 SNBI 格式过渡期，需结合 Data Crosswalk 和 Detailed Code Mapping 理解临时代码及空值。

## 4. 使用方法
1. 从 FHWA 2026 数据页选择所需州/地区或全量数据，并选择 Excel、JSON 或 GeoJSON 格式。
2. 先阅读 SNBI 规范、数据 Schema、Data Crosswalk 和 Detailed Code Mapping，再解释字段、单位和编码。
3. 处理 2026—2027 过渡数据时，保留原始字段，识别临时代码、空值及转换假设，不要直接把旧版字段与新版字段按名称强行合并。
4. 在分析记录中注明数据年份、下载日期、区域范围、字段版本和清洗规则。
5. 若用于统计或机器学习，检查样本覆盖、缺失机制、重复记录、时间口径和目标变量定义，并保留可复现的数据处理脚本。\n6. 同时查看 U.S. DOT Data Portal 目录记录时，单独记录其更新时间和 Temporal Applicability；下载后以文件自身元数据确认实际年份，避免把 2024/2025 适用范围误写为 2026。

## 5. 适用边界与局限
- 数据覆盖美国公共道路桥梁，不代表中国桥梁总体状况，不能直接用于推断中国桥梁结构性能。
- FHWA 明确提醒 NBI 数据不得用于路线净空核查；桥梁通常按约 24 个月周期检查，页面显示的净空信息可能不是最新值。
- 2026—2027 年 SNBI 过渡可能产生临时代码、空值和基于假设的字段转换；跨年度比较必须先统一数据定义。
- 不同官方目录记录的许可字段并不相同：Data.gov 记录链接到 Government Works 说明，而 U.S. DOT Data Portal 记录列出 CC0 1.0。不得把一个目录记录的许可自动套用到所有附件、图片或第三方材料。\n- U.S. DOT Data Portal 记录的 Temporal Applicability 为 2024/2025；在未核对下载文件元数据前，不得把该记录直接称为 2026 数据。不得暗示 FHWA 对研究或产品背书。

## 6. 核验记录
2026-11-16 已核对 FHWA 2026 NBI 下载页、FHWA NBI 总入口、Data.gov 数据集元数据、SNBI Data Crosswalk、Detailed Code Mapping、SNBI Schema 和 USAGov Government Works 说明。2026-11-23 进一步检索并打开美国交通部 Data Portal 的 NBI 目录记录；官方目录摘要显示数据及元数据最后更新于 2026-11-02、记录创建于 2026-10-14、Rights 为 CC0 1.0、Temporal Applicability 为 2024/2025。该目录页在直接打开时仅返回极简页面，因此详细元数据以官方检索返回的目录字段为依据；尚未下载数据文件，也未验证目录记录与 FHWA 2026 年度下载文件是否完全同一数据版本。VERIFIED 仅表示官方来源、目录版本字段、访问入口及记录级许可元数据已核对，不代表数据文件已下载、数据质量或分析结果已实测。

## 7. 关联资源
- 07-001 FHWA Bridge Inspection Resources
- 07-008 FHWA LTBP InfoBridge Portal
- 09 文献与数据模块（数据整理、元数据和复现流程）
- 08-AI与编程/projects/bridge-vibration-analysis/

## 8. 原始来源
- FHWA 2026 NBI 数据下载：https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm
- FHWA NBI 数据总入口：https://www.fhwa.dot.gov/bridge/nbi/nbi_data.cfm
- SNBI Data Crosswalk：https://www.fhwa.dot.gov/bridge/snbi/datacrosswalk.cfm
- SNBI Detailed Code Mapping：https://www.fhwa.dot.gov/bridge/snbi/codemapping.cfm
- SNBI Schema：https://www.fhwa.dot.gov/bridge/snbi/schema.cfm
- Data.gov 数据集元数据：https://catalog.data.gov/dataset/national-bridge-inventory-nbi
- USAGov Government Works 说明：https://www.usa.gov/government-copyright

## 9. 更新历史
| 日期 | 变更 | 核验人/执行方 |
|---|---|---|
| 2026-11-16 | 初次收录，状态 VERIFIED | GPT 协助核对 FHWA 官方来源、版本、公开访问和许可入口；未执行数据导入测试 |\n| 2026-11-23 | 补充 U.S. DOT Data Portal 2026-11-02 更新的目录记录及其 2024/2025 时间范围、CC0 1.0 字段；明确区分目录记录与 2026 年度下载文件 | GPT 协助核对官方目录元数据；未下载或验证数据文件 |
