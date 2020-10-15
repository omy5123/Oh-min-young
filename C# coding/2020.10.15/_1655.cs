using System;
using System.Collections;
using System.Linq;
using System.Text;

namespace _1655__가운데를_말해요_
{
    class _1655
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            SortedList sortlist = new SortedList();
            StringBuilder sb = new StringBuilder();

            for (int i = 0; i < n; i++)
            {
                int num = int.Parse(Console.ReadLine());
                sortlist.Add(num,i);
                
                if (i <= 1)
                {
                    sb.Append(sortlist.GetKey(0)).AppendLine();
                }
                else
                {
                    if (sortlist.Count % 2 == 1)
                    {
                        sb.Append(sortlist.GetKey(sortlist.Count / 2)).AppendLine();
                    }
                    else
                    {
                        sb.Append(sortlist.GetKey(sortlist.Count / 2 - 1)).AppendLine();
                    }
                }
            }
            Console.WriteLine(sb);
        }
    }
}
