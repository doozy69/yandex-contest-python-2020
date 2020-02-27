# Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.
# Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.
count = input()

max = 0
result = 0
for i in range(int(count)):
	if input() == '1':
		result +=1
	else:
		if result > max:
			max = result
		result = 0

max = result if result > max else max
print(max)