# FOMC Alignment Validation Tool

A Streamlit application for validating LLM-extracted alignment scores from Federal Reserve FOMC meeting transcripts.

## Purpose

This tool validates Claude's assessments of how FOMC meeting participants aligned with policy decisions. Human coders review Claude's alignment scores and justifications, then provide their own assessments.

## Target Meetings

| Date | Context |
|------|---------|
| October 6, 1979 | Volcker's Saturday Night Special |
| August 16, 1994 | Greenspan tightening cycle |
| December 16, 2008 | Financial crisis ZLB |
| August 9, 2011 | Calendar guidance introduced |
| July 31, 2019 | Powell mid-cycle cut |

## Alignment Scale

| Score | Meaning |
|-------|---------|
| -3 | Strongly opposed (explicitly argued against) |
| -2 | Opposed (expressed clear disagreement) |
| -1 | Somewhat opposed (raised concerns) |
| 0 | Neutral / no clear position |
| +1 | Somewhat supportive (mild support) |
| +2 | Supportive (expressed clear agreement) |
| +3 | Strongly supportive (explicitly advocated for) |

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Data Files

- `data/policy_alignment_vF.pkl` - Claude's alignment assessments
- `data/adopted_decisions.pkl` - FOMC decisions
- `data/transcripts.parquet` - Meeting transcripts
- `data/alternatives.pkl` - Policy alternatives
