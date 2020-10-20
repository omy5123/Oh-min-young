using System;

namespace _1940__주몽_
{
    class _1940
    {
        static int solution(int n, int m, int[] arr)
        {
            int answer = 0;
            for (int i = 0; i < n-1; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    if (arr[i] + arr[j] == m)
                    {
                        answer += 1;
                    }
                }
            }
            return answer;
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int m = int.Parse(Console.ReadLine());
            int[] arr = new int[n];
            string[] line = Console.ReadLine().Split();
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(line[i]);
            }
            Console.WriteLine(solution(n, m, arr));
        }
    }
}
