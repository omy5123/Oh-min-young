using System;
using System.Text;

namespace _1057__토너먼트_
{
    class _1057
    {
        static void Main(string[] args)
        {
            string[] line = Console.ReadLine().Split();
            int n = int.Parse(line[0]);
            int kim = int.Parse(line[1]);
            int im = int.Parse(line[2]);
            StringBuilder sb = new StringBuilder();
            int count = 0;
            while(kim != im)
            {
                kim -= kim / 2;
                im -= im / 2;
                count += 1;
            }
            sb.Append(count);
            Console.WriteLine(sb);

        }
    }
}
