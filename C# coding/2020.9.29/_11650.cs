using System;
using System.Text;

namespace _11650__좌표_정렬하기_
{
    class _11650
    {
        struct Cor
        {
            public int x;
            public int y;
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            Cor[] arr = new Cor[n];
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++)
            {
                string[] st = Console.ReadLine().Split();
                arr[i].x = int.Parse(st[0]);
                arr[i].y = int.Parse(st[1]);
            }
            Array.Sort(arr, delegate (Cor u, Cor v)
            {
                if (u.x < v.x)
                {
                    return -1;
                }
                else if (u.x > v.x)
                {
                    return 1;
                }
                else
                {
                    if (u.y < v.y)
                    {
                        return -1;
                    }
                    else if (u.y > v.y)
                    {
                        return 1;
                    }
                    else
                    {
                        return 0;
                    }
                }
            });

            for (int i = 0; i < n; i++)
            {
                sb.Append(arr[i].x);
                sb.Append(" ");
                sb.Append(arr[i].y).AppendLine();
            }
            Console.WriteLine(sb);
        }
    }
}
