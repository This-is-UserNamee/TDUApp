import requests

#セッションを作る これがないとログインした後にページ遷移できなくなる（毎回自動ログアウトされる）
def makesession():
  session = requests.session()
  return session