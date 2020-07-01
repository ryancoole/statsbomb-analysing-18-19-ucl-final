#Make a player pass map using Statsbomb data

#Function to draw the pitch
import matplotlib.pyplot as plt
import numpy as np

#Size of the pitch in yards (for StabsBomb data)
pitchLengthX=120
pitchWidthY=80

#ID for Tottenham Hotspur vs Liverpool UCL 2018/19 Final and player name
match_id_required = 22912
player_name_required = "Virgil van Dijk"

#Load in the data and match events 
file_name=str(match_id_required)+'.json'

import json
with open('Statsbomb/data/events/'+file_name) as data_file:
    #print (mypath+'events/'+file)
    data = json.load(data_file)

#Get the nested structure into a dataframe 
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

#A dataframe of passes
passes = df.loc[df['type_name'] == 'Pass'].set_index('id')
    
#Draw the pitch
from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')

#Plot player_name_required passes
for i,cpass in passes.iterrows():
    if cpass['player_name'] == player_name_required:        
        
        x=cpass['location'][0]
        y=cpass['location'][1]
        
        dx=cpass['pass_end_location'][0]-x
        dy=cpass['pass_end_location'][1]-y
            
        
        if (cpass['pass_end_location'][0] > x):            
            passCircle=plt.Circle((x,pitchWidthY-y),2,color="red")
            passCircle.set_alpha(.2)             
            ax.add_patch(passCircle)
            
            passArrow=plt.Arrow(x,pitchWidthY-y,dx,dy,width=2,color="red")
            ax.add_patch(passArrow)
            
        else:
            passCircle=plt.Circle((x,pitchWidthY-y),2,color="black")
            passCircle.set_alpha(.2)             
            ax.add_patch(passCircle)
            
            passArrow=plt.Arrow(x,pitchWidthY-y,dx,dy,width=2,color="black")
            ax.add_patch(passArrow) 

plt.text(80,75,player_name_required + ' passes')
   
fig.set_size_inches(10, 7)
#fig.savefig('Output/passes.pdf', dpi=100) 
plt.show()