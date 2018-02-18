import re


def exceptions_before(word, notneed, ext, need):
    l = len(word)-2
    word = list(word)
    while l > 0:
        if word[l] == notneed:
            if word[l+1] not in ext:
                word[l] = need
        l-=1
    word = ''.join(word)
    return word

def word_begin(word):
    if word.startswith('th'):
        word = re.sub('th', 'd', word)
    elif word.startswith('hl'):
        word = re.sub('hl', 'l', word)
    elif word.startswith('hn'):
        word = re.sub('hn', 'n', word)
    elif word.startswith('hr'):
        word = re.sub('hr', 'r', word)
    elif word.startswith('ch') and word[2]=='i':
        word = re.sub('ch', 'g', word)
        
        """
        chind => kind
        """
    elif word.startswith('hu') and word[2] in ['u', 'a', 'e', 'i', 'o']:
        word = re.sub('hu', 'w', word)
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
    word = exceptions_before(word, 'v', ['v'], 'f')
    word = exceptions_before(word, 'c', ['h', 'e', 'i'], 'p')
    return word

#def word_vowel(word):
#def word_consonant(word):
    
def word_work(word):
    word = word_begin(word)
    word = word_any(word)
    return(word)

df = open("C:\\Users\\1\\Desktop\\wordlist.txt", "r", encoding = "UTF-8")
words = df.readlines()
n=0

while n < len(words):
    words[n] = re.sub('\n', '', words[n])
    n+=1

for word in words:
    w = word
    word = word_work(word)
    
    if word != w:
        print (w + ' -> ' + word)
        


