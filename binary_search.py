


def bin_search(l, a, low, high):
	if l:
		while low<high:
			mid = int((low+high)/2)
		
			if a==low or a==high or a==mid:
				print('yaha to gaya')			
				return 1
			if a > l[mid] and mid > 0:
				is_found = binary_search(l, a, mid+1, high)
			elif a < l[mid] and mid>0:
				is_found = binary_search(l, a, low, mid)
	
			else:
				return 0	




print(bin_search([1,2,3,4,5], 3, 0, 5))	 
