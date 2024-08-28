import re

def filter(user_input):
    # SQL 인젝션에서 자주 사용되는 위험한 키워드 리스트
    dangerous_keywords = [
        "'",'"',"0x",'char','benchmark','substr','instr','sleep','like','ascii','#'
    ]

    # 정규표현식을 이용해 대소문자 구분 없이 위험한 키워드가 포함되어 있는지 검사
    for keyword in dangerous_keywords:
        if re.search(keyword, user_input, re.IGNORECASE):
            print(keyword)
            return True
    
    return False

