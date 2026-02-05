#include <stdio.h>
#include <string.h>

int getCPUInfo() {
    FILE *fp = popen("lscpu", "r");
    if(!fp) return 1;
    char buf[128];
    int cores = 0; 
    while (fgets(buf, sizeof(buf), fp)) {
        if (strstr(buf, "CPU(s):")) {
            sscanf(buf, "CPU(s): %d", &cores);
            break;
        }
    }
    pclose(fp);
    return cores;
}