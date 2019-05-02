from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError

input = 'https://place.map.kakao.com/27294339'
output = {
    'txt_address': '서울 마포구 방울내로7길 5 1층 (우)03960',
    'txt_addrnum': '망원동 436-4',
    'txt_operation': '월~토 ',
    'time_operation': '19:00 ~ 04:00',
    'txt_contact': '02-324-0928',
    'txt_introduce': '비스트로펍,수제맥주 및 미트볼전문'
      }


def test_crawling():
    assert crawling(input) == output


def crawling(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e, "해당 url에 접속할 수 없습니다.")
    else:
        bsObj = BeautifulSoup(html, 'html.parser')
        print(bsObj)

    try:
        place_data = bsObj.find_all('div', {'class': 'location_detail'})
        print(place_data)
    except AttributeError as e:
        print(e, "상세 정보가 없습니다.")


if __name__ == '__main__':
    crawling(input)
