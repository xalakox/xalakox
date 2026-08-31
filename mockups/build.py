#!/usr/bin/env python3
"""Builds README design mockups as self-contained HTML pages that replicate
the GitHub profile page frame (dark theme). Only layouts achievable in
GitHub-flavored markdown are used inside the README area, so any mockup can
be translated 1:1 into the real README.md later."""
import pathlib

OUT = pathlib.Path(__file__).parent

OCTO = ('M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 '
        '0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13'
        '-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07'
        '-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08'
        '-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 '
        '.27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 '
        '2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 '
        '2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z')

CSS = """
*{box-sizing:border-box}
body{margin:0;background:#0d1117;color:#e6edf3;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:#4493f8;text-decoration:none}a:hover{text-decoration:underline}
.topnav{display:flex;align-items:center;gap:14px;padding:14px 24px;background:#010409;border-bottom:1px solid #21262d;font-size:14px;font-weight:600}
.topnav svg{fill:#e6edf3}
.searchbox{margin-left:auto;border:1px solid #30363d;border-radius:6px;padding:4px 10px;color:#6e7681;font-weight:400;font-size:13px;width:280px}
.tabs{display:flex;gap:4px;padding:0 24px;border-bottom:1px solid #21262d;background:#0d1117;font-size:14px}
.tab{padding:10px 12px;color:#e6edf3;display:flex;gap:7px;align-items:center;border-bottom:2px solid transparent}
.tab.active{border-bottom-color:#f78166;font-weight:600}
.tab .count{background:rgba(110,118,129,.4);border-radius:2em;padding:0 7px;font-size:12px;font-weight:400}
.tab svg{fill:#8b949e}
.page{max-width:1280px;margin:0 auto;padding:24px 32px;display:flex;gap:32px;align-items:flex-start}
.sidebar{width:296px;flex-shrink:0;font-size:14px}
.avatar{width:296px;height:296px;border-radius:50%;border:1px solid #30363d;background:#21262d url(https://github.com/xalakox.png) center/cover}
.sb-name{font-size:24px;font-weight:600;margin-top:16px;line-height:1.25}
.sb-handle{font-size:20px;color:#8b949e;font-weight:300}
.btn{display:block;text-align:center;background:#21262d;border:1px solid rgba(240,246,252,.1);border-radius:6px;padding:5px 16px;color:#c9d1d9;font-weight:500;margin:16px 0;font-size:14px}
.sb-line{color:#8b949e;margin:10px 0}
.sb-line b{color:#e6edf3}
.sb-links div{margin:7px 0;color:#c9d1d9;font-size:14px}
.dim-note{margin-top:24px;padding:10px 12px;border:1px dashed #30363d;border-radius:6px;color:#6e7681;font-size:12px;line-height:1.5}
.main{flex:1;min-width:0}
.readme{border:1px solid #30363d;border-radius:6px;margin-bottom:24px}
.readme-head{padding:16px 32px 0;font-size:12px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:#8b949e}
.readme-head b{color:#e6edf3;font-weight:600}
.markdown-body{padding:16px 32px 32px;font-size:16px;line-height:1.5;word-wrap:break-word}
.markdown-body>*:first-child{margin-top:0}
.markdown-body h1{font-size:2em;font-weight:600;margin:24px 0 16px;padding-bottom:.3em;border-bottom:1px solid #21262d}
.markdown-body h2{font-size:1.5em;font-weight:600;margin:24px 0 16px;padding-bottom:.3em;border-bottom:1px solid #21262d}
.markdown-body h3{font-size:1.25em;font-weight:600;margin:24px 0 16px}
.markdown-body p{margin:0 0 16px}
.markdown-body ul{margin:0 0 16px;padding-left:2em}
.markdown-body li{margin:.25em 0}
.markdown-body hr{height:.25em;padding:0;margin:24px 0;background:#30363d;border:0}
.markdown-body table{border-collapse:collapse;margin:0 0 16px}
.markdown-body th,.markdown-body td{border:1px solid #30363d;padding:6px 13px}
.markdown-body tr:nth-child(2n){background:#161b22}
.markdown-body code{background:rgba(110,118,129,.4);padding:.2em .4em;border-radius:6px;font-size:85%;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.markdown-body blockquote{border-left:.25em solid #30363d;color:#8b949e;padding:0 1em;margin:0 0 16px}
.markdown-body details{margin:0 0 8px}
.markdown-body summary{cursor:pointer;margin-bottom:8px}
.markdown-body img{max-width:100%;vertical-align:middle}
.markdown-body sub{font-size:80%;color:#8b949e}
.markdown-body sub a{color:#4493f8}
.appicon{border-radius:8px}
.badge{display:inline-flex;font:700 11px/18px Verdana,'DejaVu Sans',sans-serif;border-radius:3px;overflow:hidden;vertical-align:middle;letter-spacing:.2px}
.badge span{padding:0 6px;color:#fff}
.badge .l{background:#30363d;color:#c9d1d9;font-weight:400}
.chip{display:inline-block;font:600 11px/18px Verdana,sans-serif;border-radius:3px;padding:0 7px;color:#fff;vertical-align:middle}
.pinned{opacity:.35;pointer-events:none}
.pinned h4{font-size:16px;margin:0 0 12px;font-weight:400}
.pin-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:24px}
.pin{border:1px solid #30363d;border-radius:6px;padding:16px;font-size:12px;color:#8b949e;min-height:70px}
.pin b{color:#4493f8;font-size:14px;font-weight:600}
.graph{border:1px solid #30363d;border-radius:6px;padding:16px;color:#8b949e;font-size:12px;height:120px}
.designlabel{position:fixed;top:10px;right:14px;background:#1f6feb;color:#fff;padding:5px 12px;border-radius:6px;font-size:12px;font-weight:600;z-index:9;box-shadow:0 2px 8px rgba(0,0,0,.5)}
.annot{max-width:1280px;margin:0 auto;padding:16px 32px 48px;color:#8b949e;font-size:13px;line-height:1.7}
.annot h4{color:#e6edf3;margin:0 0 6px;font-size:13px;text-transform:uppercase;letter-spacing:.5px}
.annot code{background:#161b22;border:1px solid #21262d;padding:1px 6px;border-radius:4px;font-family:ui-monospace,Menlo,monospace;font-size:12px}
"""

FRAME = """<!doctype html>
<html><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head>
<body>
<div class="designlabel">{label}</div>
<div class="topnav">
  <svg height="28" viewBox="0 0 16 16" width="28"><path d="{octo}"/></svg>
  xalakox
  <div class="searchbox">Type <span style="border:1px solid #30363d;border-radius:4px;padding:0 4px">/</span> to search</div>
</div>
<div class="tabs">
  <div class="tab active">Overview</div>
  <div class="tab">Repositories <span class="count">39</span></div>
  <div class="tab">Projects</div>
  <div class="tab">Packages</div>
  <div class="tab">Stars <span class="count">25</span></div>
</div>
<div class="page">
  <div class="sidebar">
    <div class="avatar"></div>
    <div class="sb-name">Salvador Aceves Osuna</div>
    <div class="sb-handle">xalakox</div>
    <div class="btn">Edit profile</div>
    <div class="sb-line"><b>35</b> followers · <b>13</b> following</div>
    <div class="sb-links">
      <div>🏢 @TourConnect</div>
      <div>𝕏 @salvadoraceves</div>
      <div>📷 xalakox</div>
      <div>💼 in/salvadoraceves</div>
      <div>▶️ youtube.com/xalakox</div>
    </div>
    <div class="dim-note">Sidebar, achievements, orgs, pinned repos and the contribution graph stay exactly as they are — only the README card changes.</div>
  </div>
  <div class="main">
    <div class="readme">
      <div class="readme-head">xalakox / <b>README</b>.md</div>
      <div class="markdown-body">
{body}
      </div>
    </div>
    <div class="pinned">
      <h4>Pinned</h4>
      <div class="pin-grid">
        <div class="pin"><b>TourConnect/secrets2env</b> · Public<br><br>An executable dependency that would retrieve secrets from AWS…</div>
        <div class="pin"><b>ti2travel/ti2</b> · Public<br><br>Tourism Industry Interchange</div>
      </div>
      <div class="graph">3,193 contributions in the last year — (contribution graph, unchanged)</div>
    </div>
  </div>
</div>
<div class="annot">
{annot}
</div>
</body></html>
"""

ICONS = {
    "latest": "../assets/apps/latest-icon.svg",
    "visa": "../assets/apps/visa-logger-icon.png",
    "lazy": "../assets/apps/lazy-calorie-counter-icon.png",
    "split": "../assets/apps/split-screen-translate-icon.png",
    "tokengate": "../assets/apps/tokengate-icon.svg",
    "pano": "https://panoribbon.aceves.mx/assets/panoribbon-icon-256.png",
    "ti2": "../assets/company/ti2travel-avatar.jpg",
}

def chip(text, color):
    return f'<span class="chip" style="background:{color}">{text}</span>'

CHIP_LIVE = chip("live", "#238636")
CHIP_BETA = chip("public beta", "#6546D7")
CHIP_SOON = chip("soon", "#6e7681")


# ---------------------------------------------------------------- Mockup A
BODY_A = f"""
<h1 align="center">Salvador Aceves</h1>
<p align="center">Software engineer — JavaScript / Python / DevOps · living nomadic 🌎<br>
Building AI for travel operations at <a href="#"><b>TourConnect AI</b></a>.</p>
<p align="center"><a href="#">LinkedIn</a> · <a href="#">Instagram</a> · <a href="#">YouTube</a> · <a href="#">X</a> · <a href="#">SoundCloud</a> · <a href="#">WakaTime</a></p>

<h2>Work</h2>
<p>Full-time at <a href="#"><b>TourConnect AI</b></a> (Australia / US) — production AI software for
DMCs and tour operators. I run backend APIs and integrations for itinerary and booking workflows,
AWS &amp; Kubernetes infrastructure, and Python / Node.js automation services — plus frontend work
when end-to-end delivery calls for it.</p>
<p><sub>Products I work on: <a href="#">Itinerary Assist AI</a> · <a href="#">Booking Automation AI</a> · <a href="#">Closeouts Automation</a></sub></p>

<h2>Open source</h2>
<p><img src="{ICONS['ti2']}" width="20" class="appicon"> <a href="#"><b>TI2 — Tourism Information Interchange</b></a><br>
An open framework (GPL-3.0) that standardizes how tourism systems exchange bookings, content, and
rates through a plugin architecture — one shared layer instead of one-off point-to-point integrations.</p>
<p><sub>Connectors: <a href="#">Tourplan</a> · <a href="#">Ventrata</a> · <a href="#">full plugin library</a></sub></p>

<h2>Apps</h2>
<p><sub>Personal side projects — privacy-first, mostly on-device.</sub></p>
<p><img src="{ICONS['pano']}" width="22" class="appicon"> <a href="#"><b>PanoRibbon</b></a> — turn one wide photo into a seamless carousel or pan video, entirely on your phone. {CHIP_LIVE}</p>
<p><img src="{ICONS['latest']}" width="22" class="appicon"> <a href="#"><b>Latest</b></a> — a podcast player that keeps one episode per show: the newest. No backlog to manage. {CHIP_LIVE}</p>
<p><img src="{ICONS['visa']}" width="22" class="appicon"> <a href="#"><b>Visa Logger</b></a> — private visa planner and identity wallet; country limits, timelines, and documents stay on-device. {CHIP_LIVE}</p>
<p><img src="{ICONS['tokengate']}" width="22" class="appicon"> <a href="#"><b>TokenGate</b></a> — LLM keys, versioned prompts, and quotas in one place, published as API endpoints. {CHIP_BETA}</p>
<p><img src="{ICONS['lazy']}" width="22" class="appicon"> <a href="#"><b>Lazy Calorie Counter</b></a> — macro tracking straight from your photo library; on-device food detection, no manual logging. {CHIP_SOON}</p>
<p><img src="{ICONS['split']}" width="22" class="appicon"> <a href="#"><b>SplitScreenTranslate</b></a> — live speech transcription and translation in a dual-pane view. {CHIP_SOON}</p>

<h2>Music</h2>
<p>Guitar ideas on SoundCloud — <a href="#">My Song 8</a>, <a href="#">My Song 5</a>, <a href="#">Tart Heart</a> · <a href="#">full profile</a> 🎸</p>
"""

ANNOT_A = """
<h4>Mockup A — “Quiet Typography”: how it maps to real markdown</h4>
Everything is plain GFM: centered hero via <code>&lt;h1 align="center"&gt;</code> / <code>&lt;p align="center"&gt;</code>,
apps are one-line entries with 22px inline icons, secondary info uses <code>&lt;sub&gt;</code>.
The status chips are small shields.io <code>flat</code> badges. No tables, no big badges — the whole
README fits in roughly one screen and reads like GitHub’s own UI. Deep detail (feature bullets) is
dropped in favor of each app’s website link.
"""

# ---------------------------------------------------------------- Mockup B
def card(icon, name, tagline, chip_html):
    return f"""<td align="center" width="50%" valign="top">
<br><img src="{icon}" width="64" class="appicon"><br><br>
<b><a href="#">{name}</a></b>&nbsp;&nbsp;{chip_html}<br>
<sub>{tagline}</sub><br><br>
</td>"""

BODY_B = f"""
<h1>Hi, I'm Salvador 👋</h1>
<p>Software engineer · JavaScript / Python · DevOps · living nomadic 🌎</p>
<p>
<span class="badge"><span class="l">in</span><span style="background:#0A66C2">LinkedIn</span></span>
<span class="badge"><span class="l">📷</span><span style="background:#E4405F">Instagram</span></span>
<span class="badge"><span class="l">▶</span><span style="background:#c4302b">YouTube</span></span>
<span class="badge"><span class="l">𝕏</span><span style="background:#555">@SalvadorAceves</span></span>
<span class="badge"><span class="l">☁</span><span style="background:#f50">SoundCloud</span></span>
<span class="badge"><span class="l">wakatime</span><span style="background:#2F3241">7,778 hrs</span></span>
</p>

<h2>💼 TourConnect AI</h2>
<p>Full-time at <a href="#"><b>TourConnect AI</b></a> (Australia / US), building production AI software for DMCs and tour operators.</p>
<table>
<tr>
<td width="55%" valign="top"><b>What I do</b><br><br>
· Backend APIs for itinerary &amp; booking workflows<br>
· AWS + Kubernetes deployment, scaling, reliability<br>
· Python / Node.js automation and data processing<br>
· End-to-end frontend delivery when needed
</td>
<td valign="top"><b>Products</b><br><br>
<a href="#">Itinerary Assist AI</a> — quoting workflows<br>
<a href="#">Booking Automation AI</a> — inbox to booking<br>
<a href="#">Closeouts Automation</a> — stopsell handling
</td>
</tr>
</table>

<h3>🌍 Open source — TI2 <img src="{ICONS['ti2']}" width="22" class="appicon"></h3>
<p><a href="#"><b>Tourism Information Interchange</b></a> — an open framework (GPL-3.0) developed under the
TourConnect umbrella, standardizing how tourism systems exchange bookings, content, and rates via plugins:
<a href="#">Tourplan</a>, <a href="#">Ventrata</a>, and the <a href="#">plugin library</a>.</p>

<h2>🚀 SaaS apps</h2>
<table>
<tr>
<td width="96" align="center" valign="middle"><img src="{ICONS['tokengate']}" width="64" class="appicon"></td>
<td valign="middle">
<b><a href="#">TokenGate</a></b>&nbsp;&nbsp;{CHIP_BETA}<br>
<sub>LLM keys, versioned prompts, and quotas in one place — published as API endpoints, managed from a web
dashboard or a permission-scoped remote MCP endpoint.</sub><br>
<sub><a href="#">tokengate.aceves.mx</a></sub>
</td>
</tr>
</table>

<h2>📱 Personal apps</h2>
<table>
<tr>
{card(ICONS['pano'], 'PanoRibbon', 'One wide photo → seamless carousel or pan video, all on-device', CHIP_LIVE)}
{card(ICONS['latest'], 'Latest', 'Podcast player that keeps only the newest episode of every show', CHIP_LIVE)}
</tr>
<tr>
{card(ICONS['visa'], 'Visa Logger', 'Private visa planner &amp; identity wallet — nothing leaves your device', CHIP_LIVE)}
{card(ICONS['lazy'], 'Lazy Calorie Counter', 'Macro tracking straight from your photo library, no manual logging', CHIP_SOON)}
</tr>
<tr>
<td align="center" colspan="2">
<br><img src="{ICONS['split']}" width="64" class="appicon"><br><br>
<b><a href="#">SplitScreenTranslate</a></b>&nbsp;&nbsp;{CHIP_SOON}<br>
<sub>Live speech transcription + translation in a dual-pane view</sub><br><br>
</td>
</tr>
</table>

<h2>🎸 Music</h2>
<p>Guitar ideas on <a href="#">SoundCloud</a> — <a href="#">My Song 8</a> · <a href="#">My Song 5</a> · <a href="#">Tart Heart</a></p>
"""

ANNOT_B = """
<h4>Mockup B — “Product Grid”: how it maps to real markdown</h4>
The app grids are plain HTML <code>&lt;table&gt;</code>s with <code>&lt;td align="center" width="50%"&gt;</code> cells —
GitHub draws the borders and the alternating row tint itself, which is embraced as the card look.
TI2 sits inside the TourConnect section as an <code>&lt;h3&gt;</code> (it’s under the TC umbrella). SaaS apps get a
full-width horizontal card; the odd 5th personal app uses <code>colspan="2"</code> (allowed by GitHub’s sanitizer).
Social badges become a single consistent row of shields.io <code>flat</code> badges. Everything else is standard GFM.
"""

# ---------------------------------------------------------------- Mockup C
def acc(icon, name, tagline, chip_html, body, open_=False):
    return f"""<details{' open' if open_ else ''}>
<summary><img src="{icon}" width="20" class="appicon"> <b>{name}</b> — {tagline} &nbsp;{chip_html}</summary>
{body}
</details>"""

BODY_C = f"""
<p><b>Salvador Aceves</b> — software engineer (JavaScript / Python / DevOps), living nomadic 🌎.
Full-time at <a href="#"><b>TourConnect AI</b></a>, building production AI for travel operations.</p>
<p><sub><a href="#">LinkedIn</a> · <a href="#">Instagram</a> · <a href="#">YouTube</a> · <a href="#">X</a> · <a href="#">SoundCloud</a> · <a href="#">WakaTime</a></sub></p>
<blockquote>📍 Now: booking &amp; itinerary automation at TourConnect AI · shipping privacy-first mobile apps on the side</blockquote>

<h2>Work — TourConnect AI</h2>
<p>AI software for DMCs and tour operators: <a href="#">Itinerary Assist</a>, <a href="#">Booking Automation</a>, <a href="#">Closeouts Automation</a>.</p>
<details>
<summary><b>Day-to-day scope</b></summary>
<ul>
<li>Backend APIs and integrations for itinerary and booking workflows</li>
<li>AWS infrastructure and Kubernetes operations for deployment, scaling, and reliability</li>
<li>Python and Node.js services for automation and data processing</li>
<li>Frontend product work for end-to-end delivery</li>
</ul>
</details>

<h2>Apps</h2>
<p><sub>Privacy-first personal apps — tap to expand.</sub></p>
{acc(ICONS['latest'], 'Latest', 'a podcast player that keeps one episode per show: the newest', CHIP_LIVE, '''
<ul>
<li>Rebuilds a single newest-first queue whenever feeds refresh — no backlog to manage</li>
<li>Apple Podcasts search or direct RSS, offline downloads, lock-screen + Google Cast playback</li>
</ul>
<p><a href="#">latest.aceves.mx</a></p>
''', open_=True)}
{acc(ICONS['pano'], 'PanoRibbon', 'one wide photo → seamless carousel or pan video, on-device', CHIP_LIVE, '<p><a href="#">panoribbon.aceves.mx</a></p>')}
{acc(ICONS['visa'], 'Visa Logger', 'private visa planner &amp; identity wallet', CHIP_LIVE, '<p><a href="#">visa.aceves.mx</a></p>')}
{acc(ICONS['tokengate'], 'TokenGate', 'LLM keys, prompts, and quotas in one place', CHIP_BETA, '<p><a href="#">tokengate.aceves.mx</a></p>')}
{acc(ICONS['lazy'], 'Lazy Calorie Counter', 'macro tracking straight from your photo library', CHIP_SOON, '<p>Public release soon.</p>')}
{acc(ICONS['split'], 'SplitScreenTranslate', 'live speech transcription + translation, dual-pane', CHIP_SOON, '<p>Public release soon.</p>')}

<h2>Open source — TI2</h2>
<p><img src="{ICONS['ti2']}" width="20" class="appicon"> <a href="#"><b>Tourism Information Interchange</b></a> — open framework (GPL-3.0) standardizing
bookings / content / rates exchange for the tourism industry. <a href="#">Tourplan</a> · <a href="#">Ventrata</a> · <a href="#">plugins</a></p>

<h2>Music</h2>
<p>Guitar on <a href="#">SoundCloud</a> — <a href="#">My Song 8</a> · <a href="#">My Song 5</a> · <a href="#">Tart Heart</a> 🎸</p>
"""

ANNOT_C = """
<h4>Mockup C — “Compact Dossier”: how it maps to real markdown</h4>
Every app is a native <code>&lt;details&gt;/&lt;summary&gt;</code> accordion — icons and status chips render
inside summaries on GitHub. Nothing is deleted from today’s content: the feature bullets simply live
inside the collapsed sections (first one shown expanded here for illustration). The “Now” strip is a
plain <code>blockquote</code>. Shortest default view of the three while keeping all detail one click away.
"""

PAGES = [
    ("mockup-a-quiet-typography.html", "Mockup A — Quiet Typography", BODY_A, ANNOT_A),
    ("mockup-b-product-grid.html", "Mockup B — Product Grid", BODY_B, ANNOT_B),
    ("mockup-c-compact-dossier.html", "Mockup C — Compact Dossier", BODY_C, ANNOT_C),
]

for fname, label, body, annot in PAGES:
    html = FRAME.format(title=label, css=CSS, octo=OCTO, label=label, body=body, annot=annot)
    (OUT / fname).write_text(html)
    print("wrote", fname)
