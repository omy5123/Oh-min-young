using System;
using System.Linq;
using System.Collections.Generic;

namespace _island
{
    class _island
    {
        static int[] Point = new int[101];
        
        static int solution(int n, int[,] costs)
        {
            int answer = 0;
            List<Tuple<int, int, int>> arr = new List<Tuple<int, int, int>>();

            for (int i = 0; i < costs.GetLength(0); i++)
                arr.Add(new Tuple<int, int, int>(costs[i, 0], costs[i, 1], costs[i, 2]));

            
            arr = arr.OrderBy(x => x.Item3).ToList();

            int[] visit = new int[n];
            visit[0] = 1;

            for (int i = 0; i < n; i++)
            {
                Point[i] = i;
            }

            for (int i = 0; i < arr.Count; i++)
            {
                int start = Find(arr[i].Item1);
                int end = Find(arr[i].Item2);
                int cost = arr[i].Item3;


                if (start != end)
                {
                    Point[start] = end;

                    answer += cost;
                }
            }

        static int Find(int node)
        {
            if (node == Point[node]) return node;
            else return Point[node] = Find(Point[node]);
        }

            return answer;
        }
        
        static void Main(string[] args)
        {
            int n = 4;
            int[,] costs = new int[,] { { 0, 1, 1 }, { 0, 2, 2 }, { 1, 2, 5 }, { 1, 3, 1 }, { 2, 3, 8 } };
            Console.WriteLine(solution(n, costs));
        }
    }
}
