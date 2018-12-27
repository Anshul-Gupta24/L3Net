'''
	puts videos with no audio into a folder 'removed'
'''


import os
import re


print()
print('Removing videos with no audio')
print()


vids = []
auds = []

for vid in os.listdir('./vids'):
	vids.append(vid)

for aud in os.listdir('./audio'):
	auds.append(aud)


numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

vids = sorted(vids, key=numericalSort)
auds = sorted(auds, key=numericalSort)



iv = 0
ia = 0
removed = []

for x in range(len(vids)):

	if(vids[iv][3:-4]==auds[ia][3:-4]):
		iv+=1
		ia+=1
	else:
		removed.append(vids[iv])
		iv+=1

for r in removed:
	print(r)
	os.rename('./vids/'+r, './removed/'+r)
