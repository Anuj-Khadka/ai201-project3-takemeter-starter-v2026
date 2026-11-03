import csv, json, time, urllib.request

SUB = "Cooking"
UA = "takemeter-dataset/0.1 by u/anujkhadka008"   # put your reddit username
FEEDS = [("new", ""), ("hot", ""), ("top", "year"), ("top", "month"), ("rising", "")]
TARGET = 200
seen = {}

def fetch(sort, t, after):
    url = f"https://www.reddit.com/r/{SUB}/{sort}.json?limit=100&raw_json=1"
    if t: url += f"&t={t}"
    if after: url += f"&after={after}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

for sort, t in FEEDS:
    after = ""
    for _ in range(5):                       # up to 5 pages per feed
        if len(seen) >= TARGET: break
        try:
            data = fetch(sort, t, after)
        except Exception as e:
            print("skip", sort, t, e); break
        for c in data["data"]["children"]:
            d = c["data"]
            if not d.get("is_self") or d.get("stickied"): continue
            body = (d.get("selftext") or "").strip()
            if not body or body in ("[removed]", "[deleted]"): continue
            if d["id"] in seen: continue
            text = (d["title"].strip() + " " + " ".join(body.split()[:60]))
            text = text.replace("\n", " ").replace("\r", " ").strip()
            seen[d["id"]] = (text, "https://www.reddit.com" + d["permalink"])
        after = data["data"].get("after")
        if not after: break
        time.sleep(2)                        # be polite
    if len(seen) >= TARGET: break

with open("cooking_posts.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["text", "link"])
    w.writerows(seen.values())
print(f"Wrote {len(seen)} posts to cooking_posts.csv")