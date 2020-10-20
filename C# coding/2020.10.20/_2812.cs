using System;

namespace _2812__크게_만들기_
{
    class _2812
    {
        static string solution(int n, int k, int num)
        {
            string num_str = num.ToString();
            string result = "";
            int idx = 0;
            for (int i = 0; i < n - k; i++)
            {
                int max = 0;
                for (int j = idx; j < i+k+1; j++)
                {
                    if (max < int.Parse(num_str[j].ToString()))
                    {
                        max = int.Parse(num_str[j].ToString());
                        idx = j + 1;
                    }
                }
                result += max.ToString();
            }
            return result;
        }
        static void Main(string[] args)
        {
            string[] nk = Console.ReadLine().Split();
            int n = int.Parse(nk[0]);
            int k = int.Parse(nk[1]);

            int num = int.Parse(Console.ReadLine());
            Console.WriteLine(solution(n, k, num));
        }
    }
}
