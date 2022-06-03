import requests
from bs4 import BeautifulSoup as bs

def uis_api(id, pw):
    TIMEOUT_SEC = 3
    uis_header = {
    "Referer": "https://portal.sejong.ac.kr",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
    }
    LOGIN_INFO = {'id': id, 'password': pw, 'rtUrl': '',}

    with requests.Session() as s:
        s.post('https://portal.sejong.ac.kr/jsp/login/login_action.jsp', headers=uis_header,data=LOGIN_INFO,timeout=TIMEOUT_SEC)

        res = s.get('https://portal.sejong.ac.kr/main.jsp', timeout=TIMEOUT_SEC)
        soup = bs(res.content, 'html.parser')
        txt1 = soup.find(class_ = "txt1")
        if txt1 is None:
            return {"result":False}
        first_name = txt1.text.strip()
        major = soup.find(class_ = "txt4").text

        res = s.get('https://portal.sejong.ac.kr/user/index.do#;', timeout=TIMEOUT_SEC)
        soup = bs(res.content, 'html.parser')
        ph = soup.findAll(class_='ph')[1]
        phone_number = ph.findAll('option')[1]['value']+'-'+ph.findAll(class_='inp0')[0]['value']+'-'+ph.findAll(class_='inp0')[1]['value']

        email = soup.findAll(class_='inp0')[3]['value']

        return {"result":True, "first_name":first_name, "id":id, "major":major, "phone_number":phone_number, "email":email}