using System;
using System.Collections.Generic;

namespace _두개_뽑아서_더하기
{
    class _numbers
    {
        static List<int> list = new List<int>();
        static void dfs(int cnt, int[] numbers, int k, int sum)
        {
            if (cnt == 2)
            {
                if (list.Contains(sum) == false)
                {
                    list.Add(sum);
                }
            }
            else
            {
                for (int i = k; i < numbers.Length; i++)
                {
                    sum += numbers[i];
                    dfs(cnt + 1, numbers, i + 1, sum);
                    sum -= numbers[i];
                }
            }
        }
        static void solution(int[] numbers)
        {

            dfs(0, numbers, 0, 0);
            list.Sort();
            foreach (var item in list)
            {
                Console.Write(item+" ");
            }

        }
        static void Main(string[] args)
        {
            int[] numbers = new int[] { 2, 1, 3, 4, 1 };
            solution(numbers);
        }
    }
}
