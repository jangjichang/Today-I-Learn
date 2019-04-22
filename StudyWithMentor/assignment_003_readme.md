이번 과제는 작업 관리 프로그램 입니다.
간단한 To Do List부터 Trello 같은 칸반 보드까지 자유롭게 만드시면 됩니다.

여러분이 좋아하는 언어와 기술을 이용해서 먼저 해결해 보세요. 하나를 계속 다듬어서 완벽하게 하셔도 좋고, 다양한 언어나 기술을 활용해서 문제를 탐구하셔도 좋습니다. 진행 상황을 댓글로 자주 남겨주셔도 됩니다.
다음의 과정을 따라서 진행해 주세요:
1. 이 프로그램을 사용하는 상황과 필수 요소, 제약 조건 등을 정합니다. “내가 이 프로그램을 쓴다면?”이라고 가정하면 더 쉬울 수 있습니다.
2. 이 프로그램에 무엇을 입력했을 때 어떤 결과가 나와야 하는지 유형을 분류하고 구체적인 사례를 찾아 봅니다.
3. 어디까지 구현할 건지, 무엇이 가장 중요한지, 어떤 순서대로 진행해야 할지 결정합니다.
4. 프로그램을 구현합니다.
5. 프로그램을 공유합니다.
6. 결과를 확인하고 추가로 배운 점을 적용해 1로 돌아가서 다듬습니다.

---
# 1. 애플리케이션 설계하기
- To Do List 앱을 만든다. To Do List 앱은 할 일을 시각화해 관리하고 최대 5개의 카테고리에 대해 세부 사항을 등록하고 이를 시각화한다.
- To Do List 앱에 필요한 테이블은, 할 일을 저장하는 card 테이블과 이 card들을 그룹화해 그 정보를 담을 수 있는 list 테이블과 
card에 대한 기록 사항을 담는 activity 테이블이 필요합니다.

# 1.1 화면 UI 설계
- ![trello_copy](./Today-I-Learn/image/trello_copy.png)
- trello와 같이 할 일을 card로 만들고, card들을 그룹화해 list로 보여준다.
- 왼쪽부터 시간 순으로 만든 list를 보여준다.
- 각 list, card, activity에는 생성, 보여주기(화면에 나타냄), 수정, 완료 기능이 있다.

# 1.2 테이블 설계
- card 테이블과 list 테이블 간에는 N:1 관계가 성립된다.
- 즉, 하나의 list는 여러개의 card를 가질 수 있고 하나의 card는 하나의 list에만 속하는 관계이다.
- 이 관계는 card 테이블의 list 속성에 ForeignKey 필드로 지정된다.
- 마찬가지로 activity 테이블과 card 테이블 간에는 N:1 관계가 성립된다.  


- 표 1-1 To Do List 앱 - 테이블 설계(List 모델 클래스)

| 필드명      | 타입          | 제약 조건          | 설명                 |
|-------------|---------------|--------------------|----------------------|
| id          | Integer       | PK, Auto Increment | 기본 키              |
| name        | CharField(50) |                    | 할 일 카테고리 이름  |
| owner | ForeignKey(User) |            | 할 일 카테고리 소유자 |
| create_date | DateTimeField | auto_now_add       | 카테고리 생성한 날짜 |
| modify_date | DateTimeField | auto_now           | 카테고리 수정한 날짜 |


- 표 1-2 To Do List 앱 - 테이블 설계(Card 모델 클래스)

| 필드명        | 타입             | 제약 조건          | 설명                  |
|---------------|------------------|--------------------|-----------------------|
| id            | Integer          | PK, Auto Increment | 기본 키               |
| name          | CharField(50)    |                    | 할 일 이름            |
| description   | CharField(100)   | Blank              | 할 일 내용 한 줄 설명 |
| owner         | ForeignKey(User) |                    | 할 일 소유자          |
| list          | ForeignKey(List) |                    | 할 일이 소속된 리스트 |
| create_date   | DateTimeField    | auto_now_add       | 할 일 생성한 날짜     |
| modify_date   | DateTimeField    | auto_now           | 할 일 수정한 날짜     |
| deadline_date | DateTimeField    | Blank              | 할 일 마감 날짜       |

- 표 1-3 To Do List 앱 - 테이블 설계(Activity 모델 클래스)

| 필드명      | 타입             | 제약 조건          | 설명                   |
|-------------|------------------|--------------------|------------------------|
| id          | Integer          | PK, Auto Increment | 기본 키                |
| description | CharField(100)   | Blank              | 할 일에 대한 기록 사항 |
| owner       | ForeignKey(User) |                    | 기록 사항 소유자       |
| create_date | DateTimeField    | auto_now_add       | 기록 사항 생성한 날짜  |
| modify_date | DateTimeField    | auto_now           | 기록 사항 수정한 날짜  |