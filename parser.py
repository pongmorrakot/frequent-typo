import typocheck
print("Parse CSV file")

f = open("typos.csv","r")
w = open("typocorrect.csv","a")
f1 = f.readlines()
table = ""
for x in f1:
#    print(x.rstrip())
    ret = x.split(",")
    output = typocheck.main(ret[0], ret[1], 1)
#    print(output)
    entry = ret[0] + "," + ret[1] + "," + output + "\n"
    print(entry)
    table += entry
w.write(table)
