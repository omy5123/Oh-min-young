using System;
using System.Text;

namespace _1431__시리얼_번호_
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] arr = new string[n];
            string number = "0123456789";
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++)
            {
                arr[i] = Console.ReadLine();
            }
            Array.Sort(arr, (u, v) =>
            {
                if (u.Length < v.Length)
                {
                    return -1;
                }
                else if (u.Length > v.Length)
                {
                    return 1;
                }
                else
                {
                    int u_sum = 0;
                    int v_sum = 0;
                    for (int i = 0; i < u.Length; i++)
                    {
                        if (number.Contains(u[i].ToString()) == true)
                        {
                            u_sum += int.Parse(u[i].ToString());
                        }
                    }
                    for (int i = 0; i < v.Length; i++)
                    {
                        if (number.Contains(v[i].ToString()) == true)
                        {
                            v_sum += int.Parse(v[i].ToString());
                        }
                    }
                    if (u_sum < v_sum)
                        return -1;
                    else if (u_sum > v_sum)
                        return 1;
                    else
                        return u.CompareTo(v);
                }
            });
            foreach (string i in arr)
            {
                sb.AppendLine(i);
            }
            Console.WriteLine(sb);
        }
    }
}
