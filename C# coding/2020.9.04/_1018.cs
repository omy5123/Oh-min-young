using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Globalization;

namespace _1018__브루트포스_
{
    class Program
    {
        static int n = 0;
        static int m = 0;
        static string[,] arr = { };
        static string[,] copy = { };
        static int[] dx = { -1, 1, 0, 0 };
        static int[] dy = { 0, 0, -1, 1 };
        static int cnt = int.MaxValue;
        static Queue<(int, int)> que = new Queue<(int, int)>();
        static void bfs(int i,int j)
        {
            if (copy[i,j] == "W")
            {
                string ch = "W";
                int count = 0;
                que.Enqueue((i, j));
                while (que.Count != 0)
                {
                    (int a, int b) = que.Dequeue();
                    if (a == 7 && b == 7)
                    {
                        return;
                    }
                    for (int k = 0; k < 4; k++)
                    {
                        int x = dx[k] + a;
                        int y = dy[k] + b;
                        if ((0 <= x && x < n) && (0 <= y && y < n))
                        {
                            if (copy[x, y] == ch)
                            {
                                count += 1;
                                que.Enqueue((x, y));
                                copy[x, y] = "B";
                            }
                            else
                            {
                                que.Enqueue((x, y));
                                
                            }
                        }
                    }
                }
                if (cnt > count)
                {
                    cnt = count;
                }
            }
            else if (copy[i, j] == "B")
            {
                string ch = "B";
                int count = 0;
                que.Enqueue((i, j));
                while (que.Count != 0)
                {
                    (int a, int b) = que.Dequeue();
                    if (a == 7 && b == 7)
                    {
                        return;
                    }
                    for (int k = 0; k < 4; k++)
                    {
                        int x = dx[k] + a;
                        int y = dy[k] + b;
                        if ((0 <= x && x < n) && (0 <= y && y < n))
                        {
                            if (copy[x, y] == ch)
                            {
                                count += 1;
                                que.Enqueue((x, y));
                                copy[x, y] = "W";
                            }
                            else
                            {
                                que.Enqueue((x, y));
                            }
                        }
                    }
                }
                if (cnt > count)
                {
                    cnt = count;
                }
            }

        }
        static void Main(string[] args)
        {
            string[] st = Console.ReadLine().Split();
            n = int.Parse(st[0]);
            m = int.Parse(st[1]);
            arr = new string[n, m];
            copy = new string[8, 8];
            for (int i = 0; i < n; i++)
            {
                string line = Console.ReadLine();
                for (int j = 0; j < line.Length; j++)
                {
                    arr[i,j] = line[j].ToString();
                }
            }
            int a = n - 8;
            int b = m - 8;
            for (int i = 0; i < a+1; i++)
            {
                for (int j = 0; j < b+1; j++)
                {
                    for (int q = 0; q < 8; q++)
                    {
                        for (int p = 0; p < 8; p++)
                        {
                            copy[q, p] = arr[q + i, p + j];
                        }
                    }
                    bfs(0, 0);
                }
            }
            Console.WriteLine(cnt);

        }
    }
}
