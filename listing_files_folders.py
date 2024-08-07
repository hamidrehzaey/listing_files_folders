import os, winsound

saver = ['written by hamidrehzaey\ngithub address: http://github.com/hamidrehzaey\ntelegram channel: @py_land']
for i in os.listdir(os.getcwd()):
	if 'listing files folders. @py_land.exe' in i:
		continue
	saver.append(i)

winsound.Beep(1000, 500)
folder_name = os.path.basename(os.getcwd())
txt = open(f'{folder_name}.txt', 'x', encoding = 'utf-8-sig')
txt.write('\n'.join(saver))
txt.close()