using System;
using System.Collections;
using System.Collections.Generic;

namespace _14502__브루트포스__bfs_
{
    class _14502
    {
        static int n = 0;
        static int m = 0;
        static int[,] arr = { };
        static int[,] copy = { };
        static int [] dx = { -1, 1, 0, 0 };
        static int [] dy = { 0, 0, -1, 1 };
        static Queue<(int, int)> que = new Queue<(int, int)>();
        static int cnt = 0;
        static void bfs()
        {
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    if (arr[i,j] == 2)
                    {
                        que.Enqueue((i, j));
                    }
                }
            }
            int count = 0;
            for (int s = 0; s < n; s++)
            {
                for (int q = 0; q < m; q++)
                {
                    copy[s, q] = arr[s, q];
                }
            }
            while ((que.Count) != 0)
            {
                (int a, int b) = que.Dequeue();
                for (int k = 0; k < 4; k++)
                {
                    int x = dx[k] + a;
                    int y = dy[k] + b;
                    if ((0<=x&&x<n)&&(0<=y&&y<m)&&(copy[x,y]==0))
                    {
                        copy[x, y] = 2;
                        que.Enqueue((x, y));
                    }
                }
            }
            for (int s = 0; s < n; s++)
            {
                for (int q = 0; q < m; q++)
                {
                    if (copy[s,q]==0)
                    {
                        count += 1;
                    }
                }
            }
            if (cnt < count)
            {
                cnt = count;
            }


        }
        static void dfs(int cnt)
        {
            if (cnt == 3)
            {
                bfs();
            }
            else
            {
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < m; j++)
                    {
                        if (arr[i,j] == 0)
                        {
                            arr[i, j] = 1;
                            dfs(cnt + 1);
                            arr[i, j] = 0;
                        }
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            n = int.Parse(nm[0]);
            m = int.Parse(nm[1]);
            arr = new int[n, m];
            copy = new int[n, m];
            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split();
                for (int j = 0; j < m; j++)
                {
                    arr[i, j] = int.Parse(line[j]);
                }
            }

            dfs(0);
            Console.WriteLine(cnt);
        }
    }
}
