#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>
#include <stdbool.h>

// Helper function to check if a number is prime
bool isPrime(int n) {
    if(n<=1) return false;
    if(n<=3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6) 
        if (n % i == 0 || n % (i + 2) == 0) return false;
    return true;
}

double findPrimesInParallel(int upperLimit, int N) {
    struct timespec start, end;
    int rangeSize = upperLimit / N;
    
    // Start the timer
    clock_gettime(CLOCK_MONOTONIC, &start);

    for(int i=0;i<N;i++) {
        pid_t pid = fork();

        if(pid<0) {
            perror("Fork failed");
            exit(1);
        } else if (pid == 0) {
            // Child Process logic
            int startRange = (i * rangeSize) + 1;
            // Ensure the last child covers the remainder if upperLimit isn't perfectly divisible
            int endRange = (i == N - 1) ? upperLimit : (startRange + rangeSize - 1);
            
            int count = 0;
            for (int j=startRange;j<=endRange;j++) 
                if (isPrime(j)) count++;

            // Child exits after finishing work
            exit(0);
        }
    }
    // Parent waits for all N children to finish
    for(int i=0;i<N;i++) 
        wait(NULL);
    
    // Stop the timer
    clock_gettime(CLOCK_MONOTONIC, &end);

    // Calculate time taken in seconds
    double timeTaken = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;

    return timeTaken;
}