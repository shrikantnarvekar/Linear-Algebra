import math
class Strassen_matrix:
    def __init__(self,a):
        self.matrix=[]
        self.R=[[0 for i in range(a)]for j in range(a)]
        self.A=[[0 for i in range(a)]for j in range(a)]
        self.B=[[0 for i in range(a)]for j in range(a)]

    def create_matrix(self):
        print("Enter value in matrix A")
        for i in range(0,input1):
            for j in range(0,input1):
                self.A[i][j]=int(input("Enter Value for A: "))
        print(self.A)
        print("------------------------------------------")
        print("Enter value in matrix B")
        for i in range(0,input1):
            for j in range(0,input1):
                self.B[i][j]=int(input("Enter Value for B: "))
        print(self.B)

    def mul(self,A,B):
        n=len(self.A)
        if(n==1):
            self.R[0][0]=self.A[0][0]*self.b[0][0]
        else:
            A11=[[0 for i in range(n/2)]for j in range(n/2)]
            A12=[[0 for i in range(n/2)]for j in range(n/2)]
            A21=[[0 for i in range(n/2)]for j in range(n/2)]
            A22=[[0 for i in range(n/2)]for j in range(n/2)]
            B11=[[0 for i in range(n/2)]for j in range(n/2)]
            B12=[[0 for i in range(n/2)]for j in range(n/2)]
            B21=[[0 for i in range(n/2)]for j in range(n/2)]
            B22=[[0 for i in range(n/2)]for j in range(n/2)]

            #DIVIDING MATRIX A INTO 4 HALVES
            self.split(self.A, A11, 0 , 0)
            self.split(self.A, A12, 0 , n/2)
            self.split(self.A, A21, n/2, 0)
            self.split(self.A, A22, n/2, n/2)

            #DIVIDING MATRIX B INTO 4 HALVES
            self.split(self.B, B11, 0 , 0)
            self.split(self.B, B12, 0 , n/2)
            self.split(self.B, B21, n/2, 0)
            self.split(self.B, B22, n/2, n/2)

            M1=self.mul(self.add(A11,A22),self.add(B11,B22))
            M2=self.mul(self.add(A21,A22),B11)
            M3=self.mul(A11,self.sub(B12,B22))
            M4=self.mul(A22,self.sub(B21,B11))
            M5=self.mul(self.add(A11,A12),B22)
            M6=self.mul(self.sub(A21,A11),self.add(B11,B12))
            M7=self.mul(self.sub(A12,A22),self.add(B21,B22))

            C11=self.add(self.sub(self.add(M1,M4),M5),M7)
            C12=self.add(M3,M5)
            C21=self.add(M2,M4)
            C22=self.add(self.sub(self.add(M1,M3),M2),M6)

            self.join(C11,R,0,0)
            self.join(C12,R,0,n/2)
            self.join(C21,R,n/2,0)
            self.join(C22,R,n/2,n/2)
        return R

    def sub(self,A,B):
        n=len(A)
        C=[[0 for i in range(n)]for j in range(n)]
        i=0
        j=0
        while(i<n):
            while(j<n):
                C[i][j]=self.A[i][j]-self.B[i][j]
                i+=1
                j+=1
        return C

    
    def add(self,A,B):
        n=len(A)
        C=[[0 for i in range(n)]for j in range(n)]
        i=0
        j=0
        while(i<n):
            while(j<n):
                C[i][j]=self.A[i][j]+self.B[i][j]
                i+=1
                j+=1
        return C

    def join(self,C,P,iB,jB):
        i1=0
        i2=iB
        j1=0
        j2=jB
        while(i1<len(C)):
            while(j1<len(C)):
                P[i2][j2]=C[i1][j1]
                i1+=1
                i2+=1
                j1+=1
                j2+=1

    def split():
        
    
input1=int(input("Enter value for nXn: "))
s1=Strassen_matrix(input1)
s1.create_matrix()
            

            
