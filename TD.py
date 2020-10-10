import random

class Letter:
    def __init__ (self, p, v):
        self.prev = p
        self.val = v
        self.active = False

def fill(s):
    word = []
    p = None
    for i in s:
        word.append(Letter(p,i))
        p = i
    return word

def activate(word,size):
    cur = 1
    for i in word:
        if i.val == str(cur):
            i.active = True
            cur+=1
        if cur>size:
            return 1
    return 0
def check(start,end):
    i=0
    for j in range(len(start)):
        if end[j].val == start[i].val:
            if end[j].prev == start[i].prev:
                
                i+=1
        if i == len(start):
            return True
    return False

def split(start,end,beginning):
    for j in range(len(end))[::-1]:
        if (end[j].val == start[0].val):
            if (beginning) and (end[j].prev == start[-1].val):
                if check(start[1:],end[j+1:]):
                    return j
            elif end[j].prev == start[0].prev:
                # print(end[j].val,start[i].val,'b')
                if check(start,end[j:]):
                    return j
    return 0
def duplicate(start,end):
    i = 0
    activations = []
    offset = 0
    # for x in start:
    #     print(x.val, end = '')
    # print()
    # for x in end:
    #     print(x.val, end = '')
    # print()
    for j in range(len(end)):
        j += offset
        if (end[j].val == start[i].val):
            # print('hi')
            if (i == 0) and (end[j].prev == start[-1].val):
                # print(end[j].val,start[i].val,'a')
                # if j != 0:
                #     offset = split(start[i:],end[j:],True)
                i+=1
                activations.append(j+offset)
            elif end[j].prev == start[i].prev and i != 0:
                # print(end[j].val,start[i].val,'b')
                i+=1
                if activations[-1] != j-1:
                    # offset = split(start[i-1:],end[j:],False)
                    activations.append(j+offset)
                else:
                    activations.append(j)
        if i == len(start):
            return(activations)

    return(activations)

def subsequence(start,end):
    length = 0
    templength=0
    # for i in end:
    #     print(i.val, end = '')
    # print()
    i=0
    for j in range(len(end)):
        #match
        if (end[j].val == start[i].val):
            if (end[j].prev == start[0].val):
                # print(end[j].val,start[i].val,'a')
                length=templength+1
            if end[j].prev == start[i].prev:
                # print(end[j].val,start[i].val,'b')
                templength+=1
                i+=1
    return length

def driver(word):
    done = False
    result = ''
    while not done:
        start = []
        end = []
        next = True
        longest = 0
        place = 0
        for i in range(len(word)):
            place += 1
            if word[i].active == True:
                start.append(word[i])
                # print(word[i].val,'c')
                next = True
            elif word[i].active == False and next:
                # print(word[i].val)
                tempend = []
                while i<len(word) and word[i].active == False:
                    tempend.append(word[i])
                    i+=1
                templong = subsequence(start[::-1],tempend[::-1])
                if templong > longest:
                    longest = templong
                    end = tempend
                    offset = len(start)
                    dupeplace = place
                next = False


        if longest == 0:
            for i in word:
                if i.active == False:
                    return result
            return False
        else:
            # print (offset, longest)
            # for i in start:
            #         print(i.val,end=' ')
            # print()
            activations = duplicate(start[offset-longest:offset],end)
        count = 0
        for i in activations:
            # print(activations)
            word[dupeplace-1 + i].active = True
        for i in word:
            result += (i.val+' ')
        result += '\n'
        for i in word:
            result+=((str)((int)(i.active))+' ')
        result+='\n \n'

size = 4
fail = 0
for j in range(1000):
    start = list(range(size+1))[1:]
    final = ''
    for i in range(5):
        dupe = int(random.uniform(0,len(start)))
        end = int(random.uniform(dupe,len(start)-dupe))
        start = start[:dupe]+start[dupe:end]+start[dupe:end]+start[end:]
        final += ''.join([str(i) for i in start]) + '\n'
    # print(''.join([str(i) for i in start]))
    w = fill(''.join([str(i) for i in start]))
    activate (w,size)
    result = driver(w)
    if result:
        fail += 1
        print(final)
        print(result)

print(fail)
