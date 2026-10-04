# 체크리스트 — David Labs 리브랜딩 + JJ 연결

설계: `docs/superpowers/specs/2026-10-04-davidlabs-rebrand-design.md`

## 설계
- [x] 현황 파악 (index.html, 핸드오프 README, JJ 사이트, 도메인 연결 방식)
- [x] 범위·방향 확인 (사용자 답변)
- [x] 설계 문서 작성
- [x] 설계 문서 사용자 검토
- [x] 구현 계획 작성

## 구현
- [x] `logo/` 루트 복사
- [x] README 1: 토큰·폰트 교체
- [x] README 2: 다크 → 라이트 전환
- [x] README 3: 히어로 파형 색
- [x] README 4: 헤더·푸터 로고 교체
- [x] README 5: 파비콘·OG (og:image는 github.io URL)
- [x] README 6: DLogTracer 표기
- [x] README 9: focus-visible
- [x] JJ 카드 추가 + 제품 섹션 제목/부제 + cols-3
- [x] 제품 카드 레이아웃 정리 (버튼 하단 정렬, 클래스화)

## 검증
- [x] 1280px / 390px 캡처 확인
- [x] 에셋 200, 콘솔 오류 0
- [x] 다크 테마 잔재 grep 0건
- [x] mailto 5곳 유지, JJ 새 탭
- [x] 포커스 아웃라인, 앵커 동작

## 커밋 (각각 사용자 확인 후)
- [x] 에셋 추가
- [x] 리브랜딩
- [x] JJ 카드
- [x] 문서
- [x] 추가: 제품 카드 선택자 우선순위 수정 (검증 중 발견)

## 완료 (2026-10-04 후반)
- [x] 최종 리뷰 반영 (Critical·Important 없음, Minor는 아래로 이월)
- [x] main 병합 + push, GitHub Pages 배포 확인
- [x] davidlabs.co.kr DNS 직접 연결 + HTTPS (사용자가 가비아·GitHub에서 설정)
- [x] og:image를 davidlabs.co.kr로 변경
- [x] JJ 카드에 로고 추가 (제목·부제 두 줄 왼쪽, 40px)
- [x] WebSiteDev/CLAUDE.md 공통 규칙, 사이트별 이웃 폴더 읽기 설정, 한국어 응답 전역화

## 다음 세션 후보 (우선순위 순, 사용자와 고르기)
- [ ] 화면 메모 도구 (JJ page-notes 참고) — 사용자 결정 대기
  - [ ] JJ 설계서 `../JJ_TastesAndTravels-web/docs/superpowers/specs/2026-10-04-page-notes-design.md` 읽기
  - [ ] 로컬 전용 Python 미리보기 서버 + 메모 스크립트 주입 방식으로 설계 (index.html에는 넣지 않음)
  - [ ] 위치 기록은 줄 번호 대신 CSS 선택자 + 글자 앞부분
- [ ] 집중력 앱 카드 이름 → "옆자리 (Seatmate)" 반영 여부 확인 (폴더명 Seatmat 철자도 확인)
- [ ] 문구 갱신 (사용자 확인 필요): meta description·og:description이 제품 2개만 언급, 히어로 부제에 여행 없음
- [ ] 리뷰 Minor 정리
  - [ ] 320px 이하 헤더 로고·문의 버튼 맞닿음
  - [ ] `.btn{transition:all}` 때문에 포커스 테두리 깜빡임
  - [ ] 주석 "제품: 두 가지" → 세 가지
  - [ ] 헤더 로고 링크 이름 "DAVIDLABS 홈"
  - [ ] Pretendard dynamic-subset 전환 검토 (README URL과 다름 → 사용자 결정)
  - [ ] check_site.py 검사 범위 보강

## 사용자 몫 (외부 설정)
- [ ] GitHub 계정 https://github.com/settings/pages 에서 davidlabs.co.kr 도메인 소유권 인증 (TXT)
- [ ] david@davidlabs.co.kr 메일함 개설 → 생기면 mailto 5곳 교체
- [ ] 사업자등록번호, 약관 링크 확정

## 보류
- davidlabs.kr HTTPS 경고 — 사용자가 그대로 두기로 함 (가비아 포워딩 서버가 *.gabia.com 인증서 사용)
