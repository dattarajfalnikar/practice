


def bin_search(l, a):
	
	if l:
                res=0
                res1=0
	        mid = len(l)/2
		print(l)
                print('call test')
		if a==l[mid] or a==l[-1] or a==l[0]:
			print('mil to gaya')			
			return 1
		if a > l[mid] and mid > 0 and not a > l[-1]:
			return  bin_search(l[mid:], a)
                        #return res
		if a < l[mid] and mid>0 and not a < l[0] :
			return  bin_search(l[:mid], a)
	                #return res1
                
                #return res or res1	
        print('call')
        return 0



#print(bin_search([1,2,3,4,5,6, 91, 95, 100, 101, 102, 103], 95))	 
print(bin_search(range(1000), 1001))	 
