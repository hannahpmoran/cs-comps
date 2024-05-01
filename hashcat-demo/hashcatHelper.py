# strip salt + digest
secret = open('secret.txt')

salt = ""
digest = ""

while 1:
    char = secret.read(1)
    if char == '$':
        while 1: 
            char = secret.read(1)
            if not char:
                break
            digest += char
        break
    if not char:
        break
    salt += char 

# make new modified common passwords text file 
mod = ""
with open('10k-most-common.txt','r') as f:
    for line in f:
        mod+= salt + line.strip()+"\n"
    f.close()

with open('mod-10k-most-common.txt','w') as f:
    f.write(mod)
    f.close()