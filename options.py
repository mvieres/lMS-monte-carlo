import numpy as np


class European():
    def __init__(self,n,N,K,Assetprice,t):
        """Initialize European Option Class. 
        Goal: Summarize all common European Options within one class for better calling / comparing.

        Args:
            n (Int): Number of time grid points
            N (Int): Number of samples
            K (float): Strike Price (K>0)
            Assetprice (Array): Matrix of Asset prices (axis = 1), Different samples in each row (axis = 0)
            t (Array): time grid
        """
        self.K = K
        self.N = N
        self.n = n
        self.S = Assetprice
        self.t = t
    
    def Arithmetic_asian_call(self,discounted):
        """Computes an European Arithmetic asian Call given the underlying asset S and strike price K

        Returns:
            Vector / Array: Value of the option
        """
        Value = np.zeros(shape = (self.N,))           
        if discounted == True:
            for j in range(self.N):
                Value[j] = np.exp(-self.r*(self.t[-1] -self.t[0]))*np.max((1/self.n)* np.sum(self.S[j,:]) - self.K , 0) 
        else:
            for j in range(self.N):
                Value[j] = np.max((1/self.n)* np.sum(self.S[j,:]) - self.K , 0) 
        return Value
    
    def Call(self,discounted):
        """Computes Standard European Call Option Value at Maturity T for each Sample path (N paths in total).

        Returns:
            Array: Value for each sample path
        """
        Value = np.zeros(shape = (self.N,))

        if discounted == True:
            for j in range(self.N):
                Value[j] = np.exp(-self.r*(self.t[-1] -self.t[0]))*np.max(0, self.S[j,-1] - self.K)
        else:
            for j in range(self.N):
                Value[j] = np.max(0, self.S[j,-1] - self.K)
        return Value

    
    def Put_theory(self,r,sigma):
        pass
        
    def Put(self,discounted):
        """Computes Standard European Put Option Value at Maturity T for each Sample path (N paths in total).

        Returns:
            Array: Value for each sample path
        """
        Value = np.zeros(shape = (self.N,))
        if discounted == True:
            for j in range(self.N):
                Value[j] = np.exp(-self.r*(self.t[-1] -self.t[0]))*np.max(0,  self.K - self.S[j,-1])
        else:
            for j in range(self.N):
                Value[j] = np.max(0,  self.K - self.S[j,-1])
        return Value
    
    def geo_asian_call(self,discounted):
        """Computes an European geometric asian call given the underlying asset S and strike price K

        Returns:
            Array: Value of option
        """
        Value = np.zeros(shape=(self.N,))

        if discounted == True:
            for j in range(self.N):
                Value[j] = np.exp(-self.r*(self.t[-1] - self.t[0]))*np.max(0, (np.prod(self.S)**(1/self.n)) - self.K) 
        else:
            for j in range(self.N):
                Value[j] = np.max(0, (np.prod(self.S)**(1/self.n)) - self.K) 
        return Value
    
    
    
    
    
class value_fun_t_x():
    def __init__(self,t,x):
        self.t = t
        self.x = x
        self.dim = len(x)
    
    def Call(self,K):
        Value = np.zeros(shape=(self.dim,))
        for j in range(self.dim):
            Value[j] = np.maximum(0, self.x[j] - K)
        return Value
    
    def Put(self,K):
        Value = np.zeros(shape=(self.dim,))
        for j in range(self.dim):
            Value[j] = np.maximum(0, K - self.x[j])
        return Value

class value_fun_x():
    """Single input value only!!!!!
    """
    def __init__(self) -> None:
        pass
    
    def Call(self,x,K):   
        return np.maximum(0, x - K)
    
    def Put(self,x,K):
        len_x = len(x)
        Value = np.zeros(shape=(len_x,))
        for j in range(len_x):
            Value[j] = np.maximum(0, K - x[j])
        return Value