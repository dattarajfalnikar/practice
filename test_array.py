



def test_arr(l,n):
	if l:
		if n > 0:
			l[n-1]+=1
			n-=1
			test_arr(l, n)
			

l=[1,2,3,4,5]
print(test_arr(l, 5))		
print(l)
			



