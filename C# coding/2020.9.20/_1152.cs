using System;

namespace _1152
{
    class _1152
    {
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            str = str.Trim();
            if (str == "")
            {
                Console.WriteLine(0);
            }
            else
            {
                string[] s = str.Split();
                Console.WriteLine(s.Length);
            }
            
        }
    }
}
