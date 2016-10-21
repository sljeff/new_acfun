line = '![](img/{}.gif)\r\n'
content = '新版AC娘表情包\r\n'
for i in range(1, 56):
    num = str(i) if i > 9 else '0'+str(i)
    content += line.format(num)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('success')
