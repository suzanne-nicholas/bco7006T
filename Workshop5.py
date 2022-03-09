is_done = False

while not is_done:
    marks = int(input("Enter your marks: "))
    if marks >= 0 and marks <= 100:
        is_done = True
    else:
        print("Error: your marks should be between 0 and 100.")
print("Your mark is", marks)
