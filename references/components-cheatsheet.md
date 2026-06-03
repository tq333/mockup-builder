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

### Checkbox / Radio / Toggle
- `.ck-wrap` + `.ck-box` checkbox（已选加 `.checked`，内放 `<i class="iconoir-check">`）
- `.ck-wrap` + `.radio-box` radio（已选加 `.checked`，用 `::after` 实心圆）
- `.toggle-wrap` + `.toggle-track` + `.toggle-thumb` switch（开启时给 `.toggle-track` 加 `.on`）

```html
<label class="ck-wrap">
  <div class="ck-box checked"><i class="iconoir-check" style="font-size:11px;"></i></div>
  Checked option
</label>
<div class="toggle-wrap">
  <div class="toggle-track on"><div class="toggle-thumb"></div></div>
  <span>Enabled</span>
</div>
```

### Slider（静态视觉占位）

> ⚠️ **必须用三层 div，禁止用 `<input type="range">`**。`<input type="range">` 不是规范组件，样式无法统一。

```html
<div class="mock-slider" style="width:240px;">
  <div class="mock-slider-fill" style="width:70%;"></div>
  <div class="mock-slider-thumb" style="left:calc(70% - 9px);"></div>
</div>
<!-- 轨道高 6px，填充为 accent 色，拇指 18×18 圆形绝对定位 top:-8px -->
```

### Quantity Stepper

```html
<div class="qty">
  <button class="qty-btn"><i class="iconoir-minus" style="font-size:16px;"></i></button>
  <input class="qty-value" type="number" value="1" min="1">
  <button class="qty-btn"><i class="iconoir-plus"  style="font-size:16px;"></i></button>
</div>
```

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

> ⚠️ **Accordion 分隔线用 `var(--color-light)`（浅灰），不是 `var(--border)`（黑色）**。

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
<!-- Tab 风格 1：方形 box（active = accent-bg 背景 + accent 文字） -->
<div class="tabs">
  <a class="tab-item active">Tab 1</a>
  <a class="tab-item">Tab 2</a>
</div>
<!-- Tab 风格 2：下划线 line（⚠️ active = 黑色 border-bottom，即 color-ink，不是 accent 色） -->
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

<!-- Stepper（水平，桌面） -->
<div class="stepper">
  <div class="step"><div class="step-circle done"><i class="iconoir-check"></i></div><div class="step-label">Done</div></div>
  <div class="step-line done"></div>
  <div class="step"><div class="step-circle active">2</div><div class="step-label">Active</div></div>
  <div class="step-line"></div>
  <div class="step"><div class="step-circle">3</div><div class="step-label">Next</div></div>
</div>
```

### Stepper · Mobile Vertical（移动端纵向）

默认只显示 **当前节点 + 下一节点**；点击展开按钮展示全部，无收起。

- 完成态连接线：`.m-step-vline.done`（accent 色）
- 当前节点：`.step-circle.active`
- 隐藏节点：`.m-step.m-step-hidden`（`display:none`，JS 展开后设为 `display:flex`）
- 最后一个节点无需 `.m-step-vline`

```html
<div class="m-stepper">
  <!-- done -->
  <div class="m-step">
    <div class="m-step-track">
      <div class="step-circle done"><i class="iconoir-check" style="font-size:13px"></i></div>
      <div class="m-step-vline done"></div>
    </div>
    <div class="m-step-content">
      <div class="m-step-title">Order Placed</div>
      <div class="m-step-sub">Jun 1 · 09:42</div>
    </div>
  </div>
  <!-- active (current) -->
  <div class="m-step">
    <div class="m-step-track">
      <div class="step-circle active">2</div>
      <div class="m-step-vline"></div>
    </div>
    <div class="m-step-content">
      <div class="m-step-title">Payment Confirmed</div>
      <div class="m-step-sub">In progress</div>
    </div>
  </div>
  <!-- next (shown by default) -->
  <div class="m-step">
    <div class="m-step-track">
      <div class="step-circle">3</div>
      <div class="m-step-vline"></div>
    </div>
    <div class="m-step-content">
      <div class="m-step-title">Seller Processing</div>
      <div class="m-step-sub">Next step</div>
    </div>
  </div>
  <!-- hidden steps -->
  <div class="m-step m-step-hidden">
    <div class="m-step-track">
      <div class="step-circle">4</div>
      <div class="m-step-vline"></div>
    </div>
    <div class="m-step-content">
      <div class="m-step-title">Account Transferred</div>
      <div class="m-step-sub">Pending</div>
    </div>
  </div>
  <div class="m-step m-step-hidden">
    <div class="m-step-track"><div class="step-circle">5</div></div>
    <div class="m-step-content">
      <div class="m-step-title">Order Complete</div>
      <div class="m-step-sub">Pending</div>
    </div>
  </div>
  <!-- expand trigger（无收起） -->
  <button class="m-stepper-expand" onclick="(function(btn){btn.closest('.m-stepper').querySelectorAll('.m-step-hidden').forEach(function(s){s.style.display='flex';});btn.style.display='none';})(this)">
    <i class="iconoir-nav-arrow-down icon-xs"></i>&nbsp;View all 5 steps
  </button>
</div>
```

## 11. Avatar / Badge / Tag
- `.avatar` 默认 36px；`.avatar-xs` 24px / `.avatar-sm` 32px / `.avatar-md` 44px / `.avatar-lg` 64px
- 加 `.avatar-sq` 变方形（默认圆形）
- `.badge` 红 / `.badge-blue` accent 蓝 / `.badge-green` / `.badge-gray`
- `.tag` 普通 / `.tag-filled` / `.tag-accent` / `.tag-danger` / `.tag-success` / `.tag-warning`

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
- `.bottom-sheet-wrap` + `.bottom-sheet` > `.sheet-handle-wrap` > `.sheet-handle`（把手） + `.sheet-body` > `.sheet-item`（列表行）
- `.dropdown-menu` + `.dropdown-item`
- `.popover` + `.popover-title`/`.popover-text`
- `.tooltip-box`

> ⚠️ `.sheet-handle-wrap` 是必需的把手区容器，**不能直接把 `.sheet-handle` 放在 `.bottom-sheet` 根级**。Sheet 内部列表行用 `.sheet-item`，内容 `.h` + `.list-item-content` + `.list-item-action`。

```html
<!-- Bottom Sheet 完整结构 -->
<div class="bottom-sheet-wrap">
  <div class="bottom-sheet">
    <div class="sheet-handle-wrap">
      <div class="sheet-handle"></div>
    </div>
    <div class="sheet-body">
      <div class="sheet-item">
        <i class="iconoir-XXX"></i>
        <div class="list-item-content">
          <div class="list-item-title">标题</div>
          <div class="list-item-sub">副标题</div>
        </div>
        <i class="iconoir-nav-arrow-right list-item-action"></i>
      </div>
    </div>
  </div>
</div>
```

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

## 16-A. Auto-hide Topbar（移动端滚动隐藏导航）

> 正确实现：header `position:absolute` + body `padding-top`，动画只用 `transform`。
> 详细规则与禁止方案见 `red-lines.md § R2 / R3`。

```html
<div class="m-screen-inner" style="position:relative;">
  <div id="topbar" class="m-topbar"
    style="position:absolute;top:0;left:0;right:0;z-index:10;
           transition:transform .28s cubic-bezier(.4,0,.2,1),box-shadow .28s ease;">
    <!-- 导航内容 -->
  </div>
  <div id="body-scroll" class="m-body"><!-- padding-top 由 JS 设置 --></div>
</div>
```

```js
const h = document.getElementById('topbar');
const s = document.getElementById('body-scroll');
s.style.paddingTop = h.offsetHeight + 'px';
let last=0,vis=true,tick=false;
s.addEventListener('scroll',()=>{
  if(tick)return; tick=true;
  requestAnimationFrame(()=>{
    const st=s.scrollTop;
    if(st>last&&st>10&&vis){ vis=false; h.style.transform='translateY(-100%)'; h.style.boxShadow='none'; }
    else if(st<last&&!vis){ vis=true; h.style.transform=''; h.style.boxShadow=''; }
    last=st<=0?0:st; tick=false;
  });
});
```

## 16-B. Phone Frame Overlay（底部浮层 / 遮罩）

> Overlay 必须在 `.phone-frame` 内，用 `position:absolute`，禁止 `position:fixed`。
> 详细规则见 `red-lines.md § R1`。

```html
<div class="phone-frame" style="position:relative;overflow:hidden;">
  <!-- 页面主内容 -->

  <!-- Scrim -->
  <div id="scrim" onclick="closeSheet()"
    style="display:none;position:absolute;inset:0;background:rgba(0,0,0,.45);z-index:100;"></div>

  <!-- Bottom Sheet -->
  <div id="sheet" style="
    display:none;position:absolute;left:0;right:0;bottom:0;z-index:101;
    flex-direction:column;max-height:92%;
    background:var(--color-surface);border-top:var(--border);
    transform:translateY(100%);
    transition:transform .3s cubic-bezier(.4,0,.2,1);">
    <!-- sheet 内容 -->
  </div>
</div>
```

```js
function openSheet(){
  const scrim=document.getElementById('scrim');
  const sheet=document.getElementById('sheet');
  scrim.style.display='block';
  sheet.style.display='flex';
  void sheet.offsetWidth;          // force reflow
  sheet.style.transform='translateY(0)';
}
function closeSheet(){
  const sheet=document.getElementById('sheet');
  sheet.style.transform='translateY(100%)';
  setTimeout(()=>{
    sheet.style.display='none';
    document.getElementById('scrim').style.display='none';
  },300);
}
```

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

## 19. Media Placeholders — 图片 / 视频 / 地图占位

所有占位块使用同一个 `.img-ph` 类，通过 `style` 控制尺寸和内容。

> ⚠️ `mockup-kit.html` 里已定义 `.img-ph`，但**独立 demo 文件必须自带此 CSS**，否则白色空白。

```css
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

**6 种标准变体：**

```html
<!-- Image 16:9 -->
<div class="img-ph" style="width:100%;aspect-ratio:16/9;">[ Image ]</div>

<!-- Image 1:1 -->
<div class="img-ph" style="width:120px;height:120px;">[ Image ]</div>

<!-- Video 16:9（含播放图标） -->
<div class="img-ph" style="width:100%;aspect-ratio:16/9;flex-direction:column;gap:4px;">
  <i class="iconoir-play" style="font-size:32px;opacity:.4;"></i>
  <span>[ Video ]</span>
</div>

<!-- Map（含定位图标） -->
<div class="img-ph" style="width:100%;height:160px;flex-direction:column;gap:4px;">
  <i class="iconoir-map-pin" style="font-size:32px;opacity:.4;"></i>
  <span>[ Map ]</span>
</div>

<!-- Profile Banner（宽横幅） -->
<div class="img-ph" style="width:100%;height:80px;">[ Cover Banner ]</div>

<!-- Ad Slot（虚线边框） -->
<div class="img-ph" style="width:300px;height:60px;border-style:dashed;">[ Ad Slot · 300×60 ]</div>
```

> 需要在图片下方显示标题时，套一层 flex 列：
> ```html
> <div style="display:flex;flex-direction:column;gap:var(--sp1);">
>   <div class="img-ph" style="height:72px;">[ Image ]</div>
>   <div style="font-size:var(--fs-xs);color:var(--color-muted);text-align:center;">图片标题</div>
> </div>
> ```

---

## 20. Filter Bar — 无边框筛选栏

适用于任何平台的列表筛选区（桌面 / 移动端通用），横向可滚动，按钮无边框无阴影。与 `.tabs` 的区别：tabs 有下划线选中态且互斥；filter bar 更轻量，可多选/下拉组合。

```css
.filter-bar     { display:flex; align-items:center; border-bottom:var(--border); overflow-x:auto; gap:0; background:var(--color-surface); }
.filter-btn     { display:inline-flex; align-items:center; gap:3px; padding:var(--sp2) var(--sp3); font-family:var(--font-base); font-size:var(--fs-sm); font-weight:700; color:var(--color-ink); background:transparent; border:none; cursor:pointer; white-space:nowrap; }
.filter-btn.active { color:var(--color-accent); }
.filter-sep     { color:var(--color-light); padding:0 2px; font-size:var(--fs-sm); flex-shrink:0; }
```

```html
<div class="filter-bar">
  <button class="filter-btn active">All Platforms <i class="iconoir-nav-arrow-down icon-xs"></i></button>
  <span class="filter-sep">|</span>
  <button class="filter-btn">Sort by <i class="iconoir-nav-arrow-down icon-xs"></i></button>
  <span class="filter-sep">|</span>
  <button class="filter-btn">Price <i class="iconoir-nav-arrow-down icon-xs"></i></button>
  <!-- 右对齐额外操作（如全局 Filter 按钮）-->
  <div style="margin-left:auto;flex-shrink:0;">
    <button class="filter-btn"><i class="iconoir-filter-list icon-xs"></i> Filter</button>
  </div>
</div>
```

---

## 21. Sidebar Nav — 侧边栏导航（含二级菜单）

**适用场景：** Demo shell 左侧导航树（桌面 / 宽屏页面方案对比），非 `template-multi.html` 的 TOC 列表。

### 两种模板选择

| 模板 | 适用 | 启动命令 |
|---|---|---|
| `template-base.html` | 单页面，无需左侧导航 | `python3 scripts/new_demo.py out.html` |
| `template-multi.html` | **多方案平铺**，左侧 TOC + ScrollSpy 自动高亮，页面全部展开可对比 | `python3 scripts/new_demo.py out.html --multi` |

> `template-multi.html` 的 TOC 用 `.shell-toc a` 类，由 ScrollSpy 自动驱动高亮，**不需要手写 `switchPage` JS**。适合"方案 A / B / C 对比"场景。
>
> 如果需要"点击切换、只显示当前页"的 Demo Shell（如 App 原型），需自建 `.sidebar-item` + `switchPage` JS，参见下方。

### App Demo Shell 侧边栏（手动 switchPage）

一级菜单 `.sidebar-item` + 二级菜单 `.sidebar-sub-item`（缩进，无图标）：

```css
.sidebar-item {
  display:flex; align-items:center; gap:var(--sp3);
  padding:var(--sp2) var(--sp3); border-radius:var(--radius); cursor:pointer;
  font-size:var(--fs-sm); font-weight:700; color:var(--color-muted);
  border:2px solid transparent; user-select:none;
}
.sidebar-item:hover  { color:var(--color-ink); background:var(--color-bg); }
.sidebar-item.active { color:var(--color-accent); border-color:var(--color-accent); background:var(--color-accent-bg); }

.sidebar-sub-item {
  display:flex; align-items:center;
  padding:var(--sp1) var(--sp3) var(--sp1) calc(var(--sp3) + 20px + var(--sp3));
  border-radius:var(--radius); cursor:pointer;
  font-size:var(--fs-sm); color:var(--color-muted);
  border:2px solid transparent; user-select:none;
}
.sidebar-sub-item:hover  { color:var(--color-accent); background:var(--color-accent-bg); }
.sidebar-sub-item.active { color:var(--color-accent); border-color:var(--color-accent); background:var(--color-accent-bg); font-weight:700; }
```

```html
<div class="sidebar-item active" data-page="shop" onclick="switchPage('shop', this)">
  <i class="iconoir-menu-scale"></i> Last War
</div>
<!-- 紧跟父级后面，缩进显示 -->
<div class="sidebar-sub-item" data-page="detail" onclick="switchPage('detail', this)">
  Product Details
</div>
```

**switchPage JS 需同时清除两种类的 active：**
```javascript
document.querySelectorAll('.sidebar-item,.sidebar-sub-item').forEach(el => el.classList.remove('active'));
```



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
