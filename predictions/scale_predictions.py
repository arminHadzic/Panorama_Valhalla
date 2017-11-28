import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import fileinput


V_Training_Data = np.genfromtxt("versailles.csv", delimiter=",")
v_scores = V_Training_Data[:, 2]
v_scores = v_scores[1:]

plt.figure(1)
plt.scatter(range(len(v_scores)), v_scores, s=7, color="green")
plt.title("Versailles Route")
plt.xlabel("Edge Number(1 -> max # of edges)")
plt.ylabel("Edge Safety Score")
plt.show()


P_Training_Data = np.genfromtxt("parkers_mill.csv", delimiter=",")
p_scores = P_Training_Data[:, 2]
p_scores = p_scores[1:]


plt.figure(2)
plt.scatter(range(len(p_scores)), p_scores, s=7, color="red")
plt.title("Parkers Mill Route")
plt.xlabel("Edge Number(1 -> max # of edges)")
plt.ylabel("Edge Safety Score")
plt.show()


#Combo both datasets and call clean.py to make the hybrid dataset: network_predictions
first_csv = pd.read_csv("versailles.csv")
second_csv = pd.read_csv("parkers_mill.csv")
combo_frame = [first_csv, second_csv]
Hybrid = pd.concat(combo_frame)
np_hybrid = Hybrid.as_matrix()

#Hybrid = np.genfromtxt("network_predictions.csv", delimiter=",")
pm_scores = np_hybrid[:, 2]
int_pm_scores = pm_scores.astype(int)
factor_correction_dict = {1:100000.0, 2:50000.0, 3:1.0, 4:0.5, 5:0.1}
#factor_correction_dict = {1:10.0, 2:5.0, 3:1.0, 4:0.5, 5:0.1}

adjusted_scores = []

for score in int_pm_scores:	
	val = factor_correction_dict[score]
	adjusted_scores.append(val)

#csv_input = pd.read_csv("network_predictions.csv")
Hybrid['Adjusted Score'] = adjusted_scores
#new_col = pd.DataFrame({'Adjusted Score':adjusted_scores})
#df = df.merge(new_col, left_index = True, right_index=True)
Hybrid.to_csv("network_predictions.csv", index=False)

seen = set() # set for fast O(1) amortized lookup
for line in fileinput.FileInput('network_predictions.csv', inplace=1):
    if line in seen: continue # skip duplicate

    seen.add(line)
    print line, # standard output is now redirected to the file