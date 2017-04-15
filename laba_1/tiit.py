from test import laba

tiit = laba()


def main():
	inp = input(
		"1. Добавить к элементам на интервале a, b величину x\n2. Найти кол-во нулевых элементов на интервале a, b\n")
	
	if inp == "1":
		tiit.view()
		strt = int(input("Введите элемент старта\n"))
		fnal = int(input("Введите элемент окончания\n"))
		value = int(input("Введите величину, на которую изменить элементы\n"))
		tiit.modify(strt, fnal, value)
		tiit.view()
	else:
		tiit.view()
		strt = int(input("Введите элемент старта\n"))
		fnal = int(input("Введите элемент окончания\n"))
		
		print(tiit.findcover(strt, fnal))
		tiit.view()
	return main()
if __name__ == "__main__":
	main()
