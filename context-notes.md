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
- davidlabs.co.kr / davidlabs.kr DNS를 GitHub Pages(A 레코드 + `CNAME` 파일)로 정식 연결 → 파비콘·OG·탭 제목이 도메인에서도 보이게 됨
- `david@davidlabs.co.kr` 메일함 개설 후 mailto 5곳 교체 (핸드오프 README 7번)
- 집중력 앱 정식 명칭, 사업자등록번호, 약관 링크 (기존 TODO)
