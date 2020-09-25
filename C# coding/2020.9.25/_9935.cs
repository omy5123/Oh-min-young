using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace _9935__문자열_폭발_
{
    class _9935
    {
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            string check = Console.ReadLine();
            StringBuilder sb = new StringBuilder(str.Length);

            foreach (var item in str)
            {
                sb.Append(item.ToString());
                if (sb.Length >= check.Length)
                {
                    bool flag = true;
                    for (int i = 1; i < check.Length+1; i++)
                    {
                        if (sb[sb.Length-i] != check[check.Length-i])
                        {
                            flag = false;
                            break;
                        }
                    }
                    if (flag)
                    {
                        
                        sb.Remove(sb.Length-check.Length,check.Length);
                        
                    }
                }
            }
            if (sb.Length == 0)
            {
                Console.WriteLine("FRULA");
            }
            else
            {
                Console.WriteLine(sb);
            }
            
            
        }
    }
}
