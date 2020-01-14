#define _GNU_SOURCE

#include <stdio.h>
#include <dlfcn.h>

static void (*real_srand)(unsigned int);

static void mtrace_init(void)
{
    real_srand = dlsym(RTLD_NEXT, "srand");
    if (NULL == real_srand) {
        fprintf(stderr, "Error in `dlsym`: %s\n", dlerror());
    }
}

void srand(unsigned seed)
{
    if(real_srand==NULL) {
        mtrace_init();
    }

    fprintf(stderr, "seed: %u\n", seed);
    real_srand(seed);
}
