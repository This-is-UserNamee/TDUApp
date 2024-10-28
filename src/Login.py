import time
import datas
from bs4 import BeautifulSoup
import sys
  
#UNIPAのURL
LOGIN_URL = "https://portal.sa.dendai.ac.jp/uprx/up/pk/pky001/Pky00101.xhtml"
#Login用のデータ
LOGIN_DATA = datas.login_data

def login(session):
  with session as s:
    response = s.post(LOGIN_URL,LOGIN_DATA)
    time.sleep(2)
    bs = BeautifulSoup(response.text, 'html.parser')
    # print(response.text)
    errormessage = bs.select('#errForm')
    try:
      if errormessage:
        raise LoginError()
      else:
        return response
    except LoginError:
      print("ログイン情報が間違っています")
      sys.exit()
    
class LoginError(Exception):
  pass