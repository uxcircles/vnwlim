/* VNW concept: live HMRC dates, company deadline tool, menu, contact form. Data in window.VNW. */
(function () {
  var V = window.VNW || {};
  var UI = V.ui || {};
  var DAY = 86400000;

  function today() { var n = new Date(); return new Date(n.getFullYear(), n.getMonth(), n.getDate()); }
  function iso(d) { return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); }
  function ty(y) { return y + "/" + String(y + 1).slice(2); }
  function fill(s, y) { return s.replace(/\{a\}/g, ty(y - 2)).replace(/\{b\}/g, ty(y - 1)).replace(/\{c\}/g, ty(y)); }
  function between(a, b) { return Math.round((b - a) / DAY); }
  function count(n) { return n === 0 ? UI.today : n === 1 ? UI.day : UI.days.replace("{n}", n); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function upcoming(t, n) {
    var out = [], limit = new Date(t.getTime() + 12 * 31 * DAY);
    [t.getFullYear(), t.getFullYear() + 1].forEach(function (y) {
      (V.deadlines || []).forEach(function (e) {
        var d = new Date(y, e.m - 1, e.d);
        if (d < t || d > limit) return;
        if (e.from && iso(d) < e.from) return;
        out.push({ d: d, e: e });
      });
    });
    out.sort(function (a, b) { return a.d - b.d; });
    return n ? out.slice(0, n) : out;
  }

  function row(t, x) {
    var y = x.d.getFullYear(), extra = x.e.y && x.e.y[y];
    return '<li class="d-row"><time class="d-date" datetime="' + iso(x.d) + '"><span class="d-day">' + x.d.getDate() +
      '</span><span class="d-mon">' + UI.months[x.d.getMonth()] + " " + y + '</span></time><span class="d-count">' +
      count(between(t, x.d)) + '</span><div class="d-text"><h3>' + fill(x.e.t, y) + "</h3><p>" + (extra || fill(x.e.w, y)) + "</p></div></li>";
  }

  function renderDates() {
    var t = today(), next = document.getElementById("d-next"), year = document.getElementById("d-year");
    if (!next) return;
    var stamp = document.getElementById("today");
    if (stamp && stamp.getAttribute("datetime") !== iso(t)) {
      stamp.setAttribute("datetime", iso(t));
      stamp.textContent = t.toLocaleDateString(V.lang === "en" ? "en-GB" : V.lang === "sc" ? "zh-CN" : "zh-TW",
        { weekday: "long", day: "numeric", month: "long", year: "numeric" });
    }
    next.innerHTML = upcoming(t, 4).map(function (x) { return row(t, x); }).join("");
    if (year) year.innerHTML = upcoming(t).map(function (x) { return row(t, x); }).join("");
    var p = document.getElementById("paye");
    if (p) {
      var d = new Date(t.getFullYear(), t.getMonth(), 22);
      if (t.getDate() > 22) d = new Date(t.getFullYear(), t.getMonth() + 1, 22);
      p.textContent = d.getDate() + " " + UI.months[d.getMonth()] + " " + d.getFullYear();
    }
  }

  /* Company dates. Months are added with the month-end rule Companies House uses:
     a year end on the last day of a month moves to the last day of the target month. */
  function addMonths(d, m) {
    var last = new Date(d.getFullYear(), d.getMonth() + 1, 0).getDate() === d.getDate();
    var target = new Date(d.getFullYear(), d.getMonth() + m, 1);
    var dim = new Date(target.getFullYear(), target.getMonth() + 1, 0).getDate();
    return new Date(target.getFullYear(), target.getMonth(), last ? dim : Math.min(d.getDate(), dim));
  }
  function parse(v) { var p = /^(\d{4})-(\d{2})-(\d{2})$/.exec(v || ""); return p ? new Date(+p[1], +p[2] - 1, +p[3]) : null; }
  function fmt(d) { return d.getDate() + " " + UI.months[d.getMonth()] + " " + d.getFullYear(); }

  function renderCompany() {
    var out = document.getElementById("co-out");
    if (!out) return;
    var ye = parse(document.getElementById("co-ye").value), vat = parse(document.getElementById("co-vat").value), t = today(), rows = [];
    if (ye) {
      rows.push(["ct_pay", new Date(addMonths(ye, 9).getTime() + DAY)]);
      rows.push(["ch", addMonths(ye, 9)]);
      rows.push(["ct600", addMonths(ye, 12)]);
    }
    if (vat) rows.push(["vat", new Date(addMonths(vat, 1).getTime() + 7 * DAY)]);
    if (!rows.length) { out.innerHTML = "<li>" + esc(V.co.empty) + "</li>"; return; }
    rows.sort(function (a, b) { return a[1] - b[1]; });
    out.innerHTML = rows.map(function (r) {
      var n = between(t, r[1]);
      return '<li class="' + (n < 0 ? "past" : "") + '"><strong>' + esc(V.co.rows[r[0]]) + '</strong><span class="when">' + fmt(r[1]) +
        '</span><span class="note">' + esc(V.co.notes[r[0]]) + '</span><span class="in">' + (n < 0 ? esc(V.co.passed) : esc(count(n))) + "</span></li>";
    }).join("");
  }

  function menu() {
    var b = document.querySelector(".menu-btn"), nav = document.getElementById("nav");
    if (!b || !nav) return;
    function set(open) { nav.classList.toggle("open", open); b.setAttribute("aria-expanded", open); document.body.classList.toggle("menu-open", open); }
    b.addEventListener("click", function () { set(!nav.classList.contains("open")); });
    nav.addEventListener("click", function (e) { if (e.target.tagName === "A") set(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") set(false); });
  }

  function form() {
    var f = document.getElementById("ct-form");
    if (!f) return;
    var via = "wa";
    f.querySelectorAll("button").forEach(function (b) { b.addEventListener("click", function () { via = b.value; }); });
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var g = function (n) { return (f.elements[n].value || "").trim(); }, err = document.getElementById("ct-err");
      if (!g("name") || !(g("phone") || g("reach"))) { err.textContent = V.form.need; err.hidden = false; f.elements[g("name") ? "phone" : "name"].focus(); return; }
      err.hidden = true;
      var F = V.form, lines = [F.hello + ",", "", F.name + ": " + g("name")];
      if (g("phone")) lines.push(F.phone + ": " + g("phone"));
      if (g("reach")) lines.push(F.reach + ": " + g("reach"));
      lines.push(F.topic + ": " + g("topic"), F.lang + ": " + g("lang"));
      if (g("msg")) lines.push("", g("msg"));
      var text = lines.join("\n");
      if (via === "mail") location.href = "mailto:" + V.email + "?subject=" + encodeURIComponent(g("topic") + " – " + g("name")) + "&body=" + encodeURIComponent(text);
      else window.open(V.wa + "?text=" + encodeURIComponent(text), "_blank", "noopener");
    });
  }

  renderDates();
  ["co-ye", "co-vat"].forEach(function (id) { var el = document.getElementById(id); if (el) el.addEventListener("input", renderCompany); });
  renderCompany();
  menu();
  form();
})();
