def list_of_range(start, stop):
	return list(range(start, stop))

def list_of_chars(string):
	return list(string)

def list_extend(L, to_extend):
    L.extend(to_extend)

def list_length(L):
	return len(L)

def positive_number_count(L):
	return len([n for n in L if n > 0])

def most_frequent_element(L):
	return max((L.count(c), c) for c in L)[1]
	
def square_each(L):
	return [x ** 2 for x in L]

def slice_last_n(L, n):
	return L[-n:]

def slice_from_to(L, to, f):
	return L[to:f]

def slice_every_third_element(L):
	return L[::3]

def if_even_square_each(L):
	return [x ** 2 for x in L if x % 2 == 0]

def get_second_to_last_item(L):
	return L[-2]

def get_item_at(L, i):
	return L[i]

def copy_of_list(L):
	return L[:]