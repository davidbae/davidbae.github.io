# 컨텍스트 노트 — David Labs 리브랜딩 + JJ 연결

## 2026-10-04

- **구조**: 원페이지 유지, 단일 `index.html` + `<style>` 블록. 핸드오프 README가 빌드 없는 순수 HTML을 요구하고 사용자도 "원페이지 유지 + 정리"를 선택함.
- **범위**: 핸드오프 README 1~9 + 제한적 개선. 사용자가 "구조를 세련되게"를 원했지만 README의 "레이아웃·문구·섹션 유지"와 충돌 → JJ 카드 추가에 필요한 제품 카드 정리까지만 하기로 합의.
- **JJ 연결**: 제품 섹션 3번째 카드 + 외부 링크(새 탭). iframe 임베드는 모바일·보안 헤더 이슈로 제외.
- **이메일**: `david@davidlabs.co.kr` 메일함이 아직 없음 → README 7번을 적용하지 않고 `iamdavidbae@gmail.com` 유지.
- **도메인**: `davidlabs.co.kr`, `davidlabs.kr`은 도메인 업체의 프레임 포워딩(`<frameset src="https://davidbae.github.io">`)으로 연결됨. GitHub Pages `cname: null`. 따라서
  - `og:image`는 `https://davidbae.github.io/logo/favicon-512.png` 사용 (README 5번 예외)
  - 외부 링크는 반드시 `target="_blank"` — 같은 탭이면 프레임 안에 갇힘
  - DNS 정식 연결은 별도 과제
- **에셋**: `logo/`를 루트에 복사, 핸드오프 폴더는 기록용으로 커밋. 공개 저장소이고 명함 시안에 휴대폰 번호가 있다는 점을 알렸고 사용자가 커밋을 선택함.
- **다크 모드**: 처음엔 다크/라이트 모두 지원을 제안했으나, 확정 브랜드가 라이트 베이스뿐이라 라이트만 적용.

## 2026-10-04 (구현)

- **브랜치**: `feature/davidlabs-rebrand`에서 작업. 사용자가 단계별 자동 커밋을 승인. main 병합·push는 별도 확인.
- **검사 스크립트**: `scripts/check_site.py`로 브랜드·링크 규칙을 정적 검사(`python3 scripts/check_site.py` → `ALL PASS`). 테스트 프레임워크가 없어서 추가함.
- **선택자 우선순위 버그**: `.card h3`, `.card p`(0,1,1)가 `.product-title`, `.product-sub`(0,1,0)를 덮어 제목이 18px로 나왔음. `.product-card .product-title` 형태로 수정. 정적 검사로는 못 잡고 브라우저 computed style로 발견 → 이런 종류는 Playwright 확인이 필요.
- **검증 결과**: 1280/900/390px 모두 가로 넘침 없음, 900px에서 버튼 3개 같은 높이, 390px 헤더 로고·문의 버튼 겹침 없음. 콘솔 오류 0, 로고·폰트 요청 200, 포커스 아웃라인 `#2B4A8C`, JJ 링크 `_blank`/`noopener`.
- **`.gitignore`**: `.DS_Store`, `.superpowers/`, `.playwright-mcp/`(스크린샷 임시 폴더) 제외.

## 남은 과제
- ~~davidlabs.co.kr DNS 정식 연결~~ (완료, 아래 참고)
- `david@davidlabs.co.kr` 메일함 개설 후 mailto 5곳 교체 (핸드오프 README 7번)
- 집중력 앱 정식 명칭, 사업자등록번호, 약관 링크 (기존 TODO)

## 2026-10-04 (도메인 직접 연결)

- **davidlabs.co.kr**: 가비아 포워딩 해제 → A 레코드 4개(185.199.108~111.153) + `www` CNAME `davidbae.github.io`. GitHub Pages 커스텀 도메인 설정, HTTPS 인증서 발급, Enforce HTTPS 완료. `davidbae.github.io`, `http://`, `www.`는 모두 `https://davidlabs.co.kr`로 301.
- **og:image**: 도메인 연결 후 `https://davidlabs.co.kr/logo/favicon-512.png`로 변경 (핸드오프 README 5번 원래 값).
- **davidlabs.kr**: 가비아 프레임 포워딩 → `https://davidlabs.co.kr`. 가비아 서버가 `*.gabia.com` 인증서를 내서 HTTPS 경고("주의 요함")가 뜸. 사용자가 그대로 두기로 결정. 해결하려면 (A) 리다이렉트 전용 GitHub Pages 저장소에 davidlabs.kr 연결, 또는 (B) Cloudflare 네임서버 + 리다이렉트 규칙.
- **남은 권장 사항**: 계정 설정 https://github.com/settings/pages 에서 davidlabs.co.kr 도메인 소유권 인증(TXT 레코드).

## 2026-10-04 — JJ 로고, WebSiteDev 공통 구성, 메모 도구 검토

### JJ 카드 로고
- 원본 `assets/제이제이여행맛집/Logo 제이제이 여행맛집.png`(800px)를 `sips -Z 80`으로 줄여 `images/jj-logo.png`(약 10KB) 사용. 화면 40px.
- 처음엔 제목 줄에만 붙였다가(`f9f17cc`), 사용자 요청으로 제목·부제 두 줄 왼쪽에 오는 `.product-head` 구조로 변경(`c7f1915`).
- `alt=""` — 바로 옆 제목과 같은 이름이라 스크린 리더 중복 읽기 방지.

### WebSiteDev 공통 구성 (저장소 밖 변경)
- `~/Development/WebSiteDev/CLAUDE.md` 생성: 사이트 목록·세션 규칙·공통 브랜드·연결 규칙. 하위 폴더 세션에 자동 적용.
- 각 사이트 `.claude/settings.local.json`에 `permissions.additionalDirectories: ["/Users/davidbae/Development/WebSiteDev"]`. git에는 `.git/info/exclude`로 제외(커밋 안 됨).
- 결정: WebSiteDev를 루트로 여는 방식 대신 "세션은 사이트 폴더 + 공통 규칙은 부모"를 택함. 루트를 부모로 하면 git 상태·배포 폴더 혼동, 메모리/기록 분리, node_modules 검색 잡음이 생기기 때문.
- "한국어로 응답"은 프로젝트 메모리에서 전역 `~/.claude/CLAUDE.md` 12번으로 이동.

### 화면 메모 도구 (검토만, 미구현)
- JJ의 page-notes는 Astro 개발 도구 막대·HMR 통신·`data-astro-source-file`에 묶여 있어 그대로 복사 불가.
- 가능한 방식: 로컬 전용 Python 미리보기 서버가 메모 스크립트를 주입하고 `notes/page-notes.json`에 저장. 위치는 CSS 선택자 + 글자 앞부분. index.html·공개 사이트에는 흔적 없음.
- 버린 대안: 메인 홈페이지를 Astro로 이전 — 빌드 없는 단일 HTML 원칙을 깨므로 과함.
- 구현 여부는 **사용자 확인 필요**.
