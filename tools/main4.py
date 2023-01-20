import random
m, error= input().split()
m = int(m)
error = float(error)
n=0
if m<=11:
	n=4
elif m<=31:
	n=5
else:
	n=6
if pow(0.9,100*error*((n*(n-1))//2))>=n/(100) or (3/11)*m+error*100>=(5*71)/22+36:
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
		flag=True
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
				flag=False
				break
		if flag:
			list0=[]
			list1=[]
			for i in range((n*(n-1))//2):
				h=[0 for i in range(n)]
				dd=list(d)
				switch=0
				if dd[i]=="1":
					dd[i]='0'
					switch=0
				else:
					dd[i]="1"
					switch=1
				count=0
				for j in range(n):
					for k in range(j+1,n):
						if dd[count]=="1":
							h[j]+=1
							h[k]+=1
						count+=1
				h.sort()
				hh=list(map(str,h))
				st=' '.join(hh)
				for k in range(m):
					if ans[k]==st:
						if switch==0:
							list0.append(k)
						else:
							list1.append(k)
						break
			if d.count('1')>(n*(n-1)//4):
				if len(list1)>0:
					print(random.choice(list1))
					continue
				if len(list0)>0:
					print(random.choice(list0))
					continue
				print(m-1)
			else:
				if len(list0)>0:
					print(random.choice(list0))
					continue
				if len(list1)>0:
					print(random.choice(list1))
					continue
				print(m-1)

else:
	num1=0
	num2=0
	score=[0]*101
	max_score=0
	corner=4
	for i in range(4,101):
		ac_count=0
		num1=(i*(i-1))//2
		num2=(num1)//(m-1)
		for _ in range(7):
			for k in range(100):
				ans_num=k%m
				count0=num1-ans_num*num2
				if ans_num==m-1:
					count0=0
				count1=0
				for p in range(count0):
					if random.random()<error:
						count1+=1
				for p in range(num1-count0):
					if random.random()>error:
						count1+=1
				if ans_num!=m-1:
					if (ans_num-0.5)*num2*(1-error)+(num1-(k-0.5)*num2)*(error)<=count1<(ans_num+0.5)*num2*(1-error)+(num1-(ans_num+0.5)*num2)*(error):
						ac_count+=1
				else:
					if (ans_num-0.5)*num2*(1-error)+(num1-(k-0.5)*num2)*(error)<=count1:
						ac_count+=1
			#print(ac_count)
			score[i]+=pow(0.9,100-ac_count)/i
	for i in range(4,101):
		tmp_score=score[min(i-1,4)]+score[i]+score[min(100,i+1)]
		if max_score<tmp_score:
			corner=i
			num1=(i*(i-1))//2
			num2=(num1)//(m-1)
			max_score=tmp_score
	#print(score)
	print(corner)
	g=['']*m
	graph=[['0']*(corner) for _ in range(corner)]
	count1=0
	for i in range(1,corner//2+1):
		for j in range(corner):
			if count1%num2==0 :#and (count1//num2)%2==0:
				anslist=[]
				for x in range(corner-1):
					for y in range(x+1,corner):
						anslist.append(graph[x][y])
				g[count1//num2]=''.join(anslist)
				if count1//num2==m-1:
					break
				
			graph[j][(j+i)%corner]="1"
			graph[(j+i)%corner][j]="1"
			count1+=1
		if count1//num2==m-1:
			break
	#print(graph)
	for k in range(m-1):
		if k%2==0:
			print(g[k])
		else:
			a="0" * (num1-k*num2) + "1" * (k*num2)
			print(a)
			g[k]=a
	g[m-1]="1" *num1
	print("1" *num1)
	for q in range(100):
		h = input()
		t = h.count('1')
		if t<num1*(error):
			print(0)
			continue
		for i in range(m):
			if i==m-2:
				if t<(i*num2+num1)*(1-error)/2+(num1-i*num2)*(error)/2:
					print(m-2)
				else:
					print(m-1)
				break
			if t<(i+1)*num2*(1-error)+(num1-(i+1)*num2)*(error):
				odd=i if i%2==1 else i+1
				even=i if i%2==0 else i+1
				corner_count=corner
				num=num1
				for j in reversed(range(corner)):
					num-=j
					if num1-even*num2>num:
						break
					corner_count-=1
				sum1=[0 for _ in range(corner)]
				count=0
				for j in range(corner):
					for k in range(j+1,corner):
						if h[count]=="1":
							sum1[j]+=1
							sum1[k]+=1
						count+=1
				sum1.sort()
				sum2=[0 for _ in range(corner)]
				count=0
				for j in range(corner):
					for k in range(j+1,corner):
						if g[odd][count]=="1":
							sum2[j]+=1
							sum2[k]+=1
						count+=1
				sum2.sort()
				sum3=[0 for _ in range(corner)]
				count=0
				for j in range(corner):
					for k in range(j+1,corner):
						if g[even][count]=="1":
							sum3[j]+=1
							sum3[k]+=1
						count+=1
				sum3.sort()
				if min(corner,corner-corner_count)==0:
					diff1=abs(sum(sum1))
					diff2=abs(sum(sum2))
					diff3=abs(sum(sum3))
				else:
					diff1=abs(sum(sum1[:corner_count])/corner_count-sum(sum1[corner_count+1:])/(corner-corner_count))
					diff2=abs(sum(sum2[:corner_count])/corner_count-sum(sum2[corner_count+1:])/(corner-corner_count))
					diff3=abs(sum(sum3[:corner_count])/corner_count-sum(sum3[corner_count+1:])/(corner-corner_count))
				if abs(diff2-diff1)>abs(diff1-diff3):
					print(even)
				else:
					print(odd)
				break