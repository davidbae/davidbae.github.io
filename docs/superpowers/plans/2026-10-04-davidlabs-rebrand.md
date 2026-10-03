# David Labs 리브랜딩 + 제이제이 여행맛집 연결 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 단일 `index.html`을 확정 DAVIDLABS 브랜드(라이트 + 잉크 네이비)로 바꾸고, 제품 섹션에 제이제이 여행맛집 카드를 추가해 외부 사이트로 연결한다.

**Architecture:** 빌드 없는 GitHub Pages 원페이지. 스타일은 `index.html`의 `<style>` 블록 하나에 두고, 로고는 루트 `logo/`의 확정 SVG/PNG를 그대로 참조한다. 규칙 준수는 Python 정적 검사 스크립트로, 화면은 Playwright로 확인한다.

**Tech Stack:** HTML/CSS, Google Fonts(Archivo), Pretendard CDN, Python 3(검사 스크립트), Playwright MCP(시각 검증)

**Spec:** `docs/superpowers/specs/2026-10-04-davidlabs-rebrand-design.md`
**근거 자료:** `assets/design_handoff_davidlabs_20261003_v1.0/README.md`

## Global Constraints

- 단일 `index.html` + `<style>` 블록, 빌드 도구·외부 CSS/JS 파일 없음
- 컬러: Ink Navy `#2B4A8C`, Navy Hover `#1d3466`, Cyan `#22B0D9`(작은 강조만, 본문 글자색 금지), Charcoal `#1d1f20`, Muted `#4a4d50`, Background `#f2f2f3`, Surface `#ffffff`, Border `#d5d6d8`
- 서체: Archivo 300/400/500/600/700(Google Fonts), Pretendard(`https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css`)
- 모서리 `--radius:4px`
- `logo/` 파일은 수정 금지
- 이메일은 `iamdavidbae@gmail.com` 유지 (mailto 5곳, subject 파라미터 유지)
- `og:image`는 `https://davidbae.github.io/logo/favicon-512.png`
- JJ URL: `https://jjtastesandtravels-web.iamdavidbae.workers.dev/`, 반드시 `target="_blank" rel="noopener"`
- 문구·섹션 순서·앵커(`#what #product #why #contact`)·breakpoint(720/820px) 유지. 단, 제품 섹션 제목/부제만 변경
- 푸터 TODO(사업자등록번호, 약관 링크) 유지
- 새 소스 파일 첫 줄은 한국어 역할 주석
- 커밋은 사용자 확인 후 실행

## Review Focus

1. **820~1024px 폭(태블릿 가로)**: 3열 카드가 좁아져도 버튼 글자가 넘치거나 잘리지 않아야 한다 → Task 4에서 900px 캡처
2. **390px 모바일**: 헤더에 로고와 "문의" 버튼이 겹치지 않고, 카드 3개가 1열로 쌓여야 한다 → Task 4에서 390px 캡처
3. **키보드 탐색(라이트 배경)**: Tab으로 이동할 때 네이비 포커스 아웃라인이 보여야 한다 → Task 2 검사(CSS 규칙) + Task 4 Tab 캡처
4. **폰트 CDN 차단**: Archivo/Pretendard가 로드되지 않아도 시스템 sans-serif로 표시되어야 한다 → Task 2 검사(`--sans`, `--display`가 `sans-serif`로 끝남)
5. **davidlabs.co.kr 프레임 안에서 JJ 클릭**: 프레임 안이 아니라 새 탭으로 열려야 한다 → Task 3 검사(`target="_blank"`)

---

## 파일 구조

| 파일 | 역할 | 작업 |
| --- | --- | --- |
| `scripts/check_site.py` | `index.html` 브랜드·링크 규칙 정적 검사 | 생성 (Task 1) |
| `logo/` | 확정 로고·파비콘 (핸드오프 복사본) | 생성 (Task 1) |
| `assets/design_handoff_davidlabs_20261003_v1.0/` | 원본 핸드오프 (기록용) | 커밋만 (Task 1) |
| `index.html` | 홈페이지 | 수정 (Task 2, 3) |
| `checklist.md`, `context-notes.md`, `docs/superpowers/**` | 작업 문서 | 갱신·커밋 (Task 4) |

참고: 설계서의 커밋 4개에 검사 스크립트가 더해진다. 스크립트는 Task 1 커밋에 함께 넣는다.

---

### Task 1: 에셋 배치 + 정적 검사 스크립트

**Files:**
- Create: `logo/` (`assets/design_handoff_davidlabs_20261003_v1.0/logo/` 복사)
- Create: `scripts/check_site.py`

**Interfaces:**
- Produces: `python3 scripts/check_site.py` — 항목별 `PASS`/`FAIL` 출력, 하나라도 FAIL이면 종료 코드 1. Task 2, 3, 4가 이 명령으로 검증한다.

- [ ] **Step 1: logo/ 복사**

```bash
cd /Users/davidbae/Development/WebSiteDev/davidbae.github.io
cp -R assets/design_handoff_davidlabs_20261003_v1.0/logo ./logo
ls logo
```
Expected: `favicon.svg favicon-32.png apple-touch-icon.png favicon-512.png davidlabs-horizontal.svg` 등 14개 파일

- [ ] **Step 2: 검사 스크립트 작성**

`scripts/check_site.py`:

```python
# index.html이 DAVIDLABS 브랜드·링크 규칙을 지키는지 정적으로 검사하는 스크립트
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
JJ_URL = "https://jjtastesandtravels-web.iamdavidbae.workers.dev/"

failures = []


def check(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        failures.append(name)


# 다크 테마 잔재
for leftover in ["#34d399", "52,211,153", "rgba(255,255,255", "rgba(11,14,17"]:
    check(f"다크 테마 잔재 없음: {leftover}", leftover not in HTML)

# 토큰 · 서체
check("토큰 --bg:#f2f2f3", "--bg:#f2f2f3" in HTML)
check("토큰 --accent:#2B4A8C", "--accent:#2B4A8C" in HTML)
check("토큰 --accent-hover:#1d3466", "--accent-hover:#1d3466" in HTML)
check("토큰 --highlight:#22B0D9", "--highlight:#22B0D9" in HTML)
check("토큰 --radius:4px", "--radius:4px" in HTML)
check("Archivo 로드", "fonts.googleapis.com/css2?family=Archivo" in HTML)
check("Pretendard 로드", "orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css" in HTML)
for var in ["--sans", "--display"]:
    m = re.search(var + r":([^;]+);", HTML)
    check(f"{var} 폴백이 sans-serif로 끝남", m is not None and m.group(1).strip().endswith("sans-serif"))

# 시안은 본문 글자색 금지 (color: 속성에 쓰지 않음)
check("시안을 글자색으로 쓰지 않음",
      re.search(r"(?<![-\w])color:\s*(var\(--highlight\)|#22B0D9)", HTML, re.I) is None)

# 로고 · 파비콘 · OG
for ref in re.findall(r'(?:src|href)="(logo/[^"]+)"', HTML):
    check(f"에셋 파일 존재: {ref}", (ROOT / ref).is_file())
check("헤더 로고 20px",
      re.search(r'<header>.*?<img src="logo/davidlabs-horizontal.svg" alt="DAVIDLABS" height="20">', HTML, re.S) is not None)
check("푸터 로고 16px",
      re.search(r'<footer>.*?<img src="logo/davidlabs-horizontal.svg" alt="DAVIDLABS" height="16">', HTML, re.S) is not None)
check("초록 점(.dot) 제거", 'class="dot"' not in HTML and ".brand .dot" not in HTML)
check("favicon.svg 링크", '<link rel="icon" href="logo/favicon.svg" type="image/svg+xml">' in HTML)
check("apple-touch-icon 링크", '<link rel="apple-touch-icon" href="logo/apple-touch-icon.png">' in HTML)
check("theme-color", '<meta name="theme-color" content="#2B4A8C">' in HTML)
check("og:image는 github.io",
      '<meta property="og:image" content="https://davidbae.github.io/logo/favicon-512.png">' in HTML)

# 접근성
check("focus-visible 아웃라인", "outline:2px solid var(--accent); outline-offset:2px;" in HTML)

# 이메일
mailtos = re.findall(r'href="mailto:([^"?]+)', HTML)
check("mailto 5곳", len(mailtos) == 5)
check("mailto 모두 iamdavidbae@gmail.com", all(m == "iamdavidbae@gmail.com" for m in mailtos))
check("david@davidlabs.co.kr 미사용", "david@davidlabs.co.kr" not in HTML)

# 섹션 · 앵커
for anchor in ["what", "product", "why", "contact"]:
    check(f'앵커 id="{anchor}"', f'id="{anchor}"' in HTML)

# DLogTracer 표기
check("DLogTracer 표기 규칙",
      '<span style="font-weight:600;color:var(--text)">D</span>'
      '<span style="font-weight:600;color:var(--accent)">Log</span>'
      '<span style="font-weight:300;color:var(--text)">Tracer</span>' in HTML)

# 제품 섹션 · JJ 카드
product = re.search(r'<section id="product".*?</section>', HTML, re.S)
product_html = product.group(0) if product else ""
check("제품 섹션 제목 '세 가지'", "지금 만들고 있는 세 가지" in product_html)
check("제품 그리드 cols-3", 'class="grid cols-3"' in product_html)
check("제품 카드 3개", product_html.count('class="card product-card"') == 3)
check("JJ 카드 제목", "제이제이 여행맛집" in product_html)
jj_link = re.search(r'<a [^>]*href="' + re.escape(JJ_URL) + r'"[^>]*>', product_html)
check("JJ 링크 존재", jj_link is not None)
check("JJ 링크 새 탭 + noopener",
      jj_link is not None and 'target="_blank"' in jj_link.group(0) and 'rel="noopener"' in jj_link.group(0))

print()
print(f"{len(failures)} failed" if failures else "ALL PASS")
sys.exit(1 if failures else 0)
```

- [ ] **Step 3: 스크립트 실행 — 실패 확인**

Run: `python3 scripts/check_site.py`
Expected: 종료 코드 1. `FAIL  다크 테마 잔재 없음: #34d399`, `FAIL  토큰 --accent:#2B4A8C`, `FAIL  JJ 링크 존재` 등 다수 FAIL. `PASS  앵커 id="what"` 등 앵커 4개와 `mailto 5곳`, `mailto 모두 iamdavidbae@gmail.com`은 PASS.

- [ ] **Step 4: 커밋 (사용자 확인 후)**

```bash
git add logo assets scripts/check_site.py
git commit -m "DAVIDLABS 로고 에셋과 사이트 검사 스크립트 추가"
```
(`.DS_Store`는 추가하지 않는다. `git status`로 확인)

---

### Task 2: index.html 리브랜딩 (핸드오프 README 1~6, 9)

**Files:**
- Modify: `index.html` — `<head>`(1~14행), `<style>`(15~135행), 헤더(140~150행), 히어로 파형(156~161행), DLogTracer 제목(231행), 푸터 브랜드(290행)

행 번호는 모두 **수정 전 원본 기준**이다. Step 2에서 `<head>`에 줄이 추가되어 이후 번호가 밀리므로, 행 번호보다 인용한 기존 코드 문자열로 위치를 찾는다.

**Interfaces:**
- Consumes: `scripts/check_site.py`, `logo/davidlabs-horizontal.svg`, `logo/favicon*.{svg,png}`, `logo/apple-touch-icon.png`
- Produces: CSS 토큰 `--accent`, `--accent-hover`, `--accent-dim`, `--highlight`, `--display`, `--radius`과 클래스 `.brand`, `.btn-primary`, `.btn-ghost`, `.card`, `.badge`, `.chip`. Task 3이 이 이름을 그대로 쓴다.

- [ ] **Step 1: 검사 실행 — 실패 확인**

Run: `python3 scripts/check_site.py`
Expected: 종료 코드 1 (토큰·로고·파비콘 항목 FAIL)

- [ ] **Step 2: `<head>`에 파비콘·OG·폰트 추가**

13행 `<meta property="og:locale" content="ko_KR" />` 바로 다음에 삽입:

```html
<meta property="og:image" content="https://davidbae.github.io/logo/favicon-512.png">
<meta name="theme-color" content="#2B4A8C">

<!-- 파비콘 -->
<link rel="icon" href="logo/favicon.svg" type="image/svg+xml">
<link rel="icon" href="logo/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="logo/apple-touch-icon.png">

<!-- 서체: Archivo(라틴), Pretendard(한글) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@300;400;500;600;700&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css">
```

- [ ] **Step 3: `:root` 토큰 교체**

16~30행을 아래로 교체:

```css
  /* ===== 디자인 토큰 (DAVIDLABS 브랜드 — 핸드오프 README 확정값) ===== */
  :root{
    --bg:#f2f2f3;           /* 페이지 바탕 */
    --surface:#ffffff;      /* 카드 표면 */
    --surface-2:#f7f7f9;    /* 보조 표면 */
    --text:#1d1f20;         /* 본문 (Charcoal) */
    --muted:#4a4d50;        /* 보조 텍스트 */
    --border:#d5d6d8;
    --accent:#2B4A8C;       /* Ink Navy: 버튼·링크·강조 */
    --accent-hover:#1d3466; /* Navy Hover */
    --accent-dim:rgba(43,74,140,.08);
    --highlight:#22B0D9;    /* Cyan: 작은 강조에만. 본문 글자색 금지 */
    --radius:4px;
    --maxw:1080px;
    --mono:ui-monospace,SFMono-Regular,Menlo,"SF Mono",Consolas,"Liberation Mono",monospace;
    --sans:"Pretendard",-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;
    --display:"Archivo","Pretendard",sans-serif;
  }
```

- [ ] **Step 4: 공통·헤더·버튼 CSS 수정**

`h1,h2,h3{...}` 행(46행) 다음 줄에 추가:

```css
  h1,h2,.product-name{font-family:var(--display);}
  a:focus-visible,button:focus-visible{outline:2px solid var(--accent); outline-offset:2px;}
```

헤더 배경(54행) 교체:

```css
    background:rgba(242,242,243,.85); backdrop-filter:blur(10px);
```

`.brand`, `.brand .dot` 두 행(58~59행)을 아래로 교체:

```css
  .brand{display:flex; align-items:center;}
  .brand img{display:block;}
```

`.btn` ~ `.btn-ghost:hover`(63~70행)를 아래로 교체:

```css
  .btn{
    display:inline-flex; align-items:center; gap:8px;
    padding:11px 20px; border-radius:var(--radius); font-size:15px; font-weight:600;
    border:1px solid var(--border); transition:all .15s; cursor:pointer;
  }
  .btn-primary{background:var(--accent); color:#fff; border-color:var(--accent);}
  .btn-primary:hover{background:var(--accent-hover); border-color:var(--accent-hover); transform:translateY(-1px);}
  .btn-ghost:hover{background:var(--accent-dim); border-color:var(--accent);}
```

- [ ] **Step 5: 카드·제품·배지·칩·서비스 CSS 수정**

`.card:hover`(98행) 교체:

```css
  .card:hover{border-color:rgba(43,74,140,.35); background:#fff;}
```

`.product`(104행) 교체:

```css
  .product{background:linear-gradient(180deg,transparent, rgba(43,74,140,.03));}
```

`.product-name .dlog`, `.product-name .tracer` 두 행(106~107행) 삭제 (DLogTracer는 Step 7의 inline span으로 표기).

`.badge`(108~112행) 교체:

```css
  .badge{
    display:inline-block; font-family:var(--mono); font-size:12px; letter-spacing:.06em;
    color:var(--accent); background:var(--accent-dim); border:1px solid rgba(43,74,140,.25);
    padding:5px 11px; border-radius:var(--radius); margin-bottom:18px;
  }
```

`.chip`(117행)의 `border-radius:999px`를 `border-radius:var(--radius)`로 바꾼다.

`.service`(120행)의 `background:var(--surface)`를 `background:#fff`로 바꾼다.

- [ ] **Step 6: 헤더·푸터 로고, 히어로 파형 교체**

헤더(142행):

```html
    <a href="#" class="brand"><img src="logo/davidlabs-horizontal.svg" alt="DAVIDLABS" height="20"></a>
```

푸터(290행):

```html
      <div class="brand" style="margin-bottom:8px;"><img src="logo/davidlabs-horizontal.svg" alt="DAVIDLABS" height="16"></div>
```

히어로 파형 첫 번째 polyline(158행)의 stroke 속성:

```html
        stroke="#2B4A8C" stroke-width="2" stroke-opacity="0.18" fill="none"/>
```

두 번째 polyline(160행):

```html
        stroke="#22B0D9" stroke-width="1.5" stroke-opacity="0.35" fill="none"/>
```

- [ ] **Step 7: DLogTracer 표기 교체**

231행 `<h3 ...><span class="dlog">DLog</span><span class="tracer">Tracer</span></h3>`를 아래로 교체:

```html
        <h3 style="font-family:var(--display); font-size:26px; margin:6px 0 4px; letter-spacing:-0.02em;"><span style="font-weight:600;color:var(--text)">D</span><span style="font-weight:600;color:var(--accent)">Log</span><span style="font-weight:300;color:var(--text)">Tracer</span></h3>
```

(제목 크기·여백 inline style은 Task 3에서 클래스로 옮긴다.)

- [ ] **Step 8: 검사 실행 — 리브랜딩 항목 통과 확인**

Run: `python3 scripts/check_site.py`
Expected: 제품 섹션 항목(`제품 섹션 제목 '세 가지'`, `제품 그리드 cols-3`, `제품 카드 3개`, `JJ 카드 제목`, `JJ 링크 존재`, `JJ 링크 새 탭 + noopener`) 6개만 FAIL, 나머지 전부 PASS.

- [ ] **Step 9: 커밋 (사용자 확인 후)**

```bash
git add index.html
git commit -m "홈페이지를 DAVIDLABS 브랜드(라이트·잉크 네이비)로 리브랜딩"
```

---

### Task 3: 제이제이 여행맛집 카드 + 제품 카드 정리

**Files:**
- Modify: `index.html` — `<style>`의 제품 섹션 CSS, `<section id="product">` 전체(207~247행 부근)

**Interfaces:**
- Consumes: Task 2의 `.card`, `.badge`, `.chip`, `.chips`, `.btn-primary`, `--display`, `--accent`
- Produces: 클래스 `.product-card`, `.product-title`, `.product-sub`, `.product-desc`, `.card-cta`

- [ ] **Step 1: 검사 실행 — 실패 확인**

Run: `python3 scripts/check_site.py`
Expected: 제품 섹션 항목 6개 FAIL

- [ ] **Step 2: 제품 카드 CSS 추가**

`.product .desc{...}` 행 바로 다음에 추가:

```css
  .product-card{display:flex; flex-direction:column; align-items:flex-start;}
  .product-title{font-family:var(--display); font-size:24px; margin:6px 0 12px; letter-spacing:-0.02em;}
  .product-sub{font-family:var(--mono); font-size:12.5px; color:var(--muted); margin:-8px 0 12px;}
  .product-desc{margin-top:14px;}
  .product-card .chips{margin-top:16px;}
  .card-cta{margin-top:auto; padding-top:24px;}
```

- [ ] **Step 3: 제품 섹션 HTML 교체**

`<section id="product" class="product">` ~ `</section>`를 아래로 교체:

```html
<section id="product" class="product">
  <div class="wrap">
    <p class="eyebrow">제품</p>
    <h2 style="max-width:20ch; margin-bottom:12px;">지금 만들고 있는 세 가지</h2>
    <p class="muted" style="max-width:56ch; font-size:17px; margin-bottom:40px;">
      일상의 생산성부터 자동차 진단, 여행까지 — David Labs가 직접 개발하는 제품입니다.
    </p>

    <div class="grid cols-3">
      <!-- 제품 1: 집중력 앱 -->
      <div class="card product-card">
        <span class="ico">MOBILE / PRODUCTIVITY</span>
        <!-- TODO: 앱 정식 명칭 확정 후 '집중력 앱'을 교체 -->
        <h3 class="product-title">집중력 앱 <span class="muted" style="font-size:14px; font-weight:400;">(제품명 미정)</span></h3>
        <span class="badge">● 개발 중</span>
        <p class="product-desc">집중이 필요한 순간, 몰입을 도와주는 모바일 앱. 산만함을 줄이고 한 가지에 집중하도록 돕습니다.</p>
        <div class="card-cta">
          <a href="mailto:iamdavidbae@gmail.com?subject=%EC%A7%91%EC%A4%91%EB%A0%A5%20%EC%95%B1%20%EB%AC%B8%EC%9D%98" class="btn btn-primary">출시 알림·문의</a>
        </div>
      </div>

      <!-- 제품 2: DLogTracer -->
      <div class="card product-card">
        <span class="ico">AUTOMOTIVE / DLT</span>
        <h3 class="product-title"><span style="font-weight:600;color:var(--text)">D</span><span style="font-weight:600;color:var(--accent)">Log</span><span style="font-weight:300;color:var(--text)">Tracer</span></h3>
        <p class="product-sub">디-로그-트레이서 · Diagnostic Log &amp; Trace</p>
        <span class="badge">● 개발·평가 단계</span>
        <p class="product-desc">AUTOSAR/COVESA 기반 <strong style="color:var(--text)">DLT 로그를 추적·분석하는 DLT Viewer 플러그인</strong>. 흩어진 로그를 추적하고, 필요한 신호만 걸러내고, 이상을 알립니다.</p>
        <div class="chips">
          <span class="chip">Trace 추적</span>
          <span class="chip">Export 추출</span>
          <span class="chip">Alert 알림</span>
        </div>
        <div class="card-cta">
          <!-- 지금은 평가 단계 → 메일 문의. 추후 DLogTracerHub 링크로 교체 -->
          <a href="mailto:iamdavidbae@gmail.com?subject=DLogTracer%20%EB%8F%84%EC%9E%85%C2%B7%EC%B6%9C%EC%8B%9C%20%EB%AC%B8%EC%9D%98" class="btn btn-primary">출시 알림·도입 문의</a>
        </div>
      </div>

      <!-- 제품 3: 제이제이 여행맛집 (외부 사이트, Cloudflare Workers) -->
      <div class="card product-card">
        <span class="ico">WEB / TRAVEL</span>
        <h3 class="product-title">제이제이 여행맛집</h3>
        <p class="product-sub">JJ's Tastes &amp; Travels</p>
        <span class="badge">● 운영 중</span>
        <p class="product-desc">여행·맛집 유튜브 채널의 여행자 도구 사이트. 매장에서 잠금화면만 보고 현지 가격을 원화로 확인하는 환율 잠금화면을 제공합니다.</p>
        <div class="chips">
          <span class="chip">환율 잠금화면</span>
          <span class="chip">크루즈 가이드 (준비 중)</span>
        </div>
        <div class="card-cta">
          <!-- davidlabs.co.kr이 프레임 포워딩이라 반드시 새 탭으로 연다 -->
          <a href="https://jjtastesandtravels-web.iamdavidbae.workers.dev/" target="_blank" rel="noopener" class="btn btn-primary">사이트 방문 ↗</a>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 4: 검사 실행 — 전체 통과 확인**

Run: `python3 scripts/check_site.py`
Expected: `ALL PASS`, 종료 코드 0

- [ ] **Step 5: 커밋 (사용자 확인 후)**

```bash
git add index.html
git commit -m "제품 섹션에 제이제이 여행맛집 카드 추가"
```

---

### Task 4: 브라우저 시각 검증 + 문서 정리

**Files:**
- Modify: `checklist.md`, `context-notes.md`
- Commit: `docs/superpowers/specs/2026-10-04-davidlabs-rebrand-design.md`, `docs/superpowers/plans/2026-10-04-davidlabs-rebrand.md`

**Interfaces:**
- Consumes: Task 1~3 결과물 전체

- [ ] **Step 1: 로컬 서버 실행**

```bash
cd /Users/davidbae/Development/WebSiteDev/davidbae.github.io
python3 -m http.server 8765
```
(백그라운드 실행)

- [ ] **Step 2: Playwright로 1280px 확인**

`browser_resize` 1280×900 → `browser_navigate` `http://localhost:8765/` → `browser_take_screenshot` (fullPage).
Expected: 헤더에 가로형 로고, 라이트 배경, 네이비 버튼, 제품 카드 3개가 한 줄에 있고 버튼 높이가 같음.

- [ ] **Step 3: 900px · 390px 확인 (Review Focus 1, 2)**

900×900, 390×844로 각각 리사이즈 후 fullPage 캡처.
Expected: 900px에서 카드 3열의 버튼 글자가 넘치지 않음. 390px에서 헤더 로고와 "문의" 버튼이 겹치지 않고 카드가 1열로 쌓임.

- [ ] **Step 4: 네트워크·콘솔 확인**

`browser_network_requests`: `logo/*`, Archivo, Pretendard 요청이 모두 200.
`browser_console_messages`: error 0건.

- [ ] **Step 5: 키보드 포커스·앵커·JJ 링크 확인 (Review Focus 3, 5)**

`browser_press_key` Tab을 3번 누른 뒤 캡처 → 포커스된 요소에 네이비 아웃라인이 보임.
`browser_navigate` `http://localhost:8765/#product` → 제품 섹션으로 이동.
`browser_evaluate`로 확인:

```js
() => { const a = document.querySelector('a[href^="https://jjtastesandtravels"]'); return [a.target, a.rel]; }
```
Expected: `["_blank", "noopener"]`

- [ ] **Step 6: 서버 종료, 정적 검사 재실행**

서버 프로세스를 종료하고 `python3 scripts/check_site.py` 실행.
Expected: `ALL PASS`

- [ ] **Step 7: checklist.md · context-notes.md 갱신**

`checklist.md`의 구현·검증 항목을 완료 표시한다. 검증 중 발견한 사항(예: 900px 레이아웃 조정 여부)과 남은 과제(davidlabs.co.kr DNS 정식 연결, `david@davidlabs.co.kr` 메일함 개설 후 이메일 교체)를 `context-notes.md`에 추가한다.

- [ ] **Step 8: 커밋 (사용자 확인 후)**

```bash
git add checklist.md context-notes.md docs/superpowers
git commit -m "리브랜딩 설계서·구현 계획·작업 노트 추가"
```
