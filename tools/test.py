'''
    测试

'''
import pinyin


def getStrAllAplha(str):
    return pinyin.get_initial(str, delimiter="").upper()


def getStrFirstAplha(str):
    str = getStrAllAplha(str)
    str = str[0:1]
    return str.upper()


str = '你好在哪来'

print(getStrAllAplha(str))
print(getStrFirstAplha(str))



print( 1 if "<"=="˂" else 2)
print( 1 if ">"== "˃" else 2)
print( 1 if "/"== "／" else 2)
print( 1 if "\\"== "∖" else 2)
print( 1 if "|"== "│" else 2)
print( 1 if ":"== "：" else 2)
print( 1 if "\""== "“" else 2)
print( 1 if "*"=="×" else 2)
print( 1 if "?"== "？" else 2)