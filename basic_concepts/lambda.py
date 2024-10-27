#A lambda function can take any number of arguments but can only have one expression.
#lambda arguments : expression

myFn = lambda a: a + 10

x = myFn(45)

print(x)


multiplyFn = lambda a, b: a * b
result = multiplyFn(5, 5)
print(result)


sum = lambda a, b, c: a + b + c
res = sum(5, 5, 5)
print(res)


#The power of lambda is beter shown when you use them as an anonymous function inside another function
#.................... Example with a regular anonymous function
def myFunc(n):
    def multiFn(a):
        return a * n
    return multiFn

# multi(a=?): return a + 5 = myFunc(5) #in multiFn returned the n is alrready set to 5 and we just need to pass the valus 4 to set the a
myFunc_return_multiFn = myFunc(5) #in multiFn returned the n is alrready set to 5 and we just need to pass the valus 4 to set the a
multiFn_res = myFunc_return_multiFn(4)
print(multiFn_res)

#.................... Example with a lambda function
def func1 (n):
    return lambda a: a * n

#lambda (a=?) : return a * 5
fun_lambda_host = func1(5)
lambda_res = fun_lambda_host(4)
print(lambda_res)


    
# print(myFunc(4))
# myDoubler = myFunc(3)