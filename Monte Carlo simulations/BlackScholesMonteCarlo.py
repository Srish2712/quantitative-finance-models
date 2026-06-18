import numpy as np
import math
import time
 
class OptionPricing:
    
	def __init__(self,S0,E,T,rf,sigma,iterations):
		self.S0 = S0
		self.E = E
		self.T = T
		self.rf = rf
		self.sigma = sigma     
		self.iterations = iterations 
 
	def call_option_simulation(self):
		
		#we have 2 columns: first with 0s the second column will store the payoff
		option_data = np.zeros([self.iterations, 2])
		
		#dimensions: 1 dimensional array with as many items as the itrations
		rand = np.random.normal(0, 1, [1, self.iterations])
		
		#Equation for the S(t) stock price
		stock_price = self.S0*np.exp(self.T*(self.rf - 0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand)
 
		#Need S-E because we have to calculate the max(S-E,0)
		option_data[:,1] = stock_price - self.E   
        
		#Average for the Monte-Carlo method
		average = np.sum(np.amax(option_data, axis=1))/float(self.iterations)
 
		#Discount factor
		return np.exp(-1.0*self.rf*self.T)*average
		
	def put_option_simulation(self):
	
		option_data = np.zeros([self.iterations, 2])
		
		#dimensions: 1 dimensional array with as many items as the itrations
		rand = np.random.normal(0, 1, [1, self.iterations])
		
		#equation for the S(t) stock price
		stock_price = self.S0*np.exp(self.T*(self.rf - 0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand)
 
		#Need S-E because we have to calculate the max(S-E,0)
		option_data[:,1] = self.E - stock_price  
        
		#Average for the Monte-Carlo method
		average = np.sum(np.amax(option_data, axis=1))/float(self.iterations)
 
		#Discount factor
		return np.exp(-1.0*self.rf*self.T)*average

if __name__ == "__main__":
	
	S0=100					
	E=100					
	T = 1					
	rf = 0.05				#risk-free rate
	sigma=0.2				#volatility of the underlying stock
	iterations = 1000000	#number of iterations in the Monte-Carlo simulation	
	
	model = OptionPricing(S0,E,T,rf,sigma,iterations)
	print("Call option price with Monte-Carlo approach: ", model.call_option_simulation()) 
	print("Put option price with Monte-Carlo approach: ", model.put_option_simulation())
