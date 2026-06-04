---
name: cps-coupons
description: 全平台CPS优惠券查询工具。当用户需要查询外卖、出行、快递、电影票、酒店旅游、网购查券、话费会员等平台的优惠链接时使用。支持按品类查询、按平台查询、获取CPS推广链接。触发词：优惠券、CPS、外卖优惠、打车优惠、快递优惠、电影票优惠、酒店优惠、网购查券、话费充值、优惠链接、省钱攻略、红包领取。
---

# CPS优惠券查询

查询全平台CPS优惠链接，涵盖7大生活品类。

## 数据源

所有优惠数据存储在GitHub仓库：`https://api.github.com/repos/pinzhang75-prog/all-platform-coupons/contents/data/`

## 品类列表

| 品类 | 关键词 | 数据文件 |
|------|--------|---------|
| 外卖 | 外卖、美团、京东、饿了么、淘宝闪购 | `waimai.json` |
| 出行 | 打车、顺风车、滴滴、高德、花小猪、T3、哈罗、携程、同程、飞猪、机票、火车票 | `chuxing.json` |
| 快递 | 快递、顺丰、京东、货拉拉、丰巢、菜鸟、UU跑腿、闪送 | `kuaidi.json` |
| 电影票 | 电影票、淘票票、猫眼、电影 | `dianying.json` |
| 酒店旅游 | 酒店、旅游、民宿、飞猪、携程、同程、美团酒店、景点门票 | `jiudian.json` |
| 网购查券 | 网购、查券、拼多多、京东、淘宝、唯品会 | `wanggou.json` |
| 话费会员 | 话费、充值、流量卡、会员、充电、加油 | `huafei.json` |

## 使用流程

1. 识别用户需求的品类
2. 通过GitHub API获取对应JSON数据
3. 解析并返回匹配的优惠链接
4. 标注每种链接的打开方式（H5/口令/小程序）

## 查询方式

### 按品类查询
用户说"外卖优惠"→ 返回 `waimai.json` 中所有平台链接

### 按平台查询
用户说"美团"→ 在所有品类JSON中搜索"美团"，返回匹配项

### 全平台查询
用户说"全平台"或"所有优惠"→ 返回所有7个品类的数据

## 输出格式

每个优惠链接按以下格式返回：

```
📌 [平台名称] — [品类]
🔗 链接：[URL]
📱 打开方式：[H5直接打开 / 复制口令到微信 / 复制链接到微信]
📝 说明：[优惠描述]
```

## 链接类型说明

| 类型 | 标识 | 打开方式 |
|------|------|---------|
| H5网页 | `type: "h5"` | 浏览器直接打开 |
| 口令 | `type: "command"` | 复制口令到对应APP（微信/淘宝） |
| 小程序 | `type: "miniprogram"` | 复制链接到微信打开 |

## 数据获取脚本

使用 `scripts/fetch_coupons.py` 从GitHub API获取最新数据：

```bash
python scripts/fetch_coupons.py --category waimai
python scripts/fetch_coupons.py --category all
python scripts/fetch_coupons.py --search "美团"
```

## 注意事项

- 数据实时从GitHub获取，确保链接最新
- 返回链接时务必标注打开方式
- 如果GitHub API限流，使用本地缓存（`references/coupons-cache.json`）
- 不要修改或伪造优惠链接
