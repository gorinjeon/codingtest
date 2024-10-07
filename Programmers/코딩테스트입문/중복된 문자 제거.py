'''
문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

'''
dict.fromkeys(my_string)는 문자열의 각 문자를 키로 하는 딕셔너리를 생성합니다. 딕셔너리는 키의 중복을 허용하지 않으므로, 중복된 문자는 자동으로 제거됩니다.
예: "hello"는 {'h': None, 'e': None, 'l': None, 'o': None}로 변환됩니다.

''.join(...)는 딕셔너리의 키들을 하나의 문자열로 결합합니다.
예: {'h': None, 'e': None, 'l': None, 'o': None}는 "helo"로 변환됩니다.
'''
