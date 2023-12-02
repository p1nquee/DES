IP = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
)

IP_INV = (
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
)

PC1 = (
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
)

PC2 = (
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
)

E = (
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
)

Sboxes = {
    0: {
        0: (14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7),
        1: (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8),
        2: (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0),
        3: (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13)
    },
    1: {
        0: (15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10),
        1: (3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5),
        2: (0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15),
        3: (13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9)
    },
    2: {
        0: (10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8),
        1: (13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1),
        2: (13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7),
        3: (1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12)
    },
    3: {
        0: (7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15),
        1: (13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9),
        2: (10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4),
        3: (3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14)
    },
    4: {
        0: (2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9),
        1: (14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6),
        2: (4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14),
        3: (11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3)
    },
    5: {
        0: (12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11),
        1: (10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8),
        2: (9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6),
        3: (4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13)
    },
    6: {
        0: (4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1),
        1: (13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6),
        2: (1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2),
        3: (6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12)
    },
    7: {
        0: (13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7),
        1: (1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2),
        2: (7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8),
        3: (2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11)
    }
}

P = (
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
)

P_INV = (
    9, 17, 23, 31,
    13, 28, 2, 18,
    24, 16, 30, 6,
    26, 20, 10, 1,
    8, 14, 25, 3,
    4, 29, 11, 19,
    32, 12, 22, 7,
    5, 27, 15, 21
)

key = list(input('Введите ключик:      (7 символов)  =>'))
msg = list(input('Введите сообщеньице: (8 символов)  =>'))

for i in range(len(key)):
    key[i] = bin(ord(key[i]))

msgG = msg

for i in range(len(msg)):
    msg[i] = bin(ord(msg[i]))

def razdelit_bite(spisok):
    result = {}
    for i in range(len(spisok)):
        result[i] = tuple(spisok[i][2:].zfill(8))
    return result

keyy = razdelit_bite(key)
msgg = razdelit_bite(msg)

def fill_block(bites, message=False):
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
msg_block = fill_block(msgg, message=True)

def key_conversion():
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
    Ki1 = []
    Ki2 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []}
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
            Ki1.append(C+D)
        else:
            C.append(C[0])
            del C[0]
            D.append(D[0])
            del D[0]
            Ki1.append(C+D)
    for i in range(16):
        for j in range(48):
            Ki2[i].append(Ki1[i][PC2[j]-1])
    return Ki2

Ki = key_conversion()

def msg_delenie():
    L = []
    R = []
    for i in range(64):
        if 0 <= i <= 3 or 8 <= i <= 11 or 16 <= i <= 19 or 24 <= i <= 27 or 32 <= i <= 35 or 40 <= i <= 43 or 48 <= i <= 51 or 56 <= i <= 59:
            L.append(msg_block[i])
        else:
            R.append(msg_block[i])
    return L, R

LSide, RSide = msg_delenie()

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

def function_f(RS, K):
    ERi = []
    Bii = ''
    for i in range(48):
        ERi.append(RS[E[i]-1])
    Bi1 = []
    for i in range(48):
        Bi1.append(ERi[i] ^ K[i])
    Bi = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for i in range(8):
        for j in range(6):
            Bi[i].append(Bi1[6*i+j])
    for i in range(8):
        b1b6 = binnot(int(str(Bi[i][0])+str(Bi[i][5])))
        b2tob5 = binnot(int(str(Bi[i][1])+str(Bi[i][2])+str(Bi[i][3])+str(Bi[i][4])))
        Bii += bin(Sboxes[i][b1b6][b2tob5])[2:].zfill(4)
    Bii = list(Bii)
    for i in range(32):
        Bii[i] = int(Bii[i])
    PB = []
    for i in range(32):
        PB.append(Bii[P[i]-1])
    return PB

func1 = function_f(RSide, Ki[0])
L1 = RSide
R1 = []
for i in range(32):
    k = L1[i] ^ func1[i]
    R1.append(k)

func2 = function_f(R1, Ki[1])
L2 = R1
R2 = []
for i in range(32):
    k = L2[i] ^ func2[i]
    R2.append(k)

func3 = function_f(R2, Ki[2])
L3 = R2
R3 = []
for i in range(32):
    k = L3[i] ^ func3[i]
    R3.append(k)

func4 = function_f(R3, Ki[3])
L4 = R3
R4 = []
for i in range(32):
    k = L4[i] ^ func4[i]
    R4.append(k)

func5 = function_f(R4, Ki[4])
L5 = R4
R5 = []
for i in range(32):
    k = L5[i] ^ func5[i]
    R5.append(k)

func6 = function_f(R5, Ki[5])
L6 = R5
R6 = []
for i in range(32):
    k = L6[i] ^ func6[i]
    R6.append(k)

func7 = function_f(R6, Ki[6])
L7 = R6
R7 = []
for i in range(32):
    k = L7[i] ^ func7[i]
    R7.append(k)

func8 = function_f(R7, Ki[7])
L8 = R7
R8 = []
for i in range(32):
    k = L8[i] ^ func8[i]
    R8.append(k)

func9 = function_f(R8, Ki[8])
L9 = R8
R9 = []
for i in range(32):
    k = L9[i] ^ func9[i]
    R9.append(k)

func10 = function_f(R9, Ki[9])
L10 = R9
R10 = []
for i in range(32):
    k = L10[i] ^ func10[i]
    R10.append(k)

func11 = function_f(R10, Ki[10])
L11 = R10
R11 = []
for i in range(32):
    k = L11[i] ^ func11[i]
    R11.append(k)

func12 = function_f(R11, Ki[11])
L12 = R11
R12 = []
for i in range(32):
    k = L12[i] ^ func12[i]
    R12.append(k)

func13 = function_f(R12, Ki[12])
L13 = R12
R13 = []
for i in range(32):
    k = L13[i] ^ func13[i]
    R13.append(k)

func14 = function_f(R13, Ki[13])
L14 = R13
R14 = []
for i in range(32):
    k = L14[i] ^ func14[i]
    R14.append(k)

func15 = function_f(R14, Ki[14])
L15 = R14
R15 = []
for i in range(32):
    k = L15[i] ^ func15[i]
    R15.append(k)

func16 = function_f(R15, Ki[15])
L16 = R15
R16 = []
for i in range(32):
    k = L16[i] ^ func16[i]
    R16.append(k)

ciphher = []

for i in range(8):
    for j in range(4):
        ciphher.append(L16[4*i+j])
    for j in range(4):
        ciphher.append(R16[4*i+j])

last_form_of_cipher = []

for i in range(64):
    last_form_of_cipher.append(ciphher[IP_INV[i]-1])

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

print('Ваше зашифрованное сообщеньице:    =>', encrypted)

print('==================посимвольно==================')

for i in range(4):
    print('                     |    |')

print('                     \    /')

print('                      \  /')

print('                       \/')

print('', list(encrypted))

input()