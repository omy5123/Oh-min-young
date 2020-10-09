using System;

namespace _10162__가스레인지_
{
    class _10162
    {
        static void Main(string[] args)
        {
            int t = int.Parse(Console.ReadLine());
            int[] time = new int[3];
            
            
            time[0] += t / 300;
            t %= 300;

            time[1] += t / 60;
            t %= 60;
         
            time[2] += t / 10;
            t %= 10;
          
            
            if (t != 0)
            {
                Console.WriteLine(-1);
            }
            else
            {
                Console.WriteLine(string.Join(" ", time));
            }
        }
    }
}
