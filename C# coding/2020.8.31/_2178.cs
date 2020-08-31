using System;
using System.Collections.Generic;
using System.Linq;

namespace _2178__BFS_
{
    class _2178
    {
        static int[,] arr; 
        static int[] dx = { -1, 1, 0, 0 };
        static int[] dy = { 0, 0, -1, 1 };
        static Queue<(int,int)> que = new Queue<(int,int)>(); 

        static void bfs(int x,int y,int n,int m,int[,] arr)
        {
            que.Enqueue((x, y));
            while (!(que.Count==0))
            {
                (int a,int b) = que.Dequeue();
                for (int i = 0; i < 4; i++)
                {
                    x = dx[i] + a;
                    y = dy[i] + b;
                    if ((0<=x && x<n) && (0<= y&& y<m) && (arr[x,y] == 1))
                    {
                        que.Enqueue((x, y));
                        arr[x, y] = arr[a, b] + 1;
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            string[] a = Console.ReadLine().Split();
            int n = int.Parse(a[0]);
            int m = int.Parse(a[1]);
            arr = new int[n, m]; 
            for (int i = 0; i < n; i++)
            {
                string line = Console.ReadLine();
                for (int j = 0; j < line.Length; j++)
                {
                    arr[i,j] = int.Parse(line[j].ToString());
                }
            }
            bfs(0, 0,n,m,arr);
            Console.WriteLine(arr[n-1,m-1]);
        }
    }
}
