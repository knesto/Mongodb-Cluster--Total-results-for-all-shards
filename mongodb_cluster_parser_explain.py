


nReturned = []
executionTimeMillis=[]
KeysExamined=[]
DocsExamined=[]
count=0
with open("samplefile5.txt") as file:
    for line in file:
        fields = line.split(",")
        for i in fields:
            if "\"executionStats\"" in fields[count]:
                dr = ''.join(x for x in fields[count+1] if x.isdigit())
                nReturned.append(int(dr))
                t = ''.join(x for x in fields[count+2] if x.isdigit())
                executionTimeMillis.append(int(t))
                k = ''.join(x for x in fields[count+3] if x.isdigit())
                KeysExamined.append(int(k))
                de = ''.join(x for x in fields[count+4] if x.isdigit())
                DocsExamined.append(int(de))
                
            count=count+1

totaldocs=0
for i in range (len(nReturned)):
    totaldocs= totaldocs+nReturned[i]
print("nReturned",totaldocs)

totalexecutionTimeMillis=0
for i in range (len(executionTimeMillis)):
    totalexecutionTimeMillis= totalexecutionTimeMillis+executionTimeMillis[i]
print("executionTimeMillis",totalexecutionTimeMillis)

totalKeysExamined=0
for i in range (len(KeysExamined)):
    totalKeysExamined= totalKeysExamined+KeysExamined[i]
print("totalKeysExamined",totalKeysExamined)

totalDocsExamined=0
for i in range (len(DocsExamined)):
    totalDocsExamined= totalDocsExamined+DocsExamined[i]
print("totalDocsExamined",totalDocsExamined)
