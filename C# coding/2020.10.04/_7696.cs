using System;
using System.Collections.Generic;
using System.Text;

namespace _7696__반복하지_않는_수_
{
    class _7696
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            StringBuilder sb = new StringBuilder();
            while (n != 0)
            {
                List<int> list = new List<int>();
                int num = 1;
                while (list.Count != n)
                {
                    string num_str = num.ToString();
                    bool check = true;
                    for (int i = 0; i < num_str.Length; i++)
                    {
                        for (int j = i + 1; j < num_str.Length; j++)
                        {
                            if (num_str[i] == num_str[j])
                            {
                                check = false;
                                break;
                            }
                        }
                        if (check ==false)
                        {
                            break;
                        }
                    }
                    if (check)
                    {
                        list.Add(num);
                        num += 1;
                    }
                    else
                    {
                        num += 1;
                    }
                }
                sb.Append(list[list.Count - 1]).AppendLine();
                n = int.Parse(Console.ReadLine());
            }
            Console.WriteLine(sb);
        }
    }
}
