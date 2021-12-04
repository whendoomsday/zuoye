import re
import requests

def date_yiye(name,page):
 for page_1 in range(1, page+1):
    url = "https://findcumt.libsp.com/find/unify/search"
    json_data = {
        "searchFieldContent": name,
        "searchField": "keyWord",
        "matchMode": "2",
        "sortClause": "asc",
        "page": page_1,
        "rows": "10",
    }
    headers = {
        "Content-Length": "514",
        "Content-Type": "application/json;charset=UTF-8",
        "groupCode": "200069",
        "Origin": "https://findcumt.libsp.com",
        "Referer": "https://findcumt.libsp.com/",
    }
    response = requests.post(url, json=json_data, headers=headers)
    home_page = response.content.decode()
    json_str = re.findall(r'\[.+\]', str(home_page), re.S)[0]
    date_1 = (re.findall('("title".*?,)"collectionName"', json_str))
    date_2 = (re.findall('("author".*?),"publisher"', json_str))
    date_3 = (re.findall('("publisher".*?),"isbn"', json_str))
    date_4 = (re.findall('("isbn".*?),"isbns"', json_str))
    date_5 = (re.findall('("callNoOne":.*?),"callNo"', json_str))
    date_6 = (re.findall('"groupRecordIds":\[{("recordId".*?),"', json_str))
    template = []
    for i in range(10):
        template.append('{')
        template.append(date_1[i])
        template.append(date_2[i])
        template.append(date_3[i])
        template.append(date_4[i])
        template.append(date_5[i])
        template.append(date_6[i])
        template.append('}')
    for i in range(80):
        print(template[i])


print('关键字')
a = input()
print('查询几页')
b = eval(input())
date_yiye(a,b)



