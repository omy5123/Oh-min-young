using System;
using System.Text;

namespace _큰수_만들기
{
    class _maxnum
    {
        static string solution(string number, int k)
        {
            int idx = 0;
            char max;
            StringBuilder str = new StringBuilder();

            for (int i = 0; i < number.Length - k; i++)
            {
                max = '0';
                for (int j = idx; j <= k + i; j++)
                {
                    if (max < number[j])
                    {
                        max = number[j];
                        idx = j + 1;
                    }
                }
                str.Append(max);
            }
            return str.ToString();
        }
        static void Main(string[] args)
        {
            string number = "1231234";
            string result = solution(number, 3);
            Console.WriteLine(result);
        }
    }
}
