import numpy as np

sample_list = [0,1,2,3]
print(type(sample_list))

sample_array = np.array(sample_list)
print(type(sample_array))

error_array = np.array([1,3,'test',8,7])
print(type(error_array))

ones_array = np.ones(20)
print(ones_array)

zeros_array = np.zeros(20)
print(zeros_array)

float_array = np.array([5,7,8,9,6],dtype="f")
print(float_array)
print(np.sort(float_array))

twod_array = np.array([[2,5,6],[7,9,8]])
print(twod_array)
print(twod_array.ndim) #finds out the dimension 
print(twod_array.shape)
print(twod_array.size) # how many elements it contains
print(twod_array.nbytes) # how many memory it takes

num_array = np.arange(1,100)
print(num_array)

even_array = np.arange(1,100,2)
print(even_array)

random_array = np.random.permutation(np.arange(1,10))
print(random_array)

random_number = np.random.randint(1,5)
print(random_number)

random_array2 = np.random.rand(2,3)
print(random_array2)
print(random_array2.shape)

reshaped_array = np.arange(1,10).reshape(3,3)
print(reshaped_array)
print(reshaped_array.shape)

linear_array = np.arange(1,37)
print(linear_array.reshape(6,6))
print(linear_array.reshape(12,3))
print(linear_array.reshape(18,2))


