using System;

namespace _2023__신기한_소수_
{
    class _2023
    {
        static bool sosu(int num)
        {
            bool check = true;
            for (int i = 2; i < num; i++)
            {
                if (num % i == 0)
                {
                    check = false;
                    break;
                }
            }
            if (check)
            {
                return check;
            }
            else
                return check;
        }
        static void dfs(string s, int n)
        {
            if (s.Length == n)
            {
                Console.WriteLine(s);
            }
            else
            {
                for (int i = 1; i <= 9; i++)
                {
                    if (sosu(int.Parse(s + i.ToString())))
                    {
                        dfs(s + i.ToString(), n);
                    }
                    
                }
            }
        }
        static void solution(int n)
        {
            int[] answer = { 2, 3, 5, 7 };
            for (int i = 0; i < answer.Length; i++)
            {
                string s = answer[i].ToString();
                dfs(s, n);
            }
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            solution(n);
        }
    }
}
