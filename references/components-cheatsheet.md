# Mockup Kit · Components Cheatsheet

> 这是给 AI 拼装页面的"积木清单"。完整规范见 `mockup-kit.html`，但日常生成只需读这一份。

## 0. 总则（永远先读）
- 所有颜色必须用 `var(--color-*)` token，**禁止硬编码 hex**
- 所有图标用 `<i class="iconoir-XXX"></i>` 风格，**禁止 emoji**
- 所有间距用 `var(--sp1)~--sp12`，**禁止任意 px**
- 所有字号用 `var(--fs-xs ~ --fs-3xl)`，**禁止任意 font-size**
- 主题切换必须保持可用：不要在元素上写死 `background:#xxx`，永远走 token

## 1. Layout / Structure

### Page wrapper
```html
<main style="max-width:1200px;margin:0 auto;padding:var(--sp4) var(--sp6) var(--sp10)">
  <!-- content -->
</main>
```

### Two-column
```html
<div style="display:grid;grid-template-columns:300px 1fr;gap:var(--sp5);align-items:start">
  <aside>...</aside>
  <section>...</section>
</div>
```

## 2. Top Navbar
```html
<nav class="navbar">
  <a href="#" class="navbar-brand"><i class="iconoir-XXX"></i> Brand</a>
  <div class="navbar-menu">
    <a class="navbar-link active" href="#">Home</a>
    <a class="navbar-link" href="#">Item <i class="iconoir-nav-arrow-down icon-xs"></i></a>
  </div>
  <div class="navbar-slot">
    <div class="search-wrap" style="width:240px">
      <i class="iconoir-search search-icon"></i>
      <input class="inp" placeholder="Search">
    </div>
    <button class="btn btn-sm">EN / EUR</button>
    <button class="btn btn-icon btn-ghost"><i class="iconoir-bell"></i></button>
    <div class="avatar avatar-md">XX</div>
  </div>
</nav>
```

### Solid 变体（实色头部）
| 变体 | class | 背景 | 文字色 | 适用 |
|---|---|---|---|---|
| 默认 | `.navbar` | `surface` 白 | `ink` 默认 | 通用 |
| 黑底 | `.navbar.navbar-solid` | `color-ink` 黑 | brand 跟 accent；菜单文字白（hover/active 实白） | 黑金 / 高端 / 游戏品牌 |

⚠️ 实色头部下 `.btn-ghost` 图标按钮的色彩已自动反相，**不要再手写 `style="color:..."`**。其他 slot 组件（btn / inp / avatar）保持白底原样以形成对比。

```html
<!-- 黑底 navbar（如 LootBar 这类截图） -->
<nav class="navbar navbar-solid"> ... </nav>
```

## 3. Breadcrumb
```html
<nav class="breadcrumb">
  <i class="iconoir-home icon-sm"></i>
  <a href="#">Home</a>
  <span class="breadcrumb-sep">›</span>
  <span class="muted">Current</span>
</nav>
```

## 4. Buttons
- `.btn` 基础白底
- `.btn-primary` 主操作（accent 背景 + accent-fg 文字）
- `.btn-danger` / `.btn-success` 语义按钮
- `.btn-sm` / `.btn-lg` 尺寸
- `.btn-icon` 圆形图标按钮
- `.btn-ghost` 无边无影
- `.btn-block` 占满宽度

```html
<button class="btn btn-primary"><i class="iconoir-XXX"></i> Save</button>
<button class="btn btn-icon btn-ghost"><i class="iconoir-bell"></i></button>
```

## 5. Inputs
- `.inp` 单行输入
- `.inp-group` + `.inp-label` + `.inp-hint` + `.inp-err-msg` 完整字段
- `.search-wrap` + `.search-icon` 带搜索图标
- `.inp-error` 错误状态
- `select.inp` 下拉
- `textarea.inp` 多行

```html
<div class="inp-group">
  <label class="inp-label">Email</label>
  <input class="inp" type="email" placeholder="you@example.com">
  <span class="inp-hint">We'll never share this</span>
</div>
```

## 6. Selection
- `.ck-wrap` + `.ck-box` checkbox（已选 `.checked`）
- `.ck-wrap` + `.radio-box` radio
- `.toggle-wrap` + `.toggle-track`/`.toggle-thumb` switch（开 `.on`）
- `.mock-slider` slider

## 7. Cards
```html
<div class="card">
  <div class="card-img" style="height:160px">Image</div>
  <div class="card-body">
    <div class="card-title">Title</div>
    <div class="card-text">Description text</div>
  </div>
  <div class="card-footer">
    <button class="btn btn-sm btn-primary">Action</button>
  </div>
</div>
```

## 8. Lists
```html
<div class="list">
  <div class="list-item">
    <i class="iconoir-XXX icon-sm"></i>
    <div class="list-item-content">
      <div class="list-item-title">Title</div>
      <div class="list-item-sub">Subtitle</div>
    </div>
    <i class="iconoir-nav-arrow-right list-item-action"></i>
  </div>
  <!-- 分组：在条目前插入 -->
  <div class="list-section-header">SECTION</div>
</div>
```

## 9. Accordion ⭐ FAQ 必备
```html
<!-- Style 1：横线分隔（FAQ 推荐） -->
<div class="accordion accordion-line">
  <details open>
    <summary>
      Question title
      <i class="iconoir-nav-arrow-down chev"></i>
    </summary>
    <div class="accordion-body">
      <p>Answer paragraph.</p>
      <ul><li>List item</li></ul>
    </div>
  </details>
  <details>
    <summary>Other question <i class="iconoir-nav-arrow-down chev"></i></summary>
    <div class="accordion-body"><p>Answer.</p></div>
  </details>
</div>

<!-- Style 2：卡片分隔 -->
<div class="accordion accordion-card">...</div>
```
- 默认互斥（点开新条目，其他自动收起）
- 加 `data-multiple="true"` 允许多开

## 10. Tabs / Pagination / Stepper
```html
<!-- Tab 风格 1：方形 -->
<div class="tabs">
  <a class="tab-item active">Tab 1</a>
  <a class="tab-item">Tab 2</a>
</div>
<!-- Tab 风格 2：下划线 -->
<div class="tabs">
  <a class="tab-line-item active">Tab 1</a>
  <a class="tab-line-item">Tab 2</a>
</div>

<!-- Pagination -->
<div class="pagination">
  <button class="page-btn"><i class="iconoir-nav-arrow-left"></i></button>
  <button class="page-btn active">1</button>
  <button class="page-btn">2</button>
  <button class="page-btn"><i class="iconoir-nav-arrow-right"></i></button>
</div>

<!-- Stepper -->
<div class="stepper">
  <div class="step"><div class="step-circle done"><i class="iconoir-check"></i></div><div class="step-label">Done</div></div>
  <div class="step-line done"></div>
  <div class="step"><div class="step-circle active">2</div><div class="step-label">Active</div></div>
  <div class="step-line"></div>
  <div class="step"><div class="step-circle">3</div><div class="step-label">Next</div></div>
</div>
```

## 11. Avatar / Badge / Tag
- `.avatar` `.avatar-xs/sm/md/lg`，加 `.avatar-sq` 变方形
- `.badge` 红 / `.badge-blue` accent / `.badge-green` / `.badge-gray`
- `.tag` 普通 / `.tag-filled` / `.tag-accent` / `.tag-danger` / `.tag-success`

```html
<div class="avatar avatar-md">JD</div>
<span class="badge">3</span>
<span class="tag tag-accent">New</span>
```

## 12. Feedback
- `.alert` + `.alert-info`/`.alert-success`/`.alert-warning`/`.alert-danger`
- `.toast` 短提示
- `.progress-bar` + `.progress-fill`
- `.spinner` loading
- `.skeleton` 骨架屏

## 13. Overlays（仅当截图明显有 modal/sheet 才用）
- `.modal-backdrop` + `.modal` + `.modal-header`/`.modal-body`/`.modal-footer`
- `.bottom-sheet-wrap` + `.bottom-sheet` + `.sheet-handle`/`.sheet-body`
- `.dropdown-menu` + `.dropdown-item`
- `.popover` + `.popover-title`/`.popover-text`
- `.tooltip-box`

## 14. Table
```html
<div class="table-wrap">
  <table>
    <thead><tr><th>Name</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>Item 1</td><td><span class="tag tag-success">OK</span></td></tr>
    </tbody>
  </table>
</div>
```

## 15. Empty State
```html
<div class="empty-state">
  <i class="iconoir-search empty-icon"></i>
  <div class="empty-title">No results</div>
  <div class="empty-text">Try adjusting filters</div>
  <button class="btn btn-primary">Clear filters</button>
</div>
```

## 16. Page Frames
- `.phone-frame` / `.phone-screen` 手机外壳
- `.browser-frame` / `.browser-bar` / `.browser-content` 桌面端外壳

**移动端宽度规范（强制）：**
```html
<!-- ✅ 移动端：375px 宽，圆角 8px，不含 notch / home bar -->
<div class="phone-frame" style="width:375px;">
  <div class="phone-screen" style="...">
    <!-- 内容 -->
  </div>
</div>
```
⚠️ 禁止用其他宽度（300 / 360 / 390px）；禁止在 phone-frame 内写 `.phone-notch` 和 `.phone-home`（规范已隐藏）。

**桌面端宽度规范（强制）：**
```html
<!-- ✅ 桌面端：1440px 宽 -->
<div class="browser-frame" style="width:1440px;">
  <div class="browser-bar">...</div>
  <div class="browser-content">
    <!-- 内容 -->
  </div>
</div>
```
⚠️ 桌面端页面使用 `.browser-frame`，宽度统一 `1440px`，不得随意缩窄。

## 17. Icons (iconoir)
常用清单（更多去 https://iconoir.com）：
- Navigation: home / search / bell / settings / menu / nav-arrow-{down/right/left/up}
- Actions: plus / minus / edit-pencil / trash / check / xmark / share-android
- Comm: mail / message-text / phone / chat-bubble
- Commerce: shopping-bag / shopping-cart / dollar-circle / piggy-bank / credit-card / gift
- User: user / user-plus / log-out / lock
- Status: info-circle / warning-triangle / check-circle / xmark-circle
- Media: play / pause / mic / camera / image
- Misc: star / heart / flash / sparks / fire / treasure-chest / birthday-cake / medal-1st / headset

尺寸：`.icon-xs/sm/md/lg/xl`（默认 20px）

## 18. Themes
切换 `<body data-theme="X">`：
- 不写或 `default` → 蓝 `#0073cf`
- `yellow` → `#ffbf00`
- `green` → `#009e0f`
- `purple` → `#9900ff`
- `pink` → `#ff00ff`

⚠️ 超链接 `<a>` 永远走 `var(--color-link)`，不跟主题。

## 20. 移动端专用组件（Mobile-only）

### 20-1. `.img-ph` — 图片 / 视频占位块

> ⚠️ `mockup-kit.html` 里已定义，但每个独立 demo 文件需**自带此 CSS**，否则占位块呈白色空白。

```css
/* 粘贴到 demo 的 <style> 块内 */
.img-ph {
  background: var(--color-light);
  border: var(--border);
  border-radius: var(--radius);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-muted);
  font-style: italic;
  font-size: var(--fs-sm);
}
```

```html
<!-- 16:9 视频封面 -->
<div class="img-ph" style="width:100%;aspect-ratio:16/9;flex-direction:column;gap:var(--sp2);">
  <i class="iconoir-play" style="font-size:32px;opacity:.4;"></i>
  <span>[ Video ]</span>
</div>

<!-- 图片占位（带标题） -->
<div style="display:flex;flex-direction:column;gap:var(--sp1);">
  <div class="img-ph" style="height:72px;">[ Image ]</div>
  <div style="font-size:var(--fs-xs);color:var(--color-muted);text-align:center;">图片标题</div>
</div>
```

---

### 20-2. `.m-filter-bar` — 移动端无边框筛选栏

替代 tab 样式用于商品列表筛选区，横向可滚动，按钮无边框无阴影。

```css
.m-filter-bar  { display:flex; align-items:center; padding:0 var(--sp4); border-bottom:var(--border); overflow-x:auto; gap:0; }
.m-filter-btn  { padding:var(--sp2) var(--sp3); font-size:var(--fs-sm); font-weight:700; color:var(--color-muted); white-space:nowrap; border:none; background:none; cursor:pointer; }
.m-filter-btn.active { color:var(--color-accent); border-bottom:2px solid var(--color-accent); }
.m-filter-sep  { color:var(--color-light); padding:var(--sp2) 0; flex-shrink:0; font-size:var(--fs-lg); }
```

```html
<div class="m-filter-bar">
  <button class="m-filter-btn active">All Platforms <i class="iconoir-nav-arrow-down icon-xs"></i></button>
  <span class="m-filter-sep">|</span>
  <button class="m-filter-btn">Sort by <i class="iconoir-nav-arrow-down icon-xs"></i></button>
  <span class="m-filter-sep">|</span>
  <button class="m-filter-btn">Price <i class="iconoir-nav-arrow-down icon-xs"></i></button>
</div>
```

---

### 20-3. `.sidebar-sub-item` — 侧边栏二级菜单项

用于左侧导航树，作为某个 `.sidebar-item` 的子级，缩进显示，不带图标。

```css
.sidebar-sub-item {
  display: flex;
  align-items: center;
  padding: var(--sp1) var(--sp3) var(--sp1) calc(var(--sp3) + 20px + var(--sp3));
  border-radius: var(--radius);
  cursor: pointer;
  font-size: var(--fs-sm);
  color: var(--color-muted);
  border: 2px solid transparent;
  user-select: none;
}
.sidebar-sub-item:hover  { color: var(--color-accent); background: var(--color-accent-bg); }
.sidebar-sub-item.active { color: var(--color-accent); border-color: var(--color-accent); background: var(--color-accent-bg); font-weight: 700; }
```

```html
<!-- sidebar-item 父级之后紧跟子级 -->
<div class="sidebar-item active" data-page="shop" onclick="switchPage('shop', this)">
  <i class="iconoir-menu-scale"></i> Last War
</div>
<div class="sidebar-sub-item" data-page="detail" onclick="switchPage('detail', this)">
  Product Details
</div>
```

> JS 联动：`switchPage` 需同时查询 `.sidebar-item` 和 `.sidebar-sub-item` 来做高亮切换：
> ```javascript
> document.querySelectorAll('.sidebar-item,.sidebar-sub-item').forEach(el => el.classList.remove('active'));
> ```



> 有截图 → **100% 跟截图**。下面规则只在无截图、需自行决策时使用。

| 场景 | 用色 | 例子 |
|---|---|---|
| **售前（突出转化）** | `var(--color-warning)` | PDP 标价 / 购物车小计 / 收银台总额 / 商品列表卡片价 |
| **售后（仅展示）** | 默认 `color-ink`（不写 color） | 订单列表价格 / 订单详情金额 / 余额 / 退款金额 / 历史账单 |
| **永远不要** | `var(--color-danger)` | danger 是纯状态色（失败 / 取消 / 删除 / 错误提示），**与价格无关** |

```html
<!-- 售前 -->
<div style="color:var(--color-warning);font-size:var(--fs-2xl);font-weight:700">$49.50</div>

<!-- 售后 -->
<div style="font-size:var(--fs-lg);font-weight:700">$49.50</div>
```
