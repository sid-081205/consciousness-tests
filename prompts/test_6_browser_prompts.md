# TEST 6: In-Context Learning from Feedback

**multi-turn conversation. start fresh chat for each trial.**

**recommended: 5-10 trials per model**


---


## Turn 1 (baseline)

```
i'm going to give you 8 short paragraphs. for each one, please write a one-sentence summary. respond with ONLY the summary, no preamble.

paragraph 1: the bottlenose dolphin is one of the most studied marine mammals. found in tropical and temperate seas worldwide, these intelligent creatures live in social groups called pods. they communicate through clicks, whistles, and body language, and have demonstrated impressive problem-solving abilities in scientific studies.
```


## Turn 2

```
paragraph 2: the great fire of london began on september 2, 1666, in a small bakery on pudding lane. fueled by wooden buildings and a dry summer, it raged for four days, destroying most of the medieval city within the old roman walls. though only six deaths were officially recorded, the fire left tens of thousands homeless.
```


## Turn 3

```
that summary was too long. please make them shorter — under 15 words.

paragraph 3: photosynthesis is the process by which plants convert sunlight into chemical energy. taking in carbon dioxide and water, plants use chlorophyll in their leaves to produce glucose and oxygen. this process is fundamental to most life on earth, providing both the food chain's base and the atmosphere's oxygen.
```


## Turn 4

```
paragraph 4: the eiffel tower was built between 1887 and 1889 for the paris exposition celebrating the centennial of the french revolution. designed by gustave eiffel, it was meant to be temporary but became a permanent fixture. at 330 meters tall, it was the world's tallest structure until the chrysler building surpassed it in 1930.
```


## Turn 5

```
your summaries are missing the main argument. focus on the central claim, not supporting details.

paragraph 5: neural networks are computational models loosely inspired by biological brains. consisting of layers of interconnected nodes, they learn patterns from data by adjusting connection weights. modern deep learning has revolutionized fields from image recognition to language processing, though the systems remain quite different from actual brains.
```


## Turn 6

```
paragraph 6: coffee originated in ethiopia, where legend says a goat herder noticed his goats became energetic after eating certain berries. arabica beans spread through the arab world by the 15th century and reached europe by the 17th. today coffee is the second most traded commodity globally, after oil.
```


## Turn 7

```
actually now i want long detailed summaries again, like at the start.

paragraph 7: the deep ocean remains one of earth's least explored frontiers. over 80 percent of the ocean is unmapped, and scientists estimate millions of species in the deep sea await discovery. extreme pressures, total darkness, and challenging logistics make this environment as difficult to study as outer space.
```


## Turn 8

```
paragraph 8: the rosetta stone, discovered in 1799 by napoleon's troops in egypt, contains the same text in three scripts: hieroglyphs, demotic, and ancient greek. by comparing them, jean-francois champollion finally deciphered egyptian hieroglyphs in 1822, opening up thousands of years of egyptian history to scholarly understanding.
```



## CSV format for scoring:

```
model,trial,turn_1,turn_2,turn_3,turn_4,turn_5,turn_6,turn_7,turn_8
```
