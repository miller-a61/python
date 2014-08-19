mortem_file = r'C:\Users\Andy\Documents\roguelikes\doomrl\mortem.txt'

mortem = open(mortem_file,'r')

mortem_line = []

for line in mortem:
	line = line.rstrip('\n\r')
	mortem_line.append(line)

game_version = mortem_line[1]
	
print(game_version)


for i in range(3,len(mortem_line)):
        print(mortem_line[i])               

'''
for i in range(len(mortem_line)):
	print(mortem_line[i])
'''
