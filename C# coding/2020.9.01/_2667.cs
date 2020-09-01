using System;
using System.Collections.Generic;

namespace _2667__BFS_
{
    class _2667
    {
        static int[,] arr;
        static int[] dx = {-1,1,0,0};
        static int[] dy = { 0, 0, -1, 1 };
        static List<int> count = new List<int>();
        static Queue<(int,int)> que = new Queue<(int,int)>();
        static void bfs(int i,int j,int n, int[,] arr)
        {
            arr[i, j] = 0;
            int cnt = 1; 
            que.Enqueue((i, j));
            while (!(que.Count==0))
            {
                (int a ,int b) = que.Dequeue();
                for (int k = 0; k < 4; k++)
                {
                    int x = a + dx[k];
                    int y = b + dy[k];
                    if ((0 <= x && x<n) && (0<=y && y<n) && (arr[x,y] == 1))
                    {
                        arr[x, y] = 0;
                        cnt += 1;
                        que.Enqueue((x, y));
                    }
                }
            }
            count.Add(cnt);
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            arr = new int[n,n];
            for (int i = 0; i < n; i++)
            {
                string line = Console.ReadLine();
                for (int j = 0; j < line.Length; j++)
                {
                    arr[i,j] = int.Parse(line[j].ToString());
                }
            }
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (arr[i,j]==1)
                    {
                        bfs(i, j,n,arr);
                    }
                }
            }
            count.Sort();
            Console.WriteLine(count.Count);
            foreach (int c in count)
            {
                Console.WriteLine(c);
            }
        }
    }
}
