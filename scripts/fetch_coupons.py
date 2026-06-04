#!/usr/bin/env python3
"""
CPS优惠券查询脚本
从GitHub API获取全平台优惠券数据
"""

import json
import sys
import urllib.request
import urllib.error
import os
import argparse

GITHUB_API = "https://api.github.com/repos/pinzhang75-prog/all-platform-coupons/contents/data"
RAW_BASE = "https://raw.githubusercontent.com/pinzhang75-prog/all-platform-coupons/main/data"
CACHE_FILE = os.path.join(os.path.dirname(__file__), "..", "references", "coupons-cache.json")

CATEGORIES = {
    "waimai": "外卖",
    "chuxing": "出行",
    "kuaidi": "快递",
    "dianying": "电影票",
    "jiudian": "酒店旅游",
    "wanggou": "网购查券",
    "huafei": "话费会员",
}


def fetch_from_github(filename):
    """从GitHub raw内容获取JSON数据"""
    url = f"{RAW_BASE}/{filename}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "cps-coupons-skill"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None


def load_cache():
    """加载本地缓存"""
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def save_cache(data):
    """保存本地缓存"""
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_all_data():
    """获取所有品类数据"""
    cache = load_cache()
    if cache:
        return cache

    data = {}
    for key in CATEGORIES:
        result = fetch_from_github(f"{key}.json")
        if result:
            data[key] = result

    if data:
        save_cache(data)
    return data


def query_category(category_key, keyword=None):
    """按品类查询"""
    data = get_all_data()
    if category_key == "all":
        return data

    if category_key in data:
        result = data[category_key]
        if keyword:
            filtered = [
                p for p in result.get("platforms", [])
                if keyword.lower() in p.get("name", "").lower()
                or keyword.lower() in p.get("description", "").lower()
            ]
            result = {**result, "platforms": filtered}
        return {category_key: result}
    return {}


def search_platform(platform_name):
    """跨品类搜索平台"""
    data = get_all_data()
    results = {}
    for key, category_data in data.items():
        matched = [
            p for p in category_data.get("platforms", [])
            if platform_name.lower() in p.get("name", "").lower()
            or platform_name.lower() in p.get("description", "").lower()
        ]
        if matched:
            results[key] = {**category_data, "platforms": matched}
    return results


def format_output(results):
    """格式化输出"""
    if not results:
        return "未找到匹配的优惠信息。"

    lines = []
    for key, data in results.items():
        category_name = data.get("category", CATEGORIES.get(key, key))
        lines.append(f"\n{'='*40}")
        lines.append(f"📦 {category_name}")
        lines.append(f"{'='*40}")

        for p in data.get("platforms", []):
            link_type = p.get("type", "h5")
            if link_type == "h5":
                tip = "🌐 浏览器直接打开"
            elif link_type == "command":
                tip = "📱 复制口令到微信/淘宝打开"
            elif link_type == "miniprogram":
                tip = "💬 复制链接到微信打开"
            else:
                tip = "🌐 浏览器直接打开"

            lines.append(f"\n  📌 {p['name']}")
            lines.append(f"     🔗 {p['url']}")
            lines.append(f"     {tip}")
            lines.append(f"     📝 {p.get('description', '')}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="CPS优惠券查询工具")
    parser.add_argument("--category", "-c", help="品类: waimai/chuxing/kuaidi/dianying/jiudian/wanggou/huafei/all")
    parser.add_argument("--search", "-s", help="搜索平台名称")
    parser.add_argument("--list", "-l", action="store_true", help="列出所有品类")

    args = parser.parse_args()

    if args.list:
        print("支持的品类：")
        for key, name in CATEGORIES.items():
            print(f"  {key}: {name}")
        return

    if args.search:
        results = search_platform(args.search)
    elif args.category:
        key = args.category if args.category in CATEGORIES else None
        if not key and args.category != "all":
            print(f"未知品类: {args.category}")
            print(f"支持的品类: {', '.join(CATEGORIES.keys())}")
            return
        results = query_category(args.category)
    else:
        parser.print_help()
        return

    print(format_output(results))


if __name__ == "__main__":
    main()
