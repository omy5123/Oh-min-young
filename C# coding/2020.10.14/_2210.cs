using System;
using System.Collections.Generic;

namespace _2210__숫자판_점프_
{
    class Program
    {
        
        static int[] dx = { -1, 1, 0, 0 };
        static int[] dy = { 0, 0, -1, 1 };
        static int[,] arr;
        static List<string> list = new List<string>();
        static void dfs(int i, int j,string str)
        {
            if (str.Length == 6)
            {
                if (list.Contains(str) == true)
                {
                    return;
                }
                else
                {
                    list.Add(str);
                    return;
                }
            }
            else
            {
                
                for (int k = 0; k < 4; k++)
                {
                    int x = dx[k] + i;
                    int y = dy[k] + j;
                    if ((0 <= x && x < 5) && (0 <= y && y < 5))
                    {
                        
                        dfs(x, y,str+arr[x,y].ToString());
                        
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            arr = new int[5, 5];
            for (int i = 0; i < 5; i++)
            {
                string[] str = Console.ReadLine().Split();
                for (int j = 0; j < 5; j++)
                {
                    arr[i, j] = int.Parse(str[j]);
                }
            }
            
            for (int i = 0; i < 5; i++)
            {
                for (int j = 0; j < 5; j++)
                {
                    dfs(i, j,arr[i,j].ToString());
                }
            }
                
            
            Console.WriteLine(list.Count);
        }
    }
}
