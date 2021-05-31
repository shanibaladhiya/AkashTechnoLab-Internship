def name():
    print("My name is Shani")


def hello(arg):
    print(f"Given argument is {arg}")


def addition(a, b):
    return f"Sum using return : a = {a}, b={b} and sum = {a+b}"


def default(a=10, b=20):
    return a+b


def key_args(a, b):
    return a-b


def var_length(*num):
    obj=[]
    for i in num:
        obj.append(i)
    return obj


def var_length_k(**keyargs):
    dict = {}
    for key, val in keyargs.items():
        dict[key] = val
    return dict


print("----simple function----")
name()

print("----function with arguments----")
hello("Hello World")

print("----function with return----")
print(addition(5, 10),"\n")

print("----topic: types of argumnts----\n")

print("---Default arguments---")
print("default() :", default())
print("default(4,5) :", default(4, 5))

print("---Keyword arguments---")
print("keyargs(a=10,b=20)", key_args(a=10, b=20))
print("keyargs(b=10,a=20)", key_args(b=10, a=20))

print("---Var-length(non-keyword) arguments---")
print("varlength(10,20) : ", var_length(10, 20))
print("varlength(10,20,30) : ", var_length(10, 20, 30))
print("varlength(10,20,30,40) : ", var_length(10, 20, 30, 40))

print("---Var-length(keyword) arguments---")
print('varlengthk(car="BMW", price=4500000) :::', var_length_k(car="BMW", price=2500000))
print('varlengthk(car="BMW", price=4500000, country="india") :::', var_length_k(car="BMW", price=2500000, country="india"))



