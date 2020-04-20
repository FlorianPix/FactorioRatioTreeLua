using System;
using System.Collections.Generic;
using System.Text;

namespace RecipeReader
{
    struct Item
    {
        string name;
        List<KeyValuePair<Item, int>> results;
        int craftingTime;
        List<KeyValuePair<Item, int>> ingredients;
        int craftingSpeed;

        public Item(string name, int craftingTime, int craftingSpeed, List<KeyValuePair<Item, int>> ingredients, List<KeyValuePair<Item, int>> results)
        {
            this.name = name;
            this.craftingSpeed = craftingSpeed;
            this.craftingTime = craftingTime;
            this.ingredients = ingredients;
            this.results = results;
        }
        

    }
}
