import json
import glob
import os

TotalResult = open('TotalResult.txt', 'a+')

file_names = [os.path.basename(x)[:-4] for x in glob.glob('*.jmx')]

with open('LastBuildResult/statistics.json') as json_file:
    data = json.load(json_file)
    for name in file_names:
        minResTime = 999999
        maxResTime = 0
        medianResTime = []
        failedRequest = 0
        totalRequest = 0
        
        for key in data:
            if(str(name+'-') in key):
                for i in data[key]:
                    if(str(i) == 'minResTime'):
                        if(minResTime > data[key][i]):
                            minResTime = data[key][i]
                    if(str(i) == 'maxResTime'):
                        if(maxResTime < data[key][i]):
                            maxResTime = data[key][i]
                    if(str(i) == 'medianResTime'):
                        medianResTime.append(data[key][i])
                    if(str(i) == 'errorCount'):
                        failedRequest+=1
                    totalRequest+=1
        for i in data[name]:
            if(str(i) == 'transaction'):
                TotalResult.write("transaction : " + str(name) + '\n')
                TotalResult.write("totalRequest : " + str(totalRequest) + '\n')
                TotalResult.write("failedRequest : " + str(failedRequest) + '\n')
            if(str(i)=='minResTime'):
                TotalResult.write(str(i) + " : " + str(minResTime) + '\n')
            if(str(i)=='maxResTime'):
                TotalResult.write(str(i) + " : " + str(maxResTime) + '\n')
            if(str(i)=='medianResTime'):
                TotalResult.write(str(i) + " : " + str(round(sum(medianResTime)/len(medianResTime),2)) + '\n')
            
        TotalResult.write('\n')
    for i in data['Total']:
        TotalResult.write(str(i) + " : " + str(data['Total'][i]) + '\n')

TotalResult.close()
