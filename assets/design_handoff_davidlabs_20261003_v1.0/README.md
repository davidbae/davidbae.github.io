# Handoff: DAVIDLABS 브랜드 적용 (로고 · 파비콘 · 홈페이지 리브랜딩)

## Overview
1인 개발사 DAVIDLABS의 확정 로고와 브랜드 규칙을 담은 패키지입니다. 작업 대상은 GitHub Pages 저장소 `davidbae/davidbae.github.io`의 `index.html`(파일 1개짜리 정적 원페이지)입니다. 지금 사이트는 다크 테마와 초록 강조색을 쓰는데, 이를 **라이트 베이스 + 잉크 네이비** 브랜드로 바꾸는 것이 목표입니다. 문구와 섹션 구성은 그대로 둡니다.

## About the Design Files
`design_reference/`의 HTML 파일은 Claude Design에서 만든 **디자인 참고 자료**입니다. 그대로 배포하는 코드가 아닙니다. `index.html`은 원래 방식(순수 HTML + `<style>` 블록, 빌드 없음)을 유지하면서 아래 규칙에 맞게 고쳐 주세요.

`logo/` 폴더의 SVG와 PNG는 **최종 산출물**이므로 그대로 사용합니다. 글자는 모두 외곽선(path)으로 변환되어 있어서 서체가 없는 환경에서도 똑같이 보입니다.

## Fidelity
- **로고 · 파비콘 · 컬러 · 서체**: High-fidelity, 확정값입니다. 값을 임의로 바꾸지 마세요.
- **홈페이지**: 별도 시안은 없습니다. 아래 "홈페이지 변경 사항"에 적힌 토큰 교체와 컴포넌트 수정으로 리브랜딩합니다. 레이아웃·문구·섹션 순서는 기존 `index.html`을 그대로 따릅니다.

---

## 로고 시스템

### 구성
- **심볼 `[>`**: 각진 대괄호(잉크 네이비)와 프롬프트 기호(시안)로 이루어져 있습니다. 개발자 콘솔에서 따온 모양입니다.
- **워드마크 `DAVIDLABS`**: Archivo 서체를 씁니다. `DAVID`는 Light 300에 차콜, `LABS`는 Bold 700에 잉크 네이비입니다. 자간은 0.07em입니다.
- **원칙**: 얇은 앞부분 + 굵은 네이비 뒷부분. 한글 락업과 제품 로고에도 같은 리듬을 씁니다.

### 비율 (H = 워드마크 대문자 높이 = Archivo 크기 × 0.686)
| 요소 | 값 |
| --- | --- |
| 심볼 높이 | H (대문자 높이와 정확히 같음, 수직 정렬도 대문자 높이 기준) |
| 대괄호 폭 / 획 두께 | 13/29 H / 4/29 H (≈13.8%) |
| 대괄호 → `>` 간격 | 9/29 H |
| `>` 박스 폭 / 획 두께 | 14/29 H / 4.4/29 H |
| `>` 끝 처리 | 획에 직각으로 자른 끝(butt cap), 꼭지점은 뾰족하게 이음(miter) |
| `>` → 워드마크 간격 | 13/29 H |
| 여백(클리어 스페이스) | 사방 최소 1 H |
| 최소 크기 | 가로형 높이 16px 이상 / 심볼 단독 16px 이상 |

### 파일 (`logo/`)
| 파일 | 용도 |
| --- | --- |
| `davidlabs-horizontal.svg` | 기본 로고. 사이트 헤더, 문서 머리말 |
| `davidlabs-horizontal-reversed.svg` | 네이비나 어두운 배경 위에 쓰는 버전 (흰 글자 + 시안 `>`) |
| `davidlabs-horizontal-black.svg` / `-white.svg` | 1색 버전 (팩스, 도장, 1도 인쇄) |
| `davidlabs-stacked.svg` | 적층형. 좁은 공간, 정사각형 영역 |
| `davidlabs-symbol.svg` / `-symbol-black.svg` | 심볼 단독 |
| `davidlabs-korean.svg` | 한글 락업 `데이비드랩스` (Pretendard 400 / 700) |
| `dlogtracer-wordmark.svg` | 제품 로고: `D`(차콜 600) + `Log`(네이비 600) + `Tracer`(차콜 300) |
| `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`(180), `favicon-512.png` | 네이비 정사각형 위에 흰 대괄호 + 시안 `>` |

## Design Tokens
| 이름 | 값 | 용도 |
| --- | --- | --- |
| Ink Navy | `#2B4A8C` | 주 브랜드색. LABS, 버튼, 링크, 강조 |
| Navy Hover | `#1d3466` | 버튼·링크 hover/pressed |
| Cyan Highlight | `#22B0D9` | **작은 강조에만** 사용 (심볼의 `>`, 짧은 띠, 그래프 포인트). 화면 면적의 5% 이내. 흰 배경 대비가 2.6:1이라 **본문 글자색으로 쓰면 안 됩니다** |
| Charcoal | `#1d1f20` | 본문, DAVID |
| Muted | `#4a4d50` | 보조 텍스트 (흰 배경 대비 4.5:1 이상) |
| Muted-2 | `#6a6d70` | 캡션, 영문 보조 |
| Background | `#f2f2f3` | 페이지 바탕 |
| Surface | `#ffffff` | 카드 |
| Border | `#d5d6d8` | 카드·구분선 (1px) |
| 서체 (라틴) | Archivo 300/400/500/600/700 (Google Fonts) | 로고, 영문 제목, 숫자 |
| 서체 (한글) | Pretendard 400/600/700 (CDN: `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css`) | 한글 본문·제목 |
| 모서리 | 0~4px | 로고의 각진 형태에 맞춰 둥근 모서리를 최소화 |

---

## 홈페이지 변경 사항 (`index.html`)

### 1. `:root` 토큰 교체
```css
--bg:#f2f2f3; --surface:#ffffff; --surface-2:#f7f7f9;
--text:#1d1f20; --muted:#4a4d50;
--border:#d5d6d8;
--accent:#2B4A8C; --accent-hover:#1d3466;
--accent-dim:rgba(43,74,140,.08);
--highlight:#22B0D9;
--radius:4px;
--sans:"Pretendard",-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;
--display:"Archivo","Pretendard",sans-serif;
```
- `<head>`에 Archivo(Google Fonts)와 Pretendard CSS를 추가합니다.
- `h1`, `h2`, `.product-name`처럼 영문이 섞인 큰 제목에는 `font-family:var(--display)`를 씁니다.

### 2. 다크 → 라이트 전환
- 헤더 배경을 `rgba(242,242,243,.85)`로 바꾸고, `backdrop-filter`는 그대로 둡니다.
- `.btn-primary`: 배경 `var(--accent)`, 글자 `#fff`. hover 시 배경 `var(--accent-hover)`로 바꾸고 `filter`는 제거합니다.
- `.btn-ghost:hover`: 배경 `var(--accent-dim)`, 테두리 `var(--accent)`.
- `.card:hover`: 테두리 `rgba(43,74,140,.35)`, 배경 `#fff`.
- `.badge`: 글자 `var(--accent)`, 배경 `var(--accent-dim)`, 테두리 `rgba(43,74,140,.25)`.
- `.eyebrow`: 글자색 `var(--accent)`.
- `.product` 그라디언트: `rgba(43,74,140,.03)`로 바꿉니다.
- `.service`: 배경 `#fff`.
- `rgba(255,255,255,…)`나 `#34d399`, `52,211,153`이 남아 있으면 모두 위 토큰으로 바꿉니다.

### 3. 히어로 파형
- 첫 번째 polyline: `stroke="#2B4A8C" stroke-opacity="0.18"`
- 두 번째 polyline: `stroke="#22B0D9" stroke-opacity="0.35"`
- `.hero::after` 페이드는 `var(--bg)`를 쓰므로 그대로 둡니다.

### 4. 로고 교체
- 헤더의 `.brand`(초록 점 + "David Labs")를 `<img src="logo/davidlabs-horizontal.svg" alt="DAVIDLABS" height="20">`로 바꿉니다. 높이는 20~22px입니다.
- 푸터의 `.brand`도 같은 파일을 쓰고 높이는 16px입니다.
- `.brand .dot` CSS는 삭제합니다.
- `logo/` 폴더를 저장소 루트에 그대로 복사합니다.

### 5. 파비콘 · OG 추가 (`<head>`)
```html
<link rel="icon" href="logo/favicon.svg" type="image/svg+xml">
<link rel="icon" href="logo/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="logo/apple-touch-icon.png">
<meta name="theme-color" content="#2B4A8C">
<meta property="og:image" content="https://davidlabs.co.kr/logo/favicon-512.png">
```

### 6. DLogTracer 표기 규칙
제품 카드 제목을 아래처럼 바꿉니다.
```html
<span style="font-weight:600;color:var(--text)">D</span><span style="font-weight:600;color:var(--accent)">Log</span><span style="font-weight:300;color:var(--text)">Tracer</span>
```
`font-family`는 `var(--display)`입니다. 기존 `.dlog`, `.tracer` 클래스는 위 규칙으로 고쳐도 되고 삭제해도 됩니다.

### 7. 이메일 통일
- `iamdavidbae@gmail.com`을 모두 **`david@davidlabs.co.kr`**로 바꿉니다. `mailto:` 링크 5곳(subject 파라미터는 유지)과 문의 섹션 표시 텍스트가 대상입니다.
- ⚠ 배포 전에 `david@davidlabs.co.kr` 메일함이 실제로 메일을 받는지 확인하세요.

### 8. 그대로 둘 것
- 모든 한국어 문구, 섹션 순서, 앵커(`#what #product #why #contact`), 반응형 breakpoints(720/820px)
- 푸터의 TODO(사업자등록번호 `000-00-00000`, 약관 링크). 확정 전이므로 그대로 둡니다.

### 9. 상태 · 접근성
- 모든 링크와 버튼에 `:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }`를 적용합니다.
- 본문 텍스트에 시안(`#22B0D9`)을 쓰지 않습니다.

---

## 명함 (참고, 인쇄용)
- 90×50mm 가로, 양면, 백상지 매트 용지
- **앞면**: 가로형 로고만 중앙에 배치. 로고 폭 약 50mm, 좌우 여백 약 20mm
- **뒷면**: 안쪽 여백 8mm × 9mm
  - 맨 위: `배재형`(Pretendard 600, 5.6mm) + `DAVID BAE`(Archivo 400, 3.1mm, 자간 0.1em, `#6a6d70`)
  - 그 아래 직함: `대표 / 개발자`(3mm, `#4a4d50`) + `Founder & Engineer`(Archivo 2.8mm, `#6a6d70`)
  - 시안 띠: 10mm × 0.5mm
  - 맨 아래 연락처 (Archivo 2.9mm): `010-5965-3958` / `david@davidlabs.co.kr` / `http://davidlabs.co.kr`(네이비, 500)
- 인쇄 발주용 PDF(재단선 + 블리드 1mm)는 Claude Design에서 따로 만듭니다. 웹 작업 범위가 아닙니다.

## Files
- `logo/`: 최종 로고 에셋 (위 표 참고)
- `design_reference/DAVIDLABS 로고 시안.dc.html`: 로고 탐색 과정과 확정 락업 세트 (Round 2가 확정안)
- `design_reference/명함 앞뒤 시안.dc.html`: 명함 시안
- `design_reference/support.js`: 위 참고 파일을 브라우저에서 열 때 필요한 런타임

## Claude Code에 붙여 넣을 요청 예시
> 이 폴더의 README.md를 읽고, 저장소 루트의 index.html을 "홈페이지 변경 사항" 1~9번대로 수정해줘. logo/ 폴더는 저장소 루트에 복사하고, 문구와 섹션 구조는 바꾸지 마. 끝나면 변경 사항을 요약하고 커밋해줘.
