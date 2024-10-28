import Login
import Menu
import Session
import getTT

session = Session.makesession()
login = Login.login(session)
menu_tt = Menu.openTimeTable(session,login)

#↓デバッグ用の書き出し
# with open("html/source.html", "w") as f:
#    f.write(menu_tt.text)
#    print("Wrote Successfully")

#前後期の授業一覧を書き出す
# print(getTT.getClassTitle(menu_tt,1))
# print(getTT.getClassTitle(menu_tt,2))

#空きコマ含めた授業表を書き出す
timetable = getTT.getTimeTable(menu_tt,2)
#月曜なら0,火曜なら1...
print(timetable[4])
