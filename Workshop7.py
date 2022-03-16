

#student = ["John", 75, "Engineering", "awesome", 199, "Hello"]

#student_set = set(student)

#print("student list", student)
#print("student set", student_set)

#del student[0]
#student_set.remove("Engineering")

#student.append("Great")
#student_set.add("Goodbye")
#print(student)
#print(student_set)


this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colours": ["red", "yellow", "blue"]
}

print(this_dict)

print("I have this brand of car", this_dict["brand"])

print(len(this_dict))

print("the colours available are:", this_dict["colours"])

print("the colours are:", this_dict.get("colours"))

print(this_dict.keys())

this_dict["flowers"]=["lily of the valley", "rose", "daisy", "violet"]

print(this_dict)

print(this_dict.values())

val=this_dict.values()

print("my val is", val)

#this_dict["flowers"]="roses are best"

print("but now my val is ", val)

#items
items_dict=this_dict.items()

print("so my items_dict ", items_dict)

this_dict["colours"]="I like many different colours"

print("now my items_dict ", items_dict)

del this_dict ["model"]

#pop
#this_dict.pop("colours")

#print("\n \n my dictionary", this_dict)

#use loops
print("\n \n")
for i in this_dict:
    print("printing i in my dictionary", i)
    print("printing my dictionary[i]", this_dict[i])
