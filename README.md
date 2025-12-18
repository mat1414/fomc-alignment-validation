# FOMC Alignment & Influence Validation Tool

A Streamlit application for human validation of Claude's alignment and influence assessments for FOMC meeting participants.

## Purpose

This tool enables human coders to review and validate:
- **Alignment scores** (-3 to +3): How aligned each speaker was with adopted policy decisions
- **Influence scores** (0 to 3): How much influence each speaker had on the final decision

For each speaker-decision pair, coders review Claude's assessment and provide their own score.

## Target Meetings

- **October 6, 1979**: Volcker's Saturday Night Special
- **August 16, 1994**: Greenspan tightening cycle
- **December 16, 2008**: Financial crisis ZLB
- **August 9, 2011**: Calendar guidance introduced
- **July 31, 2019**: Powell mid-cycle cut

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## Workflow

1. Enter your Coder ID
2. Select a meeting to validate
3. For each decision, review speakers one at a time:
   - Read the decision context
   - Review Claude's alignment assessment and justification
   - Indicate if quotes are accurate and support the interpretation
   - Provide your own alignment score (-3 to +3)
   - Review Claude's influence assessment
   - Provide your own influence score (0 to 3)
   - Add optional notes and confidence level
   - Mark as complete and move to next speaker
4. Download your results (JSON for progress saving, CSV for analysis)

## Scales

### Alignment Scale (-3 to +3)
- **-3**: Strongly opposed (explicitly argued against)
- **-2**: Opposed (expressed clear disagreement)
- **-1**: Somewhat opposed (raised concerns)
- **0**: Neutral / no clear position
- **+1**: Somewhat supportive (mild support)
- **+2**: Supportive (expressed clear agreement)
- **+3**: Strongly supportive (explicitly advocated for)

### Influence Scale (0 to 3)
- **0**: No influence (position ignored or overruled)
- **1**: Limited influence (acknowledged but didn't shape outcome)
- **2**: Moderate influence (arguments engaged with, some impact)
- **3**: Strong influence (clearly shaped the outcome)

## Data Files

- `data/transcripts.parquet`: Full FOMC meeting transcripts
- `data/adopted_decisions.pkl`: Policy decisions for each meeting
- `data/policy_alignments.pkl`: Claude's alignment assessments
- `data/policy_influence.pkl`: Claude's influence assessments
- `data/alternatives.pkl`: Policy alternatives presented at meetings

## Output Files

Results can be downloaded in two formats:
- **JSON**: Full data including metadata, suitable for restoring progress
- **CSV**: Flat format for statistical analysis

## Restoring Progress

To continue a previous session:
1. Use the "Restore Progress" section in the sidebar
2. Upload a previously downloaded JSON file
3. Click "Restore Progress" to resume where you left off

## Project Structure

```
fomc_alignment_validation/
├── app.py                 # Main Streamlit application
├── config.py              # Configuration and scales
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── utils/
│   ├── __init__.py
│   ├── data_loader.py     # Data loading utilities
│   └── export.py          # Export and restore utilities
└── data/
    ├── transcripts.parquet
    ├── adopted_decisions.pkl
    ├── policy_alignments.pkl
    ├── policy_influence.pkl
    └── alternatives.pkl
```
