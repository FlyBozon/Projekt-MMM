import matplotlib.pyplot as plt
import numpy as np
from turtle import *
# Create a figure and axis with a larger window size
fig, ax = plt.subplots()  # Width=12 inches, Height=8 inches

# Set axis limits
ax.set_xlim(0, 23)
ax.set_ylim(0, 10)

ax.plot([4, 5], [7, 7], color='black')

recJ1=plt.Rectangle((5, 6.5), 2, 1, fill=True, edgecolor='black', facecolor='none')
ax.add_patch(recJ1)
ax.text(6, 7, 'J1', horizontalalignment='center', verticalalignment='center')

ax.plot([7, 9], [7, 7], color='black')

recn1=plt.Rectangle((9, 6), 0.5, 2, fill=True, edgecolor='black', facecolor='none')
ax.add_patch(recn1)
ax.text(10, 7, 'n1', horizontalalignment='center', verticalalignment='center')

recn2=plt.Rectangle((9, 2), 0.5, 4, fill=True, edgecolor='black', facecolor='none')
ax.add_patch(recn2)
ax.text(10, 3, 'n1', horizontalalignment='center', verticalalignment='center')

ax.plot([9.5,11], [4, 4], color='black')

recJ2 = plt.Rectangle((11, 3.5), 2, 1, fill=True, edgecolor='black', facecolor='none')
ax.add_patch(recJ2)
ax.text(12, 4, 'J2', horizontalalignment='center', verticalalignment='center')

ax.plot([13, 17.5], [4, 4], color='black')
ax.plot([20.25, 22], [4, 4], color='black')
ax.plot([16, 16], [2.3, 5.7], color='black')
ax.plot([22, 22], [2, 6], color='black')

#sprezyna
damper_x = [17.5, 17.625, 17.825, 18, 18.25, 18.5, 18.75, 19, 19.25, 19.45, 19.65, 19.83, 20, 20.2]
damper_y = [4, 4.5, 3.5, 4.5, 3.5, 4.5, 3.5, 4.5, 3.5, 4.5, 3.5, 4.5, 3.5, 4]
ax.plot(damper_x, damper_y, color='black')
ax.text(19.5, 3, 'k', horizontalalignment='center', verticalalignment='center')

# tlumik
ax.plot([15.5, 16.5], [2, 2], color='black')
ax.plot([15.5, 15.5], [2, 3], color='black')
ax.plot([16.5, 16.5], [2, 3], color='black')

ax.plot([15.5, 16.5], [6, 6], color='black')
ax.plot([15.5, 15.5], [5, 6], color='black')
ax.plot([16.5, 16.5], [5, 6], color='black')

ax.text(16.75, 4.5, 'b', horizontalalignment='center', verticalalignment='center')

#obroty
center1 = (5 ,7)    
radius = 3.2         
start_angle = -25     
end_angle = 25        

theta = np.linspace(np.radians(start_angle), np.radians(end_angle), 100)

x1 = center1[0] + radius * np.cos(theta)
y1 = center1[1] + radius * np.sin(theta)
ax.plot(x1, y1, color='black')
ax.set_aspect('equal')
ax.arrow(8, 5.9, -0.1, -0.1, head_width=0.5, head_length=0.5, fc='black', ec='black')
ax.text(8.5, 8.5, r'$\theta_2$', horizontalalignment='center', verticalalignment='center')

center2 = (10.7 ,4)    
radius2 = 3.2        
start_angle = -25     
end_angle = 25        

theta = np.linspace(np.radians(start_angle), np.radians(end_angle), 100)

x2 = center2[0] + radius * np.cos(theta)
y2 = center2[1] + radius * np.sin(theta)
ax.plot(x2, y2, color='black')
ax.set_aspect('equal')
ax.arrow(13.7, 2.9, -0.1, -0.1, head_width=0.5, head_length=0.5, fc='black', ec='black')
ax.text(14.2, 5.5, r'$\theta_2$', horizontalalignment='center', verticalalignment='center')

center3 = (2 ,7)    
radius3 = 2     
start_angle = -25    
end_angle = 25       

theta = np.linspace(np.radians(start_angle), np.radians(end_angle), 100)

x3 = center3[0] + radius3 * np.cos(theta)
y3 = center3[1] + radius3 * np.sin(theta)
ax.plot(x3, y3, color='black')
ax.set_aspect('equal')
ax.arrow(3.85, 6.2, -0.1, -0.1, head_width=0.5, head_length=0.5, fc='black', ec='black')
ax.text(4.2, 8.3, r'$\theta_2$', horizontalalignment='center', verticalalignment='center')

#mocowania k
x=22
dx=0.5
y=2
dy=0.5
for i in range(8):
    ax.plot([x, x+dx], [y, y+dy], color='black')
    y=y+0.5

#mocowania b
x=15.25
dx=0.25
y=5
dy=0.25
for i in range(4):
    ax.plot([x, x+dx], [y, y+dy], color='black')
    y=y+0.25
for i in range(5):
    ax.plot([x, x+dx], [y, y+dy], color='black')
    x=x+0.25
for i in range(5):
    ax.plot([x, x+dx], [y, y+dy], color='black')
    y=y-0.25

x=15.25
dx=0.25
y=2.75
dy=0.25
for i in range(4):
    ax.plot([x, x+dx], [y, y+dy], color='black')
    y=y-0.25
for i in range(5):
    ax.plot([x, x+dx], [y, y+dy], color='black')
    x=x+0.25
for i in range(5):
    ax.plot([x, x+dx], [y, y+dy], color='black')
    y=y+0.25

ax.axis('off')

plt.show()