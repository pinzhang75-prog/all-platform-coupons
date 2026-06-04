# 全平台优惠券汇总

> 实时更新的全平台CPS优惠信息聚合项目，涵盖外卖、出行、快递、电影票、酒店旅游、网购、话费会员等7大生活领域。

## 📌 项目简介

本项目汇总各大平台的优惠领取链接，帮助用户在日常生活中省钱。所有链接持续更新，欢迎社区贡献。

## 🤖 Skill 安装

本项目提供 Codex Skill，支持在任何 Codex 智能体中安装使用。

### 安装方式

将 `SKILL.md`、`scripts/`、`agents/`、`references/` 文件夹复制到 Codex skills 目录：

```
~/.codex/skills/cps-coupons/
├── SKILL.md              # Skill 说明
├── scripts/
│   └── fetch_coupons.py # 查询脚本
├── agents/
│   └── openai.yaml      # UI 元数据
└── references/
    └── coupons-cache.json # 本地缓存
```

### 使用方式

安装后，在 Codex 对话中直接使用以下关键词触发：

- **查品类**：`"查外卖优惠"`、`"查打车优惠"`、`"查快递优惠"`
- **查平台**：`"查美团优惠"`、`"查京东优惠"`、`"查滴滴优惠"`
- **查全部**：`"查全平台优惠"`、`"所有优惠券"`

### 脚本独立使用

```bash
# 列出所有品类
python scripts/fetch_coupons.py --list

# 按品类查询
python scripts/fetch_coupons.py --category waimai

# 搜索平台
python scripts/fetch_coupons.py --search "美团"
```

## 📂 目录结构

```
├── README.md              # 项目说明
├── SKILL.md               # Skill 说明（Codex 智能体用）
├── scripts/
│   └── fetch_coupons.py  # 优惠券查询脚本
├── agents/
│   └── openai.yaml       # UI 元数据
├── references/
│   └── coupons-cache.json # 本地缓存数据
└── data/
    ├── waimai.json        # 外卖优惠
    ├── chuxing.json       # 出行优惠
    ├── kuaidi.json        # 快递优惠
    ├── dianying.json      # 电影票优惠
    ├── jiudian.json       # 酒店旅游优惠
    ├── wanggou.json      # 网购查券
    └── huafei.json        # 话费会员
```

## 🔗 优惠类型说明

| 类型 | 说明 | 打开方式 |
|------|------|--------|
| H5 | 网页链接 | 浏览器直接打开 |
| 口令 | 淘宝/微信口令 | 复制到对应APP打开 |
| 小程序 | 微信小程序 | 复制到微信打开 |

## 🚀 使用方式

### 方式一：Codex Skill
安装 Skill 后，直接在对话中查询优惠链接。

### 方式二：直接查看
直接查看 `data/` 目录下的对应品类JSON文件，获取最新优惠链接。

### 方式三：API 调用
```bash
# 获取全品类数据
curl https://api.github.com/repos/pinzhang75-prog/all-platform-coupons/contents/data/

# 获取具体品类
curl https://raw.githubusercontent.com/pinzhang75-prog/all-platform-coupons/main/data/waimai.json
```

## 🤝 欢迎贡献

如果你有新的优惠信息，欢迎提交PR更新！

## 📜 License

MIT License
