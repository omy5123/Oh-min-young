using System;

namespace _1120__문자열_
{
    class _1120
    {
        static void Main(string[] args)
        {
            string[] ab = Console.ReadLine().Split();
            string a = ab[0];
            string b = ab[1];
            int min = 50;
            for (int i = 0; i < b.Length - a.Length + 1; i++)
            {
                int cnt = 0;
                for (int j = 0; j < a.Length; j++)
                {
                    if (a[j] != b[i + j])
                    {
                        cnt += 1;
                    }
                }
                if (min > cnt)
                {
                    min = cnt;
                }
            }
            Console.WriteLine(min);

        }
    }
}
