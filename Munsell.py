import numpy as np
import matplotlib.pyplot as plt
MUNSELL_TABLE = np.zeros((10,40,3))
with open('munsell.txt','r') as f:
    hue_idx = 0
    for line in f:
        tmp_line = line.split()
        for i in range(10):
            rgb_string = tmp_line[i][1:-1].split(',')
            for j in range(3):
                MUNSELL_TABLE[i][hue_idx][j] = int(rgb_string[j])
        hue_idx+=1
        
#plt.imshow(MUNSELL_TABLE/255)

