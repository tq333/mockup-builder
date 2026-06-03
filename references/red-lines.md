# Red Lines · 红线 & Anti-Patterns

> 这个 skill 是产 wireframe 的，不是产视觉稿的。
> 所有"让 demo 更漂亮"的冲动都要克制——**精致是 Figma 的事**。

## Priority 1 — CRITICAL（必须）

| 规则 | 必须做 | 绝对禁止 |
|---|---|---|
| **颜色** | 全部 `var(--color-*)` token | 任何 `#xxx` / `rgb(...)` 硬编码 |
| **图标** | 100% iconoir `<i class="iconoir-*">` | emoji（🎂🚀⚙️）/ 自画 SVG / 真实品牌 logo |
| **字体** | 只用 `Balsamiq Sans` 默认栈 | 改字体（除非用户明确要求且写到 SKILL 用户偏好） |
| **保真** | 截图里有什么就还原什么；信息层级不清晰时**保持纯文本+冒号** | 截图里没有的视觉装饰一律不能加：补 icon、加 tag、加高亮、补缺失的 row、加底部链接组、加 hover 提示等 |
| **组件原样使用** | 规范组件直接用，所有 token 走默认值 | 给规范组件覆写 `background` / `border-color` / `color`（例如把 `.avatar` 灰底改成 accent 黄底）。要 accent 色版本，请用 kit 已定义的变体（`.tag-accent` / `.btn-primary` / `.badge-blue` 等） |
| **价格语义** | 有截图 → 100% 跟截图。无截图：售前（PDP / 购物车 / 收银台 / 商品列表）用 `color:var(--color-warning)`；售后（订单列表 / 订单详情 / 余额 / 退款）用默认 `color-ink`（不写 color） | 把 `color-danger` 当价格色（danger 是失败/取消/删除等状态色，与价格无关）；售后场景给价格强加颜色高亮 |

## Priority 2 — HIGH（强烈建议）

| 规则 | 必须做 | 绝对禁止 |
|---|---|---|
| **组件类名** | 用 `.btn` / `.card` / `.list` / `.accordion` 等规范类 | 自创 `.my-button` / `.special-card` 等 |
| **间距** | `var(--sp1)` 到 `var(--sp12)` | 任意 `padding:13px` / `margin:7px` |
| **字号** | `var(--fs-xs)` 到 `var(--fs-3xl)` | 任意 `font-size:17px` |
| **阴影** | `var(--shadow)` / `var(--shadow-sm)` | 自写 `box-shadow:0 4px 8px rgba(...)` |
| **边框** | `var(--border)` | 自写 `border:1px solid #ccc` |

## Priority 3 — MEDIUM（约定）

| 规则 | 必须做 | 应避免 |
|---|---|---|
| **页面专属样式** | 写在文件 `<style>` 末尾 `/* PAGE-SPECIFIC */` 区块 | 散落在各处、与组件类同名 |
| **图标风格** | 全部 outline | 混用 outline + filled |
| **动效** | 仅保留模板自带的微动效（hover / chev 旋转） | 加 fadeIn / parallax / 复杂 keyframes |
| **图片** | 用 `.img-ph` 或简单几何占位 | 拉真实图片、stock photo |

## Priority 4 — LOW（细节优化）

- 主题切换后能正常渲染（在 console 切几个主题验证）
- 多方案 / 多页面侧栏标题准确反映用户语境
- 区块之间用 `var(--sp5)` ~ `var(--sp8)` 间距，节奏一致
- 长文本走 `line-height:1.6~1.8`

---

## Anti-Patterns 反例库

### ❌ 不要这样
```html
<!-- 1. emoji 当图标 -->
<button>🎁 Coupon</button>

<!-- 2. 硬编码颜色 -->
<div style="background:#fff8e5;color:#ffbf00">VIP</div>

<!-- 3. 自创组件类 -->
<div class="vip-banner-special">...</div>

<!-- 4. 任意 px -->
<div style="padding:18px 22px;font-size:15.5px">...</div>

<!-- 5. 复杂视觉效果 -->
<div style="background:linear-gradient(135deg,#0073cf,#9900ff);
  backdrop-filter:blur(10px);box-shadow:0 8px 32px rgba(0,0,0,.2)">
  Glassmorphism Hero
</div>

<!-- 6. 真实品牌 logo -->
<img src="https://cdn.lootbar.gg/logo.png">

<!-- 7. 一堆装饰动画 -->
<div style="animation:bounce 2s infinite ease-in-out">

<!-- 8. 截图里没有的视觉装饰（"AI 加戏"） -->
<!-- 截图里 Delivery Method 是纯文字 -->
<div class="v"><span class="tag tag-accent"><i class="iconoir-flash"></i> Instant Activation</span></div>
<!-- 截图里没有的底部 helper 链接组 -->
<div><a>How to activate</a> · <a>Request refund</a> · <a>Contact support</a></div>

<!-- 9. 给规范组件覆写颜色 -->
<div class="avatar avatar-lg"
     style="background:var(--color-accent);color:var(--color-accent-fg);border-color:var(--color-accent)">TQ</div>
```

### 价格颜色场景对照

```html
<!-- ❌ 售后场景把价格涂色 -->
<!-- 订单详情、订单列表、余额、退款金额 -->
<div class="balance" style="color:var(--color-warning)">$1.000.025,00</div>

<!-- ✅ 售后用默认 ink 即可（截图也是这样） -->
<div class="balance">$1.000.025,00</div>

<!-- ✅ 售前才用 warning 突出转化 -->
<!-- 商品详情页 / 购物车 / 收银台 / 商品列表 -->
<div class="pdp-price" style="color:var(--color-warning);font-size:var(--fs-2xl);font-weight:700">$49.50</div>

<!-- ❌ 把 danger 当价格色（danger 只用于状态：失败/取消/删除） -->
<div class="pdp-price" style="color:var(--color-danger)">$49.50</div>
```

---

## Phone Frame & Multi-page Demo 规则（从实际问题中提炼）

### R1 — Overlay 定位：必须用 `position:absolute`，禁止 `position:fixed`

在 `.phone-frame` 内部渲染任何浮层（bottom-sheet / modal / scrim），一律用 `position:absolute`。
`.phone-frame` 自身须保有 `position:relative` + `overflow:hidden`。

```html
<!-- ✅ 正确：overlay 在 phone-frame 内 absolute -->
<div class="phone-frame" style="position:relative;overflow:hidden;">
  ...
  <div id="scrim" style="position:absolute;inset:0;background:rgba(0,0,0,.45);z-index:100;"></div>
  <div id="sheet" style="position:absolute;left:0;right:0;bottom:0;z-index:101;">...</div>
</div>

<!-- ❌ 错误：fixed 会冲出 phone-frame，覆盖整个浏览器视口 -->
<div id="sheet" style="position:fixed;bottom:0;">...</div>
```

---

### R2 — Auto-hide Topbar：只用 `transform`，禁止同时改 `margin-top`

正确模式：header 改为 `position:absolute`，body 用 `padding-top` 预留空间，动画只改 `transform`。

```html
<!-- HTML 结构 -->
<div class="m-screen-inner" style="position:relative;">
  <div id="topbar" style="position:absolute;top:0;left:0;right:0;z-index:10;
       transition:transform .28s cubic-bezier(.4,0,.2,1), box-shadow .28s ease;">
    <!-- 顶部导航内容 -->
  </div>
  <div id="body-scroll" style="/* padding-top 由 JS 初始化 */overflow-y:auto;">
    <!-- 页面内容 -->
  </div>
</div>
```

```js
// JS 初始化 + 滚动监听
const headerEl = document.getElementById('topbar');
const scrollEl = document.getElementById('body-scroll');
scrollEl.style.paddingTop = headerEl.offsetHeight + 'px';    // 预留空间

let lastST = 0, visible = true, ticking = false;
scrollEl.addEventListener('scroll', () => {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => {
    const st = scrollEl.scrollTop;
    if (st > lastST && st > 10 && visible) {
      visible = false;
      headerEl.style.transform = 'translateY(-100%)';
      headerEl.style.boxShadow = 'none';            // ← 同步消除阴影（见 R3）
    } else if (st < lastST && !visible) {
      visible = true;
      headerEl.style.transform = 'translateY(0)';
      headerEl.style.boxShadow = '';
    }
    lastST = st <= 0 ? 0 : st;
    ticking = false;
  });
});
```

**禁止的方案：**
```js
// ❌ transform + margin-top 双属性并行 → reflow 时序错位闪烁
headerEl.style.transform = 'translateY(-100%)';
headerEl.style.marginTop = '-' + h + 'px';

// ❌ max-height 过渡 → 从底部塌陷，不是滑出效果
clipEl.style.maxHeight = '0';
```

---

### R3 — `box-shadow` 不受 `overflow:hidden` 裁切

CSS 规范中 `overflow:hidden` **不裁切子元素的 `box-shadow`**（shadow 渲染在 border-box 外部）。
当 `position:absolute` 的元素做 show/hide 动画时，若有 `box-shadow`，shadow 会在元素滑走后残留。

**修法：** 将 `box-shadow` 加入 transition，隐藏时同步置为 `none`。

```js
// ✅ 隐藏时同步去掉阴影
headerEl.style.transform = 'translateY(-100%)';
headerEl.style.boxShadow = 'none';

// ✅ 显示时恢复（空字符串 = 回归 CSS 规则）
headerEl.style.transform = 'translateY(0)';
headerEl.style.boxShadow = '';
```

```html
<!-- ✅ transition 要包含 box-shadow -->
<div style="transition: transform .28s ease, box-shadow .28s ease;">
```

---

### R4 — 多页 Demo 的 sidebar active 状态

多页 Demo 中每个独立 HTML 文件负责自己的 sidebar，对应当前页的 `sidebar-item` / `sidebar-sub-item` 加 `active`。
新增页面时须**同步更新所有其他页面**的 sidebar。

```html
<!-- home.html 中 -->
<a class="sidebar-item active" href="home.html">Home</a>   <!-- ← 当前页 active -->
<a class="sidebar-item"        href="shop.html">Shop</a>

<!-- shop.html 中 -->
<a class="sidebar-item"        href="home.html">Home</a>
<a class="sidebar-item active" href="shop.html">Shop</a>   <!-- ← 当前页 active -->
```

---

### R5 — 独立页面 vs 页内 Overlay 的选择规则

> **左侧菜单中有对应导航项 = 必须做成独立 HTML 文件。这是不可违反的约定。**

| 场景 | 做法 |
|---|---|
| **左侧菜单中有对应导航项** | 必须做成独立 HTML 文件；sidebar 对应项加 `active` |
| 仅演示手机内交互动效，不需要菜单导航 | 可在同一 HTML 内用 `position:absolute` overlay |
| 两者都需要（菜单可跳转 + 有底部滑出效果） | 独立 HTML + `DOMContentLoaded` 时自动触发 overlay 动画 |

```js
// 独立页面（如 offer.html）：加载即自动展开 sheet
document.addEventListener('DOMContentLoaded', () => openSheet());
```

**反例：**
```js
// ❌ 左侧菜单项 onclick 触发 overlay，不做独立 HTML
<a onclick="openOfferSheet()">Offer Details</a>

// ✅ 左侧菜单项指向独立 HTML
<a href="offer.html">Offer Details</a>
```

### ✅ 应该这样
```html
<!-- 1. iconoir 图标 -->
<button class="btn"><i class="iconoir-gift"></i> Coupon</button>

<!-- 2. token 颜色 -->
<div class="tag tag-accent">VIP</div>
<!-- 或局部主题 -->
<body data-theme="yellow">

<!-- 3. 用规范类拼装 -->
<div class="card"><div class="card-body">VIP Banner content</div></div>

<!-- 4. spacing scale -->
<div style="padding:var(--sp4) var(--sp5);font-size:var(--fs-md)">

<!-- 5. wireframe 风格 -->
<div class="card" style="background:var(--color-ink);color:#fff">
  <div class="card-body">Hero content (wireframe-style)</div>
</div>

<!-- 6. 文字占位 -->
<a class="navbar-brand"><i class="iconoir-treasure-chest"></i> brand.gg</a>

<!-- 7. 不加自定义动画 -->
<!-- 模板已有 hover transform / chev rotate，足够了 -->

<!-- 8. 截图没有的装饰，宁缺勿滥 -->
<div class="v">Instant Activation</div>
<!-- 真没把握就用纯文字 + 冒号，wireframe 不需要"视觉提示" -->

<!-- 9. 想要"被强调的头像"，用规范变体 -->
<!-- 用户头像就是普通 .avatar；要表达"图片本身"用 .img-ph -->
<div class="avatar avatar-lg">TQ</div>
<!-- 或： -->
<div class="img-ph" style="width:64px;height:64px;border-radius:50%">[ User ]</div>
```

---

## 灵魂条款

> 用户说"改一下结构"→ 改 body
> 用户说"换个主题"→ 切 `body[data-theme]`
> 用户说"加个新区块"→ 用规范组件拼
> 用户说"这个按钮换成红色"→ 用 `.btn-danger`，不要写 `style="background:red"`
> 用户说"做得再精致一点"→ 反问："你是希望进 Figma 二次设计，还是有具体的结构 / 信息层级要调整？"

如果实在拗不过用户要硬上视觉效果，**告诉他：这是规范级修改，建议提到 mockup-kit.html 里**。
