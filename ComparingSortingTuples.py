fname =  input("Enter file")
if len(fname) < 1: fname = "clown.txt"
hand = open(fname)

di = dict()
for lin  in hand:
    lin = lin.strip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

tmp = list()
for k,v in di.items():
    next = (v,k)
    tmp.append(next)

tmp = sorted(tmp, reverse=True)

for v,k in tmp[:5]:
    print(k,v)


