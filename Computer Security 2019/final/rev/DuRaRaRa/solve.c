#include <stdio.h>
#include <string.h>

int main(){
    char pool[] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+,-./:;<=>?@[]^_`|~";
    int len = strlen( pool );

    int nums[4] = {2088968667, 2090886842, 2088324326, 2088287370};
    char other[8];
    *(int*)&other[4] = 825391428;
    *(int*)other = 791689773;
    char flag[17] = {0};

    for( int i = 0; i < len; ++i ){
        for( int j = 0; j < len; ++j ){
            for( int k = 0; k < len; ++k ){
                for( int l = 0; l < len; ++l ){
                    
                    for( int _index = 0; _index < 4; ++_index ){
                        if( pool[i] == other[_index+4] &&\
                            pool[j] == other[_index] &&\
                            ( pool[l] + 33*( pool[k] + 33*( pool[j] + 33*pool[i] ) ) ) + 2086473605 == nums[_index]
                        ){
                            printf("i: %d , %c%c%c%c\n", _index, pool[i], pool[j], pool[k], pool[l]);
                            flag[4*_index] = pool[i];
                            flag[4*_index+1] = pool[j];
                            flag[4*_index+2] = pool[k];
                            flag[4*_index+3] = pool[l];
                        }
                    }

                }
            }
        }
    }
    // FLAG{D-Day:2020/01/14}

    return 0;
}
