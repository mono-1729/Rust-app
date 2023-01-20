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
c-=4
num1=(c*nn*(c*nn-1))//2
num2=(num1)//(m-1)
print(nn*c)
for k in range(m-1):
	print("1" * (k*num2) + "0" * (num1-k*num2))
print("1" *num1)
for q in range(100):
	h = input()
	t = h.count('1')
	for i in range(m):
		if t<(i+0.5)*num2*(1-error)+(num1-(i+0.5)*num2)*(error):
			print(i)
			break
		if i==m-1:
			print(m-1)