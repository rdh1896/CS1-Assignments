t2 = ["a", "j", "s", "b", "t", "c", "l", "u", "d"]
t3 = ["b", "k", "t", "c", "u", "d", "m", "v", "e"]
t4 = ["c", "l", "u", "d", "v", "e", "n", "w", "f"]
t5 = ["d", "m", "v", "e", "w", "f", "o", "x", "g"]
t6 = ["e", "n", "w", "f", "x", "g", "p", "y", "h"]
t7 = ["f", "o", "x", "g", "y", "h", "q", "z", "i"]
t8 = ["g", "p", "y", "h", "z", "i", "r", "a", "j"]
t9 = ["h", "q", "z", "i", "a", "j", "s", "b", "k"]
t10 = ["i", "r", "a", "j", "b", "k", "t", "c", "l"]

def solve_cipher(n1, n2):
	n1 = int(n1)
	n2 = int(n2)
	if n2 == 1:
		n2 = 8
	else:
		n2 -= 2
	if n1 == 2:
		crypt = t2[n2]
		return crypt
	elif n1 == 3:
		crypt = t3[n2]
		return crypt
	elif n1 == 4:
		crypt = t4[n2]
		return crypt
	elif n1 == 5:
		crypt = t5[n2]
		return crypt
	elif n1 == 6:
		crypt = t6[n2]
		return crypt
	elif n1 == 7:
		crypt = t7[n2]
		return crypt
	elif n1 == 8:
		crypt = t8[n2]
		return crypt
	elif n1 == 9:
		crypt = t9[n2]
		return crypt
	elif n1 == 1:
		crypt = t10[n2]
		return crypt
	else:
		return "Error: Unaccepted Input."

def read_cipher(txt):
	file = open(txt)
	index = 0
	decrypt = ""
	line_num = 1
	line = file.readline()
	line = line.strip()
	while line != "":
		for ch in line:
			if ch == "." or ch == " ":
				index += 1
			elif index % 4 == 0:
				decrypt = decrypt + solve_cipher(line[index], line[index + 2])
				index += 1
			else:
				index += 1
		index = 0
		line_num += 1
		line = file.readline()
		line = line.strip()
	print(decrypt)

def read_cipher2(txt):
	file = open(txt)
	index = 0
	decrypt = ""
	line_num = 1
	switch = True
	line = file.readline()
	line = line.strip()
	while line != "":
		print(line)
		for ch in line:
			if ch == "." or ch == " " or ch == "0":
				index += 1
			elif ch == "1":
				if switch == True:
					if line[index + 3] == "1":
						decrypt = decrypt + solve_cipher(line[index] + line[index +1], line[index + 3] + line[index + 4])
						index += 1
						switch = False
					else:
						decrypt = decrypt + solve_cipher(line[index] + line[index + 1], line[index + 3])
						index += 1
						switch = False
				else:
					if ch == "1":
						index += 1
					elif ch == "0":
						switch = True
						index += 1
					elif "0" < ch <= "9":
						switch = True
						index += 1
			elif "0" < ch <= "9":
				if switch == True:
					if line[index + 2] == "1":
						decrypt = decrypt + solve_cipher(line[index], line[index + 2] + line[index + 3])
						index += 1
						switch = False
					else:
						decrypt = decrypt + solve_cipher(line[index], line[index + 2])
						index += 1
						switch = False
				else:
					if ch == "1":
						index += 1
					elif ch == "0":
						switch = True
						index += 1
					elif "0" < ch <= "9":
						switch = True
						index += 1
			print(index, end="")
			print(decrypt, end="")
		index = 0
		line_num += 1
		switch = True
		line = file.readline()
		line = line.strip()
	print(decrypt)



def main():
	txt = input("Insert file here: ")
	read_cipher(txt)

main()
