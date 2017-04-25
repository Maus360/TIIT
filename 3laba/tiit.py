def _init():
	sa = ""
	st = []
	count = {
		"{": 0,
		"}": 0,
	}
	a = input("Введите множество:\n")
	
	for i in a[1:len(a) - 1]:
		sa += i
		
		if i == "{":
			count["{"] += 1
		if i == "}":
			count["}"] += 1
		if count['}'] == count['{']:
			st.append(sa)
			sa = ""
	sa = [x[1] for x in enumerate(st) if x[0] % 2 != 1]
	if count["{"] != count["}"]:
		print("Error, enter a valid set")
		return _init()
	
	return set(sa)


def boolean(a = _init()):
	d = []
	
	def boo(a):
		i = 0
		a = list(a)
		while len(a) >= 0 and i < len(a):
			k = list(a)
			k.remove(a[i])
			if k not in d:
				d.append(k)
			boo(k)
			i += 1
	
	boo(a)
	d.append(a)
	d = [set(x) for x in d]
	return "Boolean:", "{"+str(sorted(d))[1:len(str(d))-1]+"}"


print(boolean())