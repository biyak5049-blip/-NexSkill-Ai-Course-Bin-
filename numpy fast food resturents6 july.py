import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

address, latitude , longitude , name, = np.genfromtxt("FastFoodRestaurants.csv", delimiter=',', usecols=(0, 4, 5, 6), unpack=True, dtype=('U100', 'f8', 'f8', 'U100'),encoding='utf-8',skip_header=1,invalid_raise=False)
print(address)
print(latitude)
print(longitude)
print(name)

cleaned_longitude = longitude[~np.isnan(longitude)]
# Zameen.com price  - statistics operations

print(np.min(latitude))
#using math operation
print("fast food .com longnitude square: ",np.square(longitude))
print("fast food .com longnitude  sqrt: ",np.sqrt(longitude))
print("fast food.com longnitude pow: ",np.power(longitude,longitude))
print("fast food .com longnitude abs: ",np.abs(longitude))
#using statistic operation
print("fast food.com longnitude mean: ", np.mean(longitude))
print("fast food.com longnitude mod: ",np.median(longitude))
print("fast food .com longnitude std: ", np.std(longitude))
print("fast food .com longnitude average: ", np.average(longitude))
print("fast food .com longnitude percentile-30: ",np.percentile(longitude,30))
print("fast food.com longnitude percentile-70: ",np.percentile(longitude,70))
print("fast food.com longnitude max: ",np.max(longitude))



# basic arthimatic operation
addition = latitude +longitude
subtraction= latitude- longitude
multiplication= latitude*longitude
division= latitude/longitude


print("fast food.com lattitude- longnitude-addition: ", addition)
print("fast food .com lattitude-longnitude -subtraction: ", subtraction)
print("fast food .com lattitude- longnitude-multiplication: ", multiplication)
print("fast food.com lattitude - longnitude -division: ",division)

#trignomatric function
latitudepie = (latitude/np.pi)+1
#calculate sine,cosine, tangent 
sine_values= np.sin(latitudepie)
cosine_values= np.cos(latitudepie)
tangent_values= np.tan(latitudepie)

print("fast food.com div-pie-sine_values: ",sine_values)
print("fast food.com div-pie-cosine_values: ",cosine_values)
print("fast food.com div-pie-tangent_values: ",tangent_values)
#calculate the natural logarthm and base 10
log_array= np.log(latitudepie)
log10_array=np.log10(latitudepie)

print("fast food.com div- pie-natural logarithms_values: ",log_array)
print("fast food.com div-pie-base10 logarithms_values: ",log10_array)

#hyperboloc function
sinh_values= np.sinh(latitudepie)
print("fast food.com lattirude- div-pie-hyperbolic sinh_values: ",sinh_values)
cosineh_values=np.cosh(latitudepie)
print("fast food.com lattitude-div-pie-hyperbolic cosineh_values: ",cosineh_values)
tangenth_values= np.tanh(latitudepie)
print("fast food.com lattitude - div-pie-hyperbolic tangenth_values: ",tangenth_values)

#inverse hyperbolic sine,cosine,tangent
asinh_values= np.arcsinh(latitudepie)
print("fast food.com lattitude-div-pie-inverse hyperbolic sine_values: ",asinh_values)

acosh_values= np.arccosh(latitudepie)
print("fast food.com lattitude -div-pie-inverse hyperbolic cosine_values: ",cosineh_values)

#fast food.com Lattitude-longnitude 2D_array
D2lattitudelongitude=np.array([latitude,longitude])
print("fast food.com lattitude plus longnitude -2 dimensional_array: ",D2lattitudelongitude)
print("fast food.com lattitude plus longnitude-2 dimensional_array-dimension: ",D2lattitudelongitude.ndim)
#return total number of elements in array
print("fast food.com lattitude plus longnitude-2 dimensional_array-total number of elements: ", D2lattitudelongitude.size)
print("fast food.com lattitude plus longnitude-2dimensional_array-give size of array in each dimension: ",D2lattitudelongitude.shape)
print("fast food.com lattitued plus longnitude-2dimensional_array-datatype: ",D2lattitudelongitude.dtype)
#slicing array
D2lattitudelongitudeslice= D2lattitudelongitude[0:1:3,1:3:4]
print("fast food.com lattitude plus longnitude-2 dimensional_array - splicing_array-D2lattitudelongnitude[1:,:4]" ,D2lattitudelongitudeslice )
D2lattitudelongitudeslice2= D2lattitudelongitude[:5,5:6:1]
print("fast food.com lattitudeplus longnitude -2 dimensional_array- splicing_array-D2lattitudelongnitude[:5,5:6:1] ", D2lattitudelongitudeslice2)
#indexing array
D2lattitudelongitudesliceitemonly= D2lattitudelongitude[1,2]
print("fast food.com lattitude plus longnitude-2 dimensional_array-index_array-D2lattitudelongnitudeslice[4,5] ",D2lattitudelongitudesliceitemonly)
#bulitin function
for elem in np.nditer(D2lattitudelongitude):
 print(elem)
 #indexes
 for index, elem in np.ndenumerate(D2lattitudelongitude):
  print(index,elem)
#2*5000---->>> 1*10000 =reshape
D2lattitudelongitude1TO10000= np.reshape(D2lattitudelongitude,(1,10000))
print("fast food.com lattitude plus longnitude-2 dimensional_array-np.reshape(D2lattitudelongnitude,(1,10000)): ",D2lattitudelongitude1TO10000 )
print("fast food.com lattitude plus longnitude-2 dimensional_array-np.reshape(D2lattitudelongnitude,(1,10000)): size",D2lattitudelongitude1TO10000.size)
print("fast food.com lattitude plus longnitude-2 dimensional_array-np.reshape(D2lattitudelongnitude,(1,10000)): shape",D2lattitudelongitude1TO10000.shape)
print("fast food.com lattitude plus longnitude-2 dimensional_array-np.reshape(D2lattitudelongnitude,(1,10000)):ndim",D2lattitudelongitude1TO10000.ndim)