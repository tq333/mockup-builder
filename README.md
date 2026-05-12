# Mockup Builder

> 一个 Claude Code / CodeMaker Skill，把截图、草图、文字 prompt 一键变成符合 **mockup-kit 设计规范**的 Balsamiq 风格线框 HTML demo。
> 产出**结构化 wireframe**，不是视觉稿——精致的事交给 Figma，结构的事交给这里。

---

## ✨ 核心特性

- 🎯 **截图 → HTML**：贴张截图，30 秒内输出可运行的 wireframe demo
- 📐 **规范驱动**：所有产出强制走 design tokens、iconoir 图标、规范组件类，杜绝 AI 加戏
- 🎨 **5 套预设主题**：default(蓝) / yellow / green / purple / pink，一键切换
- 🛡️ **红线 lint**：内置脚本拦截硬编码颜色、emoji 当图标、自创组件类等违规
- ⚡ **零配置**：单文件 HTML，自包含 token + 组件 CSS + iconoir CDN + Balsamiq Sans 字体

---

## 📸 真实示例：LootBar 订单页

输入：一张订单列表 + 一张订单详情截图 + 一句话："生成两个页面，点击订单列表打开详情"

输出：单 HTML 文件，含 navbar / sidebar / 订单列表 / 订单详情双视图，点击订单卡 → 切换到详情页。

![LootBar Orders Demo](docs/screenshots/lootbar-orders.png)

代码片段（生成器自动产出）：

```html
<body data-theme="yellow">
  <nav class="navbar navbar-solid">
    <a href="#" class="navbar-brand">
      <i class="iconoir-treasure-chest icon-sm"></i> LOOTBAR
    </a>
    ...
  </nav>

  <main>
    <section class="view active" id="view-list">
      <div class="card order-card" data-order="T1072393927">
        <div class="order-header">
          <span>Apr 27, 2026 16:51:55</span>
          <span class="order-status status-completed">Completed</span>
        </div>
        <div class="order-body">
          <div class="img-ph order-thumb">IMG</div>
          ...
        </div>
      </div>
    </section>
  </main>
</body>
```

> 全部用 `var(--color-*)` token + iconoir 图标 + 规范类（`.navbar-solid` / `.card` / `.img-ph`...），不写一个硬编码 hex。

---

## 🚀 快速开始

### 1. 安装

把整个 `mockup-builder/` 目录放到你的 Claude Code skills 路径下：

```bash
# Claude Code（macOS）
~/.claude/skills/mockup-builder/

# 或自定义路径，并在 client 配置里指向它
```

### 2. 触发方式

在 Claude Code 对话里说任意一句：

- "用 mockup-builder 帮我把这张截图做成 HTML"
- "用这套规范画一版 dashboard"
- "做个 demo / wireframe / 低保真"
- "基于 mockup-kit 出页面"

Skill 会自动激活，按下面流程产出。

### 3. 内部工作流

```
1. 读 references/red-lines.md           ← 必须遵守的规则
2. 读 references/components-cheatsheet.md ← 组件清单
3. (有截图时) 读 references/theme-mapping.md ← 选主题色
4. python3 scripts/new_demo.py out.html --theme <X>
5. 替换模板中的 <!-- SLOT:body --> 占位区
6. python3 scripts/lint_demo.py out.html  ← 上线前自检
7. 打开浏览器预览
```

---

## 📁 目录结构

```
mockup-builder/
├── SKILL.md                     ← skill 主入口（被 Claude Code 自动加载）
├── README.md                    ← 你正在看的这份
├── LICENSE                      ← MIT
├── assets/
│   ├── template-base.html       ← 单页模板
│   └── template-multi.html      ← 多方案对比模板（带 sticky TOC + ScrollSpy）
├── references/
│   ├── red-lines.md             ← 红线 + 反例库（关键文档）
│   ├── components-cheatsheet.md ← 19 章组件 + token 速查
│   └── theme-mapping.md         ← 截图 → 主题色决策树
├── scripts/
│   ├── new_demo.py              ← 用模板生成空白文件
│   └── lint_demo.py             ← 红线校验
└── docs/
    ├── mockup-kit.html          ← 规范本体（可在浏览器打开看完整组件演示）
    └── screenshots/             ← README 用截图
```

---

## 🚦 四条红线（Lint 强制）

| 维度 | 必须做 | 绝对禁止 |
|---|---|---|
| **颜色** | `var(--color-*)` token | 任何 `#xxx` / `rgb(...)` 硬编码 |
| **图标** | iconoir `<i class="iconoir-*">` | emoji（🎂🚀⚙️）/ 自画 SVG / 真实 logo |
| **类名** | `.btn` / `.card` / `.list` 等规范类 | 自创 `.my-button` / `.special-card` |
| **尺寸** | `var(--sp1~12)` / `var(--fs-xs~3xl)` | 任意 `padding:13px` / `font-size:17px` |

> 完整红线清单（含**保真原则**、**组件原样使用**、**价格语义**等高优规则）见 [`references/red-lines.md`](references/red-lines.md)。

---

## 🎨 5 套主题

| 主题 | accent 色 | 适用场景 |
|---|---|---|
| `default`（不设 data-theme） | `#0073cf` 蓝 | 通用 / 商务 / 工具 / SaaS |
| `yellow` | `#ffbf00` 金黄 | 餐饮 / 优惠 / 游戏 / 暖色品牌 |
| `green` | `#009e0f` 翠绿 | 健康 / 金融 / 环保 / 生鲜 |
| `purple` | `#9900ff` 紫 | 娱乐 / 创意 / Web3 / 美妆 |
| `pink` | `#ff00ff` 品红 | 时尚 / 萌宠 / 女性向 |

切换：`<body data-theme="yellow">` —— 全局 accent + accent-bg + accent-fg 自动联动，文字色对比度自动校准（黄底 → 墨色字，其他 → 白字）。

---

## 🧱 组件清单（节选）

- **Layout**：page wrapper / two-column / navbar(`+.navbar-solid`) / breadcrumb
- **Forms**：inp / inp-group / search-wrap / select / textarea / ck / radio / toggle / slider / qty stepper
- **Buttons**：`.btn` 矩阵（primary / danger / success / ghost / outline / sm / lg / icon / block）
- **Data**：card / list / table / accordion(line/card; mutex by default) / tabs(box/underline) / pagination / stepper
- **Status**：avatar(4 sizes + sq) / badge / tag / alert(4 semantics) / toast / progress / spinner / skeleton / empty-state
- **Overlays**：modal / dropdown / popover / tooltip / bottom-sheet
- **Frames**：phone-frame / browser-frame
- **Icons**：80+ iconoir 常用名按类目列出

完整清单见 [`references/components-cheatsheet.md`](references/components-cheatsheet.md)。

---

## ❓ 常见 pushback 自动应答

| 用户说 | Skill 回复 |
|---|---|
| "再做精致一点" | "Mockup-kit 是 wireframe 风格，再精致请进 Figma；这边只能调整结构 / 信息层级" |
| "换个真实图 / logo" | "用 `.img-ph` 占位是规范要求；真图请到 Figma 阶段再贴" |
| "加个渐变 / 玻璃拟态" | "这是规范级修改，建议先加到 mockup-kit 里" |
| "颜色我自己挑 #abcdef" | "5 个主题之外的颜色不能直接写。要新色请加到 mockup-kit 的 `body[data-theme]`" |

---

## 🔧 依赖

- **Python 3.6+**（仅脚手架/lint 脚本用）
- **Claude Code** 或兼容 Skill 协议的 AI Coding Client（CodeMaker、Cline 等）
- 浏览器（产出物是单文件 HTML，任意现代浏览器可看）
- *可选*：[`docs/mockup-kit.html`](docs/mockup-kit.html) 规范本体（含完整组件演示，可在浏览器直接打开看效果）。skill 内置 cheatsheet 已是其精简子集，不必须读，但建议添加新组件 / 新红线时先看本体

---

## 🤝 设计哲学

> "精致是 Figma 的事，结构是 wireframe 的事。"

Skill 做的是**信息层级 + 区块结构**，不做视觉抛光。所有"让 demo 更漂亮"的冲动 —— 加渐变、加阴影、加动效、补 hover 提示、用 emoji —— 都被红线和 lint 拦下。

这种自我克制带来三个收益：

1. **快**：决策少，单页 1-2 分钟出稿
2. **稳**：产出风格高度一致，不会因 LLM "灵感"漂移
3. **可演进**：今天的 wireframe 直接对得上明天的 Figma 视觉稿，结构无需重画

---

## 📜 License

MIT —— 自由 fork、改造、商用。如果对你有帮助，欢迎 ⭐ Star。

---

## 🙋 反馈 / 贡献

- 发现 bug / 不合规组件被生成 → 提 issue
- 新增组件 → 先 PR 改 `mockup-kit.html`，再同步到 `references/components-cheatsheet.md`
- 新增红线规则 → PR 改 `references/red-lines.md`，并在 `scripts/lint_demo.py` 加对应检查
