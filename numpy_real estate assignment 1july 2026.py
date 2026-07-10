# RealEstate-USA.csv
import numpy as np

status,price,bed,bath= np.genfromtxt('RealEstate-USA.csv', delimiter =',' , usecols=(1,2,3,4), unpack=True, dtype=None, skip_header=1)
print('Status:',status)
print('Price:',price)
print('Bedrooms:',bed)
print('Bathrooms:',bath)

print("Real Estate.com price average:",np.mean(price))
print("Real Estate.com price minimum:",np.min(price))
print("Real Estate.com price maximum:",np.max(price))
print("Real Estate.com price standard deviation:",np.std(price))    
print("Real Estate.com price variance:",np.var(price))
print("Real Estate.com price median:",np.median(price))
print("Real Estate.com price 25th percentile:",np.percentile(price,25))
print("Real Estate.com price 75th percentile:",np.percentile(price,75))
print("Real Estate.com price 90th percentile:",np.percentile(price,90))


print("Real Estate.com price range:",np.max(price)-np.min(price))
print("Real Estate.com price interquartile range:",np.percentile(price,75)-np.percentile(price,25))
print("Real Estate.com price sum of squares:",np.sum(price**2))
print("Real Estate.com price root mean square:",np.sqrt(np.mean(price**2)))
print("Real Estate.com price coefficient of variation:",np.std(price)/np.mean(price))
print("Real Estate.com price skewness:",(3*(np.mean(price)-np.median(price)))/np.std(price))
print("Real Estate.com price kurtosis:",(np.mean((price-np.mean(price))**4))/(np.std(price)**4)-3)


print("Real Estate.com price correlation coefficient between price and bedrooms:",np.corrcoef(price,bed)[0,1])
print("Real Estate.com price correlation coefficient between price and bathrooms:",np.corrcoef(price,bath)[0,1])        
print("Real Estate.com price correlation coefficient between bedrooms and bathrooms:",np.corrcoef(bed,bath)[0,1])
print("Real Estate.com price covariance between price and bedrooms:",np.cov(price,bed)[0,1])
print("Real Estate.com price covariance between price and bathrooms:",np.cov(price,bath)[0,1])
print("Real Estate.com price covariance between bedrooms and bathrooms:",np.cov(bed,bath)[0,1])
print("Real Estate.com price linear regression between price and bedrooms:",np.polyfit(bed,price,1))
print("Real Estate.com price linear regression between price and bathrooms:",np.polyfit(bath,price,1))

print("real estate .com bed-bath-addittion:", np.add(bed,bath))
print("real estate .com bed-bath-subtraction:", np.subtract(bed,bath))
print("real estate .com bed-bath-multiplication:", np.multiply(bed,bath))
print("real estate .com bed-bath-division:", np.divide(bed,bath))

pricepi = (price/np.pi) + 1
#trignomatic functions
sin_price = np.sin(pricepi)
cos_price = np.cos(pricepi)
tan_price = np.tan(pricepi)
print("real estate.com -div-pi sine values:", sin_price)
print("real estate.com -div-pi cosine values:", cos_price)
print("real estate.com -div-pi tangent values:", tan_price)
print("real esstate .com-div-pi-exponential values:", np.exp(pricepi))


#calculate the logarthms and base 10 logarthms of the price values
log_price = np.log(pricepi)
log10_price = np.log10(pricepi) 
print("real estate .com-div-pi-logarithm values:", log_price)
print("real estate .com-div-pi-logarithm base 10 values:", log10_price)     

#example hyperbolic sine
sinh_values = np.sinh(pricepi)
print("real estate .com-div-pi-hyperbolic sine values:", sinh_values)
#example hyperbolic cosine
cosh_values = np.cosh(pricepi)  
print("real estate .com-div-pi-hyperbolic cosine values:", cosh_values)
#example hyperbolic tangent
tanh_values = np.tanh(pricepi)  
print("real estate .com-div-pi-hyperbolic tangent values:", tanh_values)
# convert hyperbolic cosine
asinh_values = np.arcsinh(pricepi)
print("real estate .com-div-pi-inverse hyperbolic sine values:", asinh_values)
#example inverse hyperbolic cosine
acosh_values = np.arccosh(pricepi)
print("real estate .com-div-pi-inverse hyperbolic cosine values:", acosh_values)
#example inverse hyperbolic tangent
atanh_values = np.arctanh(pricepi)
print("real estate .com-div-pi-inverse hyperbolic tangent values:", atanh_values)
#real estate.com bed+bath-2 dimensional array
bed_bath_array = np.array([bed, bath])
print("real estate .com bed+bath-2 dimensional array:", bed_bath_array)
#check array 1
print("real estate .com bed+bath-2 dimensional array - dimenstion:",bed_bath_array.ndim)
#return total no of elements in the array
print("real estate .com bed+bath-2 dimensional array - size:",bed_bath_array.size)
#return tuple that gives array shape
print("real estate .com bed+bath-2 dimensional array - shape:",bed_bath_array.shape)
#check data type of array
print("real estate .com bed+bath-2 dimensional array - data type:",bed_bath_array.dtype)
#splicing the array
print("real estate .com bed+bath-2 dimensional array - splicing:",bed_bath_array[0:2,0:5])
#indexing the array
print("real estate .com bed+bath-2 dimensional array - indexing:",bed_bath_array[0,0:5])    
#you should use the bulitan fuction nditer if you donot need to index value
for element in np.nditer(bed_bath_array):
    print("real estate .com bed+bath-2 dimensional array - nditer:",element)
    # you n eed a indexed value to change the value of the ar
    for index, element in np.ndenumerate(bed_bath_array):
        print("real estate .com bed+bath-2 dimensional array - ndenumerate:",index,element)     
        ""#for loop to change the value of the array
rows= np.shape(bed_bath_array[0])[0]
cols= np.shape(bed_bath_array[0])
        
