using System;
using System.Collections;
using System.Collections.Generic;

namespace _게임_맵_최단거리
{
    class _game
    {
        static int n = 0;
        static int m = 0;
        static int[] dx = { -1, 1, 0, 0 };
        static int[] dy = { 0, 0, -1, 1 };
        static int[,] arr = new int[5, 5];
        static Queue<(int, int)> que = new Queue<(int, int)>();

        static void bfs(int i,int j)
        {
            que.Enqueue((i, j));
            
            while (que.Count != 0)
            {
                (int a, int b) = que.Dequeue();
                
                for (int k = 0; k < 4; k++)
                {
                    int x = a + dx[k];
                    int y = b + dy[k];
                    if ((0<= x&& x< n)&& (0<=y&&y<m)&&(arr[x,y] == 1))
                    {
                        que.Enqueue((x, y));
                        arr[x, y] = arr[a, b] + 1;
                        Console.WriteLine(arr[x, y]);
                    }
                }
            }
        }
        static void solution(int[,] arr)
        {
            n = arr.GetLength(0);
            m = arr.GetLength(1);

            bfs(0, 0);
            if (arr[n-1,m-1] == 1)
            {
                Console.WriteLine(-1);
            }
            else
            {
                Console.WriteLine(arr[n - 1, m - 1]);
            }
            
        }
        static void Main(string[] args)
        {
            arr = new int[5,5] { { 1,0,1,1,1},{ 1,0,1,0,1},{ 1,0,1,1,1},{ 1,1,1,0,1},{ 0,0,0,0,1 } };
            solution(arr);
        }
    }
}
