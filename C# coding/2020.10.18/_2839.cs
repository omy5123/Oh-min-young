using System;

namespace _2839
{
    class _2839
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int answer = 0;
            while (true)
            {
                if(n%5 == 0)
                {
                    answer += n / 5;
                    Console.WriteLine(answer);
                    break;
                }
                n = n - 3;
                answer += 1;
                if (n<0)
                {
                    Console.WriteLine(-1);
                    break;
                }
            }
        }
    }
}
