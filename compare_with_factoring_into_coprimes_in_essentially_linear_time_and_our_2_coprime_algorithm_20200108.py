#This is a code for my paper “Efficient Dedicated Algorithms for CRT and GCRT on Devices with Limited Computing Power”


reset()






#Function: compute the length of list List
def listSize(List):
#    print("-------List = ",List)
    if List == []:
        return 0
    return vector(List).length()
    

"""
#-----------------test---for---listSize--------
tmpList = [1,2,3,4,5,6,7]
tmpListLength = listSize(tmpList)
print("tmpListLength = ",tmpListLength)
#-----------------test---for---listSize--------
"""




##Function: compute the value of the expression  a^(2^n)
def Alg_10_1(a,n):
    if n == 0:
        return a
    for i in range(n):
        a= a**2
    return a
    
"""
#-----------------test---for---Alg_10_1--------
a = 10
n = 5
tmp = Alg_10_1(a,n)
print("tmp = ",tmp)
#-----------------test---for---Alg_10_1--------
"""



##Function: compute the value of gcd(a,c), ppi(a,c), ppo(a,c)
#ppi(a,c) 输出a的因子幂次，且这个因子在c中出现过
#ppo(a,c) 输出a的因子幂次，且这个因子在c中没有出现过
def Alg_11_3(a,c):
    x0 = gcd(a,c)
    x = x0
    y = a/x
    while 1:
        g = gcd(x,y)
        if g == 1:
            return [x0,x,y]
        x = x*g
        y = y / g

"""
#-----------------test---for---Alg_11_3--------
a = 190
c = 15
tmp = Alg_11_3(a,c)
print("tmp = ",tmp)
#-----------------test---for---Alg_11_3--------
"""

##Function: compute the value of gcd(a,b), ppg(a,b), pple(a,b)
#ppg(a,b) 输出a的因子幂次，且这个因子在a中的幂次 >b 中的幂次
#pple(a,b) 输出a的因子幂次，且这个因子在a中的幂次 <= b中的幂次
def Alg_11_4(a,b):
    y0 = gcd(a,b)
    y = y0
    x = a/y
    while 1:
        g = gcd(x,y)
        if g == 1:
            return [y0,x,y]
        x = x*g
        y = y/g
    
"""
#-----------------test---for---Alg_11_4--------
a = 125
b = 15
tmp = Alg_11_4(a,b)
print("tmp = ",tmp)
#-----------------test---for---Alg_11_4--------
"""




def Alg_13_2_coprimeBasis(a,b,coprimeBasis):
    if b == 1:
        if a != 1:
            coprimeBasis.append(a) 
        return
    [_,a,r] = Alg_11_3(a,b)
    if r!=1:
        coprimeBasis.append(r)
#        print("r = ",r)
    (g,h,c) = Alg_11_4(a,b)
    c0 = c
    x = c0
    n = 1
    while 1:
        (g,h,c) = Alg_11_4(h,g**2)
        d = gcd(c,b)
        x = x*d
        y = Alg_10_1(d,n-1)
        Alg_13_2_coprimeBasis(c/y,d,coprimeBasis)
        if h != 1:
            n = n + 1
        else:
            break
    Alg_13_2_coprimeBasis(b/x,c0,coprimeBasis)



def Alg_13_2(a,b):
    coprimeBasis = []
    Alg_13_2_coprimeBasis(a,b,coprimeBasis)
    return coprimeBasis


"""
#-----------------test---for---Alg_13_2--------
a = randint(1,2000000)
b = randint(1,2000000)
print("a = ",a, " = ", factor(a))
print("b = ",b," = ",factor(b))
tmpCoprimeBasis = Alg_13_2(a,b)
print("tmpCoprimeBasis = ",tmpCoprimeBasis)
#-----------------test---for---Alg_13_2--------
"""



def Alg_14_1(ListS):
    if ListS == []:
        return 1
#    print("11111111111111111111111111111111")
    if listSize(ListS) == 1:
        a = ListS[0]
        return a
#    print("2222222222222222222222222222222")
    index = listSize(ListS) >> 1
    X = Alg_14_1(ListS[:index])
    Y = Alg_14_1(ListS[index:])
    return X*Y
    
    
"""    
#-----------------test---for---Alg_14_1--------
tmpListS = [1,2,3,4,5,6,7,8,9,10]
tmp = Alg_14_1(tmpListS)
print("tmp = ",tmp)
#-----------------test---for---Alg_13_2--------
"""




#输出的是a在互素基coprimeBasis上的分解
#用法：直接调用函数，最后的结果存储在变量splitList中，不是返回结果中
def Alg_15_3_Split(a, coprimeBasis,splitList):
    if coprimeBasis == []:
        return 
    [_,b,_] = Alg_11_3(a,Alg_14_1(coprimeBasis))
    if listSize(coprimeBasis) == 1:
        p = coprimeBasis[0]
#        print (p,b)
        splitList.append((p,b))
        return 
#    print("3333333333333333333333333333333")
    index = listSize(coprimeBasis) >> 1
    Alg_15_3_Split(b,coprimeBasis[:index],splitList)
    Alg_15_3_Split(b,coprimeBasis[index:],splitList)


def Alg_15_3(a, coprimeBasis):
    splitList = []
    a = a
    coprimeBasis = coprimeBasis
    Alg_15_3_Split(a, coprimeBasis,splitList)
    return splitList
    
    



"""
#-----------------test---for---Alg_15_3--------
tmpCoprimeBasis = [4,9,5,7,11]
a = 256*81*25*13*17
print("tmpCoprimeBasis = ",tmpCoprimeBasis)
print("a = ",a)
tmpsplitList = Alg_15_3(a,tmpCoprimeBasis)
print("tmpsplitList = ",tmpsplitList)
#-----------------test---for---Alg_15_3--------
"""





def Alg_16_2(coprimeBasis,b):
    UnionCoprimeBasis = []
    if coprimeBasis == []:
        if b != 1: 
            UnionCoprimeBasis.append(b)
        return UnionCoprimeBasis
    x = Alg_14_1(coprimeBasis)
    [_,a,r] = Alg_11_3(b,x)
    if r != 1:
        UnionCoprimeBasis.append(r)
    S = Alg_15_3(a,coprimeBasis)
    for p_c in S:
        t = Alg_13_2(p_c[0],p_c[1])
        UnionCoprimeBasis = UnionCoprimeBasis + t
    return UnionCoprimeBasis



"""
#-----------------test---for---Alg_16_2--------
coprimeBasis = [4,9*25,7,11,13,17]
b = randint(1,500)
b = 16*81*3*25*13*19*5*23*29
print("coprimeBasis = ",coprimeBasis)
print("b = ",b)
tmpUnionCoprimeBasis = Alg_16_2(coprimeBasis,b)
print("tmpUnionCoprimeBasis = ",tmpUnionCoprimeBasis)
#-----------------test---for---Alg_16_2--------
"""







def Alg_17_3(coprimeBasisP,coprimeBasisQ):
    QBit_ik0 = []
    QBit_ik1 = []
#    print("4444444444444444444444444444")
#    print("coprimeBasisQ = ",coprimeBasisQ)
    n = listSize(coprimeBasisQ)
    if n < 2:
        nn = 2
    else:
        nn = n
    b = ceil(log(nn,2))
    if b<1 :
        b = 1
    S = coprimeBasisP
    i = 0
    while 1:
#        print("i = ",i)
        if i == b:
#            print("S = ",S)
            return S
        for k in range(n):
            if (k >> i) % 2 == 0:
                QBit_ik0.append(coprimeBasisQ[k])
        x = Alg_14_1(QBit_ik0)
        T = Alg_16_2(S,x)
        for k in range(n):
            if (k >> i) % 2 == 1:
                QBit_ik1.append(coprimeBasisQ[k])
        x = Alg_14_1(QBit_ik1)
        S = Alg_16_2(T,x)
        i = i + 1
    return S

"""
#-----------------test---for---Alg_17_3--------
coprimeBasisP = [16,9,125,49,11,169,17,19,23]
coprimeBasisQ = [8,81,25,49,11,169,29,31]
tmpS = Alg_17_3(coprimeBasisP,coprimeBasisQ)
print("coprimeBasisP = ",coprimeBasisP)
print("coprimeBasisQ = ",coprimeBasisQ)
print("tmpS = ",tmpS)
#-----------------test---for---Alg_17_3--------
"""





def Alg_18_1(S):
    coprimeBasisS = []
    if S == []:
        return coprimeBasisS
    if listSize(S) == 1:
        a = S[0]
        if a != 1:
            coprimeBasisS.append(a)
#            print("coprimeBasisS = ",coprimeBasisS)
        return coprimeBasisS
#    print("S = ",S)
    index = listSize(S) >> 1
    T = S[:index]
    P = Alg_18_1(T)
    Q = Alg_18_1(S[index:])
    tmpBasis = Alg_17_3(P,Q)
#    print("tmpBasis = ",tmpBasis)
#    print("tmpBasis = ",tmpBasis)
    coprimeBasisS = coprimeBasisS + tmpBasis
#    print("coprimeBasisS = ",coprimeBasisS)
    return coprimeBasisS





"""
#-----------------test---for---Alg_18_1--------
S = [15,25,45,123,224,235,46,76]
coprimeBasisS = Alg_18_1(S)
print("S             = ",S)
print("coprimeBasisS = ",coprimeBasisS)
#-----------------test---for---Alg_18_1--------
"""








def Alg_19_2(p,a):
    p = ZZ(p)
    a = ZZ(a)
    if not(p.divides(a)):
        return [0,a]
    [j,b] = Alg_19_2(p**2,a/p)
    if p.divides(b):
        return [2*j+2,b/p]
    return [2*j+1,b]


"""
#-----------------test---for---Alg_19_2--------
p = ZZ(7)
a = ZZ(49*14*49*34)
tmp = Alg_19_2(p,a)
print("tmp = ",tmp)
#-----------------test---for---Alg_19_2--------

"""









def Alg_20_1_factorization(a,coprimeBasis,factorizationList):
    if coprimeBasis == []:
        if a!=1:
            print("Failure!!!!!!!!")
        return False
    if listSize(coprimeBasis) == 1:
        p = coprimeBasis[0]
        (n,c) = Alg_19_2(p,a)
        if c != 1:
            print("Failure!!!!")
            return False
        else:
#            print([p,n])
            factorizationList.append([p,n])
            return True
    index = listSize(coprimeBasis)>>1
    y = Alg_14_1(coprimeBasis[:index])
    [_,b,c] = Alg_11_3(a,y)
    tmp = Alg_20_1_factorization(b,coprimeBasis[:index],factorizationList)
    if tmp == False:
        print("Failure!!!!!!")
        return False
    Alg_20_1_factorization(c,coprimeBasis[index:],factorizationList)
    if tmp == False:
        print("Failure!!!!!!")
        return False
    
    


def Alg_20_1(a,coprimeBasis):
    factorizationList = []
    Alg_20_1_factorization(a,coprimeBasis,factorizationList)
    return factorizationList



"""
#-----------------test---for---Alg_20_1--------
a = 8*9*125*8*16
coprimeBasis = [4,9,5,7,11,13,17]
tmp = Alg_20_1(a,coprimeBasis)
print("tmp = ",tmp)

#-----------------test---for---Alg_20_1--------
"""






def Alg_21_2_factorization(S,coprimeBasis,factorizationList):
    Q = []
    if S == []:
        return 
    x = Alg_14_1(coprimeBasis)
    y = Alg_14_1(S)
    [_,z,_] = Alg_11_3(x,y)
    D = Alg_15_3(z,coprimeBasis)
#    print("D = ",D)
    for p in coprimeBasis:
        if (p,p) in D:
            Q.append(p)
    #------lack-----
    if listSize(S) == 1:
        tmp = Alg_20_1(y,Q)
        factorizationList.append(tmp)
        if tmp == False:
            print("Failure!!!!!!")
        return
    index = listSize(S)>>1
    Alg_21_2_factorization(S[:index],Q,factorizationList)
    Alg_21_2_factorization(S[index:],Q,factorizationList)




def Alg_21_2(S,coprimeBasis):
    factorizationList = []
    Alg_21_2_factorization(S,coprimeBasis,factorizationList)
    return factorizationList



#-----------------test---for---Alg_21_2--------
S = [16*9,27*4,225*3,49,121]
coprimeBasis = [4,3,5,7,11,13,17,19]
tmp = Alg_21_2(S,coprimeBasis)
#print("tmp = ",tmp)
#-----------------test---for---Alg_21_2--------



#---------------The above is the implementation of Bernstein's algorithm-------------------------




















#  Algorithm 1 of Xu wang et al.
def generate_coprime_numbers(mlistPrime):
	l = 1
	mlist = []
	size_of_mlistPrime = len(mlistPrime)
	for i in range(size_of_mlistPrime):
		t = gcd(l , mlistPrime[i])
		while gcd(t , mlistPrime[i]) != 1:
			t = t**2
			mlistPrime[i] = mlistPrime[i] / gcd(t,mlistPrime[i])
		mlist.append(mlistPrime[i])
		l = l * mlist[i]
	return mlist





#  Algorithm 2 of Xu wang et al.
def composite_to_prime(mlistPrime):
	'''
	功能：将CRT中不互素的模数modular转化为互素的模数modular
	Input：the modular vector of the CRT，the modulars are composites
	Output:the coprime modulars ,the order is the same as the Input vector
	size_of_mlist : represents the number of the modulars
	处理策略：先求所有模数的lcm，1) 只保留完全属于自己的部分， 2）然后逐个除去模数中多余的部分
	'''
	M = lcm(mlistPrime)
	l = M
	mlist = []
	size_of_mlist = len(mlistPrime)
	for i in range(size_of_mlist):
		mlistPrime[i] = gcd(mlistPrime[i],l)
		t = gcd(mlistPrime[i], l/mlistPrime[i] )
		while gcd(t , mlistPrime[i]) != 1:
			t = t**2
			mlistPrime[i] = mlistPrime[i]/gcd(t , mlistPrime[i])
		mlist.append(mlistPrime[i])
		l = l / mlist[i]
	return mlist 







#the test set with 
numberOfElements = 10000
rangeOfElement = 1000000000 #This is the range of input set elements
s = [randint(1,rangeOfElement) for i in range(numberOfElements)]

for i in range(1,100):
    index = 10**i
    if index > listSize(s):
        break
    tmpSet = s[:index]
    












































































































































