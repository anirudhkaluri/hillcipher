import sys
import numpy
import math
chartext=list(input('Entr the text to be encrypted:')) #only capital letters. No spaces
print('the text entered is:',chartext)
asciitext=[]

for d in range(len(chartext)):
	asciitext.append(ord(chartext[d]))
	
#CONVERT LINEAR LIST OF TEXT INTO ROW MATRIX OF TEXT
asciitext=numpy.asarray(asciitext)

asciitext=asciitext-65
print('the numeric form of text is:',asciitext)

#PRINT LENGTH OF TEXT
length=len(chartext)
print('length of the text is:',length)


#INPUT KEY
key=list(input('Enter key')) #only capital letters 
for d in range(len(key)):
	key[d]=ord(key[d])
#CONVERT LIST OF KEY INTO MATRIX OF KEY
key=numpy.asarray(key)
key=key-65
print('the numeric of key is:',key)


#MAKE A KEY MATRIX
keylen=int(input('enter matrix dimension'))
keymatrix=numpy.asarray(key[0:keylen*keylen])
keymatrix=numpy.reshape(keymatrix,(keylen,keylen))
print('keymatrix:\n',keymatrix)




#FIND DET OF THE KEYMATRIX
detkeymatrix=numpy.linalg.det(keymatrix)
detkeymatrix=math.ceil(detkeymatrix%26) #WE GET DET IN FLOAT SO..
print('det of keymatrix is:',detkeymatrix)


#FIND ADJOINT OF KEY MATRIX
cokeymatrix=numpy.linalg.inv(keymatrix).T*numpy.linalg.det(keymatrix)
adjkeymatrix=numpy.matrix.transpose(cokeymatrix)
adjkeymatrix=adjkeymatrix%26
print('adjoint of keymatrix is:\n',adjkeymatrix)


#FIND THE DET INVERSE
detinverse=-1
for z in range(1,25):
	if (detkeymatrix*z)%26==1:
		detinverse=z
		break
if detinverse==-1:
	print('detinversen not initialized')
	exit()
	
print('det inverse is:',detinverse)

	
	

#FIND THE KEY INVERSE
keyinverse=detinverse*adjkeymatrix
keyinverse=keyinverse%26
print('keyinverse is:\n',keyinverse)




for x in range(0,length-keylen+1,keylen):
	tempmatrix=numpy.asarray(asciitext[x:x+keylen])
	tempmatrix=numpy.reshape(tempmatrix,(keylen,1))
	print('text to be encrypted matrix is:')
	for j in tempmatrix:
		for i in j:
			print(chr(i+65))
	#ENCRYPT
	enc=numpy.matmul(keymatrix,tempmatrix)
	enc=numpy.mod(enc,26)
	print('encrypted text is:\n',enc)
	#DECRYPT
	dec=numpy.matmul(keyinverse,enc)
	dec=numpy.around(dec)
	dec=dec.astype(int) #TO APPLY MODULUS WE NEED INT NOT FLOAT
	dec=numpy.mod(dec,26)
	print('decrypted text is:')
	for j in dec:
		for i in j:
			print(chr(i+65))

	