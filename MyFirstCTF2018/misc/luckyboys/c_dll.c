#include <time.h>
#include <stdlib.h>

void initialize(){
    srand(time(0));
}

int test(){
    return time(0);
}

int get_rand(){
    return rand();
}
