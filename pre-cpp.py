maxs = [0,0,0,0,0,0]
mins = [10e9, 10e9, 10e9, 10e9, 10e9, 10e9]


with open('CensusIncome/CencusIncome.data.txt', 'r') as f:
		for line in f:
				data = line.split(',')
				try:
						p = [int(data[0]), int(data[2]), int(data[4]), int(data[10]), int(data[11]), int(data[12])]
				except:
						print(data)

						
				for i in range(len(p)):
						if maxs[i] < p[i]:
								maxs[i] = p[i]
						if mins[i] > p[i]:
								mins[i] = p[i]

dataset = []
with open('CensusIncome/CencusIncome.data.txt', 'r') as f:
		count = 0
		for line in f:        
				data = line.split(',')
				try:
						p = [int(data[0]), int(data[2]), int(data[4]), int(data[10]), int(data[11]), int(data[12])]
						for i in range(len(p)):
								p[i] = p[i] / (maxs[i] - mins[i])
								print(p[i], end=' ')
						if data[14] == ' <=50K\n':
							print(0)
						else:
							print(1)
						dataset.append(p)
				except:
						pass
						#print(data)