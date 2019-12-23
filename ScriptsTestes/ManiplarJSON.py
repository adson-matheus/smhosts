import json

with open('zingchart.json') as json_file:
    data = json.load(json_file)

print(data['graphset'][0]['scaleX']['values']) #
print()
print(data['graphset'][0]['scaleX']['item']['rules'][1])
print()
print(data['graphset'][0]['series'][0]['values']) #
print()
print(data['graphset'][0]['series'][1]['values']) #
print()
print(data['graphset'][0]['series'][1]['rules'][1]['backgroundColor']) #