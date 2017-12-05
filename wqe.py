import matplotlib.pyplot as plt
import  numpy as npfrom scipy 
import optimizedata= np.loadtxt(open("C:/Users/xhs/Desktop/123/kb.csv","rb"),delimiter=",",skiprows=0)
datax = data[:,0]
datay = data[:,1]
n=20
conversion=0.1
GENERATION_COST1=0.03
GENERATION_COST2=0.0860
penalty=5
Y=np.zeros(n)
Y0=np.zeros(n)
Y1=np.zeros(n)
Y2=np.zeros(n)
COST=np.zeros(n)
for i in range(n):
  GENERATION_COST1 = GENERATION_COST1+0.003
  def mon(x3):
    M = x3 * datax * conversion
    return M
    def cf(A, x1):
      M = (datay * 1000 - A - x1) * GENERATION_COST2
      for i in range(8760):
        if M[i] < 0:
          M[i] = 0
          return M
    def R_cf(A, x1, x2):
      M = (datay * 1000 - A - x1 - x2) * (penalty - GENERATION_COST2)
      for i in range(8760):
        if M[i] < 0:
          M[i] = 0
          return M
      def IC(x1):
        M = x1 * GENERATION_COST1
        return M
      
      def f(x):
        A =mon(x[2])
        Y1 =cf(A, x[0])
        Y2 =R_cf(A, x[0], x[1])
        Y3 =IC(x[0])
        cost = 0
        for i in range(8760):
          cost = cost + Y1[i] + Y2[i] + Y3
          cost = cost + x[0] * 150 + 2.5 * x[1] + x[2] * 50
          return cost
      result = optimize.fmin_l_bfgs_b(f, np.array([1, 1, 1]), approx_grad=1,bounds=((0, 10000000), (0, 100000000), (0, 10000000)))
      X = result[0]
      COST = result[1]
      Y0[i]=X[0]
      Y1[i]=X[1]
      Y2[i]=X[2]
      Y[i]=X[2]/X[1]
plt.plot(range(n), COST,'g')
plt.plot(range(n), Y0,'b')
plt.plot(range(n), Y2,'r')
plt.plot(range(n), Y1,'y')
plt.show
