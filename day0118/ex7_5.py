#コピー元のファイルのパスとコピー後のファイルパスを入力>>
#file1.txt,filecopy.txt

b_name=input('コピー元のファイルパスを入力>>')
a_name=input('コピー後のファイルパスを入力>>')

b_file=open(b_name, 'r')
a_file=open(a_name, 'w')

for line in b_file:
    a_file.write(line)
#    print(line)
b_file.close()
a_file.close()

#先生の見本は以下。上は自分で作成
#orgName,cpName=input('コピー元のファイルパスとコピー後のファイルパスを入力>>').split(',')
#with open(orgName,'r',encoding='utf-8') as reader,open(cpName,'w',encoding='utf-8') as writer:
#    for line in reader:
#        writer.write(line)
