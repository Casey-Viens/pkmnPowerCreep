# Pokemon Power Creep

## **Problem**

To use Pokemons' base stats to debate the potential of power creep.

After completing the data analytics course at NEIT, I wanted to apply some of what I learned to a project of my own. After exploring Kaggle's various data sets, I was inspired by a Pokemon data set. This csv contained data on the first seven generations of Pokemon and could be used to research the possibility of power creep between Pokemon generations via Pokemon base stats.

## **Technologies**

- python  
- matplotlib  
- pandas  
- numpy  

## **Sources**

- Pokemon stat csv  
    - https://www.kaggle.com/rounakbanik/pokemon  
- Pokemon tier csv  
    - https://github.com/n2cholas/pokemon-analysis  

## **Approach**

To start, I removed all "legendary" Pokemon from the data set, since I felt that their higher than average base stats may poorly affect the analysis. With the legendary Pokemon removed, I used the Kaggle data set to explore the minimum, maximum, median, and average of each base stat, cumulative base stats, and damage effectiveness of each generation.

The plots of this data presented fairly insignificant results which I felt was likely caused by the overwhelming amount of weak Pokemon per game. With the vast amount of Pokemon in each generation having weaker previous evolutions, these Pokemon were pulling the averages down and making the results more difficult to analyze.

To compensate for this I created new lists of Pokemon based on the data set which only included the top ten percent of each generation based on the Pokemons' cumulative base stats. I felt that this approach was the best way to collect a sample of the strongest, most competitively viable or usable, Pokemon of each generation. With these new samples collected I retested for the minimum, median, and average of the various stats again. This test presented more dynamic results, but I wanted to consider other ways to compare the power of each generation.

At this point, I wanted to explore the competitive tiers of Pokemon so I found a second source of data. Using this data I could analyze if newer generations yielded a larger percentage of high-tier Pokemon compared to previous generations. Here since the y-axis is no longer the stat and rather the number of Pokemon I felt that it might be better to use the percentage of Pokemon in that tier from their generation since each generation has a different number of Pokemon.

## **Conclusion**

In the end, the results yielded by the program did not provide a conclusive reason to believe Pokemon has power creep. There are no noticeable trends in the graphs to suggest that future generations are meaningfully stronger than previous ones. The charts highlight some outliers and small trends between generations, such as the slight upward trend of average base stats from generations 5 through 7 or the vast amount of Pokemon from generation 4 in the higher tiers of competitive, however, no convincing trends to determine power creep.

If Pokemon does have power creep it would likely best be shown by the introduction of new mechanics throughout the generations, such as:  

- Generation 2
    - Held items
    - Special was split into Special Attack and Special Defense
- Generation 3
    - Abilites
    - Natures
- Generation 4
    - Move Physical/Special split
- Generation 6
    - Mega Evolutions
- Generation 7
    - Z - Moves
- Generation 8
    - Dynamaxing


The additions or changes of these mechanics shifted or added power to the game in ways not determined by the base stats of Pokemon. If I were to consider this problem further, I would look into these mechanics to decide how early generation Pokemon would compare to current generation Pokemon.

## **Results**

![Min](/plots/Min.png)
![Max](/plots/Max.png)
![Median](/plots/Median.png)
![Average](/plots/Average.png)
![Tiers](/plots/Tiers.png)
![MinTop10%](/plots/MinTop10.png)
![MedianTop10%](/plots/MedianTop10.png)
![AverageTop10%](/plots/AverageTop10.png)


