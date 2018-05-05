def equation1(v0, a, t):
	v = v0 + (a * t)
	return v

def equation2(v, a, t):
	v0 = v - (a * t)
	return v0

def equation3(v, v0, t):
	a = (v - v0) / t
	return a

def equation4(v, v0, a):
	t = (v - v0) / a
	return t

def equation5(v0, t, a):
	x = (v0 * t) + ((1 / 2) * a * (t ** 2))
	return x

def equation6(x, t, a):
	v0 = (x - ((1 / 2) * a * (t ** 2))) / t
	return v0

def equation7(x, v0, a):
	t = [(-v0 - (((v0 ** 2) - (4 * ((1 / 2) * a) * -x)) ** (1 / 2))) / (2 * ((1 / 2) * a)), (-v0 - (((v0 ** 2) - (4 * ((1 / 2) * a) * -x)) ** (1 / 2))) / (2 * ((1 / 2) * a))]
	return t

def equation8(x, v0, t):
	a = (x - (v0 * t)) / ((1 / 2) * (t ** 2))
	return a

def equation9(v0, a, x):
	v = ((v0 ** 2) + (2 * a * x)) ** (1 / 2)
	return v

def equation10(v, a, x):
	v0 = ((v ** 2) - (2 * a * x)) ** (1 / 2)
	return v0

def equation11(v, v0, x):
	a = ((v ** 2) - (v0 ** 2)) / (2 * x)
	return a

def equation12(v, v0, a):
	x = ((v ** 2) - (v0 ** 2)) / (2 * a)
	return x

import nltk
problem = input()
tokens = nltk.word_tokenize(problem)
tagged = nltk.pos_tag(tokens)
#[v, v0, a, t, x]
variables = [0, 0, 0, 0, 0]
given = [False, False, False, False, False]
for i in range(len(tagged) - 1):
	if (tagged[i][1] == "CD"):
		if ((tokens[i + 1] == "m/s") and (tokens[i - 1] == "to")):
			variables[0] = float(tokens[i])
			given[0] = True
		if ((tokens[i + 1] == "m/s") and (tokens[i - 1] == "from")):
			variables[1] = float(tokens[i])
			given[1] = True
		if (tokens[i + 1] == "m/s^2"):
			variables[2] = float(tokens[i])
			given[2] = True
		if (tokens[i + 1] == "s"):
			variables[3] = float(tokens[i])
			given[3] = True
		if (tokens[i + 1] == "m"):
			variables[4] = float(tokens[i])
			given[4] = True
if ((given[1] == True) and (given[2] == True) and (given[3] == True)):
	print(equation1(variables[1], variables[2], variables[3]))
if ((given[0] == True) and (given[2] == True) and (given[3] == True)):
	print(equation2(variables[0], variables[2], variables[3]))
if ((given[0] == True) and (given[1] == True) and (given[3] == True)):
	print(equation3(variables[0], variables[1], variables[3]))
if ((given[0] == True) and (given[1] == True) and (given[2] == True)):
	print(equation4(variables[0], variables[1], variables[2]))
if ((given[1] == True) and (given[3] == True) and (given[2] == True)):
	print(equation5(variables[1], variables[3], variables[2]))
if ((given[4] == True) and (given[1] == True) and (given[2] == True)):
	print(equation6(variables[4], variables[1], variables[2]))
if ((given[4] == True) and (given[1] == True) and (given[2] == True)):
	print(equation7(variables[4], variables[1], variables[2]))
if ((given[4] == True) and (given[1] == True) and (given[3] == True)):
	print(equation8(variables[4], variables[1], variables[3]))
if ((given[1] == True) and (given[2] == True) and (given[4] == True)):
	print(equation9(variables[1], variables[2], variables[4]))
if ((given[0] == True) and (given[2] == True) and (given[4] == True)):
	print(equation10(variables[0], variables[2], variables[4]))
if ((given[0] == True) and (given[1] == True) and (given[4] == True)):
	print(equation11(variables[0], variables[1], variables[4]))
if ((given[0] == True) and (given[1] == True) and (given[2] == True)):
	print(equation12(variables[0], variables[1], variables[2]))