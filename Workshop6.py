a = 3
b = 8

#if a<b:
 #   print("a<b")
#elif a == b:
 #   print("a=b")
#else:
  #  print("a>b")


#for i in range (1,5):
 #   print("with for loop", i)

#count=1

#while count <=5:
 #   print("with while loop", count)
  #  count+=1


#while True:
#    if a<b:
#        print("while True loop a=", a)
#        a+=5

#    else:
#       break



x = 2
another_list = [x, x+1,"Hello" * x]
print(another_list)

first = [1,2,3,4,5,6]
second = list(range(1,10))
print("first list", first)

print("second list", second)

length_list=len(second)
print("length of second list", length_list)

print("element 1=", first[1])
print("element -1", first[-1])

print("merge lists", first+second)

print("elements 4:7 in second =", second[4:7])

third=first+second

forth=list(range(12,20))
print(forth)

if first in second:
    print(first, second, "\n","elements")
else:
    print(first, second, "\n","elements")



