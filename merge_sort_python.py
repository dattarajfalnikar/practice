

def merge_sort(l):
	if len(l)>1:
		mid = len(l)//2
		left_l = l[:mid]
		right_l =l[mid:]	
	
			
		merge_sort(left_l)
		merge_sort(right_l)

		i=j=k=0
		while i< len(left_l) and j < len(right_l):
			if left_l[i] < right_l[j]:
				l[k] = left_l[i]
				k+=1
				i+=1
			else:
				l[k] = right_l[j]	
				k+=1
				j+=1
		while  i < len(left_l):
			l[k] = left_l[i]
			k+=1
			i+=1
		
		while  j < len(right_l):
			l[k] = right_l[j]
			k+=1
			j+=1



l=[4,3,2,1]
merge_sort(l)
print(l)
