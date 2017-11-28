import csv
from geopy.distance import vincenty

data=[[-84.555466,38.042097999999996],[-84.555718,38.042339],[-84.55619899999999,38.042728],[-84.55671699999999,38.043147999999995],[-84.557045,38.042949],[-84.557137,38.042891999999995],[-84.557198,38.04285],[-84.557442,38.042682],[-84.557839,38.042373],[-84.558274,38.042049],[-84.558419,38.041931],[-84.558579,38.041759],[-84.55864,38.041675],[-84.558793,38.041446],[-84.559624,38.040157],[-84.55982999999999,38.039843999999995],[-84.560051,38.039553999999995],[-84.560189,38.039386],[-84.560456,38.039119],[-84.560799,38.038787],[-84.561081,38.038532],[-84.56150099999999,38.038173],[-84.561852,38.037872],[-84.562111,38.037666],[-84.562378,38.037487],[-84.56244699999999,38.037448],[-84.562737,38.037284],[-84.563118,38.037093999999996],[-84.56358399999999,38.036861],[-84.564301,38.03651],[-84.56463699999999,38.036342],[-84.565491,38.035911],[-84.566109,38.03561],[-84.566338,38.035499],[-84.566544,38.035415],[-84.566712,38.035354],[-84.566918,38.035289],[-84.56765,38.035076],[-84.56875699999999,38.034793],[-84.569092,38.034706],[-84.569176,38.034683],[-84.56925299999999,38.034664],[-84.569321,38.034652],[-84.569504,38.034614],[-84.570191,38.034469],[-84.570939,38.034313],[-84.571427,38.034197999999996],[-84.57182399999999,38.034095],[-84.572037,38.034027],[-84.57244899999999,38.033896999999996],[-84.575287,38.032871],[-84.575875,38.032665],[-84.576325,38.032500999999996],[-84.577294,38.032157],[-84.577668,38.032028],[-84.578026,38.03189],[-84.57824,38.031799],[-84.578492,38.031676999999995],[-84.578637,38.031593],[-84.579087,38.031321999999996],[-84.57955199999999,38.031028],[-84.580124,38.030662],[-84.581559,38.029708],[-84.582413,38.029154999999996],[-84.58281,38.028929999999995],[-84.58367199999999,38.028514],[-84.583817,38.028472],[-84.584969,38.028064],[-84.586411,38.027575999999996],[-84.589654,38.026233],[-84.591149,38.025611],[-84.59191899999999,38.025299],[-84.59213299999999,38.025238],[-84.592354,38.025199],[-84.59255999999999,38.025183999999996],[-84.592782,38.025177],[-84.59316299999999,38.025199],[-84.593514,38.025241],[-84.593682,38.025268],[-84.593865,38.025314],[-84.594056,38.025366999999996],[-84.594849,38.025622999999996],[-84.59622999999999,38.026081],[-84.597489,38.026508],[-84.59792399999999,38.026664],[-84.598542,38.026874],[-84.598694,38.026916],[-84.598839,38.026947],[-84.59899999999999,38.026962],[-84.599198,38.026976999999995],[-84.599595,38.026981],[-84.600579,38.027011],[-84.60140299999999,38.027034],[-84.601952,38.027046],[-84.602448,38.027052999999995],[-84.603341,38.027072],[-84.60354699999999,38.027076],[-84.603577,38.027136999999996],[-84.60359199999999,38.027190999999995],[-84.603577,38.027277999999995],[-84.603539,38.027342999999995],[-84.603417,38.027477],[-84.603341,38.027553],[-84.603257,38.027622],[-84.603196,38.027682999999996],[-84.603127,38.027778],[-84.60305799999999,38.027896],[-84.602936,38.028082999999995],[-84.60279899999999,38.028228],[-84.602654,38.028369],[-84.602509,38.028521999999995],[-84.602402,38.028625],[-84.60234899999999,38.02869]]

data2=[[-84.555466,38.042097999999996],[-84.555718,38.042339],[-84.55619899999999,38.042728],[-84.55671699999999,38.043147999999995],[-84.55656499999999,38.043247],[-84.556321,38.043392],[-84.555779,38.043727],[-84.555275,38.044028999999995],[-84.554902,38.044258],[-84.55465,38.044441],[-84.554497,38.044567],[-84.55444399999999,38.044627999999996],[-84.554345,38.044773],[-84.554329,38.044803],[-84.554322,38.04486],[-84.554299,38.045246],[-84.554299,38.045372],[-84.554284,38.045725999999995],[-84.554276,38.045871],[-84.554268,38.046141999999996],[-84.554261,38.0466],[-84.5551,38.046543],[-84.55581699999999,38.046493],[-84.555954,38.046485],[-84.557244,38.046379],[-84.557244,38.046379],[-84.558915,38.046245],[-84.560006,38.046154],[-84.560463,38.046154],[-84.56115799999999,38.046119],[-84.565117,38.045791],[-84.566414,38.04568],[-84.567284,38.045612],[-84.567948,38.04557],[-84.568238,38.045555],[-84.56912299999999,38.045477999999996],[-84.56970299999999,38.045435999999995],[-84.570641,38.045359999999995],[-84.57119,38.045288],[-84.57171699999999,38.045196],[-84.57255599999999,38.044986],[-84.573273,38.044795],[-84.574074,38.044578],[-84.57424999999999,38.044528],[-84.574326,38.044506],[-84.574441,38.044475],[-84.575043,38.044315],[-84.575333,38.044258],[-84.57595099999999,38.044166],[-84.57640099999999,38.044136],[-84.57685099999999,38.044128],[-84.577332,38.044136],[-84.579278,38.044197],[-84.58176499999999,38.044261],[-84.58390899999999,38.044326],[-84.585618,38.044376],[-84.58796699999999,38.044436999999995],[-84.588723,38.044441],[-84.589089,38.044441],[-84.589379,38.044436999999995],[-84.58996599999999,38.044425],[-84.591301,38.044399],[-84.59285799999999,38.044306999999996],[-84.59333099999999,38.044264999999996],[-84.593514,38.044246],[-84.59350599999999,38.044097],[-84.59354499999999,38.041168],[-84.59354499999999,38.04047],[-84.59354499999999,38.040309],[-84.59354499999999,38.039511999999995],[-84.593552,38.039165],[-84.593537,38.038902],[-84.593499,38.038593],[-84.593453,38.038298999999995],[-84.593285,38.037731],[-84.593209,38.037535999999996],[-84.592919,38.036937],[-84.592827,38.036808],[-84.593514,38.036521],[-84.59445199999999,38.036144],[-84.594826,38.035990999999996],[-84.595063,38.035888],[-84.595215,38.035816],[-84.59543699999999,38.035700999999996],[-84.595795,38.035488],[-84.595978,38.035368999999996],[-84.596245,38.035179],[-84.59678699999999,38.034701999999996],[-84.597184,38.034296999999995],[-84.59728299999999,38.034175],[-84.597512,38.033882],[-84.59803099999999,38.033138],[-84.598618,38.032249],[-84.598832,38.031963],[-84.599274,38.031326],[-84.59935,38.031227],[-84.599488,38.031089],[-84.599564,38.031009],[-84.59979299999999,38.030826],[-84.600617,38.030257999999996],[-84.600922,38.030044],[-84.601128,38.029865],[-84.601525,38.029491],[-84.602006,38.02901],[-84.602173,38.028858],[-84.602288,38.028762],[-84.60234899999999,38.02869]]

with open('lat_ln_coor_Versailles.csv','wb') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['lon','lat', 'dist'])
    first = True
    row_prev = [0.0, 0.0]
    for row in data2:
    	if first == True:
    		row_prev = [row[1], row[0]]
    		row.append(0)
    	else:
    		temp_row = [row[1], row[0]]
    		dist = vincenty(row_prev, temp_row).meters
    		row_prev = temp_row
    		row.append(dist)
        csv_out.writerow(row)
        first = False