


def merge1(l, low, mid, high):
	
	temp_mid,k = mid, 0
	mid = mid+1
	#print l[low:mid], l[mid:high]
	while low < temp_mid and mid <= high:
		if l[low] < l[mid+1]:
			l[k] = l[low]
			low+=1
			k+=1
		else:
			l[k] = l[mid]
			mid+=1
			k+=1
	while low < temp_mid:
		l[k] = l[low]
		k+=1
		low+=1
	
	while mid < high:
		l[k] = l[mid]
		k+=1
		mid+=1
			
			
def merge(l , low, mid, high):
	
	start, mid1 = low, mid
	start2, end = mid+1, high
	while True:
		
		if start <= mid1 or start2 < end:
			print start,mid, end, start2, l[low:high]			
			if l[start] > l[start2]:
				l[start], l[start2] = l[start2], l[start]
				start +=1
				start2 +=1
			else:
				start2 +=1	
					
		else:
			break
		
		print l

def merge_sort(l, low, high, side=None):
	if low<high:
		
		mid = (low+high)//2
		print 'mid:',mid, 'low:',low, 'high:',high, 'l:',l[low:high], 'side::',side		
				
		merge_sort(l, low, mid, side='left')
		merge_sort(l, mid+1, high, side='right')
		#merge1(l, low, mid, high)



l = [4,3,2,1]
#l=[6,4,3,1,2,5,8,7]
merge_sort(l, 0, len(l)+1)
print l
