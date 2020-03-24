f = open("typos.csv","r")
w1 = open("train.csv","a")
w2 = open("test.csv","a")
f1 = f.readlines()
train = ""
test = ""
i = 0
for x in f1:
    if i % 10 < 8:
        train += x
    else:
        test += x
    i += 1
w1.write(train)
w2.write(test)
