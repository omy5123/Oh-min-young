using System;

namespace _1100__하얀_칸_
{
    class _1100
    {
        static void Main(string[] args)
        {
            string[,] str = new string[8, 8];
            int cnt = 0;
            for (int i = 0; i < 8; i++)
            {
                string line = Console.ReadLine();
                for (int j = 0; j < 8; j++)
                {
                    str[i, j] = line[j].ToString();
                }
            }
            for (int i = 0; i < 8; i++)
            {
                if (i % 2 == 0)
                {
                    for (int j = 0; j < 8; j++)
                    {
                        if (j % 2 == 0 && str[i,j] == "F")
                        {
                            cnt += 1;
                        }
                    }
                }
                else
                {
                    for (int j = 0; j < 8; j++)
                    {
                        if (j % 2 == 1 && str[i,j] =="F")
                        {
                            cnt += 1;
                        }
                    }
                }
            }
            Console.WriteLine(cnt);
        }
    }
}
