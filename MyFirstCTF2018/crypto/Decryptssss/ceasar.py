def ceasar(source, shift=None):
    '''
    source : bytes
    shift  : number (default None)
    If shift is None, ceasar will return all possible results (a list of 26 bytes).
    '''
    lower = b'abcdefghijklmnopqrstuvwxyz'
    upper = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def ceasar_char(char, shift):
        if char in lower: table = lower
        else:             table = upper
        return table[ ((char - table[0]) + shift) % 26 ]

    if shift != None:
        return bytes([ ceasar_char(c, shift) if (c in lower+upper) else c for c in source ])
    return [ bytes([ ceasar_char(c, i) if (c in lower+upper) else c for c in source ]) for i in range(26) ]
