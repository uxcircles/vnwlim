"""All words on the site, English and Traditional Chinese side by side as L(en, zh).
Simplified Chinese (/sc/) is converted from the Traditional text at build time (OpenCC t2s).
Sources: vnwlim.com home, /who-we-are, /chinese, /c-newsletter (read 17 Nov 2026)."""


def L(en, zh):
    return {"en": en, "zh": zh}


PHONE_DISPLAY = "07810 370010"
PHONE_INTL = "+44 7810 370010"
PHONE_TEL = "+447810370010"
WHATSAPP = "https://wa.me/447810370010"
EMAIL = "vl@vnwlim.com"
WECHAT = "a24980541"
LINKEDIN = "https://www.linkedin.com/in/vincent-lim-140ba69/"
OFFICIAL = "https://www.vnwlim.com/"

NAV = [
    ("#dates", L("Dates", "報稅日子")),
    ("#services", L("Services", "服務")),
    ("#vincent", L("Vincent", "林裕慶")),
    ("#column", L("The column", "稅務專欄")),
    ("#contact", L("Contact", "聯絡")),
]

UI = {
    "skip": L("Skip to content", "跳至正文"),
    "menu": L("Menu", "選單"),
    "concept": L("Concept", "概念"),
    "concept_long": L(f'Redesign concept. Not the official <a href="{OFFICIAL}" target="_blank" rel="noopener">VNW Accountancy website</a>.',
                      f'概念設計展示，並非 <a href="{OFFICIAL}" target="_blank" rel="noopener">VNW 會計事務所官方網站</a>。'),
    "concept_by": L("Designed by", "設計："),
    "concept_note": L("Unofficial redesign concept by", "非官方概念設計："),
    "call": L("Call", "致電"),
    "email": L("Email", "電郵"),
    "privacy": L("Privacy", "私隱政策"),
    "top": L("Back to top", "返回頂部"),
}

HERO = {
    "title": L("The tax year, one date at a time", "英國稅務年度，<br>每個限期都替你記住"),
    "lede": L("Vincent Lim FCCA runs a small ACCA-registered practice in south-west London. "
              "He keeps the HMRC and Companies House dates for sole traders, landlords and limited companies, "
              "and explains them in English, <span lang=\"zh-Hant\" class=\"nw\">普通話</span>, <span lang=\"zh-Hant\" class=\"nw\">廣東話</span> or <span lang=\"zh-Hant\" class=\"nw\">閩南話</span>.",
              "林裕慶（Vincent Lim）是英國皇家特許公認會計師公會資深會員（FCCA），在倫敦西南區開設 ACCA 註冊會計事務所。"
              "個體經營者、業主、有限公司的稅局和公司註冊處限期，由他一一記住，並以英語、普通話、粵語或閩南話向你解釋清楚。"),
    "next": L("Coming up", "下一個限期"),
    "today_is": L("Today is", "今天是"),
    "year_ahead": L("Show the 12 months ahead", "顯示未來 12 個月的所有日子"),
    "paye": L("Employers: PAYE and National Insurance are paid to HMRC by the 22nd of every month (19th by post). Next:",
              "僱主注意：每月 22 日前（郵寄則 19 日前）向稅局繳交上月的人工稅及國民保險。下一次："),
    "cta": L("The first consultation is free", "首次諮詢免費"),
    "whatsapp": L("WhatsApp Vincent", "WhatsApp 林先生"),
    "note": L("Dates are worked out in your browser from HMRC's published rules. They are general; your own may differ.",
              "日子由瀏覽器按稅局公佈的規則即時計算，僅供一般參考，個別情況或有不同。"),
}

# Annual HMRC dates. {a}/{b}/{c}: the tax years ending in Y-1, ending in Y, starting in Y.
DEADLINES = [
    {"m": 1, "d": 31,
     "t": L("Self Assessment {a}: online return and balance", "{a} 年度個人報稅：網上報稅及繳清稅款"),
     "w": L("Pay the balance for {a} and the first payment on account for {b}. Late returns get an automatic £100 penalty.",
            "繳清 {a} 年度餘額及 {b} 年度第一期預繳稅款。逾期報稅即罰 £100。")},
    {"m": 2, "d": 7, "from": "2026-08-07",
     "t": L("Making Tax Digital: third quarterly update for {b}", "數碼報稅（MTD）：{b} 年度第三季更新"),
     "w": L("For sole traders and landlords already in MTD for Income Tax (6 October to 5 January).",
            "適用於已加入 MTD 個人所得稅的個體經營者及業主（10 月 6 日至 1 月 5 日）。")},
    {"m": 4, "d": 5,
     "t": L("Tax year {b} ends", "{b} 稅務年度結束"),
     "w": L("Last day to use this year's ISA allowance, pension relief and capital gains exemption.",
            "使用本年度 ISA 免稅額、退休金稅務寬減及資本收益免稅額的最後一天。")},
    {"m": 4, "d": 6,
     "t": L("Tax year {c} begins", "{c} 稅務年度開始"),
     "w": L("New allowances and rates apply from today.", "新年度的免稅額及稅率由今日起生效。"),
     "y": {2027: L("Making Tax Digital for Income Tax now applies if your 2025/26 self-employed and rental income was over £30,000.",
                   "如 2025/26 年度自僱及租金收入超過 £30,000，今日起須以數碼方式報個人所得稅（MTD）。"),
           2028: L("Making Tax Digital for Income Tax now applies if your 2026/27 self-employed and rental income was over £20,000.",
                   "如 2026/27 年度自僱及租金收入超過 £20,000，今日起須以數碼方式報個人所得稅（MTD）。")}},
    {"m": 5, "d": 7, "from": "2026-08-07",
     "t": L("Making Tax Digital: fourth quarterly update for {b}", "數碼報稅（MTD）：{b} 年度第四季更新"),
     "w": L("Covers 6 January to 5 April. The year is finalised in your return by 31 January.",
            "涵蓋 1 月 6 日至 4 月 5 日，全年數字於翌年 1 月 31 日前的報稅表中確定。")},
    {"m": 5, "d": 31,
     "t": L("Employers: give staff their P60 for {b}", "僱主：向員工發出 {b} 年度 P60"),
     "w": L("Every employee on the payroll at 5 April gets one.", "4 月 5 日仍在職的每位員工都要收到。")},
    {"m": 7, "d": 6,
     "t": L("Employers: P11D and P11D(b) for {b}", "僱主：遞交 {b} 年度 P11D 及 P11D(b)"),
     "w": L("Report company cars, health cover and other benefits in kind.", "申報公司車、醫療保險等實物福利。")},
    {"m": 7, "d": 31,
     "t": L("Second payment on account for {b}", "{b} 年度第二期預繳稅款"),
     "w": L("For anyone whose last Self Assessment bill was over £1,000.", "上一年度個人稅單超過 £1,000 的人士須繳交。")},
    {"m": 8, "d": 7, "from": "2026-08-07",
     "t": L("Making Tax Digital: first quarterly update for {c}", "數碼報稅（MTD）：{c} 年度第一季更新"),
     "w": L("Covers 6 April to 5 July, sent from MTD-compatible software.", "涵蓋 4 月 6 日至 7 月 5 日，須經認可軟件遞交。")},
    {"m": 10, "d": 5,
     "t": L("Register for Self Assessment for {b}", "登記 {b} 年度個人報稅"),
     "w": L("If you started self-employment, letting or other untaxed income last tax year.",
            "如上一稅務年度開始自僱、出租物業或有其他未扣稅收入。")},
    {"m": 10, "d": 31,
     "t": L("Paper Self Assessment return for {b}", "{b} 年度紙本個人報稅表"),
     "w": L("Filing online instead gives you until 31 January.", "改為網上報稅可延至 1 月 31 日。")},
    {"m": 11, "d": 7, "from": "2026-08-07",
     "t": L("Making Tax Digital: second quarterly update for {c}", "數碼報稅（MTD）：{c} 年度第二季更新"),
     "w": L("Covers 6 July to 5 October.", "涵蓋 7 月 6 日至 10 月 5 日。")},
]

DATES_UI = {
    "days": L("{n} days", "還有 {n} 天"),
    "day": L("Tomorrow", "明天"),
    "today": L("Today", "今天"),
    "months": L(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]),
}

COMPANY = {
    "title": L("Your company's own dates", "你公司自己的限期"),
    "lede": L("Company deadlines run from your accounting year end, not the tax year. Enter it and see what follows.",
              "公司的限期由會計年結日起計，與稅務年度無關。輸入年結日，即可看到各項限期。"),
    "ye": L("Company year end", "公司年結日"),
    "vat": L("VAT quarter end (optional)", "增值稅季度結束日（選填）"),
    "rows": {
        "ct_pay": L("Corporation Tax payment", "繳交公司稅"),
        "ch": L("Accounts to Companies House", "向公司註冊處遞交年度報表"),
        "ct600": L("Corporation Tax return (CT600)", "遞交公司稅表（CT600）"),
        "vat": L("VAT return and payment", "遞交增值稅表及繳稅"),
    },
    "notes": {
        "ct_pay": L("9 months and 1 day after year end, for companies with profits under £1.5 million.", "年結後 9 個月零 1 天；適用於利潤低於 £150 萬的公司。"),
        "ch": L("9 months after year end for a private company (a first year has its own rule).", "私人公司為年結後 9 個月（首年另有規定）。"),
        "ct600": L("12 months after year end.", "年結後 12 個月。"),
        "vat": L("1 month and 7 days after the quarter ends, through MTD software.", "季度結束後 1 個月零 7 天，經 MTD 軟件遞交。"),
    },
    "empty": L("Choose a date to see your deadlines", "選擇日期後顯示限期"),
    "passed": L("passed", "已過"),
    "disclaimer": L("An estimate, not advice. Vincent will confirm your exact dates.", "僅為估算，並非專業意見。實際日子請向林先生確認。"),
}

SERVICES = {
    "title": L("What Vincent does", "服務範圍"),
    "groups": [
        (L("Tax", "稅務"), [L("Self Assessment", "個人所得稅"), L("Corporation Tax", "公司稅"), L("VAT", "增值稅（消費稅）"),
                            L("PAYE", "人工稅（PAYE）"), L("Capital Gains Tax", "資本收益稅"), L("Tax planning", "稅務策劃")]),
        (L("Accounts", "會計"), [L("Bookkeeping", "簿記"), L("Payroll", "工資單"), L("Management accounts", "管理賬目"),
                                 L("Company statutory accounts", "公司法定年終報表"), L("QuickBooks setup and training", "QuickBooks 設定及培訓")]),
        (L("Companies", "公司事務"), [L("UK company registration", "英國公司註冊"), L("Company secretary duties", "公司秘書職務"),
                                      L("Property management accounts", "物業管理賬目")]),
        (L("Starting out", "創業"), [L("New business start-up advice", "新創業諮詢"), L("Business plans", "商業計劃書"),
                                     L("Cash flow forecasts", "現金流預測"), L("Business loans", "商業貸款"), L("Business consultancy", "商業顧問")]),
    ],
    "newbiz": L("New to business, or new to the UK? Vincent will guide you through setting up and the tax that comes with it.",
                "剛開始做生意，或剛移居英國？林先生會帶你一步步完成開業手續，並講解隨之而來的稅務。"),
}

WAYS = {
    "title": L("How the practice works", "工作方式"),
    "items": [
        (L("Fixed fees, agreed first", "先定好固定收費"),
         L("Monthly, quarterly or yearly. The fee includes access to Vincent for any accounting or tax question.",
           "按月、按季或按年收費，費用已包括隨時就會計及稅務問題向林先生查詢。")),
        (L("You meet the principal", "由負責人親自見你"),
         L("Every new client has a first meeting with Vincent, at your office or wherever suits you. After that, email, phone or message.",
           "每位新客戶都會先與林先生見面，地點可以是你的辦公室或其他方便的地方。之後可隨時以電郵、電話或訊息聯絡。")),
        (L("Tax-efficient by design", "合法節稅"),
         L("A tax strategy fitted to each client, so more of the profit stays in the business.",
           "為每位客戶度身訂造節稅方案，讓更多利潤留在生意裡。")),
        (L("Your business, treated as his own", "把你的生意當作自己的生意"),
         L("If the client does well, the practice does well. That is the whole philosophy.",
           "客戶成功，事務所也就成功，這就是我們的理念。")),
    ],
}

VINCENT = {
    "title": L("Vincent Lim, FCCA", "林裕慶 Vincent Lim，FCCA"),
    "alt": L("Vincent Lim in a grey suit, arms folded, by a window", "林裕慶穿灰色西裝，雙手交叉站在窗前"),
    "bio": [
        L("Vincent founded VNW in 2005. He started out as an analyst programmer, moved into accountancy after his first degree in 1992, "
          "and has since worked in practice and in catering, IT and charities. He has been company secretary of a listed company and is a director "
          "or company secretary of several businesses today.",
          "林先生於 2005 年創立 VNW。他最初是電腦程式分析員，1992 年大學畢業後轉投會計，其後在會計事務所及餐飲、電腦、慈善機構等領域工作。"
          "他曾任一家上市公司的公司秘書，目前亦擔任多家企業的董事或公司秘書。"),
        L("He also has a working knowledge of property, refurbishment and property management.",
          "他對地產、裝修和物業管理亦有一定認識。"),
    ],
    "langs_t": L("Languages", "語言"),
    "langs": [("English", "en"), ("普通話", "zh-Hant"), ("廣東話", "zh-Hant"), ("閩南話", "zh-Hant")],
    "quals_t": L("Qualifications", "資歷"),
    "quals": [
        L("FCCA, Fellow of the Association of Chartered Certified Accountants", "英國皇家特許公認會計師公會資深會員（FCCA）"),
        L("MA Strategic Financial Management, Kingston University", "英國金斯頓大學 策略金融管理碩士"),
        L("BSc (Hons) Computing Information Systems, University of Central England", "英國英格蘭中央大學 電腦資訊系統榮譽學士"),
        L("Master of Arts in Christian Studies", "基督教研究碩士（MACS）"),
        L("Diploma in Business Administration, Singapore Polytechnic", "新加坡理工學院 商業行政文憑"),
    ],
    "firm_t": L("The practice", "事務所"),
    "firm": [
        L("ACCA registered general practice", "ACCA 註冊會計事務所"),
        L("ACCA Approved Employer, training future accountants", "ACCA 認可僱主，培訓未來會計師"),
        L("QuickBooks Advanced Certified ProAdvisor (Online)", "QuickBooks 高級認證顧問（網上版）"),
    ],
}

COLUMN = {
    "title": L("Vincent's tax column", "英國稅務資訊專欄"),
    "lede": L("For fifteen months Vincent wrote a monthly column in Chinese for Herald UK (英國僑報), on the questions newcomers to Britain ask most. "
              "The newspaper's links no longer open, so here is the index. Ask Vincent for any article.",
              "林先生曾在《英國僑報》撰寫每月稅務專欄，共十五期，解答新移民最常問的問題。報章網站的連結已無法開啟，以下為文章目錄，如需全文可向林先生索取。"),
    "changed": L("Rules changed in April 2025", "2025 年 4 月規則已改變"),
    "changed_note": L("Non-dom status and the remittance basis ended on 5 April 2025. People arriving after ten years abroad may use the four-year foreign income and gains (FIG) regime instead.",
                      "非原籍居民身份及匯款基礎已於 2025 年 4 月 5 日取消。在海外居住滿十年後來英的人士，可改用四年的「海外收入及收益」（FIG）制度。"),
    "ask": L("Ask for this article", "索取全文"),
    "items": [
        ("2022-03", "英國稅務免稅額", "UK tax allowances", "免費的東西，人人都喜歡！我們處在高稅率的西方國家，如何付少一點稅，大概是大家關心的議題！", "Which income you don't pay tax on, and how to use the allowances.", False),
        ("2022-04", "英國稅率和報稅", "Tax rates and filing", "如果收入超過免稅額，那我們應該繳多少稅呢？", "What you pay once income goes above the allowances.", False),
        ("2022-05", "英國稅務居民", "Becoming UK tax resident", "英國稅務居民有義務申報全世界的個人收入，對於有國外收入和資產的新移民，成為稅務居民的時間點可能是很重要的！", "When newcomers become resident, and why the date matters for income abroad.", False),
        ("2022-06", "開心繳稅？！", "Happy to pay tax?!", "對於從來沒有付過個人所得稅或習慣低稅率的人士，要在這裡交付高稅，的確是不容易！", "Getting used to UK tax when you come from a low-tax country.", False),
        ("2022-07", "退休金的稅務優惠", "Tax relief on pensions", "以稅務的角度讓大家明白為何供退休金是一項有效的省稅方案。", "Why paying into a pension is an efficient way to save tax.", False),
        ("2022-08", "英國遺產稅", "Inheritance tax", "遺產稅是「死人」要付的稅，一般不是「活人」需要付的稅！", "Who actually pays inheritance tax, and a common misunderstanding.", False),
        ("2022-09", "「一刀兩斷」的稅務", "Taxed in two countries", "若在兩個國家都有收入，可能在兩個國家都要申報收入和繳稅。", "Double taxation when you have income in two countries.", False),
        ("2022-10", "海外匯錢進入英國要交稅嗎？", "Is money sent from abroad taxed?", "從海外匯到英國的儲蓄、家用、學費、遺產，到底需要付稅嗎？", "Savings, family money, fees and inheritances sent to the UK.", True),
        ("2022-11", "非英國原住民的權益", "Non-domiciled residents", "非英國原住民 (Non-Domicile) 有權利決定他們如何申報國外的收入。", "How non-doms could choose to report foreign income.", True),
        ("2022-12", "淺談英國商業結構（一）", "UK business structures, part 1", "選擇適當的結構來經商是很重要的。", "Sole trader, partnership, LLP or limited company.", False),
        ("2023-01", "淺談英國商業結構（二）", "UK business structures, part 2", "以稅務的角度來比較哪一個結構是比較有效的。", "Which structure is most tax-efficient.", False),
        ("2023-02", "捐獻給慈善機構和稅務回扣", "Charity giving and tax relief", "捐款給英國的慈善機構，個體納稅人有沒有稅務優惠呢？", "Gift Aid and what donors can claim back.", False),
        ("2023-03", "避稅與逃稅有何不同？", "Avoidance or evasion?", "這些省稅的「策略」是否是逃稅的行為呢？", "Where legitimate tax planning ends.", False),
        ("2023-04", "避稅與逃稅有何後果？", "What happens if you get it wrong", "逃稅 (Tax Evasion) 是一種犯罪行為。", "The consequences of avoidance and evasion.", False),
        ("2023-05", "物業稅務現在與未來", "Property tax, now and next", "從稅務的角度，物業投資者現在需要注意什麼？未來又有什麼改變呢？", "What property investors should watch.", False),
    ],
}

CONTACT = {
    "title": L("Book the free first consultation", "預約免費首次諮詢"),
    "lede": L("Tell Vincent what you need, in whichever language suits you.", "告訴林先生你需要甚麼幫助，用你最方便的語言就可以。"),
    "name": L("Your name", "姓名"),
    "phone": L("Phone", "電話"),
    "reach": L("Email or WeChat ID", "電郵或微信號"),
    "topic": L("What is it about?", "查詢事項"),
    "topics": [L("Self Assessment", "個人報稅"), L("Company accounts and Corporation Tax", "公司賬目及公司稅"),
               L("VAT or payroll", "增值稅或工資單"), L("Starting a business", "開業"), L("New to the UK", "剛移居英國"),
               L("Landlord or property", "業主或物業"), L("Something else", "其他")],
    "lang": L("Reply in", "回覆語言"),
    "msg": L("Message", "內容"),
    "send_wa": L("Send by WhatsApp", "經 WhatsApp 發送"),
    "send_mail": L("Send by email", "經電郵發送"),
    "nothing": L("Nothing is stored on this website. Your message opens in WhatsApp or your email app, ready to send.",
                 "本網站不會儲存任何資料。訊息會在 WhatsApp 或電郵程式中打開，由你自行發送。"),
    "need": L("Please add your name and a way to reach you.", "請填寫姓名及聯絡方式。"),
    "meet": L("Meetings at your office, wherever suits you, or online", "可在你的辦公室、其他方便地點或網上會面"),
    "wechat": L("WeChat", "微信"),
    "company": L("VNW Limited, registered in England and Wales, company number 05278110. Registered office: 70 Dowdeswell Close, London SW15 5RL.",
                 "VNW Limited，於英格蘭及威爾斯註冊，公司編號 05278110。註冊地址：70 Dowdeswell Close, London SW15 5RL。"),
    "hello": L("Hello Vincent", "林先生您好"),
}
