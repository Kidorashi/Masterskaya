import re


vow = 'aȃáiîíuúoóôeéêę'
cons = 'bcdðfghjklmnprstvwxz'


def lists():
    global vow, cons
    vow = list(vow)
    cons = list(cons)
    return


def word_begin(word):
    if word.startswith('th'):
        word = re.sub('^th', 'd', word)
    elif word.startswith('hl'):
        word = re.sub('^hl', 'l', word)
    elif word.startswith('hn'):
        word = re.sub('^hn', 'n', word)
    elif word.startswith('hr'):
        word = re.sub('^hr', 'r', word)
    elif word.startswith('ch') and word[2] == 'i':
        word = re.sub('^ch', 'g', word)

        """
        chind => kind
        """
    elif word.startswith('hu') and word[2] in vow:
        word = re.sub('^hu', 'w', word)
    elif word.startswith('z'):
        word = re.sub('^z', 'z', word)
    elif word.startswith('ch'):
        word = re.sub('^ch', 'k', word)
    elif word.startswith('kh'):
        word = re.sub('^kh', 'k', word)
    elif word.startswith('h'):
        word = re.sub(r"h(?=("+'|'.join(vow)+r"))", "h", word)
    else:
        return word
    return word


def word_any(word):
    word = re.sub('dh', 'd', word)
    word = re.sub('ð', 'd', word)
    word = re.sub('gh', 'g', word)
    word = re.sub('pph', 'pf', word)
    word = re.sub('sc', 'sk', word)
    word = re.sub('sch', 'sk', word)
    word = re.sub('kch', 'k', word)
    word = re.sub('qu', 'kw', word)
    word = re.sub('quh', 'kw', word)
    word = re.sub('(?<!l|p|r)ph', 'pf', word)
    word = re.sub('v(?!v)', 'f', word)
    word = re.sub('c(?!h|e|i)', 'k', word)
    return word


def word_vowel(word):
    word = re.sub(r"(?<=("+'|'.join(vow)+r"))zss", "ȥȥ", word)
    word = re.sub(r"(?<=("+'|'.join(vow)+r"))c(?=(e|i))", "z", word)
    word = re.sub(r"(?<=("+'|'.join(vow)+r"))c(?!(" + '|'.join(cons) +r"))", "z", word) # РАБОТАЕТ
    word = re.sub(r"(?<=("+'|'.join(vow)+r"))zss^\\b", "ȥȥ", word)
    word = re.sub(r"(?<=("+'|'.join(vow)+r"))zss\\b", "ȥ", word)
    return word


def word_consonant(word):
    word = re.sub(r"(?<=("+'|'.join(cons)+r"))zz", "z", word)
    word = re.sub('(?<=l|r)ph', 'f', word)
    if 'cch' and 'kch' and 'sch' not in word:
        word = re.sub(r"(?<=("+'|'.join(cons)+r"))ch", "k", word)
    if 'skh' not in word:
        word = re.sub(r"(?<=("+'|'.join(cons)+r"))kh", "k", word)
    return word


def word_intervoc(word):
    word = re.sub(r"(?<=("+'|'.join(vow)+r"))zc(?!(" + '|'.join(vow) +r"))", "ȥȥ", word)
    word = re.sub(r"(?<=("+'|'.join(vow)+r"))h(?!(" + '|'.join(vow) +r"))", "hȥ", word)
    return word


def word_work(word):
    word = word_begin(word)
    word = word_any(word)
    word = word_vowel(word)
    word = word_consonant(word)
    word = word_intervoc(word)
    return(word)

df = open("C:\\Users\\1\\Desktop\\wordlist.txt", "r", encoding="UTF-8")
words = df.readlines()
n = 0
lists()

while n < len(words):
    words[n] = re.sub('\n', '', words[n])
    n += 1

for word in words:
    w = word
    word = word_work(word)
    k+=1
    if word != w:
        print (w + ' -> ' + word)
