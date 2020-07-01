#Make a player ball carry map using Statsbomb data

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

#A dataframe of carries
carries = df.loc[df['type_name'] == 'Carry'].set_index('id')
    
#Draw the pitch
from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')

#Plot player_name_required carries
for i,carry in carries.iterrows():
    if carry['player_name'] == player_name_required:
    
        x=carry['location'][0]
        y=carry['location'][1]
        
        dx=carry['carry_end_location'][0]-x
        dy=carry['carry_end_location'][1]-y
            
        
        if (carry['carry_end_location'][0] > x):            
            carryCircle=plt.Circle((x,pitchWidthY-y),2,color="red")
            carryCircle.set_alpha(.2)            
            ax.add_patch(carryCircle)
            
            carryArrow=plt.Arrow(x,pitchWidthY-y,dx,dy,width=2,color="red")
            ax.add_patch(carryArrow)
            
        else:
            carryCircle=plt.Circle((x,pitchWidthY-y),2,color="black")
            carryCircle.set_alpha(.2)             
            ax.add_patch(carryCircle)
            
            carryArrow=plt.Arrow(x,pitchWidthY-y,dx,dy,width=2,color="black")
            ax.add_patch(carryArrow)   


plt.text(80,75,player_name_required + ' ball carries')
   
fig.set_size_inches(10, 7)
#fig.savefig('Output/carries.pdf', dpi=100) 
plt.show()