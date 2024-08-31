import re

def filter(user_input):
    dangerous_keywords = [
        "'",'"',"0x",'char','benchmark','substr','instr','sleep','like','ascii','#','schema'
    ]

    for keyword in dangerous_keywords:
        if re.search(keyword, user_input, re.IGNORECASE):
            print(keyword)
            return True
    
    return False

