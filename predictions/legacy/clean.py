import fileinput
seen = set() # set for fast O(1) amortized lookup
for line in fileinput.FileInput('pm_predictions_good.csv', inplace=1):
    if line in seen: continue # skip duplicate

    seen.add(line)
    print line, # standard output is now redirected to the file