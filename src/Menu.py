import time
import datas
from bs4 import BeautifulSoup

#学生授業一覧のページに飛ぶためのURL
TimeTable_URL = "https://portal.sa.dendai.ac.jp/uprx/up/bs/bsd007/Bsd00701.xhtml"
#そのページに送る（POSTする）データ
TimeTable_DATA = datas.menu_timetable_data
  
def openTimeTable(session,login):
  bs = BeautifulSoup(login.text, 'html.parser')
  #ログイン毎に変わるデータを取得する
  rx_token = bs.find(attrs={'name':'rx-token'}).get('value')
  rx_loginKey = bs.find(attrs={'name':'rx-loginKey'}).get('value')
  rx_deviceKbn = bs.find(attrs={'name':'rx-deviceKbn'}).get('value')
  javax_faces_ViewState = bs.find(attrs={'name':'javax.faces.ViewState'}).get('value')
  #POSTするデータに追加する
  TimeTable_DATA['rx-token'] = rx_token
  TimeTable_DATA['rx-loginKey'] = rx_loginKey
  TimeTable_DATA['rx-deviceKbn'] = rx_deviceKbn
  TimeTable_DATA['javax.faces.ViewState'] = javax_faces_ViewState
  with session as s:
    response = s.post(TimeTable_URL, data = TimeTable_DATA)
    time.sleep(2)
  return response