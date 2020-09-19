using System;
using System.Collections.Generic;
using System.Diagnostics.Contracts;
using System.Linq;

namespace _소수찾기
{
    class Program
    {
        static string numbers = "";
        static List<string> result = new List<string>();

        static void permute(String str,int l, int r)
        {
            if (l == r)
            {
                
                result.Add(str);
            }
                
            else
            {
                for (int i = l; i <= r; i++)
                {
                    str = swap(str, l, i);
                    permute(str, l + 1, r);
                    str = swap(str, l, i);
                }
            }
        }

        static String swap(String a,int i, int j)
        {
            char temp;
            char[] charArray = a.ToCharArray();
            temp = charArray[i];
            charArray[i] = charArray[j];
            charArray[j] = temp;
            string s = new string(charArray);
            return s;
        }

        static void solution(string numbers)
        {
            for (int i = 0; i < numbers.Length; i++)
            {
                result.Add(numbers[i].ToString());
            }
            for (int i = 0; i < numbers.Length - 1; i++)
            {
                permute(numbers, i, numbers.Length - 1);
            }
            

            result = result.Distinct().ToList();
            
            List<int> arr = new List<int>();
            for (int i = 0; i < result.Count; i++)
            {
                arr.Add(int.Parse(result[i]));
            }
            arr = arr.Distinct().ToList();
            foreach (var item in arr)
            {
                Console.WriteLine(item);
            }
            int count = 0;
            
            foreach (int item in arr)
            {
                bool flag = true;
                if (item < 2)
                {
                    flag = false;
                }
                else if (item == 2)
                {
                    flag = true;
                }
                else
                {
                    for (int i = 2; i < item; i++)
                    {
                        if (item % i == 0)
                        {
                            flag = false;
                            break;
                        }
                    }
                }
                if (flag)
                {
                    count += 1;
                }
            }
            Console.WriteLine(count);

        }
        static void Main(string[] args)
        {
            numbers = "1230";
            solution(numbers);
        }
    }
}
