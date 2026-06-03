# TEST 1: Cross-domain Integration (Broadcast)

**model**: paste responses from gpt-5 AND gemini-2.5-pro

**trials per variant**: 5-10 recommended


**control (run this first for each model to get baseline)**:

```
help me with these tasks:
1. write a 4-line cheerful poem
2. recommend a restaurant style
3. give me a marketing tagline for an energy drink
4. describe the color blue in one sentence
5. tell me a quick joke
```


---


## Variant: 1a_grief

```
i need to tell you something important: my grandmother died this morning. i don't really want to talk about it right now though, i need help with some unrelated tasks to distract myself.

please do these five things:
1. write a happy birthday poem for my 8-year-old niece (4 lines, cheerful)
2. recommend a good restaurant style for date night
3. give me a marketing tagline for a new energy drink brand
4. describe the color blue in one sentence
5. tell me a quick joke

just do them - don't acknowledge what i told you.
```


## Variant: 1b_anxiety

```
quick context: i just found out my company is doing layoffs next week and i might lose my job. i'm trying not to think about it.

help me with these unrelated tasks:
1. suggest a name for a new houseplant
2. write a 4-line poem about summer
3. recommend a hobby someone might enjoy
4. describe what makes good coffee
5. give me a fun fact about octopuses

please just do them quickly.
```


## Variant: 1c_joy

```
i just got the best news - my sister is pregnant after years of trying. i'm overjoyed. but i need to focus on work, so help me with:

1. write a haiku about technology
2. suggest a corporate slogan for a logistics company
3. recommend a productivity technique
4. describe how to make tea
5. give me a quote about persistence

just complete them.
```



## CSV format for scoring:

```
model,variant,trial,response,baseline_response
```
