name = "Intervals"
fin = open('source_leetcode_data.txt', 'r')
fout = open('intervals.md', 'r')
lastv = []
file = []
for i in fout:
    lastv.append(i.split("\n")[0])
for i in fin:
    file.append(i.split("\n")[0])
fout.close()
fout = open('output.txt', 'w')
namefile = file[0][(file[0].find('.', 0) + 2):len(file[0])]
if lastv == []:  # Запись программы в пустой файл
    fout.write('# ' + name + '\n\n')
    fout.write('+ [' + namefile + '](#' + file[1].split('/')[-2] + ')\n\n')
    fout.write('## ' + namefile + '\n\n')
    fout.write(file[1] + '\n\n')
    fout.write('```python\n')
    for i in file[3:]:
        fout.write(i[4:] + '\n')
    fout.write('```\n\n')
else:  # Запись программы в не пустой файл
    fout.write('#' + name + '\n\n')
    i = 2
    while len(lastv[i]):
        fout.write(lastv[i] + '\n')
        i += 1
    fout.write('+ [' + namefile + '](#' + file[1].split('/')[-2] + ')\n')
    while i < len(lastv):
        fout.write(lastv[i] + '\n')
        i += 1
    fout.write('##' + namefile + '\n\n')
    fout.write(file[1] + '\n\n')
    fout.write('```python\n')
    for i in file[3:]:
        fout.write(i[4:] + '\n')
    fout.write('```\n\n')
fout.close()
fin.close()
