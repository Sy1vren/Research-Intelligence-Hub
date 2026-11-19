# 11 PDF 手写化资源索引

本索引记录候选开源项目、官方文档及本模块自研程序。资源状态以实际核验为准。

| 资源 | 类型 | 用途 | 状态 | 来源 |
|---|---|---|---|---|
| handglyph | 开源项目 | 从本人手写样本建立逐字字形库 | DISCOVERED | https://github.com/jiangyonghan760/handglyph |
| handwriting-engine | 开源项目 | 中文手写生成及个人字形采集流程 | DISCOVERED | https://github.com/8-321/handwriting-engine |
| handwritten-pdf-tool | 开源项目 | 在原 PDF 页面叠加手写文本层 | DISCOVERED | https://github.com/Nemoyuzx/handwritten-pdf-tool |
| handwriting-web | 开源项目 | 浏览器端手写渲染和 PDF 导出 | DISCOVERED | https://github.com/is-cau/handwriting-web |
| PyMuPDF | 官方文档/库 | PDF 读取、页面处理与图像叠加 | REVIEWED（选型） | https://pymupdf.readthedocs.io/ |

## 收录规则

- DISCOVERED：已发现，尚未检查代码、许可证和运行情况。
- REVIEWED：已阅读文档并初步判断适用性。
- VERIFIED：完成许可证检查、依赖检查和本机运行测试。
- ADAPTED：已将代码或方法适配到本模块，并通过回归测试。
- DEPRECATED：已过时或不再推荐。

不得仅凭项目介绍或星标数将资源标记为 VERIFIED。外部项目集成前，应检查维护状态、依赖风险、许可证、字体许可及模型权重许可。

## 本模块自研资产

- [SKILL.md](../SKILL.md)：调用规范与质量标准
- [README.md](../README.md)：Windows 部署与使用说明
- [scripts/pdf_handwrite.py](../scripts/pdf_handwrite.py)：配置驱动的 PDF 手写叠加 MVP
- [config/example.json](../config/example.json)：示例配置

个人笔迹、字形图片、字体文件、真实 PDF 和输出文件只保存在本机，不归档到公开资源索引。
