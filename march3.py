#------------------prog1----------------------------------------
# How  to  print  each  element  and  the  corresponding  index
'''
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)


a = [25 , 10.8 , 'Hyd' , True]
#using indexed for loop
for i in range(len(a)):
	print(i,a[i])
#using for each loop
for i in a:
	print(i,a.index(i))
'''
#----------------------------------------------------------------

#------------------------prog2----------------------------------

#  How  to  print  list  elements  in  reverse  order   without  slice
'''
a = eval(input('Enter  list  of  elements : '))
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable)

a = eval(input('Enter  list  of  elements : '))
for i in range(1,len(a)+1):	
	print(i-1,a[-i])
print()
for i in a[::-1]:
	print(i)
'''

'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []

How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop

#using for index
for i in range(len(a)):
	c.append(a[i]+b[i])
print(c)

#using for each

k=0
for i in a:
	c.append(i+b[k])
	k=k+1
print(c)

'''
'''
#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')

How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop

for i in range(2,5):
	print(a[i])

print('for each loop')
for i,value in enumerate(a):
	if i>=2 and i<=4:
		print(value)
'''
'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers  with  while  loop

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Use  while  loop

count=1
i=1
while count<=20:
	print(2*i)
	i=i+1
	count+=1
'''

