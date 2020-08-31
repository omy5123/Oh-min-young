using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.Collections;

namespace _2630__색종이만들기_
{
    class _2630
    {
        static int w = 0;
        static int bi = 0;

        static void cut(int a, int b, int n,List<List<string>> arr)
        {
            string check = arr[a][b];
            for (int i = a; i < a+n; i++)
            {
                for (int j = b; j < b+n; j++)
                {
                    if (check != arr[i][j])
                    {
                        cut(a, b, n / 2, arr);
                        cut(a, b + n / 2, n / 2, arr);
                        cut(a + n / 2, b, n / 2, arr);
                        cut(a + n / 2, b + n / 2, n / 2, arr);
                        return;
                    }
                }
            }
            if (check == "0")
            {
                 w += 1;
                return;
            }
            else
            {
                bi += 1;
                return;
            }
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            List<string> line = new List<string>();
            List<List<string>> arr = new List<List<string>>();
            for (int i = 0; i < n; i++)
            {
                line.Add(Console.ReadLine());
                arr.Add(line[i].Split().ToList());
            }
            cut(0, 0, n, arr);
            Console.WriteLine(w);
            Console.WriteLine(bi);
        }
    }
}
