s='hai hello how are you'
ss=""
for i in range(len(s)):
    if s[i]=='h':
        continue    #continue means passs the control to immideate one 
    else:
        ss+=s[i]
print(ss)