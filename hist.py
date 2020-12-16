# This program does grayscale linear transformation

inputFile = open("Girl.pgm", "r")
counter = 0

outputFile = open("Girl3.pgm", "w")

n = 256
histogram = [0] * n # [0 0 0 0 0 0 0]
                    # [0 1 2 3 ... 255]
for line in inputFile:
    if counter < 3:  # copy the image header
        outputFile.writelines(line)
        counter += 1
    else:
        x = int(line)
        histogram[x] += 1

with open("histogram", "w") as outfile:
    outfile.write(str(histogram))

inputFile.close()
outputFile.close()
