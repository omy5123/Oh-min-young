using System;
using System.Collections.Generic;
using System.Text;

namespace C_sharp_study._1차원_배열
{
    class _2562
    {
        static void Main()
        {
            int[] arr = new int[9];
            for (int i = 0; i < 9; i++)
            {
                arr[i] = int.Parse(Console.ReadLine());
            }
            int max = arr[0];
            for (int i = 1; i < 9; i++)
            {
                if (max < arr[i])
                    max = arr[i];
            }
            Console.WriteLine(max);
            Console.WriteLine(Array.FindIndex(arr, i=> i == max)+1);
        }
    }
}
