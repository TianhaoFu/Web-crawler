inport re
pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)"
#字母，任意的字符 字母 出现多次 @ 字母 任意的字符 字母出现多次 任意字符 出现多次  任意的字符字母出现多次
string = "fdewfewfewfe"
result = re.research(pattern.string)
print(result)