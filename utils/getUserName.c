#include <unistd.h>

char * getUserName() {
    char *userName = getlogin();
    return userName;
}