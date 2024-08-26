import re

def filter(user_input):
    """
    주어진 사용자 입력이 안전한지 확인합니다.
    SQL 인젝션에 사용될 수 있는 특수 문자가 포함되어 있으면 False를 반환합니다.
    
    :param user_input: 사용자가 입력한 문자열
    :return: 안전한 경우 True, 그렇지 않은 경우 False
    """
    # 정규 표현식 패턴: SQL 인젝션에서 자주 사용되는 문자들
    pattern = r"['\";--]"
    
    # 정규 표현식 패턴에 해당하는 문자가 있는지 검사
    if re.search(pattern, user_input):
        return False
    
    return True