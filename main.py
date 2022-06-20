def Encryption(text,key):
    initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                    60, 52, 44, 36, 28, 20, 12, 4,
                    62, 54, 46, 38, 30, 22, 14, 6,
                    64, 56, 48, 40, 32, 24, 16, 8,
                    57, 49, 41, 33, 25, 17, 9, 1,
                    59, 51, 43, 35, 27, 19, 11, 3,
                    61, 53, 45, 37, 29, 21, 13, 5,
                    63, 55, 47, 39, 31, 23, 15, 7]

    if len(text) == 64 and len(key)==64:
        # initial permutation
        temptext = ""
        for a in range(0, len(text)):
            temptext = temptext + text[initial_perm[a] - 1]
        text = temptext
        for step in range(1, 17):
            #left right split
            left=text[0:32]
            right = text[32:64]
            print("Left part: "+left)
            print("Right part: "+right)

            #round key
            for a in range(0,63):
                if (a+1)%8==0:
                    key.replace(key[a],"")
            #split key
            leftkey = key[0:28]
            rightkey= key[28:56]
            print("Left key: "+leftkey)
            print("Right key:"+rightkey)

            #rotation of key
            chartorotate=""
            if(a==1 or a==2 or a==9 or a==16):
                chartorotate=leftkey[0]
                leftkey = leftkey.replace(leftkey[0],"",1)
                leftkey=leftkey+chartorotate
                chartorotate=rightkey[0]
                rightkey=rightkey.replace(rightkey[0],"",1)
                rightkey=rightkey+chartorotate
            else:
                chartorotate= leftkey[0] + leftkey[1]
                leftkey=leftkey.replace(leftkey[0],"",1)
                leftkey=leftkey.replace(leftkey[0],"",1)
                leftkey=leftkey+chartorotate
                chartorotate=rightkey[0]+rightkey[1]
                rightkey= rightkey.replace(rightkey[0],"",1)
                rightkey= rightkey.replace(rightkey[0],"",1)
                rightkey=rightkey+chartorotate
                print("{step} .step Left key: ".format(step=step)+ leftkey)
                print("{step} .step Right key: ".format(step=step)+ rightkey)
            key = leftkey+rightkey

            #key 56 bit to 48 bit

            key_comp = [14, 17, 11, 24, 1, 5,
                        3, 28, 15, 6, 21, 10,
                        23, 19, 12, 4, 26, 8,
                        16, 7, 27, 20, 13, 2,
                        41, 52, 31, 37, 47, 55,
                        30, 40, 51, 45, 33, 48,
                        44, 49, 39, 56, 34, 53,
                        46, 42, 50, 36, 29, 32]
            key48 = ""

            for a in range(0,48):
                key48 = key48+key[key_comp[a]-1]

            print(key48)

            #f function
            #right part 32 bit to 48 bit expansion

            expandedright=""
            exp_d = [32, 1, 2, 3, 4, 5, 4, 5,
                     6, 7, 8, 9, 8, 9, 10, 11,
                     12, 13, 12, 13, 14, 15, 16, 17,
                     16, 17, 18, 19, 20, 21, 20, 21,
                     22, 23, 24, 25, 24, 25, 26, 27,
                     28, 29, 28, 29, 30, 31, 32, 1]

            for a in range(0,48):
                expandedright=expandedright+ right[exp_d[a]-1]

            #xor

            result= bin(int(expandedright,2) ^ int(key48,2))[2:]

            












Encryption("0010111000010100011011110110010001010011010010010001110000000110","0001110001100110000001101110001100011000001000111001110000101100")