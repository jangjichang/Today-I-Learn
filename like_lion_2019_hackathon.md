# 멋쟁이 사자처럼 연합 해커톤 후기

## 해커톤 참여
이번 해커톤은 장고(Django) 기술 스택 기반으로 진행되는 웹 서비스 해커톤이다. 주제는 총 4가지로 아래와 같다.
1. 지역 사회와 소외 계층을 위한 서비스
2. 엔터테인먼트(문화생활, 게임, 여행 등) 서비스
3. 이미 있는 서비스 개선하기
4. 자유 주제

우리 팀은 2번 엔터테인먼트 서비스를 만들었다. 토요일 오후 3시부터 일요일 오전 8시까지 개발했다.

## 주제 선정

팀은 미리 제출해준 구글 폼을 기반으로 주제와 희망 포지션에 따라 랜덤으로 매칭됐다. 처음에 인디밴드 공연 정보 알리미 서비스를 만드려고 했다. 하지만 나는 이 아이디어로 서비스를 구현하는데 힘들 것이라고 생각했다. 그 이유는 아래와 같았다.
1. 아이디어 제시한 사람의 기획이 명확하지 않음
2. 팀원들의 도메인 지식 부족
3. 페이스북 크롤링 API에 대한 불 확실성

그래서 나는 `멜론 좋아요 Up&Down 게임` 아이디어를 제시했다. 팀원들에게 아래와 같은 장점을 제시했다.

1. 많은 사람들이 즐길 수 있는 엔터테인먼트(음악 게임)
2. Easy To Learn, Hard To Master (누구나 할 수 있는 게임이지만, 잘하기에는 어려운 게임)
3. 멜론 음악 데이터의 접근 용이성

모든 팀원들의 동의를 얻고 개발을 시작했다.

내가 제시한 게임은 이렇다. 발라드, 랩, R&B, 댄스 등 장르별 인기가 많은 음악과
2018, 2017, 2016등 연도별 히트곡들 중에서 멜론 좋아요가 더 많은 노래를 고르는 Up&Down 게임이다.

## 개발

#### 리더

시간이 부족한 만큼 서로의 시너지를 극대화 해야한다고 생각했다. 프로젝트 완성을 위해 해야할 일을 100이라고 하면 짧은 시간에 혼자 100을 할 수는 없다. 그래서 먼저 각자 잘 할 수 있는 분야를 선정하고 UX/UI, 프론트 엔드, 백엔드, 크롤링으로 분야를 나눴다. 그리고 나는 리더를 맡았다. 리더로서 나는 `프로젝트의 기획 및 백엔드 개발을 담당했다.`

#### 크롤링

크롤링하는 팀원과 이야기를 하다보니 서로 생각이 달랐다. 나는 게임 카테고리를 발라드, 댄스, 랩/힙합 등의 음악 장르와 2018, 2017, 2016 히트곡. 이렇게 두가지를 생각 했고 각각 크롤링 하는 것을 원했다. 하지만 팀원은 굳이 년도별 히트곡을 크롤링하지 말고 음악 장르별 크롤링한 노래에서 연도를 따와서 게임을 생성하자고 했다. 나는 '장르별 노래들의 연도 스펙트럼이 넓기 때문에 한 연도별 히트곡 게임을 할 때 노래 갯수가 부족할 수 있다.', '장르별 노래들의 연도로 게임을 만들면 게임 종류가 너무 많아진다.' 라고 명확히 나의 의견을 이야기 했고 결국 장르별, 연도별 히트곡을 따로 크롤링했다.


멜론에는 노래에 고유한 ID를 부여하고 ID로 노래의 상세 화면에 접근이 가능하다. 따라서 id를 멜론의 그것과 같이 부여했다. 이렇게 하여 같은 music 데이터를 저장하지 않도록 했다. music과 game의 관계는 `manytomany` 관계이다. 따라서 musicgame table을 생성하여 두 필드를 foreignkey로 지정했다.


```python
# models.py

class music(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    like = models.IntegerField()
    album_cover = models.ImageField(upload_to="music/%Y/%m/%d")

    def __str__(self):
        return '{} - {}'.format(self.title, self.artist)


class game(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class musicgame(models.Model):
    music = models.ForeignKey('music', on_delete=models.CASCADE, )
    game = models.ForeignKey('game', on_delete=models.CASCADE, )

    def __str__(self):
        return '{} : {}'.format(str(self.game), str(self.music))

```

#### 백엔드
 
게임을 고르는 화면은 game 필드의 데이터를 렌더링하여 구현했다.
 

```python
# views.py

def select_game(request):
    games = game.objects.all()
    context = {'games': games}
    return render(request, 'main/select_game.html', context)

```

카테고리를 고르면 게임 진행 화면으로 이동하고 사용할 음악 목록으로 게임이 진행된다. 협업하는 과정에서 약간의 문제가 생겼다. 음악 목록을 Django views에서 template rendering 할 때 context로 전달 하려고 했는데 항상 바이트의 배열이 반환됐다. context를 javascript에서 사용할 순 있는데 `바이트로 반환되면 b'{{데이터}}' 형식으로 나오기 때문에` 프론트 엔드에서 string slicing으로 데이터를 굳이 변환해야하는 문제가 생긴다. `그래서 나는 django-rest-framework의 serializer로 api를 만들었다.`

```python
# views.py

@api_view(['POST'])
def music_list_of_game(request, gamename):
    if request.method == 'POST':
        gamename = game.objects.filter(name=gamename)
        music_list = musicgame.objects.filter(game=gamename[0]).order_by('?')
        serializer = MusicGameSerializer(music_list, many=True)
        return Response(serializer.data)
```

#### 프론트엔드

UX/UI 전공자 분께서 디자인을 담당해줬다. 프로젝트를 진행하면서 표정이 좋지 않은 것을 발견했다. 무언가 도움이 필요해 보여서 `혹시 안되는거 있어요?`라고 묻자 프로젝트 초기 설정에 애를 먹고 있다고 이야기를 했다. 어떻게 에러를 해결할지 한 두마디 이야기를 했지만 쉽게 해결되지 않았다. 그래서 나는 `자리를 바꿔 그 분의 옆자리로 가서 프로젝트 설정을 해줬다.` 가상 환경에 패키지를 설치하지 않아 runserver 명렁이 실행되지 않았고 static 파일 경로 설정에 오타가 있었다.

 
그리고 프론트엔드 개발자 분도 도움을 청했다. 게임을 구현하는데 제대로 되지 않는다고 했다. `그래서 나는 다시 자리를 옮겨 크롬 개발자 도구로 같이 디버깅을 통해 문제를 해결했다.`


## 시상식

밤새가며 열심히 코딩한 결과 우리는 원하는 기능도 구현했고 배포도 성공했다. 예상치 못하게 18개팀 중 엔터테인먼트 분야에서 가장 높은 최우수상을 받았다. 부상으로 블루투스 키보드도 받았다.

## 후기

아마존 해커톤에 이어 두번째 해커톤에 참여했다. 첫 해커톤에서 너무 아쉬운 점이 많아서 이번 헤커톤은 반드시 좋은 성과가 있기를 바랐다. 이번에는 반드시 기능 구현, 배포를 마치리라. 각오를 하며 참여했다. 그래서 나는 혼자 개발에 집중하기 보다는 각자에게 파트를 부여하고 어느정도의 책임감을 주려고 했다. 해커톤을 하다보면 혼자서 다 하고 나머지는 자는 경우도 있어서 함께 하기 위해 파트를 나누려고 노력했다. 
 
그리고 `핵심 기능을 구현하자.`고 생각했다. 로그인 기능이라든지 게임 랭킹 기능은 구현하지 않았다.

`장점을 최대한 살렸다.` 나는 프론트 엔드 개발 보다는 백엔드 개발을 잘하기 때문에 최대한 백엔드 개발에 집중하려고 했고 아이디어 기획 및 구체화에 힘썼다. 각자의 장점을 파악하고 그에 맡는 파트를 담당하는게 중요하다.

`해커톤 주제와 심사 위원 생각하자.` 심사위원들이 젊은 나이 대에 속하기 때문에 음악과 유행에 관심이 많을 것이라 생각했다. 사회 복지 같은 주제도 좋지만 사회 복지라는 분야는 너무 광범위하고 사람들의 관심사를 파악하는것도 힘들다고 생각해서 주제 선정을 게임으로 했고 이러한 게임을 만들었다.

## 작성한 코드
- https://github.com/jangjichang/TruckHackerton_4
- 