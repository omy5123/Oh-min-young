using System;

namespace _1068__트리_
{
    class _1068
    {
        static int cnt = 0;
        static int delete;
        static int n;
        static int[,] arr;
        static int[] visit;
        static int root;
        static void dfs(int root)
        {
            bool check = false;
            visit[root] = 1;
            for (int i = 0; i < n; i++)
            {
                if (arr[root, i] == 1 && visit[i] == 0)
                {
                    check = true;
                    dfs(i);
                }
            }
            if (check == false)
            {
                cnt += 1;
            }

        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            arr = new int[n, n];
            visit = new int[n];
            string[] line = Console.ReadLine().Split();
            for (int i = 0; i < n; i++)
            {
                if (int.Parse(line[i]) != -1)
                {
                    arr[i, int.Parse(line[i])] = 1;
                    arr[int.Parse(line[i]), i] = 1;
                }
                else
                {
                    root = i;
                }
            }
            delete = int.Parse(Console.ReadLine());
            for(int i = 0; i< n;i++)
            {
                arr[i, delete] = 0;
                arr[delete, i] = 0;
            }

            dfs(root);
            if(delete == root)
            {
                Console.WriteLine(0);
            }
            else
            {
                Console.WriteLine(cnt);
            }
            
        }
    }
}
