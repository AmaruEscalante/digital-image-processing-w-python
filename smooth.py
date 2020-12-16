# This program applies a smoothing filter to the image
import numpy as np

inputFile = open("Girl.pgm", "r")
counter = 0

outputFile = open("GirlSmooth.pgm", "w")

k = 11 # Kernel size
# kernel = np.ones[k,k]

# Create output matrix
img = []
shape = []
for line in inputFile:
    if counter < 3:  # copy the image header

        if counter == 1: # store the shape
            shape = [int(s) for s in line.split() if s.isdigit()]
        outputFile.writelines(line)
        counter += 1
    else:
        break
        #img.append(int(line))

counter = 0

w, h = shape[0], shape[1]
img = [[0 for x in range(w)] for y in range(h)]

counter_i = 0
counter_j = 0
for line in inputFile:
    if counter < 3:
        counter += 1
        continue
    else:
        #outputFile.writelines(line)
        img[counter_j][counter_i] = int(line)
        counter_i += 1
        if counter_i == shape[0]:
            counter_i = 0
            counter_j += 1
        #if counter_j == shape[1]:




print(shape)

# Define the shape of the padded matrix
# The new shape is calculated as follows:
#
# Given an I with shape [row,col] and a Kernel of K
# The padded matrix is [row+(K-1/2), col+(K-1)/2]

for i in range(len(shape)):
    shape[i] += ((k-1)//2)**2
print(shape)

extra = (k-1)//2

# Initialize the matrix
w2, h2 = shape[0], shape[1]
matrix = [[0 for x in range(w2)] for y in range(h2)]

for j in range(h):
    for i in range(w):
        matrix[j+(k-1)//2][i+(k-1)//2] = img[j][i]


# val = [[matrix[m+2][k+2] for m in range(-extra, extra+1)] for k in range(-extra,extra+1)]
# prom = [sum(list) for list in val]
# prom = sum(prom)//(k*k)

smooth = [[0 for x in range(w)] for y in range(h)]


for j in range(h):
   for i in range(w):
        # print(str(i) + " " + str(j))
        val = [[matrix[j + m + extra][i + k + extra] for m in range(-extra, extra + 1)] for k in range(-extra, extra + 1)]
        prom = [sum(list) for list in val]
        prom = sum(prom) // (k * k)
        smooth[j][i] = prom


for j in range(h):
    for i in range(w):
        outputFile.writelines(str(smooth[j][i])+"\n")


inputFile.close()
outputFile.close()
