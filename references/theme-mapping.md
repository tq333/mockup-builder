# Theme Mapping · 主题色识别规则

## 5 个可用主题

| 主题 | accent | accent-bg | accent-fg | 适用产品调性 |
|---|---|---|---|---|
| `default`（不设 data-theme） | `#0073cf` 蓝 | `#e6f1fa` | `#fff` | 通用 / 商务 / 工具 / SaaS / 政务 |
| `yellow` | `#ffbf00` 金黄 | `#fff8e5` | `#1a1a1a` | 餐饮 / 优惠促销 / 游戏 / 暖色品牌 |
| `green` | `#009e0f` 翠绿 | `#e6f5e7` | `#fff` | 健康 / 金融绿 / 环保 / 生鲜 |
| `purple` | `#9900ff` 紫 | `#f5e6ff` | `#fff` | 娱乐 / 创意 / Web3 / 美妆 |
| `pink` | `#ff00ff` 品红 | `#ffe6ff` | `#fff` | 时尚 / 萌宠 / 女性向 / 玩具 |

---

## 截图主色识别决策树

```
看截图主色（不是背景色，是 accent / 按钮 / logo / 链接的颜色）
│
├─ 蓝 (#0050~~#3399FF) / 灰蓝 / 青       → default
├─ 黄 / 金 / 暖橙 (#FF8800~#FFD700)      → yellow
├─ 绿 / 翠 / 薄荷 (#00A000~#66CC66)      → green
├─ 紫 / 靛 / 深紫红 (#6600CC~#CC00FF)    → purple
├─ 粉 / 品红 / 玫红 (#FF00CC~#FF66AA)    → pink
├─ 红色 (#CC0000~#FF3300)                → 用 default + 局部 .btn-danger
├─ 黑金 / 黑紫 等高对比深底              → default + body 背景置黑（特殊变体，见下）
└─ 不确定 / 多色混杂                     → default
```

## 文字描述识别规则

| 用户表述 | 选择 |
|---|---|
| 不提颜色 | `default` |
| "蓝色 / 商务蓝 / 经典蓝" | `default` |
| "黄 / 暖色 / 金色 / 阳光" | `yellow` |
| "绿色 / 自然 / 健康" | `green` |
| "紫色 / 神秘 / 梦幻" | `purple` |
| "粉色 / 少女 / 萌" | `pink` |
| "黑金 / 高端深色" | `default` + 局部 ink 黑底 hero |
| "红 / 警示" | `default` + 局部 `.btn-danger` |

## 兜底原则
- 不确定永远 `default`
- **绝不发明新主题色**（要新色让用户提到 mockup-kit 改 token）
- 截图含品牌 logo 时，识别 logo 颜色而非配图颜色

---

## 黑金 / 高对比深底场景的处理（特殊）

LootBar 那种黑金品牌，主题仍选 `default`，但允许在**单个区块**用 ink 黑底突出：

```html
<!-- Hero 黑底，但仍走 token -->
<div class="card" style="background:var(--color-ink);color:#fff;border-color:var(--color-ink)">
  <div class="card-body">
    <!-- 内部用 --color-warning 表达"金"的感觉 -->
    <div class="avatar" style="background:var(--color-warning);color:#fff">V5</div>
  </div>
</div>
```

⚠️ 红线：
- 整个 body 背景**不能**改黑（会破坏其他组件的对比度）
- 局部黑底**只**用在 hero / 强调卡，且该卡内部颜色仍走 token
- 如果整个 demo 都要黑的，提示用户："dark mode 不是规范现有能力，要加要先升级 mockup-kit"

---

## 如何识别截图主色（操作建议）

AI 看截图时按这个顺序找主色：
1. **CTA 按钮**的填充色（最高权重）
2. **Logo / Brand mark** 的颜色
3. 链接 / 高亮文字的颜色
4. Active tab / selected nav 的颜色
5. 装饰性大色块（如 hero 背景）

忽略：
- 中性色（黑/白/灰）
- 警告色（红/橙警告）—— 这是语义色不是主题色
- 真实图片 / 照片中的颜色
