---
title: "FHWA National Bridge Inventory 2026 Data"
resource_id: "07-007"
source_url: "https://www.fhwa.dot.gov/bridge/nbi/nbi_data_2026.cfm"
publisher_or_author: "Federal Highway Administration, U.S. Department of Transportation"
version: "2026 annual National Bridge Inventory dataset; FHWA page updated 2026-10-07"
published_date: "2026 annual submission; page updated 2026-10-07"
verified_date: "2026-11-16"
license_or_access: "Public download. Data.gov metadata lists Government Works (https://www.usa.gov/government-works). USAGov cautions that some federal-site content may contain third-party rights; verify individual materials before reuse."
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
- Data.gov 元数据将许可证链接指向 USAGov Government Works 说明。
- FHWA 明确说明 2026—2027 年处于旧 Coding Guide 向新 SNBI 格式过渡期，需结合 Data Crosswalk 和 Detailed Code Mapping 理解临时代码及空值。

## 4. 使用方法
1. 从 FHWA 2026 数据页选择所需州/地区或全量数据，并选择 Excel、JSON 或 GeoJSON 格式。
2. 先阅读 SNBI 规范、数据 Schema、Data Crosswalk 和 Detailed Code Mapping，再解释字段、单位和编码。
3. 处理 2026—2027 过渡数据时，保留原始字段，识别临时代码、空值及转换假设，不要直接把旧版字段与新版字段按名称强行合并。
4. 在分析记录中注明数据年份、下载日期、区域范围、字段版本和清洗规则。
5. 若用于统计或机器学习，检查样本覆盖、缺失机制、重复记录、时间口径和目标变量定义，并保留可复现的数据处理脚本。

## 5. 适用边界与局限
- 数据覆盖美国公共道路桥梁，不代表中国桥梁总体状况，不能直接用于推断中国桥梁结构性能。
- FHWA 明确提醒 NBI 数据不得用于路线净空核查；桥梁通常按约 24 个月周期检查，页面显示的净空信息可能不是最新值。
- 2026—2027 年 SNBI 过渡可能产生临时代码、空值和基于假设的字段转换；跨年度比较必须先统一数据定义。
- Data.gov 标注 Government Works，但 USAGov 说明联邦网站内容不一定全部属于政府作品；图片、标识或第三方材料应单独核对权利。不得暗示 FHWA 对研究或产品背书。

## 6. 核验记录
2026-11-16 已打开 FHWA 2026 NBI 下载页、FHWA NBI 总入口、Data.gov 数据集元数据、SNBI Data Crosswalk、Detailed Code Mapping、SNBI Schema 和 USAGov Government Works 说明。核对了发布机构、页面更新时间、下载格式、公开访问级别及 Data.gov 所列许可证入口。Data.gov 数据集元数据最后修改日期为 2026-09-03，FHWA 2026 下载页标注更新时间为 2026-10-07。未下载或运行数据文件；VERIFIED 仅表示来源、版本、访问条件和许可元数据已核对，不代表数据质量或分析结果已实测。

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
| 2026-11-16 | 初次收录，状态 VERIFIED | GPT 协助核对官方来源、版本、公开访问和许可元数据；未执行数据导入测试 |
