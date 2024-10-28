
#ログインに必要なデータ（学籍番号、共通パスワードだけいじる)
login_data = {
  'loginForm': "loginForm",
  #学籍番号（小文字）
  'loginForm:userId': "学籍番号",
  #共通パスワード ⚠️人に見せちゃダメー
  'loginForm:password': "Password",
  'loginForm:loginButton': "",
  'javax.faces.ViewState': "stateless"
}

#学生授業一覧に飛ぶためのデータ（なんにもいじらない）
menu_timetable_data = {
  'menuForm': "menuForm",
  'rx.sync.source': "menuForm:mainMenu",
  'menuForm:mainMenu': "menuForm:mainMenu",
  'menuForm:mainMenu_menuid': "3_0_0_1"
}