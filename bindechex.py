def BinDec(input):
	dec=0
	magnitude=1
	while input:
		last=input%10
		input = int(input*.1)
		#slices last element off input
		dec+=last*magnitude
		magnitude*=2
	return dec

def DecBin(input):
	bin=""
	while input:
		#print("bin before execution: ", bin)
		bin=str(input%2)+bin
		#print("bin after execution: ", bin)
		input=input//2
	return bin

def HexDec(input):
	counter=1
	dec=0
	input=str(input)
	inputLen=len(input)
	hexDict={
		"0":0,
		"1":1,
		"2":2,
		"3":3,
		"4":4,
		"5":5,
		"6":6,
		"7":7,
		"8":8,
		"9":9,
		"A":10,
		"B":11,
		"C":12,
		"D":13,
		"E":14,
		"F":15
	}
	for i in input:
		dec+=(hexDict.get(i)*(16**(inputLen-counter)))
		counter+=1
	return dec