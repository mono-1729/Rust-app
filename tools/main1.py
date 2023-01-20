m, error= input().split()
m = int(m)
error = float(error)
n=0
nn=0

if m<=11:
	n=4
elif m<=31:
	n=5
else:
	n=6
while (nn*(nn-1))//2<m-1:
	nn+=1
c=1
num1=(c*nn*(c*nn-1))//2
num2=(num1)//(m-1)
while nn*(c+1)<=100:
	c+=1
	num1=(c*nn*(c*nn-1))//2
	num2=(num1)//(m-1)

print(n)
dp=[bin(i)[2:].zfill((n*(n-1))//2) for i in range(pow(2,((n*(n-1))//2)))]
numlist=set()
ans=[]
cc=0
for d in dp:
	h=[0 for i in range(n)]
	count=0
	for j in range(n):
		for k in range(j+1,n):
			if d[count]=="1":
				h[j]+=1
				h[k]+=1
			count+=1
	h.sort()
	hh=list(map(str,h))
	st=' '.join(hh)
	if st in numlist:
		continue
	else:
		numlist.add(st)
		print(d)
		ans.append(st)
		cc+=1
		if cc==m:
			break
for q in range(100):
	d = input()
	h=[0 for i in range(n)]
	count=0
	for j in range(n):
		for k in range(j+1,n):
			if d[count]=="1":
				h[j]+=1
				h[k]+=1
			count+=1
	h.sort()
	hh=list(map(str,h))
	st=' '.join(hh)
	for i in range(m):
		if ans[i]==st:
			print(i)
			break
		if i==m-1:
			print(m-1)