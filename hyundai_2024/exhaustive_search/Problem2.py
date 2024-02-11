strr=input()
result=""
for i in range(len(strr)):
    if strr[i]=="0":
        result=strr[:i]+"1"+strr[i+1:]
        break

if result=="":
    result=strr[:i]+"0"



sum=0

for i in range(len(result)-1,-1,-1):
    sum+=int(result[len(result)-1-i])*2**(i)

print(sum)