using System;
using System.Linq;

namespace _1145__적어도_대부분의_배수_
{
    class _1145
    {
        static void Main(string[] args)
        {
            string[] line = Console.ReadLine().Split();
            int[] arr = new int[5];

            for (int i = 0; i < 5; i++)
            {
                arr[i] = int.Parse(line[i]);
            }
            int min = arr.Min();
            while(true)
            {
                int cnt = 0;
                for (int i = 0; i < 5; i++)
                {
                    if(min % arr[i] == 0)
                    {
                        cnt += 1;
                    }
                }
                if (cnt >=3)
                {
                    Console.WriteLine(min);
                    break;
                }
                min += 1;
            }
        }
    }
}
