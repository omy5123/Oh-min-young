using System;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace _1946__신입_사원_
{
    class _1946
    {
        struct Cor
        {
            public int x;
            public int y;
        }
        static void Main(string[] args)
        {
            int t = int.Parse(Console.ReadLine());
            StringBuilder sb = new StringBuilder();
            for (int tr = 0; tr < t; tr++)
            {
                int n = int.Parse(Console.ReadLine());
                Cor[] arr = new Cor[n];
                for (int i = 0; i < n; i++)
                {
                    string[] str = Console.ReadLine().Split();
                    arr[i].x = int.Parse(str[0]);
                    arr[i].y = int.Parse(str[1]);
                }
                Array.Sort(arr, delegate(Cor u ,Cor v)
                {
                    if (u.x < v.x)
                    {
                        return -1;
                    }
                    else if(u.x > v.x)
                    {
                        return 1;
                    }
                    else
                    {
                        return 0;
                    }
                });
                int m = arr[0].y;
                int cnt = n;
                for (int i = 1; i < n; i++)
                {
                    int a = arr[i].y;
                    if(a > m)
                    {
                        cnt -= 1;
                    }
                    else
                    {
                        m = a;
                    }
                    
                }
                sb.Append(cnt).AppendLine();
            }
            Console.WriteLine(sb);
        }
    }
}
