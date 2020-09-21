


def selection_sort(l_):
	if l_:
		for i in range(len(l_)):
			min = i
			for k in range(i+1, len(l_)):
				if l_[k] < l_[min]:
					min = k
			l_[min], l_[i]=l_[i], l_[min]
	return l_



print(selection_sort([4,3,2,1]))
