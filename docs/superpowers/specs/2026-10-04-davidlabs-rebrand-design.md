# David Labs 홈페이지 리브랜딩 + 제이제이 여행맛집 연결 — 설계

- 작성일: 2026-10-04
- 대상: `davidbae/davidbae.github.io` (GitHub Pages, `main` 브랜치 루트, 빌드 없음)
- 근거 자료: `assets/design_handoff_davidlabs_20261003_v1.0/README.md` (이하 "핸드오프 README")

## 1. 목적

1. Claude Design에서 확정한 DAVIDLABS 브랜드(로고·파비콘·컬러·서체)를 홈페이지에 적용한다.
2. 다른 프로젝트로 운영 중인 "제이제이 여행맛집" 사이트(`https://jjtastesandtravels-web.iamdavidbae.workers.dev/`)를 David Labs 제품으로 소개하고 연결한다.
3. 세 번째 제품이 들어가면서 깨지는 레이아웃만 제한적으로 다듬는다.

## 2. 범위

### 포함
- 핸드오프 README "홈페이지 변경 사항" 1~9번 적용 (아래 예외 2개 제외)
- 제품 섹션에 JJ 카드 추가, 섹션 제목·부제 수정
- 제품 카드 레이아웃 개선 (버튼 하단 정렬, 반복 inline style → 클래스)
- `logo/` 루트 복사, 핸드오프 폴더 커밋

### 제외
- davidlabs.co.kr의 DNS 정식 연결 (현재 프레임 포워딩 — 7절 참고)
- 섹션 순서·문구(제품 섹션 제목/부제 제외)·앵커·breakpoint 변경
- CSS/JS 파일 분리, 빌드 도구 도입, 다크 모드
- 푸터 TODO(사업자등록번호, 약관 링크)

## 3. 핸드오프 README 적용 방침

| 항목 | 적용 |
| --- | --- |
| 1. `:root` 토큰 교체, Archivo·Pretendard 로드, 큰 제목에 `--display` | 그대로 |
| 2. 다크 → 라이트 전환 (헤더, 버튼, 카드, 배지 등) | 그대로 |
| 3. 히어로 파형 색 | 그대로 |
| 4. 헤더(20px)·푸터(16px) 로고를 `logo/davidlabs-horizontal.svg`로 교체, `.brand .dot` 삭제 | 그대로 |
| 5. 파비콘·theme-color·og:image | **예외**: `og:image`는 `https://davidbae.github.io/logo/favicon-512.png` |
| 6. DLogTracer 표기 (D 600 / Log 네이비 600 / Tracer 300) | 그대로 |
| 7. 이메일 `david@davidlabs.co.kr`로 통일 | **예외**: 메일함이 아직 없어 `iamdavidbae@gmail.com` 유지 |
| 8. 문구·섹션·앵커·breakpoint 유지 | 그대로 (제품 섹션 제목/부제만 JJ 추가로 변경) |
| 9. `:focus-visible` 아웃라인, 본문에 시안 금지 | 그대로 |

## 4. JJ 카드

제품 섹션(`#product`)의 세 번째 카드로 추가한다.

- 섹션 제목: "지금 만들고 있는 두 가지" → **"지금 만들고 있는 세 가지"**
- 섹션 부제: "일상의 생산성부터 자동차 진단까지 — …" → **"일상의 생산성부터 자동차 진단, 여행까지 — David Labs가 직접 개발하는 제품입니다."**
- 그리드: `cols-2` → `cols-3` (기존 820px breakpoint에서 1열)

| 요소 | 내용 |
| --- | --- |
| 라벨(`.ico`) | `WEB / TRAVEL` |
| 제목 | 제이제이 여행맛집 |
| 부제(모노) | JJ's Tastes & Travels |
| 배지 | `● 운영 중` |
| 설명 | 여행·맛집 유튜브 채널의 여행자 도구 사이트. 매장에서 잠금화면만 보고 현지 가격을 원화로 확인하는 환율 잠금화면을 제공합니다. |
| 칩 | `환율 잠금화면`, `크루즈 가이드 (준비 중)` |
| 버튼 | `사이트 방문 ↗` → JJ URL, `target="_blank" rel="noopener"` |

새 탭 열기는 필수다. davidlabs.co.kr이 프레임으로 감싸고 있어서, 같은 탭으로 열면 JJ 사이트가 프레임 안에 갇힌다.

## 5. 제한적 레이아웃 개선

- 제품 카드: `display:flex; flex-direction:column`, 버튼 영역 `margin-top:auto` → 세 카드의 버튼 높이 정렬
- 제품 카드 안의 반복 inline style(제목 크기, 부제 모노 텍스트, 버튼 영역)을 클래스(`.product-card`, `.product-title`, `.product-sub`, `.card-cta` 등)로 옮긴다. 수정하는 제품 카드에만 적용한다.
- 그 외 섹션의 inline style은 건드리지 않는다.

## 6. 파일 구조

```
index.html                       # 단일 파일 + <style> 블록
logo/                            # 핸드오프 logo/ 복사본 (수정 금지)
assets/design_handoff_davidlabs_20261003_v1.0/   # 원본 핸드오프 (기록용)
docs/superpowers/specs/2026-10-04-davidlabs-rebrand-design.md
checklist.md
context-notes.md
```

참고: 저장소는 공개이며, 핸드오프의 명함 시안에 휴대폰 번호가 포함되어 있다. 사용자가 커밋을 선택했다.

## 7. 알려진 제약 — 프레임 포워딩

`davidlabs.co.kr`, `davidlabs.kr`은 도메인 업체 서버(Apache)가 `<frameset>`으로 `https://davidbae.github.io`를 감싸 보여주는 방식이다.

- 커스텀 도메인 경로(`davidlabs.co.kr/logo/...`)로는 에셋에 접근할 수 없다 → OG 이미지는 github.io 절대 URL 사용
- 도메인으로 접속 시 탭 제목은 래퍼의 "DAVIDLABS", 파비콘은 표시되지 않는다
- SNS 미리보기도 래퍼 페이지 메타를 읽는다

해결(별도 과제): 도메인 DNS를 GitHub Pages A/CNAME 레코드로 바꾸고 저장소에 `CNAME` 파일 추가.

## 8. 검증 기준 (완료 조건)

1. 로컬 서버 + Playwright로 1280px, 390px 캡처 — 헤더 로고, 히어로, 카드 3개, 푸터가 깨지지 않음
2. 로고·파비콘·폰트 요청 모두 200, 콘솔 오류 0
3. `index.html`에 `#34d399`, `52,211,153`, `rgba(255,255,255` 없음
4. `iamdavidbae@gmail.com` mailto 링크 5곳과 subject 파라미터 유지
5. JJ 버튼이 새 탭으로 해당 URL을 연다
6. 키보드 Tab 이동 시 링크·버튼에 포커스 아웃라인 표시
7. 앵커 `#what #product #why #contact` 동작

## 9. 커밋 단위

1. 핸드오프 에셋과 `logo/` 추가
2. 핸드오프 README에 따른 `index.html` 리브랜딩
3. 제이제이 여행맛집 제품 카드 추가
4. 설계 문서·체크리스트·컨텍스트 노트 추가

각 커밋 전에 사용자 확인을 받는다.
