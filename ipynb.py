#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pygame.locals import *

pygame.init()

X = 400
Y = 400
cell_x = 50
cell_y = 50

img_01_loc = r"C:\Users\Lyndall_Holstein\Desktop\high_lighted_pdfs\66dea1c1e61018cc0d383fa93fe22cdd.jpg"
img_02_loc = r"C:\Users\Lyndall_Holstein\Desktop\high_lighted_pdfs\cyber-demon.jpg"
img_03_loc = r"C:\Users\Lyndall_Holstein\Desktop\high_lighted_pdfs\snowden_Obama.jpg"

img_01 = pygame.image.load(img_01_loc)
img_01 = pygame.transform.scale(img_01,(cell_x,cell_y))

img_02 = pygame.image.load(img_02_loc)
img_02 = pygame.transform.scale(img_02,(cell_x,cell_y))

D_surf = pygame.display.set_mode((X,Y),0,32)

#this is the name of the unit herafter known as self
class personage:
    #this __init__ keyword sits in the function and makes it a specal function
    #it calls back around and assigns memory locations for each of these variables
    #including the .self object itself
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = personage("graham",40)

print(p1.name)



class box_dets:
    def __init__(self,top_x,top_y,cell_x,cell_y,img_obj_top,img_obj_bot):
        self.top_x = top_x
        self.top_y = top_y
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.img_obj_top = img_obj_top
        self.img_obj_bot = img_obj_bot 

        

p2 = box_dets(50,50,cell_x,cell_y,img_02,img_01)
p3 = box_dets(100,100,cell_x,cell_y,img_02,img_01)

this_list = [p2,p3]

while True:
    D_surf.fill(pygame.Color("#272392"))
   
    D_surf.blit(this_list[1].img_obj_bot,(this_list[1].top_x,this_list[1].top_y))
    D_surf.blit(this_list[0].img_obj_top,(this_list[0].top_x,this_list[0].top_y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            quit()
            
    pygame.display.update()





