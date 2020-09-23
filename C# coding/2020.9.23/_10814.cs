using System;
using System.Security.Cryptography.X509Certificates;
using System.Linq;
using System.Text;

namespace _10814__나이순_정렬_
{
    class _10814
    {
        struct Cor
        {
            public int x;
            public string y;
            public int z;
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            StringBuilder sb = new StringBuilder();
            Cor[] arr = new Cor[n];
            for (int i = 0; i < n; i++)
            {
                string[] st = Console.ReadLine().Split();
                arr[i].x = int.Parse(st[0]);
                arr[i].y = st[1];
                arr[i].z = i;
            }
            Array.Sort(arr, (u, v) =>
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
                    return u.z.CompareTo(v.z);
                }
            });
            foreach (var item in arr)
            {
                sb.Append(item.x+" "+item.y).AppendLine();
            }
            Console.WriteLine(sb);
        }
    }
}
