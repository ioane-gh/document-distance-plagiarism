# split text into words
def txt_split(txt):
    ls = []
    prev = 0
    for i in range(len(txt)):
        if len(txt) == 0:
            n = ls[:]
            return n
        if txt[i].isalnum():
            continue
        else:
            if txt[prev:i] == " ":
                continue
            ls.append(txt[prev:i])
            prev = i + 1
    else:
        ls.append(txt[prev:])
    n = ls[:]
    while " " in n:
        ind = n.find(" ")
        del n[ind]
    return n

#count each word in text and make a dictionary, vector
def make_dict(arr):
    dc = {}
    for i in arr:
        if i == "":
            continue
        if i not in dc:
            dc[i] = 1
        else:
            dc[i] += 1
    return dc

t1 = input('enter first text: ')
t2 = input('enter second text: ')

res1 = make_dict(txt_split(t1.lower()))
res2 = make_dict(txt_split(t2.lower()))

# finding cosinus of vectors and print percentage of similarity

sum = 0
for i in res1.keys():
    if i in res2.keys():
        sum += res2[i] * res1[i]

# multiplying length of the vectors
divisor1 = 0
divisor2 = 0
for i in res1.values():
    divisor1 += i**2
for i in res2.values():
    divisor2 += i**2

divisor1 = divisor1**(1/2)
divisor2 = divisor2**(1/2)
divisor = divisor2 * divisor1

similarity = sum/divisor

print(f'similarity is {similarity*10000//100}%')


