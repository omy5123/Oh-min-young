using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Text;

namespace C_sharp_study._1차원_배열
{
    class _4344
    {
        static void Main(string args)
        {
            int n = int.Parse(Console.ReadLine());
            

            for (int i = 0; i < n; i++)
            {
                string[] ar = Console.ReadLine().Split();
                for (int j = 0; j < ar.Length; j++)
                {
                    int[] arr = new int[ar.Length];
                    arr[j] = int.Parse(ar[j]);
                    int sum = 0;
                    double result = 0;
                    for (int k = 1; k < arr.Length; k++)
                    {
                        sum += arr[k];
                    }
                    Console.WriteLine(sum / arr.Length);
                }

            }
        }
    }
}
