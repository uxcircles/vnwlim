# VNW Accountancy：網站改版概念

UX CIRCLES 為 VNW Accountancy（VNW Limited，林裕慶 Vincent Lim FCCA）製作的**非官方**網站改版概念。官方網站為 <https://www.vnwlim.com/>。每頁頂部都有概念標示，並設 `noindex`，`robots.txt` 禁止搜尋引擎收錄。

網址：<https://uxcircles.github.io/vnwlim/>（英文）、`/zh/`（繁體）、`/sc/`（簡體）

## 頁面

- `index.html`、`zh/index.html`、`sc/index.html`：主頁（報稅日子、公司限期工具、服務、工作方式、林先生、稅務專欄、聯絡）
- `privacy.html`（三種語言）：私隱政策草擬本
- `404.html`：「這一頁不在本期」

## 如何修改

文字都在 `_build/content.py`，以 `L(英文, 繁體)` 並列；簡體由 OpenCC 自動轉換。

```bash
pip install opencc-python-reimplemented
python3 _build/pages.py      # 重建所有頁面
python3 _build/fonts.py      # 中文字改了之後，重新擷取字型子集
```

報稅日子規則同時寫在 `_build/content.py`（`DEADLINES`）及 `assets/js/main.js`：頁面先顯示建置當天的日子，瀏覽器再按今天的日期即時重算。CSS/JS 的 `?v=` 由檔案內容雜湊自動產生。

## 設計概念

- **標誌元素：** 林先生在《英國僑報》寫了十五期的稅務專欄。整個網站排成一份報紙：雙線報頭、日期行（dateline）、欄線、專欄目錄，連 404 頁都是「不在本期」。VW 標誌的藍色勾用於報頭、favicon 及頁尾。
- **首屏類型：** `calendar-led`。首屏是即時計算的稅局限期（下一個 1 月 31 日還有幾天），配合「你公司自己的限期」工具（輸入年結日，算出公司稅、CT600、公司註冊處報表及增值稅限期）。會計師客戶最常問「幾時要交」，所以首屏直接回答。
- **字型：** Instrument Serif（報紙標題）、Familjen Grotesk（內文）、DM Mono（日期與數字，像日曆和賬簿）；中文用 Noto Serif / Sans TC 及 SC，按使用字元子集化。
- **顏色：** 冷白紙色 `#f5f6f4`、油墨黑 `#1a1e23`、VW 標誌藍 `#1f66a3`（取自現有標誌）。刻意不用米色加深藍。
- **標題：** The tax year, one date at a time ／ 英國稅務年度，每個限期都替你記住
- **與同行業前幾個網站的分別：** KY、Tan & Co、IQTi、William Lai 都是左文右圖（拱形相片或資料卡）。這裡沒有拱形、沒有浮動標籤、沒有數字統計列，首屏是一份日期表，不是圖片。

## 資料來源（2026 年 11 月 17 日讀取）

- 服務、理念、資歷、語言、聯絡方式：vnwlim.com 主頁、/who-we-are、/chinese
- 公司編號 05278110 及註冊地址：Companies House
- 專欄目錄：vnwlim.com/c-newsletter（標題及摘要為原文）
- 林先生照片及 VW 標誌：取自現有網站，未使用圖庫相片
- 稅局日子：HMRC 公佈規則；MTD 個人所得稅門檻（2026 年 £50,000、2027 年 £30,000、2028 年 £20,000）

## 需要林先生確認

- 專欄十五個「阅读更多，请点击」連結（herald-uk.org）全部無法開啟，所以目錄只列標題，改為「索取全文」。如願意，可把全文重新刊登在網站上。
- 2022 年 10 月及 11 月兩篇（海外匯款、非原籍居民）的規則已於 2025 年 4 月改變，網站上已加註。
- Skype 已於 2025 年 5 月停止服務，故未列出 Skype 聯絡方式。
- 會面地點：現有網站寫「在客戶辦公室或其他方便地點」，所以沒有放地圖（註冊地址為住宅地址）。
- 私隱政策為草擬本（現有頁面寫成「VNM Accountancy Limited」），需審閱。
- 收費未列出，現有網站只寫「固定收費」。
