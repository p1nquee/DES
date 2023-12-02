IP = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
)
IP_INV = (
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
)
PC1 = (
    57, 49, 41, 33, 25, 17, 9,
    1,  58, 50, 42, 34, 26, 18,
    10, 2,  59, 51, 43, 35, 27,
    19, 11, 3,  60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14, 6,  61, 53, 45, 37, 29,
    21, 13, 5,  28, 20, 12, 4
)
PC2 = (
    14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
)
 
E  = (
    32, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
)
 
Sboxes = {
    0: {
    0: (14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7),
    1: (0,  15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8),
    2: (4,   1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0),
    3: (15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13)
    },
    1: {
    0: (15, 1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10),
    1: (3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5),
    2: (0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15),
    3: (13, 8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9)
    },
    2: {
    0: (10, 0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8),
    1: (13, 7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1),
    2: (13, 6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7),
    3: (1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12)
    },
    3: {
    0: (7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15),
    1: (13, 8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9),
    2: (10, 6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4),
    3: (3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14)
    },
    4: {
    0: (2,  12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9),
    1: (14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6),
    2: (4,   2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14),
    3: (11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3)
    },
    5: {
    0: (12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11),
    1: (10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8),
    2: (9,  14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6),
    3: (4,  3,   2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13)
    },
    6: {
    0: (4,  11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1),
    1: (13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6),
    2: (1,   4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2),
    3: (6,  11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12)
    },
    7: {
    0: (13, 2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7),
    1: (1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2),
    2: (7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8),
    3: (2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11)
    }
}
 
P = (
    16,  7, 20, 21,
    29, 12, 28, 17,
    1,  15, 23, 26,
    5,  18, 31, 10,
    2,   8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4,  25
) 
P_INV = (
    9,  17, 23, 31,
    13, 28,  2, 18,
    24,  16, 30,  6,
    26,  20, 10,  1,
    8,  14, 25,  3,
    4,  29, 11,  19,
    32, 12,  22,  7,
    5, 27,  15,  21
)

key = list(input('Введите ключик:                 '))
for i in range(len(key)):
    key[i] = bin(ord(key[i]))
msg = list(input('Введите сообщеньице:            '))
for i in range(len(msg)):
    msg[i] = bin(ord(msg[i]))
#print('Ключик:      ', key, len(key))
#print('Сообщеньице: ', msg, len(msg))

def slowit(spisok):
    summa = ''
    for i in range(len(spisok)):
        spisok[i] = str(spisok[i][2:]).zfill(8)
        summa += spisok[i]
    return summa

def razdelit_bite(spisok):
    result = {}
    for i in range(len(spisok)):
        result[i] = tuple(spisok[i][2:].zfill(8))
    return result
keyy = razdelit_bite(key)
msgg = razdelit_bite(msg)


def fill_block(bites, message = False):
    if not message:
        our_block = [0] * 56
        for i in range(7):
            if i == 0:
                for j in range(8):
                    our_block[j] = int(bites[i][j])
            if i == 1:
                for j in range(8):
                    our_block[8+j] = int(bites[i][j])
            if i == 2:
                for j in range(8):
                    our_block[16+j] = int(bites[i][j])
            if i == 3:
                for j in range(8):
                    our_block[24+j] = int(bites[i][j])
            if i == 4:
                for j in range(8):
                    our_block[32+j] = int(bites[i][j])
            if i == 5:
                for j in range(8):
                    our_block[40+j] = int(bites[i][j])
            if i == 6:
                for j in range(8):
                    our_block[48+j] = int(bites[i][j])
        return our_block
    if message:
        our_block = [0] * 64
        for i in range(8):
            if i == 0:
                for j in range(8):
                    our_block[j] = int(bites[i][j])
            if i == 1:
                for j in range(8):
                    our_block[8+j] = int(bites[i][j])
            if i == 2:
                for j in range(8):
                    our_block[16+j] = int(bites[i][j])
            if i == 3:
                for j in range(8):
                    our_block[24+j] = int(bites[i][j])
            if i == 4:
                for j in range(8):
                    our_block[32+j] = int(bites[i][j])
            if i == 5:
                for j in range(8):
                    our_block[40+j] = int(bites[i][j])
            if i == 6:
                for j in range(8):
                    our_block[48+j] = int(bites[i][j])
            if i == 7:
                for j in range(8):
                    our_block[56+j] = int(bites[i][j])
        return our_block

key_block = fill_block(keyy)
msg_block = fill_block(msgg, message = True)
#print('ключеблок: ',key_block, len(key_block))
#print('мсжблок:   ',msg_block, len(msg_block))


def permutation_by_table(block, last_message = False):
    permutated = [0] * 64
    for i in range(64):
        permutated[IP[i]-1] = block[i]
    return permutated
    if last_message:
        for i in range(64):
            permutated[IP_INV[i]-1] = block[i]
        return permutated


def key_conversion():
### расширение 56-битового ключа до 64-битового
    summed = 0
    for i in range(7):
        summed += key_block[i]
    if summed % 2 == 0:
        key_block.insert(7, 1)
    else:
        key_block.insert(7, 0)
    summed = 0
    for i in range(7):
        summed += key_block[i+8]
    if summed % 2 == 0:
        key_block.insert(15, 1)
    else:
        key_block.insert(15, 0)
    summed = 0
    for i in range(7):
        summed += key_block[i+16]
    if summed % 2 == 0:
        key_block.insert(23, 1)
    else:
        key_block.insert(23, 0)
    summed = 0
    for i in range(7):
        summed += key_block[i+24]
    if summed % 2 == 0:
        key_block.insert(31, 1)
    else:
        key_block.insert(31, 0)
    summed = 0
    for i in range(7):
        summed += key_block[i+32]
    if summed % 2 == 0:
        key_block.insert(39, 1)
    else:
        key_block.insert(39, 0)
    summed = 0
    for i in range(7):
        summed += key_block[i+40]
    if summed % 2 == 0:
        key_block.insert(47, 1)
    else:
        key_block.insert(47, 0)
    summed = 0
    for i in range(7):
        summed += key_block[i+48]
    if summed % 2 == 0:
        key_block.insert(55, 1)
    else:
        key_block.insert(55, 0)
    summed = 0
    for i in range(7):
        summed += key_block[i+56]
    if summed % 2 == 0:
        key_block.insert(63, 1)
    else:
        key_block.insert(63, 0)
    C = []
    D = []
    for i in range(28):
        C.append(key_block[PC1[i]-1])
    for i in range(28, 56, 1):
        D.append(key_block[PC1[i]-1])
    for i in range(16):
        if 1 < i < 8 or 8 < i < 15:
            C.append(C[0])
            del C[0]
            C.append(C[0])
            del C[0]
            D.append(C[0])
            del D[0]
            D.append(D[0])
            del D[0]
        else:
            C.append(C[0])
            del C[0]
            D.append(D[0])
            del D[0]
    CD = C + D
    L_key_block = [0] * 48
    for i in range(48):
        L_key_block[i] = CD[PC2[i]-1]
    return L_key_block
L_key_block = key_conversion()

def msg_delenie():
    L = []
    R = []
    for i in range(64):
        if 0 <= i <= 3 or 8 <= i <= 11 or 16 <= i <= 19 or 24 <= i <= 27 or 32 <= i <= 35 or 40 <= i <= 43 or 48 <= i <= 51 or 56 <= i <= 59:
            L.append(msg_block[i])
        else:
            R.append(msg_block[i])
    return L, R

LSide = msg_delenie()[0]
RSide = msg_delenie()[1]
def binnot(num):
    a = []
    k = 0
    for i in range(len(str(num))):
        a.append(num % 10)
        num //= 10
    for i in range(len(a)):
        if a[i] == 1:
            k += 2**i
    return k

def function_f(RS):
    ERi = []
    Bii = ''
    for i in range(48):
        ERi.append(RS[E[i]-1])
    Bi1 = []
    for i in range(48):
        Bi1.append(ERi[i] ^ L_key_block[i])
    Bi = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
    for i in range(8):
        for j in range(6):
            Bi[i].append(Bi1[6*i+j])
#            print(ERi,len(ERi),'                ', L_key_block, len(L_key_block))
#            print('i : ', i, ', Bi: ',Bi)
#    print('Bi: ',Bi)
    for i in range(8):
        b1b6 = binnot(int(str(Bi[i][0])+str(Bi[i][5])))
        b2tob5 = binnot(int(str(Bi[i][1])+str(Bi[i][2])+str(Bi[i][3])+str(Bi[i][4])))
        Bii += bin(Sboxes[i][b1b6][b2tob5])[2:].zfill(4)
#        print('b1b6:   ', b1b6)
#        print('b2tob5: ', b2tob5)
    Bii = list(Bii)
#    print(Bii)
    for i in range(32):
        Bii[i] = int(Bii[i])
    PB = []
    for i in range(32):
        PB.append(Bii[P[i]-1])
    return PB
func1 = function_f(RSide)
L1 = RSide
R1 = []
for i in range(32):
    k = L1[i] ^ func1[i]
    R1.append(k)
#print('func:  ', func1)
#print('L:     ', L1)
#print('R:     ',R1)
func2 = function_f(R1)
L2 = R1
R2 = []
for i in range(32):
    k = L2[i] ^ func2[i]
    R2.append(k)
#print('func:  ', func2)
#print('L:     ', L2)
#print('R:     ',R2)
func3 = function_f(R2)
L3 = R2
R3 = []
for i in range(32):
    k = L3[i] ^ func3[i]
    R3.append(k)
#print('func:  ', func3)
#print('L:     ', L3)
#print('R:     ',R3)
func4 = function_f(R3)
L4 = R3
R4 = []
for i in range(32):
    k = L4[i] ^ func4[i]
    R4.append(k)
#print('func:  ', func4)
#print('L:     ', L4)
#print('R:     ',R4)
func5 = function_f(R4)
L5 = R4
R5 = []
for i in range(32):
    k = L5[i] ^ func5[i]
    R5.append(k)
#print('func:  ', func5)
#print('L:     ', L5)
#print('R:     ',R5)
func6 = function_f(R5)
L6 = R5
R6 = []
for i in range(32):
    k = L6[i] ^ func6[i]
    R6.append(k)
#print('func:  ', func6)
#print('L:     ', L6)
#print('R:     ',R6)
func7 = function_f(R6)
L7 = R6
R7 = []
for i in range(32):
    k = L7[i] ^ func7[i]
    R7.append(k)
#print('func:  ', func7)
#print('L:     ', L7)
#print('R:     ',R7)
func8 = function_f(R7)
L8 = R7
R8 = []
for i in range(32):
    k = L8[i] ^ func8[i]
    R8.append(k)
#print('func:  ', func8)
#print('L:     ', L8)
#print('R:     ',R8)
func9 = function_f(R8)
L9 = R8
R9 = []
for i in range(32):
    k = L9[i] ^ func9[i]
    R9.append(k)
#print('func:  ', func9)
#print('L:     ', L9)
#print('R:     ',R9)
func10 = function_f(R9)
L10 = R9
R10 = []
for i in range(32):
    k = L10[i] ^ func10[i]
    R10.append(k)
#print('func:  ', func10)
#print('L:     ', L10)
#print('R:     ',R10)
func11 = function_f(R10)
L11 = R10
R11 = []
for i in range(32):
    k = L11[i] ^ func11[i]
    R11.append(k)
#print('func:  ', func11)
#print('L:     ', L11)
#print('R:     ',R11)
func12 = function_f(R11)
L12 = R11
R12 = []
for i in range(32):
    k = L12[i] ^ func12[i]
    R12.append(k)
#print('func:  ', func12)
#print('L:     ', L12)
#print('R:     ',R12)
func13 = function_f(R12)
L13 = R12
R13 = []
for i in range(32):
    k = L13[i] ^ func13[i]
    R13.append(k)
#print('func:  ', func13)
#print('L:     ', L13)
#print('R:     ',R13)
func14 = function_f(R13)
L14 = R13
R14 = []
for i in range(32):
    k = L14[i] ^ func14[i]
    R14.append(k)
#print('func:  ', func14)
#print('L:     ', L14)
#print('R:     ',R14)
func15 = function_f(R14)
L15 = R14
R15 = []
for i in range(32):
    k = L15[i] ^ func15[i]
    R15.append(k)
#print('func:  ', func15)
print('L:     ', L15)
print('R:     ',R15)
func16 = function_f(R15)
L16 = R15
R16 = []
for i in range(32):
    k = L16[i] ^ func16[i]
    R16.append(k)
#print('func:  ', func16)
print('L16:   ',L16)
print('R16:   ',R16)
ciphher = []
for i in range(8):
    for j in range(4):
        ciphher.append(L16[4*i+j])
    for j in range(4):
        ciphher.append(R16[4*i+j])
print(ciphher, len(ciphher))
last_form_of_cipher = []
for i in range(64):
    last_form_of_cipher.append(ciphher[IP_INV[i]-1])
#print(last_form_of_cipher)
LFOC = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6:[], 7: []}
for i in range(8):
    for j in range(8):
        LFOC[i].append(last_form_of_cipher[8*i+j])
bin_LFOC = []
for i in range(8):
    bin_LFOC.append(chr(binnot(int(str(LFOC[i][0])+str(LFOC[i][1])+str(LFOC[i][2])+str(LFOC[i][3])+str(LFOC[i][4])+str(LFOC[i][5])+str(LFOC[i][6])+str(LFOC[i][7]))))) 
encrypted = ''
for i in range(8):
    encrypted += bin_LFOC[i]
print('Ваше зашифрованное сообщеньице:', encrypted)

#def rev_f(PB):
#    Biii = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
#    Bii = []
#    for i in range(32):
#        Bii.append(PB[P_INV[i]-1])
#    for i in range(32):
#        Bii[i] = str(Bii[i])
#    for i in range(8):
#        for j in range(4):
#            Biii[i].append(Bii[i*4+j])
#    print(Biii)
#    for i in range(8):
#        K = ''
#        for j in range(4):
#            K += Biii[i][0]
#            del Biii[i][0]
#        Biii[i].append(binnot(int(K.zfill(4))))
##    print(Biii)
#    for i in range(8):
#        for i in range(64)
#        if Biii[i][0] == 
    
La = []
for i in range(32):
    La.append(L16[i] ^ R16[i])
    
#rev_f(La)
def decrypt():
    msg_block = []
    L16 = []
    L15 = []
    L14 = []
    L13 = []
    L12 = []
    L11 = []
    L10 = []
    L9 = []
    L8 = []
    L7 = []
    L6 = []
    L5 = []
    L4 = []
    L3 = []
    L2 = []
    L1 = []
    LSide = []
    R16 = []
    R15 = []
    R14 = []
    R13 = []
    R12 = []
    R11 = []
    R10 = []
    R9 = []
    R8 = []
    R7 = []
    R6 = []
    R5 = []
    R4 = []
    R3 = []
    R2 = []
    R1 = []
    RSide = []    
    ciphher = []
    last_form_of_cipher = []
    LFOC = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6:[], 7: []}
    bin_LFOC = []
    chastnoe = list(encrypted)
    for i in range(8):
        bin_LFOC.append(bin(ord(chastnoe[i]))[2:].zfill(8))
#    print(bin_LFOC)
    for i in range(8):
        for j in range(8):
            k = list(bin_LFOC[i])
            LFOC[i].append(int(k[j]))
#    print(LFOC)
    for i in range(8):
        for j in range(8):
            last_form_of_cipher.append(list(LFOC[i])[j])
#    print(last_form_of_cipher, len(last_form_of_cipher))
    for i in range(64):
        ciphher.append(last_form_of_cipher[IP[i]-1])
#    print(ciphher)
    for i in range(64):
        if i < 32:
            L16.append(ciphher[i])
        else:
            R16.append(ciphher[i])
#    print('L16:   ',L16)
#    print('R16:   ',R16)
    R15 = L16
    for i in range(32):
        L15.append(R16[i] ^ function_f(L16)[i])
    print(L15, R15)
    R14 = L15
    for i in range(32):
        L14.append(R15[i] ^ function_f(L15)[i])
    R13 = L14
    for i in range(32):
        L13.append(R14[i] ^ function_f(L14)[i])
    R12 = L13
    for i in range(32):
        L12.append(R13[i] ^ function_f(L13)[i])
    R11 = L12
    for i in range(32):
        L11.append(R12[i] ^ function_f(L12)[i])
    R10 = L11
    for i in range(32):
        L10.append(R11[i] ^ function_f(L11)[i])
    R9 = L10
    for i in range(32):
        L9.append(R10[i] ^ function_f(L10)[i])
    R8 = L9
    for i in range(32):
        L8.append(R9[i] ^ function_f(L9)[i])
    R7 = L8
    for i in range(32):
        L7.append(R8[i] ^ function_f(L8)[i])
    R6 = L7
    for i in range(32):
        L6.append(R7[i] ^ function_f(L7)[i])
    R5 = L6
    for i in range(32):
        L5.append(R6[i] ^ function_f(L6)[i])
    R4 = L5
    for i in range(32):
        L4.append(R5[i] ^ function_f(L5)[i])
    R3 = L4
    for i in range(32):
        L3.append(R4[i] ^ function_f(L4)[i])
    R2 = L3
    for i in range(32):
        L2.append(R3[i] ^ function_f(L3)[i])
    R1 = L2
    for i in range(32):
        L1.append(R2[i] ^ function_f(L2)[i])
    RSide = L1
    for i in range(32):
        LSide.append(R1[i] ^ function_f(L1)[i])
    for i in range(8):
        for j in range(4):
            msg_block.append(LSide[4*i+j])
        for j in range(4):
            msg_block.append(RSide[4*i+j])
    print(LSide)
    print(RSide)
    print(msg_block)
decrypt()
