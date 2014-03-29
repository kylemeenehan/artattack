#Script to generate every black and white possibility for an image of a given size

#this script uses pygame
import pygame

#Specify width and height
width = 4
height = 4

#Specify the path that the image files should be written to
file_path = "possible2/"

#initialize pygame with a surface of the given width and height
pygame.init()
all_possible = pygame.Surface((width,height), depth=8)

#Initialize the possibility instance count to zero
count = 0

#for every possibility, write the possibility to the file
while count < 2**(width*height):
    
    #print to the console to give an idea of how long the program has left.
    print "%2E" % int((2**(width*height))-count)
    
    #convert count into binary to iterate through the bits and determine whether a pixel should be black or white
    bin_string = bin(count)
    
    #Fill the pygame surface with white
    all_possible.fill((255,255,255))
    
    #iterate through the binary representatin of count and paint black pixels accordingly
    for i in xrange(1,len(bin_string)-1):
        #Read bin_string backwards to iterate effectively through bits
        #If bit = 1 then create a black pixel
        if bin_string[-i] == "1":
            x = (i-1) % width
            y = (i-1) // width
            all_possible.set_at((x, y), (0, 0, 0))
        
    pygame.image.save(all_possible, file_path + str(count) + ".png")
    count += 1
