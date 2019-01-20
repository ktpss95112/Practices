#include<stdio.h>
#include<stdlib.h>

void init(){
    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
}

int main(){
    init();

    char flag[] = "MyFirstCTF{THIS_IS_THE_FAKE_FLAG}";
    char buf[0x30];

    memset( buf , 0 , sizeof( buf ) );

    puts( "Say hello to the stack :D" );

    read( 0 , buf , 0x2f );

    printf( "You said:" );
    printf( buf );

    return 0;
}