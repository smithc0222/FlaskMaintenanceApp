import os,csv

testlist=[]
comparelist=[]
comparelist1=[]
successlist=[]
faillist=[]

with open('testlist.csv', 'rb') as inp:
    valid_rows=[row for row in csv.reader(inp) if any(field.strip() for field in row)]

with open('testlist.csv', 'wb') as out:
    csv.writer(out).writerows(valid_rows)

with open('testlist.csv', 'rb') as x:
    myfiles=csv.reader(x, delimiter=',')
    fileslist=list(myfiles)
    for each in fileslist:
        print(each)
        for first in each:
            #first=first.rstrip(first[:-3])
            doc=first+'.doc'
            docx=first+'.docx'
            pdf=first+'.pdf'
            txt=first+'.txt'
            csv=first+'.csv'
            #if first != '' and first != ' ':
            comparelist.append(first)
            testlist.append(first)
            testlist.append(doc)
            testlist.append(docx)
            testlist.append(pdf)
            testlist.append(txt)
            testlist.append(csv)
            #else:
            #    pass

currentdir=os.getcwd()
mydir=[os.path.join(root, name)
for root, dirs, files in os.walk(currentdir)
    for name in files]

for each in mydir:
    for x in testlist:
        if each.endswith(x) == True:
            print (x + ' ' + each + ' || Success')
            successlist.append(x)
            #os.startfile(each, 'print')


#remove file extension for comparison to find ones not successful
for each in successlist:
    if each.endswith('.doc') or each.endswith('.pdf') or each.endswith('.csv') or each.endswith('.txt'):
        w=each[:-4]
        comparelist1.append(w)
    else:
        v=each[:-5]
        comparelist1.append(v)

#find missing from both lists
faillist=list(set(comparelist)-set(comparelist1))


def main():
    f=open("this.txt", "w+")
    f.write("++-------------------++"+ "\n"+"Sucessfully Printed" + "\n"+"++-------------------++"+ "\n\n")
    for each in comparelist1:
        f.write(each + "\n\n")
    f.write("++-------------------++"+ "\n"+"Failed to Print" + "\n"+"++-------------------++"+ "\n\n")
    for each in faillist:
        f.write(each + "\n\n")
    f.close()
os.startfile("this.txt")

if __name__ == "__main__":
    main()

print(faillist)
