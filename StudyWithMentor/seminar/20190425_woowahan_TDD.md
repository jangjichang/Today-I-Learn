2019년 4월 25일 우아한형제들에서 진행한 우아한 테크 세미나 "의식적인 TDD, 리팩토링"을 참여하고 요약한 내용입니다.

---

## 시작하기 전에

- 이 발표는 'TDD와 리팩토링을 왜 해야하는지 알고있다'는 가정하에 진행한다.
- "현재 교육자로 살고 있고 현장을 떠난지 6년이 지났으니 내 말을 너무 맹신하지 마라."
- 브런치에 쓴 글 중 "시간 확보를 위해 애인과의 만남을 2주에 1회로 줄인다."에서 볼 수 있듯이  
    - 저는 꼰대입니다.
    
---


## 발표 내용
1. 의식적인 연습이란?
2. **TDD 리팩토링 적용 - 개인**
3. TDD 리팩토링 적용 - 개인(주니어) -> 팀
4. TDD 리팩토링 적용 - 내가 리더

---

## 1. 의식적인 연습
- 무조건 연습을 많이 한다고 잘 할 수 있을까?
    - 평생 이 닦으면 이 닦는 노하우가 생길까?
    - 무의식으로 하면 노하우가 생기지 않음
    - 무조건 시간 투자가 답이 아니다.

- TDD는 멋져 보이지만 생각만큼 쉽게 연습할 수 있지 않다.
    - 교육자로서 최근의 고민
    - 좀 더 효과적으로 연습할 수 있는 방법은 없을까?
    - 목적의식 있는 연습이 필요함

- 의식적인 연습의 7가지 원칙 중
    - 컴포트 존을 살짝 벗어나라.
    - 명확하고 구체적인 목표를 가지고 진행
    - 피드백과 피드백에 따른 행동 변경 -> 코드 리뷰, 짝 프로그래밍 등
    - 기존에 습득한 기술의 특정 부분을 집중적으로 개선함으로써 발전시키기 -> 단축키를 익히기 위해 마우스 안쓰고 개발하기

- 의식적인 연습 예시 - 우아한테크코스 프리코스
- 진행방식
    - 3주 동안 진행, 과제 작성
    - PR	 
    - 피드백
- 선발 과정이지만 배움이 있는 과정을 만들자.

- 1주차-프로그래밍 제약사항
    - 코드 컨벤션
    - 인덴트, depth를 3이 넘지 않도록	 
    - 함수가 한 가지 일만 하도록 최대한 작게 만들기
    - 등등... 2, 3주차 반복
    - 점점 제약사항을 강력하게 넣어서 과제 제출함
		 
- 1주차-피드백	 
    - 공백도 컨벤션이다.
    - 불필요하게 공백 라인 만들지 않기			 
    - 깃 커밋 메시지 의미있게하기
    - 등등... 2, 3주차 반복
		 
- 프리코스 후기
    - 최종불합격한 사람도 감사하다는 메일을 보낼 정도

---

## 1. TDD 리팩토링 적용 - 개인
- 운동과 같다. 평생동안 연습하겠다는 마음가짐으로 시작
- 한번에 안되더라도 포기하지말고 간다는 생각으로 하라.

- 시작하기 - 주변 정리해 꾸준히 연습할 시간 확보
    - 애인과의 만남 시간 조정
    - 친구들과의 관계 끊기
    - TV 보지 않기, 게임하지 않기

- 시작하기 - 장난감 프로젝트 찾기
    - 주변 환경에 영향을 받지 않고 꾸준히 연습하기 위함
    - 절대 회사업무에 적용하지마라
    - 우선 순위가 언제 바뀔지 모르고 리듬이 깨지기 쉽다.
    - 꾸준히 연습하고 단계를 올라가라.

- 1단계 - 단위테스트 연습
    - 내가 사용하는 API 사용법을 익히기 위한 학습 테스트에서 시작
    - 내가 사용하는 API를 사용했을때 원하는 결과가 나오는지 확인한다.
    - 내가 구현하는 메소드 중 입력과 출력 값이 명확한 메소드
        - 알고리즘 공부도 연습하기 상당히 좋다.

- 2단계 - TDD 연습하기
    - 어려운 문제를 해결 하려고 하지마라.
    - TDD 연습이 목적이다.
    - 난이도가 낮거나 자신에게 익숙한 문제로 시작하라.
    - 무조건 복잡한게 좋은게 아니다.
    - 작은 코드라도 연습할게 많다. (계산기, 로또 프로그램 등등)
    - 웹, 모바일 UI나 DB에 의존관계를 가지지 않는 요구사항으로 진행하라.
        - 예: 문자열 덧셈 계산기 요구사항
            - 입력과 출력 모으기
            - 메소드, 클래스 분리 등등

    - TDD 사이클
        - 테스트 실패 -> 테스트 성공 -> 리팩토링 -> 테스트 실패 -> 반복...
        - 하지만 대부분 이렇게 한다. 테스트 실패 -> 테스트 성공 -> 테스트 실패 -> 반복...
        - 리팩토링 중요하다. 반드시하라.

- 3단계 - 메소드 분리 리팩토링
    - 연습 - 메소드 분리
        - 인덴트 줄이기! -> 인덴트는 1번만, 최대 2번
        - else 예약어 쓰지 않기
        - 메소드가 한 가지 일만 하도록 구현하기
        - 로컬 변수가 정말 필요한가?
    
    - 추상화 레벨 맞추기(이 부분은 잘 못 들었음 컴포즈 뭐뭐뭐 라고 말한 것 같음)
    
    - 한번에 모든 원칙을 지키면서 리팩토링하려고 하지마라
        - 한번에 한 가지 명확한 요구 사항을 지켜라.
        - 연습은 극단적인 방법으로 하는 것도 좋다.
        - 메소드 라인을 15 -> 10으로 줄이는 것도 좋은 방법이다.
    
    - 연습 - 클래스 분리
        - 모든 원시값과 문자열을 포장한다.
        
- 4단계 - 장난감 프로젝트 난이도 높이기
    - 리팩토링 연습하기 좋은 프로그램들
        - 게임과 같이 요구 사항 명확한 것
        - UI 없는 것
        - 데이터베이스 의존 없는 것
        
    - 객체지향 생활체조 원칙
        - 책- 소트웍스 앤솔러지
        - 책- 클린 코드
        - 메소드 분리 같은 것도 위 책에 나오는 이야기임
        
    - 연습을 위해 필요한 것은?
        - 조급해 하지 않는 마음의 여유
        - 장난감 프로젝트
        - 같은 과제를 반복적으로 구현할 수 있는 인내력, 꾸준함, 성실함
            
---
            
## 마치며
- 작은 성공을 쌓아 큰 성공
- 처음부터 너무 큰 성공을 기대하면서 도전하여 중간에 멈추는 걸 보면 안타까움
- 장난감 프로젝트로 TDD, 리팩토링 연습해 작은 성공 맛보기
- 내가 구현하는 코드에 한해 TDD, 리팩토링 적용해 작은 성공 맛보기
- 직장에서 혼자 TDD, 동료에게 전파하고 작은 성공 맛보기 
- 실패해도 괜찮다.
- 실패하기 전보다는 나는 한 단계 성장한다.
- 가장 필요한 것은 가보지 않은 길에 꾸준히 도전할 수 있는 용기가 중요하다.

---

## 질문
- 질문 요약
    - 프로그램 속도 vs 코드 가독성
- 답변
    - 어차피 내가 만든 서비스 아무도 안쓰니까 성능보단 읽기 좋은 코드를 만들어라.
    - 하지만 네이버, 우아한 형제, 카카오처럼 큰 회사는 처음부터 성능을 신경 쓰고 코드를 작성해야한다.
- 질문 전체
    - 레거시 코드를 리팩토링하다보면 가독성 좋은 코드로 바꾸게 되는데 실제 테스트를하면
    성능은 레거시 코드가 더 좋은 경우가 꽤 있다. 메소드를 분리하거나, 반복문이나 조건문의 구조가 바뀌게
    되기 때문에 그런 것 같은데, 리팩토링을 해서 프로그램 속도가 더 느려졌다면, 이럴 때는 어떻게 타협해야
    할까요?

---

## 느낀점
- 멘토링을 하면서 피드백을 받고 있는데, 다시 한 번 정말 좋은 기회를 얻었다는 생각이 들었다.
- '프로그래머의 길 멘토에게 묻는다', '탤런트 코드' 등에서 읽은 내용이 나와서 익숙한 내용도 있었다.
- '장난감 프로젝트를 만들어라.'는 최근에도 하고 있는데 여기에 TDD도 연습해야 겠다.
- 깃 커밋 메시지를 작성하는 것이나
- 코딩을 하기 전에 요구 사항을 명시하는 것들도 TDD의 시작이다.
- 작은 성공에서 시작해야겠다.

- 멘토님이 과제를 내주실때 항상 입력과 출력 값을 모으고
- 구체적인 프로그램 사용 사례를 생각하라고 하는 것도
- 사실은 TDD의 기초를 말하고 싶었던게 아닐까? 라는 생각이 든다.
- 경력 오래된 사람들 중에도 그다지 멋있지 않은 개발자들이 많은데
- 다시 한 번 멘토님이 멋있게 느껴졌다.

- 나는 상당히 조급해 하는 편인데, 조급해 하지 않는 마음의 여유를 갖는게 중요하다고 하니 여유는 갖되 많이 공부해야겠다.
- 어떤 공부를 하든지 '의식적인 연습'이 중요하다.
- '1만 시간의 재발견 - 노력은 왜 우리를 배신하는가'를 읽어야겠다.
- 나는 아직 유닛 테스트만 하는 단계이다.
- 우아한 형제들 직원들도 왔는데 부러웠다.