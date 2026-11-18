"""Build every page:  python3 _build/pages.py   (then python3 _build/fonts.py if Chinese text changed)

English at /, Traditional Chinese at /zh/, Simplified Chinese at /sc/ (converted from /zh/ with OpenCC t2s:
pip install opencc-python-reimplemented)."""
import datetime as dt
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import *  # noqa

try:
    from opencc import OpenCC
    T2S = OpenCC("t2s").convert
except ImportError:
    sys.exit("pip install opencc-python-reimplemented")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://uxcircles.github.io/vnwlim/"
LANGS = {"en": ("", "en-GB", "EN"), "zh": ("zh/", "zh-Hant", "繁"), "sc": ("sc/", "zh-Hans", "简")}


def ver(path):
    return hashlib.md5(open(os.path.join(ROOT, path), "rb").read()).hexdigest()[:8]


def r(x, lang):
    if isinstance(x, dict) and "en" in x:
        return x["en"] if lang == "en" else x["zh"]
    return x


def pre(lang):
    return "" if lang == "en" else "../"


# ---------- dates (the same rules as assets/js/main.js, for the no-JS first paint) ----------

def ty(y):
    return f"{y}/{str(y + 1)[2:]}"


def upcoming(today, n=None, months=12):
    out = []
    for y in range(today.year, today.year + 2):
        for e in DEADLINES:
            d = dt.date(y, e["m"], e["d"])
            if d < today or (e.get("from") and d < dt.date.fromisoformat(e["from"])):
                continue
            if d > today + dt.timedelta(days=months * 31):
                continue
            out.append((d, e))
    out.sort(key=lambda x: x[0])
    return out[:n] if n else out


def fill(s, y):
    return s.format(a=ty(y - 2), b=ty(y - 1), c=ty(y))


def date_rows(lang, today, n):
    rows = []
    for d, e in upcoming(today, n):
        days = (d - today).days
        cnt = r(DATES_UI["today"], lang) if days == 0 else r(DATES_UI["day"], lang) if days == 1 else r(DATES_UI["days"], lang).format(n=days)
        extra = e.get("y", {}).get(d.year)
        w = r(extra, lang) if extra else fill(r(e["w"], lang), d.year)
        mon = r(DATES_UI["months"], lang)[d.month - 1]
        rows.append(f'''<li class="d-row"><time class="d-date" datetime="{d.isoformat()}"><span class="d-day">{d.day}</span><span class="d-mon">{mon} {d.year}</span></time>
<span class="d-count">{cnt}</span><div class="d-text"><h3>{fill(r(e["t"], lang), d.year)}</h3><p>{w}</p></div></li>''')
    return "\n".join(rows)


def js_data(lang):
    return {
        "lang": lang,
        "deadlines": [{"m": e["m"], "d": e["d"], "from": e.get("from"), "t": r(e["t"], lang), "w": r(e["w"], lang),
                       "y": {str(k): r(v, lang) for k, v in e.get("y", {}).items()}} for e in DEADLINES],
        "ui": {k: r(v, lang) for k, v in DATES_UI.items()},
        "co": {"rows": {k: r(v, lang) for k, v in COMPANY["rows"].items()}, "notes": {k: r(v, lang) for k, v in COMPANY["notes"].items()},
               "empty": r(COMPANY["empty"], lang), "passed": r(COMPANY["passed"], lang)},
        "form": {"need": r(CONTACT["need"], lang), "hello": r(CONTACT["hello"], lang), "name": r(CONTACT["name"], lang),
                 "phone": r(CONTACT["phone"], lang), "reach": r(CONTACT["reach"], lang), "topic": r(CONTACT["topic"], lang),
                 "lang": r(CONTACT["lang"], lang)},
        "wa": WHATSAPP, "email": EMAIL,
    }


# ---------- shell ----------

def head(lang, title, desc, path):
    p = pre(lang)
    alts = "\n".join(f'<link rel="alternate" hreflang="{LANGS[l][1]}" href="{BASE}{LANGS[l][0]}{path}">' for l in LANGS)
    css = f"{p}assets/css/site.css?v={ver('assets/css/site.css')}"
    fonts = ['instrument-serif', 'familjen']
    if lang != "en":
        fonts.append(f"noto-serif-{'tc' if lang == 'zh' else 'sc'}-700")
    preload = "\n".join(f'<link rel="preload" href="{p}assets/fonts/{f}.woff2" as="font" type="font/woff2" crossorigin>' for f in fonts)
    return f'''<!doctype html>
<html lang="{LANGS[lang][1]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#f5f6f4">
<link rel="icon" href="{p}assets/img/favicon.svg" type="image/svg+xml">
{alts}
{preload}
<link rel="stylesheet" href="{css}">
</head>'''


def concept(lang):
    tag = "Concept" if lang == "en" else "概念"
    return f'''<div class="concept" role="note"><div class="concept-in">
<p><span class="concept-tag">{tag}</span><span class="concept-long">{r(UI["concept_long"], lang)}</span></p>
<a class="concept-by" href="https://ux-circles.com/professionals" target="_blank" rel="noopener"><span class="concept-by-pre">{r(UI["concept_by"], lang)} </span><strong>UX CIRCLES</strong> ↗</a></div></div>'''


def lang_switch(lang, path, cls="lang"):
    items = []
    for l, (d, code, label) in LANGS.items():
        href = pre(lang) + d + path
        cur = ' aria-current="true"' if l == lang else ""
        name = {"en": "English", "zh": "繁體中文", "sc": "简体中文"}[l]
        items.append(f'<a href="{href or "./"}" hreflang="{code}" lang="{code}"{cur} title="{name}">{label}</a>')
    return f'<nav class="{cls}" aria-label="Language / 語言">' + "".join(items) + "</nav>"


def header(lang, path, home=True):
    base = "" if home else "./"
    nav = "".join(f'<a href="{base}{h}">{r(t, lang)}</a>' for h, t in NAV)
    return f'''<header class="mast" id="top">
<div class="mast-in">
<a class="brand" href="./" aria-label="VNW Accountancy">
<img src="{pre(lang)}assets/img/vw-mark.png" width="61" height="27" alt=""><span class="brand-name">VNW Accountancy</span></a>
<nav class="nav" id="nav" aria-label="{r(UI["menu"], lang)}">{nav}</nav>
{lang_switch(lang, path)}
<button class="menu-btn" aria-expanded="false" aria-controls="nav">{r(UI["menu"], lang)}</button>
</div>
</header>'''


def footer(lang, path):
    p = pre(lang)
    return f'''<footer class="foot">
<div class="wrap foot-in">
<div><img src="{p}assets/img/vw-mark.png" width="61" height="27" alt=""><p class="foot-name">VNW Accountancy</p>
<p>{r(CONTACT["company"], lang)}</p></div>
<div><p><a href="tel:{PHONE_TEL}">{PHONE_INTL}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>{r(CONTACT["wechat"], lang)}: {WECHAT}<br>
<a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></p></div>
<div><p><a href="{p}{LANGS[lang][0]}privacy.html">{r(UI["privacy"], lang)}</a><br><a href="#top">{r(UI["top"], lang)}</a></p>
{lang_switch(lang, path, "lang lang-foot")}</div>
</div>
<p class="wrap foot-note">{r(UI["concept_note"], lang)} <a href="https://ux-circles.com/professionals" target="_blank" rel="noopener">UX CIRCLES</a></p>
</footer>
<nav class="mbar" aria-label="{r(UI["call"], lang)}">
<a href="tel:{PHONE_TEL}">{r(UI["call"], lang)}</a><a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a><a href="mailto:{EMAIL}">{r(UI["email"], lang)}</a>
</nav>'''


def scripts(lang):
    p = pre(lang)
    data = json.dumps(js_data(lang), ensure_ascii=False)
    return f'''<script>window.VNW={data};</script>
<script src="{p}assets/js/main.js?v={ver('assets/js/main.js')}" defer></script>'''


# ---------- home ----------

def home(lang, today):
    t = lambda x: r(x, lang)  # noqa
    weekday = today.strftime("%A") if lang == "en" else "星期" + "一二三四五六日"[today.weekday()]
    todays = f"{weekday} {today.day} {today.strftime('%B')} {today.year}" if lang == "en" else f"{today.year} 年 {today.month} 月 {today.day} 日（{weekday}）"
    nxt22 = today.replace(day=22) if today.day <= 22 else (today.replace(day=1) + dt.timedelta(days=32)).replace(day=22)
    paye = f"{nxt22.day} {t(DATES_UI['months'])[nxt22.month - 1]} {nxt22.year}"

    groups = "".join(f'<div class="svc-col"><h3>{t(g)}</h3><ul>' + "".join(f"<li>{t(i)}</li>" for i in items) + "</ul></div>" for g, items in SERVICES["groups"])
    ways = "".join(f'<li><span class="w-n">{i + 1}</span><h3>{t(a)}</h3><p>{t(b)}</p></li>' for i, (a, b) in enumerate(WAYS["items"]))
    quals = "".join(f"<li>{t(q)}</li>" for q in VINCENT["quals"])
    firm = "".join(f"<li>{t(q)}</li>" for q in VINCENT["firm"])
    langs = "".join(f'<li lang="{c}">{n}</li>' for n, c in VINCENT["langs"])
    bio = "".join(f"<p>{t(b)}</p>" for b in VINCENT["bio"])

    cols = []
    for ym, zh, en, zx, ex, changed in COLUMN["items"]:
        y, m = ym.split("-")
        mon = t(DATES_UI["months"])[int(m) - 1]
        flag = f'<p class="c-flag"><strong>{t(COLUMN["changed"])}</strong> {t(COLUMN["changed_note"])}</p>' if changed else ""
        ask = f"{WHATSAPP}?text=" + __import__("urllib.parse").parse.quote(f"{t(CONTACT['hello'])}, {zh} ({ym})")
        if lang == "en":
            body = f'<h3><span lang="zh-Hant">{zh}</span><span class="c-en">{en}</span></h3><p>{ex}</p>'
        else:
            body = f"<h3>{zh}</h3><p>{zx}</p>"
        cols.append(f'<li class="c-item"><time datetime="{ym}">{mon} {y}</time>{body}{flag}<a class="c-ask" href="{ask}" target="_blank" rel="noopener">{t(COLUMN["ask"])}</a></li>')

    topics = "".join(f"<option>{t(x)}</option>" for x in CONTACT["topics"])
    first_lang = {"en": "English", "zh": "廣東話", "sc": "普通话"}[lang]
    reply_langs = "".join(f"<option{' selected' if n == first_lang else ''}>{n}</option>" for n in ["English", "普通話" if lang != "sc" else "普通话", "廣東話", "閩南話"])

    return f'''<main id="main">
<section class="hero" id="dates" aria-labelledby="h1">
<div class="wrap">
<p class="dateline"><span>Roehampton, London</span><span>{t(HERO["today_is"])} <time id="today" datetime="{today.isoformat()}">{todays}</time></span><span>ACCA · FCCA</span></p>
<div class="hero-top"><h1 id="h1">{t(HERO["title"])}</h1>
<p class="lede">{t(HERO["lede"])}</p></div>
<h2 class="d-head">{t(HERO["next"])}</h2>
<ol class="d-list" id="d-next">
{date_rows(lang, today, 4)}
</ol>
<details class="d-more"><summary>{t(HERO["year_ahead"])}</summary>
<ol class="d-list d-list-sm" id="d-year">
{date_rows(lang, today, None)}
</ol></details>
<p class="d-paye">{t(HERO["paye"])} <strong id="paye">{paye}</strong></p>
<div class="hero-cta"><p class="cta-label">{t(HERO["cta"])}</p>
<a class="btn btn-ink" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
<a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">{t(HERO["whatsapp"])}</a></div>
<p class="d-note">{t(HERO["note"])}</p>
</div>
</section>

<section class="co" id="company" aria-labelledby="co-h">
<div class="wrap co-in">
<div><h2 id="co-h">{t(COMPANY["title"])}</h2><p>{t(COMPANY["lede"])}</p>
<form class="co-form" onsubmit="return false">
<label>{t(COMPANY["ye"])}<input type="date" id="co-ye" value="{today.year if today.month > 3 else today.year - 1}-03-31"></label>
<label>{t(COMPANY["vat"])}<input type="date" id="co-vat"></label>
</form>
<p class="small">{t(COMPANY["disclaimer"])}</p></div>
<ol class="co-out" id="co-out" aria-live="polite"><li>{t(COMPANY["empty"])}</li></ol>
</div>
</section>

<section class="svc" id="services" aria-labelledby="svc-h">
<div class="wrap">
<h2 id="svc-h">{t(SERVICES["title"])}</h2>
<div class="svc-grid">{groups}</div>
<p class="svc-new">{t(SERVICES["newbiz"])}</p>
</div>
</section>

<section class="ways" aria-labelledby="ways-h">
<div class="wrap"><h2 id="ways-h">{t(WAYS["title"])}</h2><ol class="ways-list">{ways}</ol></div>
</section>

<section class="vin" id="vincent" aria-labelledby="vin-h">
<div class="wrap vin-in">
<figure class="vin-photo"><img src="{pre(lang)}assets/img/vincent-700.jpg" srcset="{pre(lang)}assets/img/vincent-700.jpg 700w, {pre(lang)}assets/img/vincent.jpg 1400w" sizes="(min-width: 900px) 40vw, 100vw" width="700" height="467" alt="{t(VINCENT["alt"])}" loading="lazy"></figure>
<div class="vin-text">
<h2 id="vin-h">{t(VINCENT["title"])}</h2>
{bio}
<div class="vin-facts">
<div><h3>{t(VINCENT["langs_t"])}</h3><ul class="langs">{langs}</ul></div>
<div><h3>{t(VINCENT["quals_t"])}</h3><ul>{quals}</ul></div>
<div><h3>{t(VINCENT["firm_t"])}</h3><ul>{firm}</ul></div>
</div></div>
</div>
</section>

<section class="col" id="column" aria-labelledby="col-h">
<div class="wrap">
<div class="col-head"><h2 id="col-h">{t(COLUMN["title"])}</h2><p>{t(COLUMN["lede"])}</p></div>
<ol class="col-grid">{"".join(cols)}</ol>
</div>
</section>

<section class="contact" id="contact" aria-labelledby="ct-h">
<div class="wrap ct-in">
<div class="ct-info">
<h2 id="ct-h">{t(CONTACT["title"])}</h2>
<p>{t(CONTACT["lede"])}</p>
<p class="ct-phone"><a href="tel:{PHONE_TEL}">{PHONE_INTL}</a></p>
<ul class="ct-list"><li>WhatsApp <a href="{WHATSAPP}" target="_blank" rel="noopener">{PHONE_DISPLAY}</a></li>
<li>{t(UI["email"])} <a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{t(CONTACT["wechat"])} {WECHAT}</li>
<li>{t(CONTACT["meet"])}</li></ul>
</div>
<form class="ct-form" id="ct-form" novalidate>
<label>{t(CONTACT["name"])}<input name="name" autocomplete="name" required></label>
<div class="two"><label>{t(CONTACT["phone"])}<input name="phone" type="tel" autocomplete="tel"></label>
<label>{t(CONTACT["reach"])}<input name="reach" autocomplete="email"></label></div>
<div class="two"><label>{t(CONTACT["topic"])}<select name="topic">{topics}</select></label>
<label>{t(CONTACT["lang"])}<select name="lang">{reply_langs}</select></label></div>
<label>{t(CONTACT["msg"])}<textarea name="msg" rows="4"></textarea></label>
<p class="ct-err" id="ct-err" role="alert" hidden></p>
<div class="ct-btns"><button class="btn btn-ink" value="wa">{t(CONTACT["send_wa"])}</button><button class="btn" value="mail">{t(CONTACT["send_mail"])}</button></div>
<p class="small">{t(CONTACT["nothing"])}</p>
</form>
</div>
</section>
</main>'''


PRIVACY = {
    "title": L("Privacy notice", "私隱政策"),
    "draft": L("Draft for VNW Limited to review. It replaces the current page, which names “VNM Accountancy Limited”.",
               "草擬本，待 VNW Limited 審閱。用以取代現有頁面（現有頁面誤寫為「VNM Accountancy Limited」）。"),
    "body": [
        (L("Who we are", "我們是誰"), L("VNW Limited (trading as VNW Accountancy), company number 05278110, 70 Dowdeswell Close, London SW15 5RL. Contact: vl@vnwlim.com.",
                                       "VNW Limited（VNW 會計事務所），公司編號 05278110，地址 70 Dowdeswell Close, London SW15 5RL。聯絡：vl@vnwlim.com。")),
        (L("What this website collects", "本網站收集甚麼資料"), L("Nothing. The contact form opens WhatsApp or your email app with your message; the website does not store it. There are no analytics or advertising cookies.",
                                                       "不收集任何資料。聯絡表格只會在 WhatsApp 或電郵程式中打開你的訊息，網站本身不會儲存。本網站不使用分析或廣告 Cookie。")),
        (L("When you become a client", "成為客戶後", ), L("We hold the information needed to prepare your accounts and tax returns and to meet our anti-money-laundering duties, under our contract with you and our legal obligations. We keep records for at least six years after the work ends.",
                                                       "我們會按與你的合約及法律責任，持有編製賬目、報稅及履行反洗錢義務所需的資料，並於工作完成後保存最少六年。")),
        (L("Your rights", "你的權利"), L("You can ask to see, correct or delete your information, or object to its use. If you are unhappy, you can complain to the Information Commissioner's Office (ico.org.uk).",
                                         "你可要求查閱、更正或刪除你的資料，或反對使用。如有不滿，可向資訊專員辦公室（ico.org.uk）投訴。")),
    ],
}


def privacy(lang):
    t = lambda x: r(x, lang)  # noqa
    secs = "".join(f"<h2>{t(h)}</h2><p>{t(b)}</p>" for h, b in PRIVACY["body"])
    return f'''<main id="main" class="page"><div class="wrap narrow"><h1>{t(PRIVACY["title"])}</h1><p class="d-note">{t(PRIVACY["draft"])}</p>{secs}</div></main>'''


def page(lang, path, title, desc, body, today, home_page=True):
    html = (head(lang, title, desc, path) + "\n<body>\n" + f'<a class="skip" href="#main">{r(UI["skip"], lang)}</a>\n'
            + concept(lang) + header(lang, path, home_page) + body + footer(lang, path) + scripts(lang) + "\n</body>\n</html>\n")
    if not home_page:
        html = html.replace('href="./#', 'href="./index.html#')
    return T2S(html) if lang == "sc" else html


def write(rel, html):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(html)
    print("wrote", rel)


NOT_FOUND = '''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Not in this edition | VNW Accountancy</title>
<link rel="icon" href="/vnwlim/assets/img/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/vnwlim/assets/css/site.css?v={v}"></head>
<body class="nf">{concept}<main id="main" class="wrap nf-in"><p class="dateline"><span>VNW Accountancy</span><span>Page 404</span></p>
<h1>This page isn't in today's edition</h1><p lang="zh-Hant" class="nf-zh">這一頁不在本期</p>
<p>The address may have changed, like the old column links did.</p>
<p><a class="btn btn-ink" href="/vnwlim/">Front page</a> <a class="btn" href="/vnwlim/zh/">中文主頁</a></p></main></body></html>
'''

if __name__ == "__main__":
    today = dt.date.today()
    titles = {"en": "VNW Accountancy | Vincent Lim FCCA, accountant in south-west London",
              "zh": "VNW 會計事務所 | 林裕慶 FCCA，倫敦會計師", "sc": "VNW 會計事務所 | 林裕慶 FCCA，倫敦會計師"}
    descs = {"en": "Tax and accounts for sole traders, landlords and limited companies, in English, Mandarin, Cantonese and Hokkien.",
             "zh": "為個體經營者、業主及有限公司處理稅務和賬目，提供英語、普通話、粵語及閩南話服務。",
             "sc": "為個體經營者、業主及有限公司處理稅務和賬目，提供英語、普通話、粵語及閩南話服務。"}
    for lang, (d, _, _) in LANGS.items():
        write(d + "index.html", page(lang, "", titles[lang], descs[lang], home(lang, today), today))
        write(d + "privacy.html", page(lang, "privacy.html", r(PRIVACY["title"], lang) + " | VNW Accountancy", descs[lang], privacy(lang), today, False))
    write("404.html", NOT_FOUND.replace("{v}", ver("assets/css/site.css")).replace("{concept}", concept("en")))
    open(os.path.join(ROOT, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
