import requests
import re # 정규식

url = "https://www.google.com"

res = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}) # 유저에이전트를 쓰면서 스크랩 막아놓은 걸 우회할 수 있다.
# 에러가 나면 Raise Error 프로그램을 종료한다. 에러가 안 나면 밑에 코드 실행! 보통 같이 쓰고 시작.
res.raise_for_status()

##정규식
# . (ca.e): 하나의 문자를 의미 -> care, case ...
# ^ (^de) : 문자열의 시작 -> desk, decrease ...
# $ (se$) : 문자열의 끝 -> base, case ...

p = re.compile("ca.e")

word = "careless"
sentence = "be careful on the cafe"
match = p.match(word)
search = p.search(sentence)
list_matched = p.findall(sentence) #일치하는 모든 것을 리스트 형태로 저장

def print_match(m):
    if m:
        print(f"{m.group()} is matched") # 일치하는 문자열 반환
        print(f"{m.string}") # 입력받은 문자열
        print(f"{m.start()}") # 일치하는 문자열의 시작 index
        print(f"{m.end()}") # 일치하는 문자열의 끝 index
        print(f"{m.span()}") # 일치하는 문자열의 시작, 끝 index
    else:
        print("It doesn't match on our system")
        
# print_match(search)
# print(list_matched)