# 패키지안에 있는 다른 모듈 사용하는 방법
# from game.sound.echo import echo_test
from ..sound.echo import echo_test


def render_test():
    print("render")
    echo_test()
