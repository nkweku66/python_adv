#x = int(input("Type a number: ")
#initial code
numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
def is_even(x):
#numbers = [1, 56,234,87,4,76,24,69,90,135]
#x = int(input("Type a number: "))
    if  not x % 2:
        return False
    else:
        return True
call = (lambda x : False if not x % 2 else True)
ans = filter(call, numbers)

print(list(ans))
#numbers = [1,56,234,87,4,76,24,69,90,135]
#is_even = (lambda x: f"{x} is even" if x % 2==0 else f"")
