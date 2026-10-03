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
check("og:image는 davidlabs.co.kr",
      '<meta property="og:image" content="https://davidlabs.co.kr/logo/favicon-512.png">' in HTML)

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
check("JJ 로고 (제목 왼쪽)",
      re.search(r'<h3 class="product-title product-title-logo"><img src="images/jj-logo.png" alt="" width="40" height="40">제이제이 여행맛집</h3>',
                product_html) is not None)
check("JJ 로고 파일 존재", (ROOT / "images/jj-logo.png").is_file())
jj_link = re.search(r'<a [^>]*href="' + re.escape(JJ_URL) + r'"[^>]*>', product_html)
check("JJ 링크 존재", jj_link is not None)
check("JJ 링크 새 탭 + noopener",
      jj_link is not None and 'target="_blank"' in jj_link.group(0) and 'rel="noopener"' in jj_link.group(0))

print()
print(f"{len(failures)} failed" if failures else "ALL PASS")
sys.exit(1 if failures else 0)
