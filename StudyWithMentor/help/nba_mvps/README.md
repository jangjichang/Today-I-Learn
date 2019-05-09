# 후기

[링크](http://homoefficio.github.io/2019/05/08/%EC%9E%AC%EB%AF%B8%EB%A1%9C-%EB%B3%B4%EB%8A%94-%EC%96%B8%EC%96%B4%EB%B3%84-%EC%8A%A4%ED%8A%B8%EB%A6%BC-%EC%B2%98%EB%A6%AC-%EB%B9%84%EA%B5%90/?fbclid=IwAR1GGwXbnBXJc0GP8rlPsL3CLhy5U5M9BtqdyQlYDYg3n3Z643Qbt_O1FcM)

---

'재미로 보는...' 이지만 재미보다는 다큐로 봤다. 이렇게 여러 언어들을 비교해가면서 하나의 문제를 해결한 글은 처음봤다.

문제 풀이 흐름은 비슷하지만, 언어별로 사용하는 자료형이나 메소드의 차이점을 정리한 점이 인상적이다.
마지막으로 메소드의 공식 문서를 비교하는 글을 보고
python의 [collections](https://docs.python.org/3/library/collections.html#collections.Counter)를 봤더니 설명도 풍부하고
예제도 있었다.

내가 아는 지식으로 파이썬으로 코드를 작성하고 다른 언어들과 비교해보니, 나는 groupby라는걸 사용하지 않았다.

"python count list element frequency"로 구글링해보니 from itertools import groupby 사용 방법과 import colllections Counter를
사용하는 방법이 있었고 나는 이 라이브러리에 어떤 기능들이 있는지 알지 못했다. 
그래서 문제를 풀 때 itertools나 collections는 모르기 때문에 사용을 안하게 된다.
이미 존재하는 기능이 있다면 굳이 내가 그 기능을 다시 작성할 필요는 없다.

나는 지금까지 이미 존재하는 기능인지 확인도 안해보고 무작정 코드 작성하려고 했다.
나는 map, labmda, collections, itertools를 사용할 줄 모른다. 하지만
의식적인 연습을 위해 기존에 익숙했던 것에서 벗어나려고 했어야 했다. 알고 있던대로만 하는건 나에게 도움되지 않았을 것이다. 심지어 그
방법 외에 다른 방법이 있는지 찾으려고도 하지 않았다. 

내가 작성한 코드를 리팩토링하자.

---


[링크](http://homoefficio.github.io/2019/05/08/%EC%9E%AC%EB%AF%B8%EB%A1%9C-%EB%B3%B4%EB%8A%94-%EC%96%B8%EC%96%B4%EB%B3%84-%EC%8A%A4%ED%8A%B8%EB%A6%BC-%EC%B2%98%EB%A6%AC-%EB%B9%84%EA%B5%90/?fbclid=IwAR1GGwXbnBXJc0GP8rlPsL3CLhy5U5M9BtqdyQlYDYg3n3Z643Qbt_O1FcM)
에 있는 글을 보고 python으로 코드를 작성해봤습니다.


