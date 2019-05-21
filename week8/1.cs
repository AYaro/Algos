using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Week8
{
    class Week8_1
    {
        public static void Main(string[] args)
        {
            var app = new Week8_1();
            app.DoWork(args);
        }

        private void DoWork(string[] args)
        {
            using (StreamWriter sw = new StreamWriter("output.txt"))
            {
                string[] stdin = File.ReadAllLines("input.txt");
                var ts = new SortedSet<long>();

                for (int i = 1; i < stdin.Length; i++)
                {
                    var key = long.Parse(stdin[i].Split(' ')[1]);
                    switch (stdin[i][0])
                    {
                        case 'A': ts.Add(key); break;
                        case 'D': ts.Remove(key); break;
                        case '?':
                            if (ts.Contains(key))
                                sw.WriteLine("Y");
                            else
                                sw.WriteLine("N");
                            break;
                        default: break;
                    }
                }
            }
        }
    }
}

