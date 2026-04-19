#include <stdio.h>
#include <stdbool.h>

int main()
{
    int t;
    // 1. Read the number of test cases
    if (scanf("%d", &t) != 1)
        return 0;

    while (t--)
    {
        int k;
        int a1, b1, a2, b2;

        // 2. Read the parameters for this specific test case
        scanf("%d", &k);
        scanf("%d %d", &a1, &b1);
        scanf("%d %d", &a2, &b2);

        // 3. Force the absolute best-case scenario for Bob
        int a3 = 0;
        int b3 = k;

        // 4. Calculate final totals based on the perfect state
        int alice_score = a1 + a2 + a3;
        int bob_score = b1 + b2 + b3;

        // 5. Evaluate the logic we extracted
        bool bob_wins = (bob_score > alice_score) ||
                        ((bob_score == alice_score) && ((b1 > a1) + (b2 > a2) >= 1));

        // 6. Output exactly what the judge expects
        if (bob_wins)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}