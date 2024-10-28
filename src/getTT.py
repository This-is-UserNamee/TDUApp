from bs4 import BeautifulSoup

#授業コードを取得する関数 semester は 1 で前期、2 で後期
def getClassCode(response,semester):
  bs = BeautifulSoup(response.text, 'html.parser')
  codes = []
  #前期
  if(semester == 1):
    for i in range(2,7):
      for j in range(1,6):
        #css_selecterで指定
        class_code = bs.select_one(f'#funcForm\:j_idt250\:0\:j_idt252 > div > table > tbody > tr:nth-child({str(j)}) > td:nth-child({str(i)}) > div > div:nth-child(4)')
        if class_code != None:
          codes.append(class_code.text)
  #後期
  elif(semester == 2):
    for i in range(2,7):
      for j in range(1,6):
          #css_selecterで指定
          class_code = bs.select_one(f'#funcForm\:j_idt250\:1\:j_idt252 > div > table > tbody > tr:nth-child({str(j)}) > td:nth-child({str(i)}) > div > div:nth-child(4)')
          if class_code != None:
            codes.append(class_code.text)
  else:
    print("Error: semester must be 1 or 2")
  
  return codes

#授業名を取得する関数 semester は 1 で前期、2 で後期
def getClassTitle(response,semester):
  bs = BeautifulSoup(response.text, 'html.parser')
  titles = []
  
  if(semester == 1):
    for i in range(2,7):
      for j in range(1,6):
        class_title = bs.select_one(f'#funcForm\:j_idt250\:0\:j_idt252 > div > table > tbody > tr:nth-child({str(j)}) > td:nth-child({str(i)}) > div > div.fontB')
        if class_title != None:
          titles.append(class_title.text)
  elif(semester == 2):
    for i in range(2,7):
      for j in range(1,6):
          class_title = bs.select_one(f'#funcForm\:j_idt250\:1\:j_idt252 > div > table > tbody > tr:nth-child({str(j)}) > td:nth-child({str(i)}) > div > div.fontB')
          if class_title != None:
            titles.append(class_title.text)
  else:
    print("Error: semester must be 1 or 2")
  
  return titles

def getTimeTable(response,semester):
  bs = BeautifulSoup(response.text, 'html.parser')
  timetable = [[],[],[],[],[]]
  
  if(semester == 1):
    for i in range(2,7):
      for j in range(1,6):
        class_title = bs.select_one(f'#funcForm\:j_idt250\:0\:j_idt252 > div > table > tbody > tr:nth-child({str(j)}) > td:nth-child({str(i)}) > div > div.fontB')
        if class_title != None:
          timetable[i-2].append(class_title.text)
        else:
          timetable[i-2].append("None")
  elif(semester == 2):
    for i in range(2,7):
      for j in range(1,6):
          class_title = bs.select_one(f'#funcForm\:j_idt250\:1\:j_idt252 > div > table > tbody > tr:nth-child({str(j)}) > td:nth-child({str(i)}) > div > div.fontB')
          if class_title != None:
            timetable[i-2].append(class_title.text)
          else:
            timetable[i-2].append("None")
  else:
    print("Error: semester must be 1 or 2")
    
  return timetable
  