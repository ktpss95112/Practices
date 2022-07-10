def ks(seed):
    random.seed(seed)
    while True:
        yield ((random.randint(0, 255) + 13) * 17) % 256

