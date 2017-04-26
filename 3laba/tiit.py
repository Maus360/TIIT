def _init(a=None):
	sa = ""
	st = []
	count = {
		"{": 0,
		"}": 0,
		"<": 0,
		">": 0
	}
	if not a:
		a = input("Введите множество:\n")
	
	for i in a[1:len(a) - 1]:
		sa += i
		if i == "<":
			count["<"] += 1
		if i == ">":
			count[">"] += 1
		if i == "{":
			count["{"] += 1
		if i == "}":
			count["}"] += 1
		if count['}'] == count['{'] and count["<"] == count[">"]:
			st.append(sa)
			sa = ""
	sa = [x[1] for x in enumerate(st) if x[0] % 2 != 1]
	if count["{"] != count["}"]:
		print("Error, enter a valid set")
		return _init()
	
	return set(sa)


def _boo(a, d):
	i = 0
	a = list(a)
	while len(a) >= 0 and i < len(a):
		k = list(a)
		k.remove(a[i])
		if k not in d:
			d.append(k)
		_boo(k, d)
		i += 1
		
		
def boolean(a = _init()):
	d = []
	_boo(a, d)
	d.append(a)
	d = [set(x) for x in d]
	return "Boolean: {"+str(sorted(d))[1:len(str(d))-1]+"}"


print(boolean())