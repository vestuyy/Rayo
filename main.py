print("Enter number")
N = int(input())
A = []
i = 0
max = 1
min = 1
for i in range(N):
    print("Enter your number is list")
    c = int(input())
    A.append(c)
for i in range(N):
    if(A[i] > min):
        min = A[i]
    elif(A[i] < max):
        max = A[i]
print("max number in list is", max,"; min number in list is", min, "; Here is the list ", A)

print("                **    **  ********  **        **            **      ")
print("               **    **  ********  **        **         **     **   ")
print("              ********  **        **        **         **      **  ")
print("             ********  ********  **        **         **      **  ")
print("            **    **  **        **        **         **      **  ")
print("           **    **  ********  ********  ********    **    **   ")
print("          **    **  ********  ********  ********       **      ")


