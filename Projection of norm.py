class projection_norm:
              def __init__(self):
                            self.u=[]
                            self.v=[]
              def create_vector(self):
                            input1=int(input("Enter Range of Vector U & V:"))
                            print("Enter value in Vector U:")
                            for i in range(0,input1):
                                          x=int(input("Enter Value for U: "))
                                          self.u.append(x)
                            print(self.u)
                            print("------------------------------------------")
                            print("Enter value in Vector V:")
                            for j in range(0,input1):
                                          y=int(input("Enter Value for V: "))
                                          self.v.append(y)
                            print(self.v) 
                            print("------------------------------------------")

              def UXV(self):
                            sum_UXV=0
                            for i in range(0,len(self.u)):
                                          sum_UXV=sum_UXV+(self.u[i]*self.v[i])
                            print("The value of U X V is ",sum_UXV)
                            return sum_UXV

              def norm_v_sqr(self):
                            mult_v=0
                            for i in range(0,len(self.u)):
                                          mult_v=mult_v+self.v[i]**2
                            print("The value of square norm of V sqr is ",mult_v)
                            return mult_v
              def norm_u_sqr(self):
                            mult_u=0
                            for i in range(0,len(self.u)):
                                          mult_u= mult_u+self.u[i]**2
                            print("The value of square norm of U sqr is ",mult_u)
                            return mult_u
              def final_proj(self):
                            uxv=self .UXV()
                            norm_v=self.norm_v_sqr()
                            norm_u=self.norm_u_sqr()
                            div_u_on_v=uxv/norm_v
                            div_v_on_u=uxv/norm_u
                            for i in range(0,len(self.u)):
                                          proj=div_u_on_v*self.v[i]
                                          print("The projection of U on V on index ",i,"is",proj)
                            print("--------------------------------------------------")
                            for i in range(0,len(self.u)):
                                          proj1=div_v_on_u*self.v[i]
                                          print("The projection of V on U on index ",i,"is",proj)
                                          

pn=projection_norm()
pn.create_vector()
pn.UXV()
pn.norm_v_sqr()
pn.norm_u_sqr()
pn.final_proj()
