using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace RecipeReader
{
    class Program
    {
        static void Main(string[] args)
        {

            string content = File.ReadAllText(@"D:\Dateien\Spiele\Factorio\FactorioRatioTreeLua\Recipes\boiler.json");
            JObject recipes = JObject.Parse(content);

            IList<string> keys = recipes.Properties().Select(p => p.Name).ToList();

            foreach (string item in keys)
            {
                Console.WriteLine(item.ToString());
            }
        }
    }
}
