def main():
    x = int(input("what is x?:"))
    if  is_even(x):
        print("even")
    else:
        print("ood")

def is_even(num):
     return num % 2 == 0 
main ()