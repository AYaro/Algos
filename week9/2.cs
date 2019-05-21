using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Week9
{
    class Program
    {
        public static void Main(string[] args)
        {
            var input = File.ReadAllLines("input.txt")[0].Replace(" ", "");

            int[] letterCount = new int[26];
            int[] lastIndeces = new int[26];
            long[] diff = new long[26];
            long count = 0;

            for (int i = 0; i < input.Length; i++)
            {
                int index = input[i] - 'a';
                int length = i - lastIndeces[index] - 1;
                if (letterCount[index] > 1)
                {
                    diff[index] += letterCount[index] - 1;
                }

                diff[index] += length * (letterCount[index]);
                letterCount[index]++;
                count += diff[index];
                lastIndeces[index] = i;
            }

            TextWriter output = new StreamWriter("output.txt");
            Console.SetOut(output);
            Console.WriteLine(count);
            output.Close();
        }
    }
}
