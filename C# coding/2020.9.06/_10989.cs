using System;
using System.Text;

namespace _10989__sort_
{
    class _10989
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr = new int[10001];
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++)
            {
                int a = int.Parse(Console.ReadLine());
                arr[a] += 1;
            }
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] == 0)
                {
                    continue;
                }
                else
                {
                    for (int j = 0; j < arr[i]; j++)
                    {
                        sb.AppendLine(i.ToString());
                    }
                }
            }
            Console.WriteLine(sb.ToString());
        }
    }
}
