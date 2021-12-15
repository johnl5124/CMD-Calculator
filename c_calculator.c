#include <stdio.h>
#include <stdlib.h>

// cmd calculator in C

int addition(x, y)
{
    return x + y;
}

int subtraction(x, y)
{
    return x - y;
}

int main()
{
    int user_input, answer, x, y, counter = 1;
    
    printf("-------------CALCULTOR MENU-------------\n");
    printf("Please enter a number (1-5): ");
    // below is casting an int to 
    scanf("%d", &user_input);
    
    while (counter == 1)
    {
        switch (user_input)
        {
            case 1:
                printf("You have selected Addition \n");
                printf("Please enter a number: ");
                scanf("%d", &x);
                printf("Please enter a number: ");
                scanf("%d", &y);
                answer = addition(x, y);
                printf("Answer: %d \n", answer);
            break;
            case 2:
                printf("You have selected Subtraction \n");
                printf("Please enter a number: ");
                scanf("%d", &x);
                printf("Please enter a number: ");
                scanf("%d", &y);
                answer = subtraction(x, y);
                printf("Answer: %d \n", answer);
            break;
            case 3:
                printf("You have selected Multiplication \n");
            break;
            case 4:
                printf("You have selected Division \n");  
            break;
            case 5:
                printf("Thankyou! Exiting...");
                exit(0);
            break;
        }
        printf("Please enter a number (1-5): ");
        // below is casting an int to 
        scanf("%d", &user_input);
    }

}

