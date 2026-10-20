# Agent Fieldnotes · AI Agent 开发手册

从理解原理到构建、评测、部署的中英双语技术知识站。纯 HTML / CSS / JavaScript，无构建依赖、无后端、无登录、无 API Key。发布至公开 GitHub Pages 后，访客无需 GitHub 或 ChatGPT 账号即可阅读。

[中文网站](https://aidify2025.github.io/agent-fieldnotes/index.html?lang=zh) · [English website](https://aidify2025.github.io/agent-fieldnotes/index-en.html?lang=en) · [贡献指南 / Contributing](CONTRIBUTING.md)

A bilingual, browser-only learning site for AI Agent engineering: 32 chapters, 8 interactive labs, 100 algorithm walkthroughs and a JavaScript coding playground. No account, API key or build dependencies required.

![Agent Fieldnotes 英文首页真实截图，右上角支持中英文切换](site-preview.jpg)

## 从哪里开始 / Learning paths

| 你的目标 / Goal | 推荐路径 / Path |
| --- | --- |
| 理解 Agent 执行机制 / Agent fundamentals | [Agent Loop](https://aidify2025.github.io/agent-fieldnotes/agent-loop.html) → 工具契约 → 权限与预算 |
| 接入工具 / Connect tools | [MCP 教程](https://aidify2025.github.io/agent-fieldnotes/mcp-tutorial.html) → 错误语义 → 权限校验 |
| 构建可恢复流程 / Recoverable workflows | [LangGraph](https://aidify2025.github.io/agent-fieldnotes/langgraph-tutorial.html) → [HITL 与 Checkpoint](https://aidify2025.github.io/agent-fieldnotes/hitl-checkpoint.html) → 幂等与故障注入 |
| 做完整应用 / Build an application | 手册第 23–26 章：RAG → 检索 → 证据约束 → 合同审查助手 |
| 验证上线质量 / Production readiness | 手册第 27–32 章：评测 → 重试 → Trace → 成本 → 安全 → 部署 |
| 练算法 / Algorithm practice | [Hot 100 详解](https://aidify2025.github.io/agent-fieldnotes/hot100.html?lang=zh) → [编程练习](https://aidify2025.github.io/agent-fieldnotes/practice.html?lang=zh) |

每个专题页提供中文 / EN 切换。先阅读例子，再打开对应的交互章节做实验，最后检查验收项。

## 功能

- **32 章、6 个模块**：运行时基础；工具、权限与上下文；LangGraph；任务协作；RAG 与完整应用；评测、安全与上线。
- 每章包含原理、分步实现、具体场景、注释代码、交互实验、误区、验收项与来源链接。
- **8 类确定性本地实验**：Agent Loop、上下文压缩、跨会话记忆、Reducer、审批与崩溃恢复、依赖 DAG、证据召回、评测门槛。
- 章节搜索、模块筛选、收藏、学习进度、独立章节链接、代码复制与上线清单。
- 保留算法练习场与 Hot 100 可视化详解，原页面和学习记录不受影响。
- 无模型调用、无真实外部写入、无上传合同功能；实验是机制教学，不是框架运行或产品基准。

## 参考与内容边界（2026-10-14）

- [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code/tree/ce8f9f186058939da54c9d6fead78dfb5d0fd6c3)：当前根目录 s01–s17，不混用旧 agents/docs 12课编号。
- [langgraph-in-action](https://github.com/webup/langgraph-in-action/tree/9f02d60e115dd1c4d9b5231a0d415e9fe785e3cc)：chapter2–7，原依赖基线 Python>=3.13、LangGraph>=0.6.6、LangChain>=0.3.27。框架 API 迁移另链接官方文档。
- 本站原创解释、场景、示意代码与交互实现；未整段复制第三方教程。每章标出具体参考。RAG、安全、评测与生产工程是原创扩展，不声称参考项目已实现全部能力。
- 明确区分 mock MCP 与真实传输、worktree 与安全沙箱、内存存档与持久存储、节点重跑与外部幂等。

## 中英文版本

所有三个主页面支持中文 / EN 切换，英文版本包含完整教学内容，不依赖在线翻译服务：

| 中文 | English |
| --- | --- |
| `index.html` | `index-en.html` — 32-chapter Agent Handbook |
| `practice.html` | `practice-en.html` — 8 coding exercises |
| `hot100.html` | `hot100-en.html` — all 100 detailed lessons |

语言选择保存在 `agent-fieldnotes-language`。切换时保留当前章节或题目 hash；已学、收藏、代码草稿与提交记录共用原有存储键和稳定 ID。显式 `?lang=zh` / `?lang=en` 覆盖已保存偏好；英文页面的站内导航继续使用英文入口。不会发送内容到翻译服务，也不需要登录。

手册和练习场英文页面包含自己的翻译数据与交互脚本；Hot 100 改为中英文共用数据与渲染器，避免两个版本出现内容差异。修改教学内容时请同步两种语言；标识符、题目 ID、函数签名与判题数据保持一致。不要翻译用户自行输入的代码或数据。新增双语回归检查：`node test-i18n.cjs`。

## GitHub Pages 部署

本仓库使用 GitHub Pages 原生分支部署，不需要自定义工作流。

1. 在 Settings → Pages → Build and deployment 中选择 **Deploy from a branch**。
2. 选择 **main** 和 **/(root)**，点击 Save。
3. GitHub 自动构建和发布。后续提交到 main 会自动更新网站。

实际发布地址请以 Settings → Pages 中显示的地址为准。访客无需 GitHub 或 ChatGPT 登录。

Fork 本仓库后，在你自己的仓库按以上步骤启用 Pages 即可。所有资源使用相对路径，支持项目路径。

## 本地运行

在项目根目录运行：

```bash
python -m http.server 8000
```

访问 `http://localhost:8000`。Windows 也可使用 `py -m http.server 8000`。停止服务按 Ctrl+C。无需 `npm install`；Node 用于运行手册回归检查：`node test-handbook.cjs`（建议 Node 18+）。

## 目录与维护

| 路径 | 用途 |
| --- | --- |
| `index.html` | 自包含手册：样式、HANDBOOK 数据、纯实验引擎、阅读交互，均为可读源码 |
| `test-handbook.cjs` | 从首页提取脚本，校验章节完整性与实验关键不变量 |
| `style.css` / `app.js` | 旧版首页资源，当前手册已不加载；保留便于历史对照 |
| `.nojekyll` | 静态 Pages 部署 |
| `CONTRIBUTING.md` / `LICENSE` | 贡献说明 / MIT 许可证 |

在 `index.html` 的 `window.HANDBOOK` 中维护模块和章节。每章使用稳定 `id`，新增章节时同步维护章节编号与首页介绍统计；列表和学习进度按数据动态计算。`Engines` 中的模拟逻辑为纯函数，`mountLab` 负责交互展示，阅读器负责目录、深链接和本地进度。交互章节链接形如 `#chapter=interrupt`。重点专题另有静态正文页，由 `build-seo.cjs` 从中英文首页数据生成；不要手工修改生成页。内容更新后运行 `node build-seo.cjs`，同步提交生成结果。

## 数据与边界

- 收藏、已学状态与检查清单保存在浏览器 localStorage，新手册键为 `agent-fieldnotes-handbook-v2`；不上传服务器、不跨设备同步。清理站点数据会清空记录。从旧域名迁移到 GitHub Pages 后，不会自动迁移旧域名的进度。
- 首次打开新手册时，将旧 `agent-fieldnotes` 中12章的已学/收藏按对应主题迁移到稳定 ID；旧键保留，算法页面存储不变。旧版上线检查清单不自动勾选新版验收条件。
- 无统计跟踪脚本、远程字体或 CDN 运行依赖。官方资料链接仅在点击后访问对应网站。
- GitHub Pages 托管的是静态网站；没有在线编辑后台、用户系统或真实模型推理服务。修改内容通过提交代码完成。
- 本包不含原托管平台配置、原站点标识、Git 历史、账号信息或凭证。它是可独立部署的源码副本。
- 已检查 JavaScript 语法、相对资源路径及部署目录；部署进度可在仓库 Actions 中查看。若失败，请检查 Pages 的 Source 设置、分支与目录。

## 开源许可

本项目代码与随附原创文档采用 MIT License，见 `LICENSE`。外链官方资料的内容与商标仍归原权利人；链接不意味着其内容也使用本项目许可证。

## 官方部署资料

- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## 算法练习场

打开 `practice.html`，或从首页的“算法练习”入口进入。首批 8 道原创表述的经典算法练习，支持 JavaScript 编码、样例运行、完整测试集提交、自定义 JSON 参数、题解、代码草稿和提交历史。

- `problems.js`：题库，使用稳定 ID；每题定义函数名、参数、约束、样例、测试及参考解法。
- `practice.js`：编辑器交互、本地判题与存储；`practice.css`：响应式布局。
- 用户代码在带 CSP 的 sandbox iframe 内部 Web Worker 运行，不在页面主线程执行；不开放网络，执行超时会终止。
- 保存键为 `agent-fieldnotes-coding-v1`。保留最近 40 次提交，本地数据不跨设备同步。
- 前端测试集公开，适合个人学习，不能用作可信竞赛排名。仅支持 JavaScript；Python/Java 等需要另外接入语言运行时或服务端判题。
- 单次 Worker 限时 2 秒，整个运行器响应上限 5 秒。没有操作系统级内存配额；不要运行来源不明的代码。运行耗时仅供本机参考，不代表复杂度证明。


## Hot 100：按方法学习 / Method-oriented guides

[中文题解](https://aidify2025.github.io/agent-fieldnotes/hot100.html?lang=zh) · [English guides](https://aidify2025.github.io/agent-fieldnotes/hot100-en.html?lang=en)

覆盖 Hot 100 全部 100 题和 17 个类型。题意、关键约束与有效自编示例经过重新核对；本站独立编写讲解和代码，不复制官方题面或官方题解。原题链接和力扣题解入口保留；部分题解可能需要登录。

每题先列出可选方法与复杂度，再按方法展开：

- 思路推导与算法步骤；不再套用旧的六段阅读路线，也不强制划分初中高阶。
- 每种方法独立的示例状态推演，切换方法后同步切换；可前进、后退、重置或自动播放。
- Java 17 / Python 3 完整解法，可切换和复制；链表/树节点定义由原题评测器提供。
- 正确性解释，以及与实际代码一致的时间和空间复杂度推导。基线解法和进阶要求的限制在说明中标注。

`hot100-data.js` 为中英文共用数据源，`hot100.js` 为共用渲染器，`hot100.css` 为共用响应式样式。新增字段 `statement`、`constraints`、`example` 与方法内的 `intuition / steps / correctness / complexity / trace` 使用 `{zh, en}`；代码只维护一份。编辑任一方法时，须同步解释、代码、复杂度和演示状态。

代码块用于学习与前往力扣提交，本页不直接执行 Java/Python。动画是自编示例的关键状态，不是任意输入的运行器。原算法练习场继续提供浏览器内 JavaScript 练习。

收藏、已学状态和导入导出保持 `agent-fieldnotes-hot100-v1` 与稳定题号；无需迁移历史记录。运行 `node test-hot100.cjs` 验证完整性与双语方法/代码切换，再运行 `node test-i18n.cjs` 和 `node test-seo.cjs`。

All 100 lessons share bilingual data and a method-oriented renderer. Each approach includes original reasoning, Java/Python implementations, correctness, complexity and its own example trace. The page is a learning guide, not a Java/Python execution environment. Saved progress remains compatible with previous versions.

验证范围与已知边界见 [HOT100-VALIDATION.md](HOT100-VALIDATION.md)。

## SEO 与独立教程页

- `agent-loop.html`、`mcp-tutorial.html`、`hitl-checkpoint.html`、`langgraph-tutorial.html` 及对应 `-en.html`：共 8 个静态正文页，覆盖 7 个重点章节。关闭 JavaScript 仍可阅读；实验入口通往原手册。
- 六个原页面和八个教程页均声明 canonical、双向 hreflang 与 Open Graph 分享信息。
- `sitemap.xml` 列出 14 个公开页面，不包含 hash 或语言查询参数。没有伪造更新时间、评分或索引状态。
- 修改正文后运行 `node build-seo.cjs`；Fork 后使用 `node build-seo.cjs https://你的用户名.github.io/仓库名/` 重新生成站点 URL。
- 运行 `node test-seo.cjs`、`node test-handbook.cjs`、`node test-i18n.cjs` 验证。
- 搜索引擎所有权验证与站点地图提交步骤见 [SEARCH-SETUP.md](SEARCH-SETUP.md)。发布 sitemap 不等于已提交或已收录。

## AI Agent 面试题 / Interview handbook

- [中文详解](https://leftagent.github.io/agent-fieldnotes/interview.html) · [English](https://leftagent.github.io/agent-fieldnotes/interview-en.html)
- 96 道原创详解，12 个模块：模型基础、架构、提示、RAG、工具、记忆、规划、多 Agent、评测、安全、部署、项目与手写题。
- 每题包含核心回答、原理与实现、工程例子、追问、易错点和参考链接；支持全文搜索、模块筛选、单题链接和浏览器本地进度。
- 主题参考 [Agent-Interview-100](https://github.com/BigKunLun/Agent-Interview-100) 与 [kaomian](https://github.com/smile-struggler/kaomian)，解释独立编写，不代表原作者或官方答案。
- 内容源：`interview-data.json`；生成中英文静态全文页面：`python build-interview.py`。无需服务端、API 密钥或登录。
- 验证：`python test-interview.py` 与 `node test-seo.cjs`。
