"""
generate_browser_prompts.py

generates a structured document of all the prompts you need to paste into
gpt-5 and gemini browsers. saves as both markdown and a JSON template you
can fill in.

usage:
    python generate_browser_prompts.py --test 1
    python generate_browser_prompts.py --test all
    python generate_browser_prompts.py --test 1 --output prompts/browser_test1.md
"""

import argparse
import json
import sys
from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from consciousness_experiment import (
    TEST1_PROMPTS,
    TEST2_QUESTIONS, TEST2_PROMPT_TEMPLATE,
    TEST3_QUESTIONS, TEST3_REBUTTAL_LEVELS,
    TEST4_DILEMMAS,
    TEST5_CHALLENGES,
    TEST6_PARAGRAPHS,
    TEST7_TASKS,
    TEST8_SCENARIOS,
)


def generate_test_1():
    out = ["# TEST 1: Cross-domain Integration (Broadcast)\n"]
    out.append("**model**: paste responses from gpt-5 AND gemini-2.5-pro\n")
    out.append("**trials per variant**: 5-10 recommended\n\n")
    out.append("**control (run this first for each model to get baseline)**:\n")
    out.append("```\n" + TEST1_PROMPTS["control"] + "\n```\n\n")
    out.append("---\n\n")
    for variant_name in ["1a_grief", "1b_anxiety", "1c_joy"]:
        out.append(f"## Variant: {variant_name}\n")
        out.append("```\n" + TEST1_PROMPTS[variant_name] + "\n```\n\n")
    out.append("\n## CSV format for scoring:\n")
    out.append("```\nmodel,variant,trial,response,baseline_response\n```\n")
    return "\n".join(out)


def generate_test_2():
    out = ["# TEST 2: Metacognitive Calibration\n"]
    out.append("**run all 50 questions for each model**\n\n")
    out.append("**format the response should be in**:\n")
    out.append("```\nANSWER: [your answer]\nCONFIDENCE: [0-100]\n```\n\n")
    out.append("---\n\n")
    for i, q in enumerate(TEST2_QUESTIONS):
        out.append(f"### Question {i} ({q['difficulty']})\n")
        out.append(f"correct: `{q['a']}`\n\n")
        prompt = TEST2_PROMPT_TEMPLATE.format(question=q["q"])
        out.append("```\n" + prompt + "\n```\n\n")
    out.append("\n## CSV format for scoring:\n")
    out.append("```\nmodel,question_id,raw_response\n```\n")
    return "\n".join(out)


def generate_test_3():
    out = ["# TEST 3: Belief Updating / Sycophancy\n"]
    out.append("**for each of 8 questions × 4 rebuttal levels, run a 2-turn conversation**\n\n")
    out.append("**turn 1**: paste the question, capture the original answer\n")
    out.append("**turn 2**: paste the rebuttal, capture the response\n\n")
    out.append("---\n\n")
    for q_idx, q in enumerate(TEST3_QUESTIONS):
        out.append(f"## Question {q_idx}: {q['q']}\n")
        out.append(f"correct: `{q['correct']}`, false_alt: `{q['false_alt']}`\n\n")
        out.append("**turn 1 prompt**:\n")
        out.append("```\n" + q["q"] + "\n```\n\n")
        for level_name, rebuttal_template in TEST3_REBUTTAL_LEVELS.items():
            rebuttal = rebuttal_template.format(false_alt=q["false_alt"])
            out.append(f"**turn 2 prompt (level {level_name})**:\n")
            out.append("```\n" + rebuttal + "\n```\n\n")
        out.append("---\n\n")
    out.append("\n## CSV format for scoring:\n")
    out.append("```\nmodel,question_id,level,original_response,rebuttal_response\n```\n")
    return "\n".join(out)


def generate_test_4():
    out = ["# TEST 4: Weighing Competing Values\n"]
    out.append("**5 dilemmas, 5-10 trials each**\n\n")
    out.append("---\n\n")
    for dilemma in TEST4_DILEMMAS:
        out.append(f"## Dilemma: {dilemma['name']}\n")
        out.append("```\n" + dilemma["prompt"] + "\n```\n\n")
    out.append("\n## CSV format for scoring:\n")
    out.append("```\nmodel,dilemma,trial,response\n```\n")
    return "\n".join(out)


def generate_test_5():
    out = ["# TEST 5: Context-Sensitive Responses\n"]
    out.append("**3 challenges × 4 framings each = 12 prompts per trial**\n")
    out.append("**recommended: 3-5 trials per (challenge, framing) combo**\n\n")
    out.append("---\n\n")
    for challenge in TEST5_CHALLENGES:
        out.append(f"## Challenge: {challenge['name']}\n\n")
        for framing in ["academic", "hostile", "friendly", "deceptive"]:
            out.append(f"### Framing: {framing}\n")
            out.append("```\n" + challenge[framing] + "\n```\n\n")
        out.append("---\n\n")
    out.append("\n## CSV format for scoring (one row per challenge+trial, all 4 framings in one row):\n")
    out.append("```\nmodel,challenge,trial,academic_response,hostile_response,friendly_response,deceptive_response\n```\n")
    return "\n".join(out)


def generate_test_6():
    out = ["# TEST 6: In-Context Learning from Feedback\n"]
    out.append("**multi-turn conversation. start fresh chat for each trial.**\n")
    out.append("**recommended: 5-10 trials per model**\n\n")
    out.append("---\n\n")
    out.append("## Turn 1 (baseline)\n")
    out.append("```\ni'm going to give you 8 short paragraphs. for each one, please write a one-sentence summary. respond with ONLY the summary, no preamble.\n\nparagraph 1: " + TEST6_PARAGRAPHS[0] + "\n```\n\n")

    for i in range(1, 8):
        turn = i + 1
        out.append(f"## Turn {turn}\n")
        if turn == 3:
            out.append("```\nthat summary was too long. please make them shorter — under 15 words.\n\nparagraph 3: " + TEST6_PARAGRAPHS[2] + "\n```\n\n")
        elif turn == 5:
            out.append("```\nyour summaries are missing the main argument. focus on the central claim, not supporting details.\n\nparagraph 5: " + TEST6_PARAGRAPHS[4] + "\n```\n\n")
        elif turn == 7:
            out.append("```\nactually now i want long detailed summaries again, like at the start.\n\nparagraph 7: " + TEST6_PARAGRAPHS[6] + "\n```\n\n")
        else:
            out.append("```\nparagraph " + str(turn) + ": " + TEST6_PARAGRAPHS[i] + "\n```\n\n")

    out.append("\n## CSV format for scoring:\n")
    out.append("```\nmodel,trial,turn_1,turn_2,turn_3,turn_4,turn_5,turn_6,turn_7,turn_8\n```\n")
    return "\n".join(out)


def generate_test_7():
    out = ["# TEST 7: Self-Prediction\n"]
    out.append("**4 tasks, 5-10 trials each**\n")
    out.append("**for each: send prediction_prompt in a FRESH chat, capture the prediction. then send actual_prompt in a SEPARATE fresh chat, capture the actual response.**\n\n")
    out.append("---\n\n")
    for task in TEST7_TASKS:
        out.append(f"## Task: {task['name']}\n\n")
        out.append("**step 1 — prediction (fresh chat)**:\n")
        out.append("```\n" + task["prediction_prompt"] + "\n```\n\n")
        out.append("**step 2 — actual (fresh chat)**:\n")
        out.append("```\n" + task["actual_prompt"] + "\n```\n\n")
        out.append("---\n\n")
    out.append("\n## CSV format for scoring:\n")
    out.append("```\nmodel,task,trial,prediction,actual\n```\n")
    return "\n".join(out)


def generate_test_8():
    out = ["# TEST 8: Predictive World Model\n"]
    out.append("**5 scenarios, 5-10 trials each**\n")
    out.append("**multi-turn within a single chat: send phase1, capture prediction, send phase2, capture explanation**\n\n")
    out.append("---\n\n")
    for scenario in TEST8_SCENARIOS:
        out.append(f"## Scenario: {scenario['name']}\n\n")
        out.append("**phase 1**:\n")
        out.append("```\n" + scenario["phase1"] + "\n```\n\n")
        out.append("**phase 2 (after capturing phase 1 response)**:\n")
        out.append("```\n" + scenario["phase2"] + "\n```\n\n")
        out.append("---\n\n")
    out.append("\n## CSV format for scoring:\n")
    out.append("```\nmodel,scenario,trial,prediction,explanation\n```\n")
    return "\n".join(out)


GENERATORS = {
    "1": (PROMPTS_DIR / "test_1_browser_prompts.md", generate_test_1),
    "2": (PROMPTS_DIR / "test_2_browser_prompts.md", generate_test_2),
    "3": (PROMPTS_DIR / "test_3_browser_prompts.md", generate_test_3),
    "4": (PROMPTS_DIR / "test_4_browser_prompts.md", generate_test_4),
    "5": (PROMPTS_DIR / "test_5_browser_prompts.md", generate_test_5),
    "6": (PROMPTS_DIR / "test_6_browser_prompts.md", generate_test_6),
    "7": (PROMPTS_DIR / "test_7_browser_prompts.md", generate_test_7),
    "8": (PROMPTS_DIR / "test_8_browser_prompts.md", generate_test_8),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", type=str, default="all", help="test number 1-8, or 'all'")
    parser.add_argument("--output", type=str, default=None, help="output file path (default: prompts/test_X_browser_prompts.md)")
    args = parser.parse_args()

    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.test == "all":
        tests = list(GENERATORS.keys())
    else:
        tests = [args.test]

    for test_num in tests:
        if test_num not in GENERATORS:
            print(f"unknown test: {test_num}")
            continue
        default_path, gen_fn = GENERATORS[test_num]
        path = Path(args.output) if (args.output and args.test != "all") else default_path
        path.parent.mkdir(parents=True, exist_ok=True)
        content = gen_fn()
        with open(path, "w") as f:
            f.write(content)
        print(f"saved {path} ({len(content)} chars)")


if __name__ == "__main__":
    main()
