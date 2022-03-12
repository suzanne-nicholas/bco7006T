#numbers=[1,2,3,4,10]

#index=0

#while index < len(numbers):
#    print("current index=", index)
#    print("old number in a list", numbers[index])
#    numbers[index]*=2
#    print("new number in a list", numbers[index])
#    index+=1
#    print("new index=", index)

#print(numbers)



#new_list = []

#for fruit in fruits:
#    if "a" in fruit:
#        new_list.append(fruit)
#print(new_list)


#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#new_list = []
#new_list = [fruit for fruit in fruits if "a" in fruit]
#print(new_list)


first=[1,2,3,4,5,6]
new_list=[]
second=[1,2,3]

index=0

while index<len(first):
    print("second[index]", second[index])
    if second[index] in first:
        new_list.append(second[index])
        print("new_list", new_list)
    else:
        print("no change to list")
    index+=1


