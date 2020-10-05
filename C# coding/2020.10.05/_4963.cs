using System;
using System.Collections.Generic;
using System.Text;

namespace _4963__섬의_개수_
{
    class Program
    {
        static int[,] arr;
        
        static void bfs(int i, int j,int w, int h)
        {
            Queue<(int, int)> que = new Queue<(int, int)>();
            que.Enqueue((i, j));
            arr[i, j] = 0;
            int[] dx = { -1, -1, 1, 1, 0, 0, 1, -1 };
            int[] dy = { -1, -0, 0, 1, -1, 1, -1, 1 };
            while (que.Count != 0)
            {
                (int a, int b) = que.Dequeue();
                for (int k = 0; k < 8; k++)
                {
                    int x = a + dx[k];
                    int y = b + dy[k];
                    if ((0 <= x && x < h) && (0 <= y && y < w) && arr[x, y] == 1)
                    {
                        que.Enqueue((x, y));
                        arr[x, y] = 0;
                    }
                }
            }

        }
        static void Main(string[] args)
        {
            
            StringBuilder sb = new StringBuilder();
            while (true)
            {
                string[] wh = Console.ReadLine().Split();
                int w = int.Parse(wh[0]);
                int h = int.Parse(wh[1]);
                if (w == 0 && h == 0)
                    break;
                if(w == 1 && h == 1)
                {
                    int line = int.Parse(Console.ReadLine());
                    if (line == 1)
                    {
                        sb.Append(1).AppendLine();
                    }
                    else
                    {
                        sb.Append(0).AppendLine();
                    }
                    continue;
                }
                arr = new int[h, w];
                for (int i = 0; i < h; i++)
                {
                    string[] line = Console.ReadLine().Split();
                    for (int j = 0; j < w; j++)
                    {
                        arr[i, j] = int.Parse(line[j].ToString());
                    }
                }
                int cnt = 0;
                for (int i = 0; i < h; i++)
                {
                    for (int j = 0; j < w; j++)
                    {
                        if (arr[i, j] == 1)
                        {
                            bfs(i, j,w,h);
                            cnt += 1;
                        }
                    }
                }
                sb.Append(cnt).AppendLine();
                
            }
            Console.WriteLine(sb);
        }
    }
}
