import json

TotalResult = open('TotalResult.txt', 'a+')

with open('LastBuildResult/statistics.json') as json_file:
    data = json.load(json_file)
    for i in data['Total']:
        TotalResult.write(str(i) + " : " + str(data['Total'][i]) + '\n')

TotalResult.close()
