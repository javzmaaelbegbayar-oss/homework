def F(A,K,L):
    return A*(K**0.3)*(L**0.7)
c=1.0
while c<=10.0:
    A=K=L=round(c,1)
    result=F(A,K,L)
    print(f"A={A}, K={K}, L={L} => F={round(result,2)}")
    c+=0.1