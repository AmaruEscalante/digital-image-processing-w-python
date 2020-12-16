# This program does grayscale linear transformation

inputFile = open("Girl.pgm", "r")
counter = 0

outputFile = open("Girl2.pgm", "w")
for line in inputFile:
    if counter < 3:  # copy the image header
        outputFile.writelines(line)
        counter += 1
    else:
        x = 255 - int(line)   # linear transformation
        if x < 0:        # truncate grayscale values lower than 0
            x = 0
        outputFile.write(str(x)+"\n")
        counter += 1

inputFile.close()
outputFile.close()
