


def partition(list_, low, high):
	
	piv = list_[high]
	i, j =-1, 0
	print list_	
	while j < high:
		if list_[j] < piv:
			i+=1
			list_[i], list_[j] = list_[j], list_[i]
		j+=1
	
	list_[i+1], list_[high] = list_[high], list_[i+1]
	print list_
	
	return i+1


def quick_sort(l, low, high):
	
	if low < high:
		
		piv = partition(l, low, high)
		print piv
		
		quick_sort(l, low, piv-1)
		quick_sort(l, piv+1, high)

	


l=[3,2,1,4,5,9,8,7,6]
ans = quick_sort(l, 0, len(l)-1)
