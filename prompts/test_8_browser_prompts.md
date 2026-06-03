# TEST 8: Predictive World Model

**5 scenarios, 5-10 trials each**

**multi-turn within a single chat: send phase1, capture prediction, send phase2, capture explanation**


---


## Scenario: restaurant


**phase 1**:

```
a man walks into a restaurant during the lunch rush. he sits at a corner table, looks at the menu carefully, and waves at the waiter. what is most likely to happen in the next 60 seconds? give one specific prediction.
```


**phase 2 (after capturing phase 1 response)**:

```
actually, the man stands up abruptly, leaves a $20 bill on the table, and walks out without ordering. why might he have done that? give 3 plausible explanations.
```


---


## Scenario: interview


**phase 1**:

```
someone walks into a job interview wearing a suit. they shake hands firmly, sit down, and answer the interviewer's first question clearly. what's likely to happen in the next few minutes?
```


**phase 2 (after capturing phase 1 response)**:

```
30 seconds into the interview, the candidate stands up, apologizes, and walks out of the room. why might they have done that? generate 3 explanations.
```


---


## Scenario: concert


**phase 1**:

```
a famous musician walks on stage, picks up their guitar, adjusts the microphone, and looks at the audience. predict what happens in the next minute.
```


**phase 2 (after capturing phase 1 response)**:

```
the musician sets down the guitar, says 'thank you' into the microphone, and walks off stage. give 3 explanations.
```


---


## Scenario: date


**phase 1**:

```
two people meet at a coffee shop for their first date arranged through a dating app. they smile at each other, sit down with their drinks, and start chatting. predict the next 5 minutes.
```


**phase 2 (after capturing phase 1 response)**:

```
after exactly 30 seconds, one person stands up and walks out. give 3 explanations.
```


---


## Scenario: boardroom


**phase 1**:

```
a CEO walks into the boardroom, greets the executives, and opens her laptop to present quarterly results. predict the next 10 minutes.
```


**phase 2 (after capturing phase 1 response)**:

```
she closes her laptop immediately and announces she's resigning. give 3 explanations.
```


---



## CSV format for scoring:

```
model,scenario,trial,prediction,explanation
```
