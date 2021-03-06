# 과제 설명

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

# 1. 기능명세
- ToDoList 작성
    - 할 일을 worklist에 저장
    - 할 일에 대한 세부 항목은 card에 저장
![todolistdeploy](../../image/todolistdeploy.png)
    
- 인증
    - 로그인, 로그아웃, 회원가입, 비밀번호 변경

# 2. 개선사항
- 전체적인 디자인
    - 트렐로를 따라하려다가 너무 디자인이 너무 아쉽게 나왔다.
    - 차라리 부트스트랩에 이미 있는걸 갖다 쓰는게 낫겠다.
    [여기링크](https://www.jquery-az.com/6-templates-bootstrap-4-cards-online-examples/)에서 
    Using list group inside a card template 따라하기
- worklist 수정 화면 접속 시 inlineformset으로 card 보여주기
- card 수정 화면 접속 시 inlineformset으로 activity 보여주기
- 도메인 이름 바꾸기

---
# 1. 애플리케이션 설계하기
- To Do List 앱을 만든다. To Do List 앱은 할 일을 시각화해 관리하고 최대 5개의 카테고리에 대해 세부 사항을 등록하고 이를 시각화한다.
- To Do List 앱에 필요한 테이블은, 할 일을 저장하는 card 테이블과 이 card들을 그룹화해 그 정보를 담을 수 있는 list 테이블과 
card에 대한 기록 사항을 담는 activity 테이블이 필요합니다.

# 1.1 화면 UI 설계

Work list(이하 list) 레코드 하나에 여러 개의 card 레코드를 같이 출력해, list 레코드와 card 레코드를 수정할 수 있도록한다.

![리스트생성과카드생성](../../image/trello_add_list.png)
- 사진 1-1 ToDoList 앱 - list 및 card를 보여주고 이 화면에서 각 list를 추가하거나, list에 card를 추가한다.

![리스트수정](../../image/trello_update_list.png)
- 사진 1-2 ToDoList 앱 - list를 수정한다.

![카드옵션](../../image/trello_option_card.png)
- 사진 1-3 card에 ... 옵션을 누른 경우 다음과 같은 옵션을 선택할 수 있다.

![카드수정](../../image/trello_update_card.png)
- 사진 1-4 ToDoList 앱 - card를 수정한다.
- 사진 1-3에서 Update card(만들 예정임)를 클릭하면 card 수정 화면이 나온다.

- trello와 같이 할 일을 card로 만들고, card들을 그룹화해 list로 보여준다.
- 왼쪽부터 시간 순으로 만든 list를 보여준다.
- 각 list, card, activity에는 생성, 보여주기(화면에 나타냄), 수정, 완료 기능이 있다.

# 1.2 테이블 설계
- card 테이블과 list 테이블 간에는 N:1 관계가 성립된다.
- 즉, 하나의 list는 여러개의 card를 가질 수 있고 하나의 card는 하나의 list에만 속하는 관계이다.
- 이 관계는 card 테이블의 list 속성에 ForeignKey 필드로 지정된다.
- 마찬가지로 activity 테이블과 card 테이블 간에는 N:1 관계가 성립된다.  


- 표 1-1 To Do List 앱 - 테이블 설계(WorkList 모델 클래스)

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
| worklist          | ForeignKey(List) |                | 할 일이 소속된 리스트 |
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

# 1.3 URL 설계

| URL 패턴              | 뷰 이름                    | 템플릿 파일명            |
|-----------------------|----------------------------|--------------------------|
| /todo/                | ListCardLV(ListView)       | worklist_list.html      |
| /todo/list/           | ListCardLV(ListView)       | worklist_list.html      |
| /todo/list/99         | ListDV(DetailView)       | worklist_detail.html      |
| /todo/list/add/       | ListCreateView(CreateView) | worklist_form.html           |
| /todo/list/99/update/ | ListUpdateView(UpdateView) | worklist_form.html           |
| /todo/list/99/delete/ | ListDeleteView(DeleteView) | worklist_confirm_delete.html |
| /todo/card/99         | CardDV(DetailView) | card_detail.html           |
| /todo/card/add/       | CardCreateView(CreateView) | card_form.html           |
| /todo/card/99/99/update  | CardUpdateView(CreateView) | card_form.html           |
| /todo/card/99/99/delete/ | CardDeleteView(DeleteView) | card_confirm_delete.html |

- 표 1-4 To Do List 앱 - URLconf 설계

# 1.4 작업/코딩 순서

| 작업 순서        | 관련 명령/파일     | 필요한 작업 내용                  |
|------------------|--------------------|-----------------------------------|
| 뼈대 만들기      | startproject       | todoapp 프로젝트 생성             |
|                  | settings.py        | 프로젝트 설정 항목 변경           |
|                  | migrate            | User/Group 테이블 생성            |
|                  | createsuperuser    | 프로젝트 관리자인 슈퍼유저를 만듦 |
|                  | startapp           | workmanagement 앱 생성            |
|                  | settings.py        | workmanagement 앱 등록            |
| 모델 코딩하기    | models.py          | 모델(테이블) 정의                 |
|                  | admin.py           | Admin 사이트에 모델 등록          |
|                  | makemigrations     | 모델을 데이터베이스에 반영        |
|                  | migrate            |                                   |
| URLconf 코딩하기 | urls.py            | URL 정의                          |
| 뷰 코딩하기      | views.py           | 뷰 로직 작성                      |
| 템플릿 코딩하기  | templates 디렉터리 | 템플릿 파일 작성                  |
| 그 외 코딩하기   | -                  | (없음)                            |

- 표 1-5 To Do List 앱 - 작업/코딩 순서

# 2 개발 코딩하기

# 2.1 뼈대 만들기


# 2.2 모델 코딩하기


# 2.3 URLconf 코딩하기

# 2.4 뷰 코딩하기

# 2.5 템플릿 코딩하기

# 2.6 그 외 작업 코딩하기

# 3 지금까지의 작업 확인하기