# Configuration for FOMC Alignment & Influence Validation Tool

TARGET_MEETINGS = {
    "19791006": "October 6, 1979 (Volcker's Saturday Night Special)",
    "19940816": "August 16, 1994 (Greenspan tightening cycle)",
    "20081216": "December 16, 2008 (Financial crisis ZLB)",
    "20110809": "August 9, 2011 (Calendar guidance introduced)",
    "20190731": "July 31, 2019 (Powell mid-cycle cut)"
}

ALIGNMENT_SCALE = {
    -3: "Strongly opposed (explicitly argued against)",
    -2: "Opposed (expressed clear disagreement)",
    -1: "Somewhat opposed (raised concerns)",
    0: "Neutral / no clear position",
    1: "Somewhat supportive (mild support)",
    2: "Supportive (expressed clear agreement)",
    3: "Strongly supportive (explicitly advocated for)"
}

INFLUENCE_SCALE = {
    0: "No influence (position ignored or overruled)",
    1: "Limited influence (acknowledged but didn't shape outcome)",
    2: "Moderate influence (arguments engaged with, some impact)",
    3: "Strong influence (clearly shaped the outcome)"
}

ACCURACY_OPTIONS = ["yes", "partially", "no"]

CONFIDENCE_LEVELS = ["high", "medium", "low"]

DATA_PATHS = {
    "transcripts": "data/transcripts.parquet",
    "decisions": "data/adopted_decisions.pkl",
    "alignments": "data/policy_alignments.pkl",
    "influence": "data/policy_influence.pkl",
    "alternatives": "data/alternatives.pkl",
    "results_dir": "data/coding_results/"
}
