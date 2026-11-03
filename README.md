# CCF Submission Guide

CCF A/B 类会议与期刊检索工具，帮助安排全年投稿计划。

同时查询所属领域、CCF 等级、全称、出版社、原目录网址和常见投稿月份。可在浏览器中使用，也可下载后离线使用。

[在线使用](https://wangjiajingxjtu.github.io/ccf-submission-guide/) · [GitHub 仓库](https://github.com/wangjiajingxjtu/ccf-submission-guide) · [维护者 Jiajing Wang](https://github.com/wangjiajingxjtu)

## 当前版本

- 按 CCF 第七版正式目录整理，仅含 A、B 类，覆盖 10 个领域。
- 340 条目录记录，合并为 190 个会议和 148 个不同期刊；跨领域收录保留全部分类。
- 支持名称搜索、领域／等级／类型／月份筛选、CSV 导出和单条打印。
- 附具体届次的官方来源，并区分明确日期、常规投稿推断和待复核信息。
- 当前资料核查日期：2026-11-03；不会自动抓取或更新截止日期。

## 使用

直接打开[在线网站](https://wangjiajingxjtu.github.io/ccf-submission-guide/)，或在仓库中选择 Code → Download ZIP，解压后用浏览器打开根目录的 `index.html`。离线使用无需安装依赖或运行服务器。

本地检索、筛选和导出无需联网；访问外部来源链接需要联网。

## 如何理解时间

这里的月份用于规划，不表示某一届已经开放投稿。会议可能在举办前一年截稿，摘要和全文也可能有不同日期。期刊常规稿、特刊和会议关联轨道分别遵循各自规则。

合并后的 338 个条目中：192 个有官方具体日期或明确规则，118 个根据该刊常规收稿流程或出版说明推断，28 个仍需复核（27 个期刊及 VEE）。待复核条目不纳入月份筛选。

这是个人整理的非官方工具，与 CCF 及各会议、期刊无隶属或背书关系。分类与等级依据 CCF 目录，截止安排请以目标届次和稿型的官方通知为准。来源与核查方法见 [SOURCES.md](SOURCES.md)。

## 纠错与更新

欢迎[提交 Issue](https://github.com/wangjiajingxjtu/ccf-submission-guide/issues) 或 Pull Request。请附会议／期刊名称、届次、主轨或稿型、官方链接、摘要／全文日期及时区信息。具体步骤见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 文件结构

```text
index.html               可直接部署与离线使用的网页
src/index.template.html  页面模板
data/venues.json         完整数据及逐条来源
data/venues.csv          可用 Excel 打开的数据
scripts/build.py         将数据内嵌到网页，并同步生成 CSV
.nojekyll                让 GitHub Pages 直接发布静态文件
```

更新 `data/venues.json` 或模板后，在仓库根目录运行：

```sh
python3 scripts/build.py
```

构建脚本只使用 Python 3 标准库。提交源码时一并提交重新生成的 `index.html` 和 `data/venues.csv`。

## 部署到 GitHub Pages

本项目使用仓库 `wangjiajingxjtu/ccf-submission-guide` 的 `main` 分支根目录发布：

1. 确保 `index.html` 和 `.nojekyll` 位于仓库根目录，生成的网页已经提交到 `main`。
2. 打开仓库 Settings → Pages，在 Build and deployment 下将 Source 设为 **Deploy from a branch**。
3. Branch 选择 **main**，文件夹选择 **/(root)**，点击 Save。
4. 在 Actions 中确认 Pages 部署成功，再打开[项目网站](https://wangjiajingxjtu.github.io/ccf-submission-guide/)，检查名称搜索、详情、来源链接及 CSV 导出。

后续提交到发布分支后，GitHub Pages 会重新部署。页面的数据已内嵌到 HTML；更新数据后须先运行构建脚本并提交生成文件。若部署到自己的 Fork，网站地址中的账号名须改成自己的用户名。

配置说明见 [GitHub Pages 官方文档](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

## 制作说明

本工具由项目维护者发起，借助 AI 辅助提取目录、查找资料和实现网页；逐条保留可追溯来源，尚未确认的规则明确标注。后续更正以可核对的官方证据为准。

## 许可状态

项目尚未指定软件许可证。CCF 目录及官方网页等外部资料归原发布方；公开仓库不改变这些资料的权利归属。
