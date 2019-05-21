using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Week9
{
    class _1_cs
    {
        public static void maiin(string[] args)
        {
            var input = File.ReadAllLines("input.txt");
            string p = input[0];
            string t = input[1];
            int i = 0;
            var startIndeces = new List<int>();

            while (i < t.Length)
            {
                int j = 0;
                for (; j < p.Length && i + j < t.Length && t[i + j] == p[j];) { j++; }
                if (j == p.Length)
                {
                    startIndeces.Add(i + 1);
                }
                i++;
            }

            TextWriter output = new StreamWriter("output.txt");
            Console.SetOut(output);

            Console.WriteLine(startIndeces.Count);
            Console.WriteLine(String.Join(" ", startIndeces));

            output.Close();
        }
    }
}
