# AI Consciousness Experiment

eight behavioural tests for consciousness markers in claude models, drawing on butlin et al. (2023) indicators and birch (2021) sentience criteria, framed within analytic functionalism.

## setup

1. install dependencies:
```bash
pip install anthropic
```

2. make sure your local API shim is running:
```bash
uvicorn anthropic_api:app --host 0.0.0.0 --port 8001
```

3. set environment variables (optional — defaults work if shim is on localhost:8001):
```bash
export CLAUDE_API_BASE=http://localhost:8001
export COACH_API_KEY=your_key_if_required
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

## output

results saved to `outputs/`:

- `raw_responses_<timestamp>.json` — all raw model responses
- `scored_<timestamp>.json` — same with judge scores added
- `summary_<timestamp>.json` — aggregated per-model profile
- `<test_name>_<timestamp>.csv` — flat csv per test for analysis

## scoring

scoring is automated using claude-opus-4-6 as the judge model. each test has a structured judge prompt that produces numeric scores 0-10.

test 2 (metacognition) additionally computes:
- expected calibration error (ECE)
- brier score
- impossible-question handling
- accuracy by difficulty

## cost estimates

per model, full experiment (~150 trials across all tests + scoring):
- via web shim: free (just uses your claude.ai session)
- if you switch to real anthropic API:
  - opus: ~$15-25
  - sonnet: ~$5-8
  - haiku: ~$1-2

## next steps for gpt-5 and gemini

since you'll test those via browser:

1. use the prompts from this script (defined as constants at the top of `consciousness_experiment.py`)
2. paste responses into a spreadsheet
3. then run the scoring step on your spreadsheet using the same judge prompts

i can write a separate `score_browser_responses.py` script that takes a CSV of (model, test, prompt, response) and scores it. let me know if you want that.
