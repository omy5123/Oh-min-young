using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace _max_number
{
    class _max_number
    {
        static string solution(int[] numbers)
        {
            Array.Sort(numbers, (x, y) =>
            {
                string XY = x.ToString() + y.ToString();
                string YX = y.ToString() + x.ToString();
                return string.Compare(YX, XY);
            });
            if (numbers[0] == 0)
            {
                return "0";
            }
            else
            {
                return string.Join("", numbers);
            }
            

        }
        static void Main(string[] args)
        {
            int[] numbers = { 3, 30, 34, 5, 9,3 };
            numbers = numbers.Distinct().ToArray();
            Console.WriteLine(numbers.Length);
            string str = solution(numbers);
            Console.WriteLine(str);
        }
    }
}
