import json
#importing the list from another file, if you don't need it just remove this line.
from intents import list
#change file.json for your json file, change utf8 for your file's encoding
file = open('file.json', encoding="utf8")
data = json.load(file)
freq = {}
for item in list:
    if (item in freq):
       freq[item] += 1
    else:
       freq[item] = 0
#change data['dialog_nodes'] for your json main entity, if it doesn't have a name just remove ['dialog_nodes']
for index in range(len(data['dialog_nodes'])):
    for item in freq:
        #only if you need to add # to the start of each string
        fix = f"#{item}"
        #check if field conditions exist on this index
        if 'conditions' in data['dialog_nodes'][index]:
            #if this field has multiple strings, split them after each space
            test = data['dialog_nodes'][index]['conditions'].split(' ')
            #if found fix inside of array test, count+1
            if fix in test:
                freq[item]+=1 

for key, value in freq.items():
    print ("% s : % d"%(key, value))
