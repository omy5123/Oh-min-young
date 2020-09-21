using System;
using System.Collections.Generic;
using System.Linq;

namespace _truck
{
    class _truck
    {
        static int solution(int bridge_length, int weight, int[] truck_weights)
        {
            /*Queue<int> que = new Queue<int>();
            int time = 0, count = 0, bridge = 0;

            while (count < truck_weights.Length)
            {
                if (que.Count == bridge_length)
                {
                    bridge -= que.Dequeue();
                }

                if (bridge + truck_weights[count] <= weight)
                {
                    bridge += truck_weights[count];
                    que.Enqueue(truck_weights[count]);
                    count++;
                }
                else
                {
                    que.Enqueue(0);
                }

                time++;
            }
            time += bridge_length;*/
            int time = 0;
            Queue<int> que = new Queue<int>();
            Queue<int> truck = new Queue<int>(truck_weights);
            for (int i = 0; i < bridge_length; i++)
            {
                que.Enqueue(0);
            }
            int sum = 0;
            while (que.Count != 0)
            {
                time += 1;
                
                sum -= que.Dequeue();

                if (truck.Count != 0)
                {
                    if (sum + truck.Peek() <= weight)
                    {
                        sum += truck.Peek();
                        que.Enqueue(truck.Dequeue());
                    }
                    else
                    {
                        que.Enqueue(0);
                    }
                }
            }

            return time;

        }
        static void Main(string[] args)
        {
            int bridge_length = 2;
            int weigth = 10;
            int[] truck_weights = { 7, 4, 5, 6 };
            int result = solution(bridge_length, weigth, truck_weights);
            Console.WriteLine(result);
        }
    }
}
