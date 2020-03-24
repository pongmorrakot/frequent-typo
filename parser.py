import typocheck
print("Parse CSV file")
nocorrect = 0
insertion = 0
deletion = 0
substitution = 0
transposition = 0
fail = 0
f = open("typos.csv","r")
w = open("typocorrect2.csv","a")
f1 = f.readlines()
table = ""
for x in f1:
#    print(x.rstrip())
    ret = x.split(",")
    output = typocheck.main(ret[0], ret[1], 1)
#    print(output)
    if output=="0":
        nocorrect += 1
    elif output=="i":
        insertion += 1
    elif output=="d":
        deletion += 1
    elif output=="t":
        transposition += 1
    elif output=="s":
        substitution += 1
    elif output=="x":
        fail += 1
    entry = ret[0] + "," + ret[1] + "," + output + "\n"
    print(entry)
    table += entry
table =  "no-correction,insertion,deletion,transposition,substitution,fail\n" + str(nocorrect) + "," + str(insertion) + "," + str(deletion) + "," + str(transposition) + "," + str(substitution) + "," + str(fail) + "\n" + table
w.write(table)
