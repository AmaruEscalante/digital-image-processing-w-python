# This program does grayscale linear transformation

inputFile = open("Girl.pgm", "r")
counter = 0

outputFile = open("Girl3.pgm", "w")
for line in inputFile:
    if counter < 3:  # copy the image header
        outputFile.writelines(line)
        counter += 1
    else:
        gamma = 1.2
        x = int(int(line)**gamma)   # linear transformation
        if x > 255:        # truncate grayscale values lower than 0
            x = 255
        outputFile.write(str(x)+"\n")
        counter += 1

inputFile.close()
outputFile.close()
