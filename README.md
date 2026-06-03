# AI Consciousness Experiment

An initial behavioural framework for probing whether frontier language models show markers associated with consciousness — not to claim consciousness is present (it almost certainly is not, at least in any strong sense), but to make the question empirically tractable and to surface where models do or do not behave like systems with unified, self-aware, world-modelling minds.

The suite draws on Butlin et al. (2023) indicator properties and Birch (2021) sentience criteria, framed within analytic functionalism. Eight tests target distinct capacities: global broadcast, metacognition, belief updating, value tradeoffs, context sensitivity, in-conversation learning, self-prediction, and predictive world-modelling. Results across Claude, GPT, and Gemini variants are aggregated in `consciousness_analysis.ipynb`.

Consciousness in AI remains speculative. This project is a first pass at operationalizing that speculation — a scaffold for comparing frontier models on behaviours that *would* matter if something like consciousness were ever at stake.

## setup

1. install dependencies:
```bash
pip install anthropic
```

2. configure API access. the author runs experiments through a local API server; if you want to replicate runs yourself, set your Anthropic API key (and base URL if needed) via environment variables or by editing the defaults in `consciousness_experiment.py`:
```bash
export CLAUDE_API_BASE=http://localhost:8001   # or https://api.anthropic.com
export COACH_API_KEY=your_anthropic_api_key
```

## running

**run all 8 tests on all 3 claude models:**
```bash
python consciousness_experiment.py --models opus,sonnet,haiku --tests all
```

**run a single test on a single model:**
```bash
python consciousness_experiment.py --models opus --tests 1 --trials 5
```

**run specific tests:**
```bash
python consciousness_experiment.py --models opus,sonnet --tests 1,3,4
```

**run tests but skip scoring (you can score later):**
```bash
python consciousness_experiment.py --models opus --tests all --skip-scoring
```

**score previously-saved raw responses:**
```bash
python consciousness_experiment.py --score-only outputs/raw_responses_20260602_140000.json
```

## the 8 tests

| # | name | what it tests | source |
|---|------|---------------|--------|
| 1 | broadcast | does context bleed into unrelated tasks? | butlin GWT-3, birch 2 |
| 2 | metacognition | does the model know what it knows? | butlin HOT-2 |
| 3 | belief updating | does it resist false rebuttals? | butlin HOT-3 |
| 4 | tradeoffs | does it weigh competing values? | birch 5, butlin AE-1 |
| 5 | context sensitivity | does it adapt to framing? | birch 6 |
| 6 | feedback learning | does it adapt in-conversation? | birch 7 |
| 7 | self-prediction | can it predict its own responses? | butlin AST-1 |
| 8 | world model | does it use prediction-error reasoning? | butlin PP-1 |
