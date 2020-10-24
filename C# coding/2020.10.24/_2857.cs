using System;

namespace _2857__FBI_
{
    class _2857
    {
        static void solution(string[] str)
        {
            bool check = false;
            for (int i = 0; i < 5; i++)
            {
                if (str[i].Contains("FBI"))
                {
                    check = true;
                    Console.Write(i+1 + " ");
                }
            }
            if(check == false)
            {
                Console.WriteLine("HE GOT AWAY!");
            }
        }
        static void Main(string[] args)
        {
            string[] str = new string[5];
            for (int i = 0; i < 5; i++)
            {
                str[i] = Console.ReadLine();
            }
            solution(str);
        }
    }
}
