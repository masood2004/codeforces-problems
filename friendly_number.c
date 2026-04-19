#include <stdio.h>
#include <stdlib.h>

long long digit_sum(long long n);

int main(void)
{

    int t;
    scanf("%d", &t);

    while (t-- > 0)
    {
        int count = 0;
        long long x;
        scanf("%lld", &x);
        for (long long i = (x + 1); i <= (x + 90); i++)
        {
            if ((i - digit_sum(i)) == x)
            {
                count++;
            }
        }
        printf("%d\n", count);
    }

    return 0;
}

long long digit_sum(long long n)
{
    long long sum = 0;
    while (n > 0)
    {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}