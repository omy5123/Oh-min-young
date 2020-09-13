using System;

namespace _1991__트리_순회_
{
    class _1991
    {
        static string[,] arr = { };
        static void preorder(char str)
        {
            Console.Write(str);
            if (arr[(int)str-65,1] != ".")
            {
                preorder(char.Parse(arr[(int)str - 65, 1]));
            }
            if (arr[(int)str - 65, 2] != ".")
            {
                preorder(char.Parse(arr[(int)str - 65, 2]));
            }
        }
        static void inorder(char str)
        {
            if (arr[(int)str - 65, 1] != ".")
            {
                inorder(char.Parse(arr[(int)str - 65, 1]));
            }
            Console.Write(str);
            if (arr[(int)str - 65, 2] != ".")
            {
                inorder(char.Parse(arr[(int)str - 65, 2]));
            }
        }
        static void postorder(char str)
        {
            if (arr[(int)str - 65, 1] != ".")
            {
                postorder(char.Parse(arr[(int)str - 65, 1]));
            }
            if (arr[(int)str - 65, 2] != ".")
            {
                postorder(char.Parse(arr[(int)str - 65, 2]));
            }
            Console.Write(str);
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            arr = new string[n, 3];
            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split();
                char ch = char.Parse(line[0]);
                int li = (int)ch-65;
                for (int j = 0; j < 3; j++)
                {
                    arr[li, j] = line[j];
                }
            }
            preorder('A');
            Console.WriteLine();
            inorder('A');
            Console.WriteLine();
            postorder('A');
        }
    }
}
