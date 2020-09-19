e = 0.1
a = []
a.append(1)
a.append(2)
k = 1
while abs(a[k] - a[k-1]) >= e:
	k += 1
	a.append((a[k-2]+2*(a[k-1]))/3)
print(k+1 , a[k] , a[k-1])

