import numpy as np
Industry, FundingRound, InvestmentAmount, Valuation= np.genfromtxt('startup_growth_investment_data (1).csv', delimiter=',', usecols=(1, 2, 3, 4), dtype=None, unpack=True, skip_header=1)

print("industry loaded shape: ", Industry.shape)
print("funding round loaded shape: ", FundingRound.shape)
print("investment amount loaded shape: ", InvestmentAmount.shape)
print("valuation loaded shape: ", Valuation.shape)


print(np.min(InvestmentAmount))
#using statistic operation on startup-growth-investment data
print("startup.com investmentamount mean: ", np.mean(InvestmentAmount))
print("startup.com investmentamount average: ", np.average(InvestmentAmount))
print("startup.com investmentamount mod: ", np.median(InvestmentAmount))
print("startup.com investmentamount std: ",np.std(InvestmentAmount))
print("startup.com investmentamount percentile-30: ", np.percentile(InvestmentAmount,30))
print("starup .com investmentamount percentile-70: ", np.percentile(InvestmentAmount,70))

#startup using math operation
print("startup.com investmentamount square: ", np.square(InvestmentAmount))
print("startup.com investmentamount sqrt: ", np.sqrt(InvestmentAmount))
print("startup.com investmentamount pow: ", np.power(InvestmentAmount, InvestmentAmount))
print("startup.com investmentamount abs: ", np.abs(InvestmentAmount))

# BASIC arthimatic operation
addition= InvestmentAmount + Valuation
subtraction = InvestmentAmount - Valuation
multiplication = InvestmentAmount*Valuation
division = InvestmentAmount / Valuation
print("startup.com investmentamount-valuation-addition: ", addition)
print("startup.com investmentamount - valuation-subtraction: ", subtraction)
print("startup.com investmentamount - valuation-multiplication: ", multiplication)
print("startup.com investmentamount - valuation-division: ",division)

# trignometric function
InvestmentAmountpie = (InvestmentAmount/np.pi)+1
# calculate sine , cosine,tangent

sine_values= np.sin(InvestmentAmountpie)
cosine_values= np.cos(InvestmentAmountpie)
tangent_values= np.tan(InvestmentAmountpie)

print("startup.com investmentamount - div - pie- sine_values: ",sine_values)
print("startup.com investmentamount - div - pie-cosine_values: ",cosine_values)
print("startup.com investmentamount - div-pie-tangent_values: ",tangent_values)
print("startup.com investmentamount - div-pie -exponentional_values: ",np.exp(InvestmentAmountpie))
#calculate the natural logarthm and base 10 logarthms
log_array= np.log(InvestmentAmountpie)
log10_array= np.log10(InvestmentAmount)
print("startup.com investmentamount-div-pie-natural logarithms: ", log_array)
print("startup.com investmentamount-div-pie = base10 logarithms: ", log10_array)
#hyperbolic sine
sinh_values= np.sinh(InvestmentAmountpie)
print("startup.com investmentamount - div -pie hyperbolic sine values:", sinh_values)
#hyperbolic cosine values
cosh_values= np.cosh(InvestmentAmountpie)
print("startup.com investmentamount -div-pie hyperbolic cosine values: ",cosh_values)
tanh_values= np.tanh(InvestmentAmountpie)
print("startup.com investmentamount - div-pie-hyperbolic tangent values: ", tanh_values)
#inverse hyperbolic sine
asinh_values= np.arcsinh(InvestmentAmountpie)
print("startup.com investmentamount -div-pie inverse ")