using System;
using System.Linq;

namespace _10610__30_
{
    class _10610
    {
        static void Main(string[] args)
        {
            string n = Console.ReadLine();
            char[] arr = n.ToCharArray();
            
            Array.Sort(arr);
            Array.Reverse(arr);
            int sum = 0;
            if (arr[arr.Length-1] != '0')
            {
                Console.WriteLine(-1);
            }
            else
            {
                for (int i = 0; i < arr.Length; i++)
                {
                    sum += Convert.ToInt32(arr[i]);
                }
                if (sum % 3 != 0)
                {
                    Console.WriteLine(-1);
                    return;
                }
                else
                {
                    for (int i = 0; i < arr.Length; i++)
                    {
                        Console.Write(arr[i]);
                    }
                }
            }
            
        }
    }
}
