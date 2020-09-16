using System;

namespace _network
{
    class _network
    {
        static void dfs(int k, int[,] computers, int[] visit, int n)
        {
            visit[k] = 1;
            for (int i = 0; i < n; i++)
            {
                if (visit[i] == 0 && computers[k, i] == 1)
                {
                    dfs(i, computers, visit, n);
                }
            }
        }
        static int solution(int n, int[,] computers)
        {
            int answer = 0;
            int[] visit = new int[n];

            for (int i = 0; i < n; i++)
            {
                if (visit[i] == 0)
                {
                    dfs(i, computers, visit, n);
                    answer += 1;
                }
            }
            return answer;
        }
        static void Main(string[] args)
        {
            int n = 3;
            int[,] computers = { { 1, 1, 0 }, { 1, 1, 0 }, {0, 0, 1 }};
            Console.WriteLine(solution(n, computers));
        }
    }

}
