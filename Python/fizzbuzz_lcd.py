#FizzBuzz LCD
#Author: @vipenl26



def print_num(nums):
	def printList(l):
		for i in l:
			print(i,end='')
		print(end=' ')


	a = (0,1)
	b = (1,2)
	c = (3,2)
	d = (4,1)
	e = (3,0)
	f = (1,0)
	g = (2,1)


	lcd_on =  [[' ', '-', ' '], ['|', ' ', '|'], [' ', '-', ' '], ['|', ' ', '|'], [' ', '-', ' ']]
	lcd_off = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

	dic = {0: {a,b,c,d,e,f},
		   1: {b,c},
		   2: {a,b,d,e,g},
		   3: {a,b,c,d,g},
		   4: {b,c,f,g},
		   5: {a,c,d,f,g},
		   6: {a,c,d,e,f,g},
		   7: {a,b,c},
		   8: {a,b,c,d,e,f,g},
		   9: {a,b,c,d,f,g},
		   }


	size=2
	nums=list(map(int,nums))

	for i in range(5):
		lcd_on[i][1]*=size
		lcd_off[i][1]*=size



	for i in range(5):
		if (i%2):
			for _ in range(size):
				for temp in range(len(nums)):
					num=nums[temp]
					for j in range(3):
						if (i,j) in dic[num]:
							print(lcd_on[i][j],end='')
						else:
							print(lcd_off[i][j],end='')
						if(j==2 and temp!=len(nums)-1):print(end=' ')

				print()

		else:
			for temp in range(len(nums)):
				num=nums[temp]
				for j in range(3):
					if (i,j) in dic[num]:
						print(lcd_on[i][j],end='')
					else:
						print(lcd_off[i][j],end='')
					if(j==2 and temp!=len(nums)-1):print(end=' ')

			print()

print('enter a number')
n=int(input())

def fizz():
	l=[' ____     ____  ____  ', '|      |     /     /  ', '|____  |    /     /   ', '|      |   /     /      ', '|      |  /___  /___ ']
	for i in l:
		print(*i)

def fizzbuzz():
	l=[' ____     ____  ____   ___          ____  ____', '|      |     /     /  |   |  |   |     /     /', '|____  |    /     /   |___/  |   |    /     /', '|      |   /     /    |   \\  |   |   /     /   ', '|      |  /___  /___  |___|  |___|  /___  /___']
	for i in l:
		print(*i)


def buzz():
	l=[' ___          ____  ____', '|   |  |   |     /     /', '|___/  |   |    /     /', '|   \\  |   |   /     /   ', '|___|  |___|  /___  /___']
	for i in l:
		print(*i)


for i in range(1,n+1):
	if i%5==0 and i%3==0:
		fizzbuzz()
	elif i%3==0:
		fizz()
	elif i%5==0:
		buzz()
	else:
		print_num(str(i))


