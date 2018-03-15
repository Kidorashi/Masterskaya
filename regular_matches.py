from numpy import genfromtxt
import re


VOW = list('aȃáiîíuúoóôeéêę')
CONS = list('bcdðfghjklmnprstvwxz')


# кодировка - что-то не так, диакритические знаки не парсятся
my_data = open('/Users/a123/PycharmProjects/Kolbaster/prefix.csv', 'r', encoding='utf-8')
my_data = my_data.read()
prefix = re.sub("^\s+|\n|\r|\s+", '', my_data)

prefix = prefix.split(';')
prefix = list(filter(None, prefix)) # ура, массив префиксов!

eide = open('eide.txt', 'r', encoding='utf-8')
eide = eide.read()
word = ['ecchi', 'ghechi', 'ghunch']
d = {}
for el in word:
    ecci = re.findall('\w*?e[bcdðfghjklmnprstvwxz]+i\w?', el) # a|e
    icciu = re.findall('\w*?i[bcdðfghjklmnprstvwxz]+i|u\w?', el) # e|i
    inc = re.findall('\w*?in[bcdðfghjklmnprstvwxz]+\w?', el) # e|i
    unc = re.findall('\w*?un[bcdðfghjklmnprstvwxz]+\w?', el) # o|u
    ucciu = re.findall('\w*?u[bcdðfghjklmnprstvwxz]+i|u\w?', el) # o|u
    iucciu = re.findall('\w*?iu[bcdðfghjklmnprstvwxz]+i|u\w?', el) # ie
    iunc = re.findall('\w*?iun[bcdðfghjklmnprstvwxz]+\w?', el) # ie
    iucci = re.findall('\w*?iu[bcdðfghjklmnprstvwxz]+i\w?', el) # û, только notker.txt
    for el in ecci:
        el1 = re.sub(r'('+'|'.join(prefix)+r'*?'+'|'.join(CONS)+r'*?)e('+'|'.join(CONS)+r'+i)', r'\1a\2', el) # 1st vowel after prefix, not \w*e
        el2 = re.sub(r'('+'|'.join(prefix)+r'*?'+'|'.join(CONS)+r'*?)e('+'|'.join(CONS)+r'+i)', r'\1e\2', el)
        d.setdefault(el, []).append(el1)
        d.setdefault(el, []).append(el2)
    for el in icciu:
        el1 = re.sub(r'(' + '|'.join(prefix) + r'*?' + '|'.join(CONS) + r'*?)i(' + '|'.join(CONS) + r'+i|u)', r'\1e\2',
                     el)
        el2 = re.sub(r'(' + '|'.join(prefix) + r'*?' + '|'.join(CONS) + r'*?)i(' + '|'.join(CONS) + r'+i|u)', r'\1i\2',
                     el)
        d.setdefault(el, []).append(el1)
        d.setdefault(el, []).append(el2)
    for el in inc:
        el1 = re.sub(r'(' + '|'.join(prefix) + r'*?' + '|'.join(CONS) + r'*?)in(' + '|'.join(CONS)+r')', r'\1en\2',
                     el)
        el2 = re.sub(r'(' + '|'.join(prefix) + r'*?' + '|'.join(CONS) + r'*?)in(' + '|'.join(CONS) + r')', r'\1in\2',
                     el)
        d.setdefault(el, []).append(el1)
        d.setdefault(el, []).append(el2)
    for el in unc:
        el1 = re.sub(r'(' + '|'.join(prefix) + r'*?' + '|'.join(CONS) + r'*?)un(' + '|'.join(CONS) + r')', r'\1on\2',
                     el)
        el2 = re.sub(r'(' + '|'.join(prefix) + r'*?' + '|'.join(CONS) + r'*?)un(' + '|'.join(CONS) + r')', r'\1un\2',
                     el)
        d.setdefault(el, []).append(el1)
        d.setdefault(el, []).append(el2)
    for el in ucciu:
        el1 = re.sub(r'(' + '|'.join(prefix) + r'*?' + '|'.join(CONS) + r'*?)u(' + '|'.join(CONS) + r'+i|u)', r'\1o\2',
                     el)
        el2 = re.sub(r'(' + '|'.join(prefix) + r'*?' + '|'.join(CONS) + r'*?)u(' + '|'.join(CONS) + r'+i|u)', r'\1u\2',
                     el)
        d.setdefault(el, []).append(el1)
        d.setdefault(el, []).append(el2)
    for el in iucciu:
        el1 = re.sub(r'(' + '|'.join(prefix) + r'*?' + '|'.join(CONS) + r'*?)iu(' + '|'.join(CONS) + r'+i|u)', r'\1ie\2',
                     el)
        d.setdefault(el, []).append(el1)
    for el in iunc:
        el1 = re.sub(r'(' + '|'.join(prefix) + r'*?' + '|'.join(CONS) + r'*?)iun(' + '|'.join(CONS) + r')', r'\1ien\2',
                     el)
    for el in iucci:
        el1 = re.sub(r'(' + '|'.join(prefix) + r'*?' + '|'.join(CONS) + r'*?)iu(' + '|'.join(CONS) + r'+i)', r'\1û\2',
                     el)
        d.setdefault(el, []).append(el1)