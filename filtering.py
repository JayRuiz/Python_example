"""
Example 1-4
Filtering list
"""

sample_list=[25,'Kim',30,'Jay', 45, 'Jay Kim']

def filter_mark(lst):
	integers = []
	rests=[]
	
	for ele in lst:
		if type(ele) is int:
			integers.append(ele)
		else:
			rests.append(ele)
	return integers, rests

integers, rests = filter_mark(sample_list)

print 'Integer: ', ','.join([str(x) for x in integers])
print 'Others: ', ','.join(rests)
