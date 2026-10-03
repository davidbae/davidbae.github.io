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

## 남은 작업
- [ ] 최종 리뷰 반영
- [ ] main 병합 + push (사용자 확인 필요)
