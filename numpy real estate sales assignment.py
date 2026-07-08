import numpy as np
serialnumber,listyear, assessedvalue,saleamount= np.genfromtxt("Real_Estate_Sales_2001-2022_GL-Short.csv", delimiter=",", usecols=(0,1,5,6), unpack=True, dtype= None,skip_header=1, encoding='utf-8',invalid_raise=False)

print(serialnumber)
print(listyear)
print(assessedvalue)
print(saleamount)
#statistic operation
print("real estate.com saleamount-mean: ",np.mean(saleamount))
print("real estate.com saleamount-mod: ",np.median(saleamount))
print("real estate.com saleamount-str: ",np.std(saleamount))
print("real estate.com saleamount-average: ",np.average(saleamount))
print("real estate.com saleamount-percentile-30: ",np.percentile(saleamount,30))
print("real estate.com saleamount-min: ",np.min(saleamount))
print("real estate.com saleamount-max: ",np.max(saleamount))
#mathematics operations
print("real estate.com saleamount-square: ",np.square(saleamount))
print("real estate.com saleamount-sqrt: ",np.sqrt(saleamount))
print("real estate.com saleamount-pow: ", np.power(saleamount,saleamount))
print("real estate.com saleamount-abs: ",np.abs(saleamount))
# Perform basic arithmetic operations
addition = listyear+ saleamount
subtraction = listyear - saleamount
multiplication = listyear * saleamount
division = listyear / saleamount
print("real state.com listyear-saleamount-addition: ", addition)
print("real state.com listyear-saleamount-subtraction: ", subtraction)
print("real state.com listyear-saleamount-multiplication: ", multiplication)
print("real state.com listyear-saleamount-division: ", division)

#Trigonometric Functions
saleamountPie = (saleamount/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(saleamountPie)
cosine_values = np.cos(saleamountPie)
tangent_values = np.tan(saleamountPie)
print("real estate.com saleamount -div-pie-sine_values ", sine_values)

print("real estate.com saleamount -div-pie-cosine_values ", cosine_values)
print("real estate.com saleamount -div-pie-tangent_values ", tangent_values)
 #Calculate the natural logarithm and base-10 logarithm
log_array = np.log(saleamountPie)
log10_array = np.log10(saleamountPie)

print("real estate.com saleamount - div - pie  - Natural logarithm values:", log_array)
print("real estate.com saleamount - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(saleamountPie)
print("real estate.com saleamount- div - pie   - Hyperbolic Sine values:", sinh_values)



#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(saleamountPie)
print("real estae.com saleamount - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(saleamountPie)
print("real estate.com saleamount - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(saleamountPie)
print("real estate.com saleamount - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(saleamountPie)
print("real estate.com saleamount - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#Zameen.com Long Plus Lat - 2 dimentional arrary
D2LongLat = np.array([serialnumber,
                  saleamount])

print ("real estate.com serialnumberPlus saleamount - 2 dimentional arrary - " ,D2LongLat)

# check the dimension of array1
print("real estate.com serial number Plus saleamount - 2 dimentional arrary - dimension" , D2LongLat.ndim) 
# Output: 2

# return total number of elements in array1
print("real estate.com serial number  Plus saleamount - 2 dimentional arrary - total number of elements" ,D2LongLat.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("real estate.com serialnumber Plus saleamount - 2 dimentional arrary - gives size of array in each dimension" ,D2LongLat.shape)
# Output: (2,3)

# check the data type of array1
print("real estate.com serialnumber Plus saleamount - 2 dimentional arrary - data type" ,D2LongLat.dtype) 
# Output: int64

# Splicing array 
D2serialnumbersaleamountSlice=  D2LongLat[0:1:1 , 1:5:1]
print("real estate.com serial number Plus saleamount - 2 dimentional arrary - Splicing array - D2LongLat[:1,:5] " , D2serialnumbersaleamountSlice)
D2serialnumbersaleamountSlice2=  D2LongLat[:1, 4:15:4]
print("real estate.com serialnumber Plus saleamount - 2 dimentional arrary - Splicing array - D2LongLat[:1, 4:15:4] " , D2serialnumbersaleamountSlice2)



# Indexing array
D2serialnumbersaleamountSliceItemOnly=  D2serialnumbersaleamountSlice[0,1]
print("real estate.com serialnumber plus saleamount - 2 dimentional arrary - Index array - D2LongLatSlice[1,5] " , D2serialnumbersaleamountSliceItemOnly)
D2serialnumbersaleamountSlice2ItemOnly=  D2serialnumbersaleamountSlice2[0, 2]
print("real estate.com serialnumber plussaleamount - 2 dimentional arrary - index array - D2LongLatSlice2[0, 2] " , D2serialnumbersaleamountSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2serialnumbersaleamountSlice):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2serialnumbersaleamountSlice):
    print(index, elem)
#2*142----->>> 1*284 reshape
D2serialnumbersaleamount1TO284= np.reshape (D2serialnumbersaleamount,(1,284))
print("real estate.com serialnumber plus saleamount-2 dimentional arrary - np.reshape(D2serialnumbersaleamount, (1,284)): ", D2serialnumbersaleamount1TO284)

