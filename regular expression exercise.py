import re
text = 'UPPER PYTHON, lower python, Mixed Python'
a=re.findall('python', text, flags=re.IGNORECASE)
b=re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(a)
print(b)

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
a=re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(a)

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
... multiline comment */
... '''
a=comment.findall(text1)
b=comment.findall(text2)
print(a)
print(b)
print(text1)