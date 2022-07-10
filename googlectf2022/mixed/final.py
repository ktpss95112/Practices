import random

def ks(seed):
    random.seed(seed)
    while True:
        yield (random.randint(0, 255) * 13 + 17) % 256

def cry(s, seed):
    r = []
    for x, y in zip(ks(seed), s):
        r.append(x ^ y)
    return bytes(r)

def main():
    log1 = 'sssddwwddwddsssdssaaawwssaaaassddddddd'
    log2 = '_17_31_72_3_2_'
    log3 = '_BECAUSE_OF_ITS_PERFORMANCE_ADVANTAGE,_TODAY_MANY_LANGUAGE_IMPLEMENTATIONS_EXECUTE_A_PROGRAM_IN_TWO_PHASES,_FIRST_COMPILING_THE_SOURCE_CODE_INTO_BYTECODE,_AND_THEN_PASSING_THE_BYTECODE_TO_THE_VIRTUAL_MACHINE._'

    print('Pass 3 tests to prove your worth!')
    seed = 'seed:'
    seed += log1 + ':'
    print(seed)
    seed += log2 + ':'
    print(seed)
    seed += log3
    print(seed)
    print()
    print("You can drive to work, know some maths and can type fast. You're hired!")
    print(
        cry(
            b'\xa0?n\xa5\x7f)\x1f6Jvh\x95\xcc!\x1e\x95\x996a\x11\xf6OV\x88\xc1\x9f\xde\xb50\x9d\xae\x14\xde\x18YHI\xd8\xd5\x90\x8a\x181l\xb0\x16^O;]',
            seed,
        ).decode(),
    )

main()
# CTF{4t_l3ast_1t_w4s_n0t_4n_x86_opc0d3_p3rmut4tion}
