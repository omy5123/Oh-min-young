using System;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;

namespace _1249__swea_보급로_
{
    class _1249
    {
        static int n = 0;
        static int[,] arr = { };
        static int[,] visit = { };
        static int[] dx = { -1, 1, 0, 0 };
        static int[] dy = { 0, 0, -1, 1 };
        static Queue<(int, int)> que = new Queue<(int, int)>();
        static void bfs()
        {
            visit[0, 0] = 0;
            que.Enqueue((0, 0));
            while ((que.Count) != 0)
            {
                (int a, int b) = que.Dequeue();
                for (int k = 0; k < 4; k++)
                {
                    int x = dx[k] + a;
                    int y = dy[k] + b;
                    if ((0 <= x && x < n) && (0 <= y && y < n))
                    {
                        if (visit[x,y] == -1)
                        {
                            visit[x, y] = visit[a, b] + arr[x, y];
                            que.Enqueue((x, y));
                        }
                        else
                        {
                            if (visit[x,y] > visit[a,b]+arr[x,y])
                            {
                                visit[x, y] = visit[a, b] + arr[x, y];
                                que.Enqueue((x, y));
                            }
                            else
                            {
                                continue;
                            }

                        }
                      
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            int t = int.Parse(Console.ReadLine());
            
            for (int tr = 0; tr < t; tr++)
            {
                n = int.Parse(Console.ReadLine());
                arr = new int[n, n];
                visit = new int[n, n];
                for (int i = 0; i < n; i++)
                {
                    string line = Console.ReadLine();
                    for (int j = 0; j < line.Length; j++)
                    {
                        arr[i, j] = int.Parse(line[j].ToString());
                        visit[i, j] = -1;
                    }
                }
                bfs();
                Console.WriteLine(visit[n - 1, n - 1]);
            }
        }
    }
}
