using System;

namespace _1065__브루트포스_
{
    class _1065
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int cnt = 0;
            for (int i = 1; i < n+1; i++)
            {
                if (i < 10)
                {
                    cnt += 1;
                }
                else if (10<=i && i < 100)
                {
                    cnt += 1;
                }
                else
                {
                    int a = i / 100;
                    int b = (i % 100) / 10;
                    int c = i % 10;
                    if ((b-a)==(c-b))
                    {
                        cnt += 1;
                    }
                }
            }
            Console.WriteLine(cnt);
        }
    }
}
