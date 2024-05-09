# _________________Print “Hello” in vertical order using a nested loop._______________

# for i in range(2):
#   for j in range(3):
#     print("Hello");
 
# for i in range(2):
#     bag=""
#     for j in range(3):
#         bag+="hello"+" "
#     print(bag);    

for _ in range(5):
    for i in range(5, 0, -1):
        print(i, end="")
    print()

    for i in range(1, 6):
     for j in range(1, i + 1): 
        print(j, end=" ") 
    print() 