#include<stdio.h>

// cmd calculator in C

int addition(x, y)
{
    return x + y;
}

int main(void)
{
    int user_input, answer, x, y;
    
    printf("-------------CALCULTOR MENU-------------\n");
    printf("Please enter a number (1-5): ");
    // below is casting an int to 
    scanf("%d", &user_input);
    
    switch (user_input)
    {
        case 1:
            printf("You have selected Addition");
            printf("Please enter a number: ");
            scanf("%d", &x);
            printf("Please enter a number: ");
            scanf("%d", &y);
            answer = addition(x, y);
            printf("Answer: %d \n", answer);
        break;
    }
}

