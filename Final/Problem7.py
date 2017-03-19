def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE 
    def cal_poly(x):
        k = len(L)-1
        result = 0
        for n in L:
            result += n * (x ** k)
#            print("{}*{}^{}={}".format(n,x,k,n*x**k),result)
            k -= 1
        return result
    return cal_poly

a = general_poly([1,2])
print(a(1))
print(a(2))
print(a(3))