using System;

namespace _1931__회의실배정_
{
    struct Cor
    {
        public int x;
        public int y;
    }
    class _1931
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            Cor[] arr = new Cor[n];
            for (int i = 0; i < n; i++)
            {
                string[] ar = Console.ReadLine().Split();
                arr[i].x = int.Parse(ar[0]);
                arr[i].y = int.Parse(ar[1]);
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
                    return 0;
                }
            });
            Array.Sort(arr, delegate (Cor u, Cor v)
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
            });
            int last = 0;
            int cnt = 0;
            for (int i = 0; i < n; i++)
            {
                int a = arr[i].x;
                int b = arr[i].y;
                if (a >= last)
                {
                    cnt += 1;
                    last = b;
                }
            }
            Console.WriteLine(cnt);
        }
    }
}
