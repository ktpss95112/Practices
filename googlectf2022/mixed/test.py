

def print_lines(co):
    prev = None
    for st, en, li in co.co_lines():
        if li != prev:
            print(li, st, list(co.co_code[st:en]), sep='\t')
            prev = li
        else:
            print('', st, list(co.co_code[st:en]), sep='\t')




def test():
    import marshal

    # content = open('__pycache__/module.cpython-311.pyc', 'rb').read()
    content = open('x.pyc', 'rb').read()

    content = content[4:] # magic
    content = content[4:] # ts
    content = content[8:] # older-style timestamp and size

    co = marshal.loads(content)

    # co = co.co_consts[0]
    co = co.co_consts[2]
    print(co)

    for attrb in dir(co):
        print(f'  co.{attrb} = {getattr(co, attrb)}')

    print(list(co.co_code))
    print_lines(co)

    print('\n\n\n\n\n\n')
    print(*map(repr, co.co_consts), sep='\n')
    print()
    print(*map(repr, co.co_names), sep='\n')


def fail(*args, **kwargs):
    print(*args, **kwargs)
    exit(1)


def gen():
    import dis

    import random
    import time

    ks = lambda seed: None

    def game3():
        # ('t', 'text', 'words', 'it', 'log', 'inp')
        print('Speed typing game.')
        t = time.time()
        text = '\n  Text: Because of its performance advantage, today many language implementations\n  execute a program in two phases, first compiling the source code into bytecode,\n  and then passing the bytecode to the virtual machine.\n  '
        words = text.split()
        it = 1
        log = '_'
        while it != len(words):
            print(
                '%0.2f seconds left.' % (20 - (time.time() - t)),
                '\x1b[32m',
                ' '.join(words),
                '\x1b[39m ',
                words[it],
            ) # not pretty sure, but doesn't matter

            inp = input()
            if time.time() > t + 20:
                fail('Too slow!')
            if inp == words[it]:
                log += words[it].upper() + '_'
                it += 1
            else: fail('You made a mistake!')

        print('Nice!')
        return log

    def game2():
        print('Math quiz time!')

        qs = (('sum', 12, 5), ('difference', 45, 14), ('product', 8, 9), ('ratio', 18, 6), ('remainder from division', 23, 7))
        log = '_'
        for q in qs:
            print('What is the %s of %d and %d?' % q)
            x, a, b = q

            if x == 'sum': r = a + b
            elif x == 'difference': r = a - b
            elif x == 'product': r = a * b
            elif x == 'ratio': r = a // b
            elif x == 'remainder from division': r = a % b
            else: fail('What?')

            inp = int(input())
            if inp == r:
                print('Correct!')
                log += str(inp) + '_'
            else:
                fail('Wrong!')
        return log


    def main():
        print('Pass 3 tests to prove your worth!')
        seed = 'seed:'
        seed += game1() + ':'
        print(seed)
        seed += game2() + ':'
        print(seed)
        seed += game3()
        print(seed)
        print()
        print("You can drive to work, know some maths and can type fast. You're hired!")
        print(
            'Your sign-on bonus:',
            cry(
                b'\xa0?n\xa5\x7f)\x1f6Jvh\x95\xcc!\x1e\x95\x996a\x11\xf6OV\x88\xc1\x9f\xde\xb50\x9d\xae\x14\xde\x18YHI\xd8\xd5\x90\x8a\x181l\xb0\x16^O;]',
                seed,
            ).decode(),
        )

    def ks(seed):
        random.seed(seed)
        while True:
            yield (random.randint(0, 255) * 13 + 17) % 256

    co = ks.__code__
    print(dis.dis(ks))
    print(list(co.co_code))
    print(co.co_names)
    print()

    print_lines(co)

    # for l in co.co_lines():
    #     print(l)


# gen()
test()
