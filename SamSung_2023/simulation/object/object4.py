class Person():
    def __init__(self,name="0",num="0",destinations="0"):
        self.name=name
        self.num=num
        self.destinations=destinations

n=int(input())

people=[Person() for _ in range(n)]
for i in range(n):
    na,nu,de=map(str,input().split())
    people[i].name=na
    people[i].num=nu
    people[i].destinations=de


index=0

for i in range(1,n):
    if people[i].name>people[index].name:
        index=i

print("name " +people[index].name)
print("addr " +people[index].num)
print("city "+people[index].destinations)