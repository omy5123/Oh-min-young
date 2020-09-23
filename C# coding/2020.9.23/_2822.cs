using System;
using System.Text;

namespace _2822
{
    class _2822
    {
        static void Main(string[] args)
        {
            int[] arr = new int[8];
            int[] check = new int[8];
            StringBuilder sb = new StringBuilder();
            int[] result = new int[5];
            for (int i = 0; i < 8; i++)
            {
                arr[i] = int.Parse(Console.ReadLine());
                check[i] = arr[i];
            }
            Array.Sort(arr);
            
            int sum = 0;
            for (int i = 3; i < 8; i++)
            {
                sum += arr[i];
                result[i-3] = (Array.IndexOf(check, arr[i]) + 1);
            }
            sb.AppendLine(sum.ToString());
            
            Array.Sort(result);
            foreach (var item in result)
            {
                sb.Append(item + " ");
            }
            Console.WriteLine(sb);
        }
    }
}
