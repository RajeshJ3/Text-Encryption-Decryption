def decrypy(msg):
    # encrypt = open('data//99-d@j-d_hhd.cryp', 'r')
    # msg = encrypt.read()
    # encrypt.close()

    f = open('9-d@j-d_hhd.cryp', 'r')
    keys = f.read()
    f.close()
    message = ''
    i=0
    while(i < len(msg)):
        values = msg[i:i+7]
        BA = keys.find(values)
        BA /= 7
        message = message + chr(int(BA))
        i+=7
    return message

def encryption(msg):
    f = open('9-d@j-d_hhd.cryp', 'r')
    fp = f.read()
    final_key = ""
    for i in msg:
        value = ord(i)
        value *= 7
        key = fp[value:value+7]
        final_key = final_key + key
    f.close()
    return final_key
