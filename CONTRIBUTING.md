# 纠错与更新

欢迎在 [wangjiajingxjtu/ccf-submission-guide](https://github.com/wangjiajingxjtu/ccf-submission-guide) [提交 Issue](https://github.com/wangjiajingxjtu/ccf-submission-guide/issues)，或通过 Fork 提交 Pull Request。不会修改代码也可以直接报告问题。

报告日期问题时，请提供：

1. 会议或期刊的名称与简称，以及会议届次。
2. 主轨、短文、专题、特刊或常规论文等稿型。
3. 官网、主办方或出版社的原始链接。
4. 摘要截止、全文截止、时区，及是否延期。
5. 当前展示内容和建议更正内容。

数据保存在 [data/venues.json](data/venues.json) 的 `records` 中。稳定的 `id` 来自目录页码与序号；如无目录版本变化，请不要重排或改变它。

`submission.months` 仅写有依据的整数月份（1—12）。没有足够证据时保留空数组，并说明待复核原因。跨领域重复记录（TOMM、DKE）应同步修改投稿说明。

修改数据或模板后，在仓库根目录运行：

```sh
python3 scripts/build.py
```

用浏览器打开根目录的 `index.html`，检查受影响条目的搜索结果、月份和来源。将数据、模板（如修改）、生成的网页和 CSV 一起提交。Pull Request 中写明修改内容和验证结果，避免只更新生成网页而遗漏数据源。

合并到 `main` 后，由 GitHub Pages 发布更新。维护者应确认部署成功，并在[在线网站](https://wangjiajingxjtu.github.io/ccf-submission-guide/)检查受影响条目；首次部署步骤见 [README.md](README.md#部署到-github-pages)。

网站的核查日期按本次整体资料快照显示。更新少数条目时，应在该条目的备注中写明补核日期；不要仅因为改了几条记录，就把所有条目的核查日期改成当天。

请只提交必要的目录字段、自己的说明与公开来源链接，不上传原始 PDF、官网页面全文或私人联系信息。
