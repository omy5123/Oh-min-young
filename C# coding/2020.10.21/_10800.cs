using System;
using System.Collections.Generic;
using System.Drawing;

namespace _10800__컬러볼_
{
    class _10800
    {
        struct Cor
        {
            public int x;
            public int y;
            public int z;
        }
        static int[] solution(int n, int[,]arr)
        {
            Cor[] ball = new Cor[n];
            for (int i = 0; i < n; i++)
            {
                ball[i].x = arr[i, 1];
                ball[i].y = arr[i, 0];
                ball[i].z = i;
            }
            Array.Sort(ball, delegate (Cor u, Cor v)
            {
                if(u.x<v.x)
                {
                    return -1;
                }
                else if(u.x>v.x)
                {
                    return 1;
                }
                else
                {
                    if(u.y<v.y)
                    {
                        return -1;
                    }
                    else if(u.y>v.y)
                    {
                        return 1;
                    }
                    else
                    {
                        if(u.z<v.z)
                        {
                            return -1;
                        }
                        else if(u.z>v.z)
                        {
                            return 1;
                        }
                        else
                        {
                            return 0;
                        }
                    }
                }
            });

            int[] color = new int[n];
            int su = 0;
            int j = 0;
            int[] res = new int[n];
            for (int i = 0; i < ball.Length; i++)
            {
                while(ball[j].x < ball[i].x)
                {
                    su += ball[j].x;
                    color[ball[j].y - 1] += ball[j].x;
                    j += 1;
                }
                res[ball[i].z] = su - color[ball[i].y - 1];
            }
            return res;
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int[,] arr = new int[n, 2];
            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split();
                for (int j = 0; j < 2; j++)
                {
                    arr[i, j] = int.Parse(line[j]);
                }
            }
            int[]result = solution(n, arr);

            for (int i = 0; i < result.Length; i++)
            {
                Console.WriteLine(result[i]);
            }
        }
    }
}
