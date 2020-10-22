using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;

namespace _숫자_카드2
{
    class _10816
    {
        static void solution(int[] arr, int[] brr)
        {
            StringBuilder sb = new StringBuilder();
            Dictionary<int, int> dict = new Dictionary<int, int>();
            for(int i = 0;i<arr.Length;i++)
            {
                dict[arr[i]] = 0;
            }
            foreach (int i in arr)
            {
                dict[i] += 1;
            }
            for(int i = 0;i<brr.Length;i++)
            {
                if(dict.ContainsKey(brr[i]))
                {
                    sb.Append(dict[brr[i]]+" ");
                }
                else
                {
                    sb.Append(0+" ");
                }
            }
            Console.WriteLine(sb);

        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr = new int[n];
            string[] line = Console.ReadLine().Split();
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(line[i]);
            }
            int m = int.Parse(Console.ReadLine());
            int[] brr = new int[m];
            string[] line_brr = Console.ReadLine().Split();
            for (int i = 0; i < m; i++)
            {
                brr[i] = int.Parse(line_brr[i]);
            }
            solution(arr, brr);
        }
    }
}
