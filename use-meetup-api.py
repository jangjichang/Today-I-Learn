import requests


def meetup_group_event_title(url):
    res = requests.get(url)
    res_json = res.json()
    data = dict()
    for event in range(len(res_json)):
        data[event] = res_json[event]['name']
    return data
        # print(event, res_json[event]['name'], res_json[event]['local_date'], res_json[event]['local_time'], res_json[event]['venue'])
    # return res_json[0]['name']


def test_meetup_group_event():
    data = {0: '[8th GroundBreakers Meetup] 여덟번째 스토리 : GraalVM! : fast, economical & polyglot'}
    assert meetup_group_event_title(
        'https://api.meetup.com/OracleDeveloperKR/events?&sign=true&photo-host=public&page=20') == data
    # data = {'0': 'HONGDAE Language Exchange Meet ups - English - Korean!!',
    #         '1': '1920 Gatsby Social Party (Hongdae)',
    #         '2': '1920 Gatsby Social Party	'}
    # assert meetup_group_event_title('https://api.meetup.com/Globalseoulmates/events?&sign=true&photo-host=public&page=3') == data