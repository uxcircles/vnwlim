"""Self-host fonts as WOFF2. Run after changing Chinese text:  python3 _build/pages.py && python3 _build/fonts.py
Latin: Spectral 400/500, Familjen Grotesk 400-700, DM Mono 500 (Google's latin subset).
Chinese: Noto Serif/Sans TC (from /zh/) and SC (from /sc/), subset to the characters used, via Google Fonts text=."""
import glob, html, os, re, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "fonts")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
API = "https://fonts.googleapis.com/css2?"


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read()


def latin(family):
    css = get(API + "family=" + family + "&display=swap").decode()
    for name, block in re.findall(r"/\* ([\w-]+) \*/\s*@font-face \{(.*?)\}", css, re.S):
        if name == "latin":
            return get(re.search(r"url\((.*?)\)", block).group(1))
    raise SystemExit("no latin block for " + family)


def save(name, data):
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, name + ".woff2"), "wb").write(data)
    print(f"{name}.woff2  {len(data) // 1024} KB")


def chars(pattern):
    s = set()
    for f in glob.glob(os.path.join(ROOT, pattern), recursive=True):
        s.update(c for c in html.unescape(open(f, encoding="utf-8").read()) if ord(c) > 0x2E7F)
    s.update("，。：；！？（）「」、·…")
    return "".join(sorted(s))


if __name__ == "__main__":
    save("spectral-400", latin("Spectral:wght@400"))
    save("spectral-500", latin("Spectral:wght@500"))
    save("familjen", latin("Familjen+Grotesk:wght@400..700"))
    save("dm-mono-500", latin("DM+Mono:wght@500"))
    save("montserrat", latin("Montserrat:wght@300..500"))  # wordmark only, to sit with the VW logo
    # Traditional: /zh/ plus the Chinese column titles used on the English page and 404
    tc = chars("zh/*.html") + chars("index.html") + chars("404.html") + chars("privacy.html")
    sc = chars("sc/*.html")
    for script, text in (("tc", "".join(sorted(set(tc)))), ("sc", sc)):
        fam = "TC" if script == "tc" else "SC"
        for kind, weights in (("serif", (700,)), ("sans", (400, 700))):
            for w in weights:
                css = get(API + f"family=Noto+{kind.title()}+{fam}:wght@{w}&display=swap&text=" + urllib.parse.quote(text)).decode()
                urls = re.findall(r"url\((.*?)\)", css)
                save(f"noto-{kind}-{script}-{w}", b"".join(get(u) for u in urls[:1]))
        print(len(text), script, "characters")
