#https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e/train/python
# Good Luck!

def encode(string):
    bits=''
    temp=''
    for i in string:
        temp=bin(ord(i))[2:]
        if len(temp)<8:
            temp=(8-len(temp))*'0'+temp
        for j in temp:
            bits+=j*3
    return bits

def decode(bits):
    bits=bits[::3]
    temp=''
    string=''
    j,k=0,8
    for i in range(len(bits)//8):
        string+=chr(int(bits[j:k],2))
        j=k
        k+=8
    return string
if __name__ == "__main__":
    a='hey'
    print(encode(a))
    print(decode(encode(a)))
