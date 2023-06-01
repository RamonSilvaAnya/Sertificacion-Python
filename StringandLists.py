han = open("mbox.short.txt")

for line in han:
    line = line.strip()
    wds = line.split()
    
    if len(wds) < 3 or wds[0] != "from":
        continue
    print(wds[2])