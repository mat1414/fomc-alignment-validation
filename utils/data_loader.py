"""
Data loading utilities for FOMC Alignment Validation Tool.
"""
import pandas as pd
import pickle
from typing import List, Dict, Optional
import streamlit as st

from config import DATA_PATHS


@st.cache_data
def load_all_data() -> Dict[str, pd.DataFrame]:
    """Load all data files once. Cached for performance."""
    data = {}

    # Load transcripts (parquet format)
    data['transcripts'] = pd.read_parquet(DATA_PATHS["transcripts"])

    # Load pickle files
    with open(DATA_PATHS["decisions"], 'rb') as f:
        data['decisions'] = pickle.load(f)

    with open(DATA_PATHS["alignments"], 'rb') as f:
        data['alignments'] = pickle.load(f)

    with open(DATA_PATHS["alternatives"], 'rb') as f:
        data['alternatives'] = pickle.load(f)

    return data


def get_meeting_decisions(ymd: str, decisions_df: pd.DataFrame) -> pd.DataFrame:
    """Get all decisions for a meeting."""
    return decisions_df[decisions_df['ymd'] == ymd].reset_index(drop=True)


def get_decision_speakers(ymd: str, description: str, alignments_df: pd.DataFrame) -> List[str]:
    """Get all speakers assessed for a specific decision."""
    # Use description_y to match with decisions table description
    mask = (alignments_df['ymd'] == ymd) & (alignments_df['description_y'] == description)
    speakers = alignments_df[mask]['stablespeaker'].unique().tolist()
    return sorted(speakers)


def get_alignment(ymd: str, description: str, speaker: str, alignments_df: pd.DataFrame) -> Optional[Dict]:
    """Get Claude's alignment assessment for a speaker-decision pair."""
    # Use description_y to match with decisions table description
    mask = (
        (alignments_df['ymd'] == ymd) &
        (alignments_df['description_y'] == description) &
        (alignments_df['stablespeaker'] == speaker)
    )
    rows = alignments_df[mask]

    if len(rows) == 0:
        return None

    row = rows.iloc[0]
    return {
        'score': row['alignment'],
        'justification': row['justification']
    }


def get_speaker_transcript(ymd: str, speaker: str, transcripts_df: pd.DataFrame) -> str:
    """Get all statements by a specific speaker in a meeting."""
    mask = (
        (transcripts_df['ymd'].astype(str) == str(ymd)) &
        (transcripts_df['stablespeaker'] == speaker)
    )
    speaker_df = transcripts_df[mask].sort_values('n')

    if len(speaker_df) == 0:
        return f"No statements found for {speaker} in this meeting."

    lines = []
    for _, row in speaker_df.iterrows():
        title = str(row.get('titletidy', '')).strip()
        name = str(row.get('stablespeaker', '')).strip()
        text = str(row.get('combined', '')).strip()

        if title and name:
            speaker_label = f"{title} {name}"
        elif name:
            speaker_label = name
        else:
            speaker_label = "UNKNOWN"

        if text:
            lines.append(f"{speaker_label}: {text}")

    return "\n\n".join(lines)


def get_full_transcript(ymd: str, transcripts_df: pd.DataFrame) -> str:
    """Get full transcript for a meeting."""
    mask = transcripts_df['ymd'].astype(str) == str(ymd)
    meeting_df = transcripts_df[mask].sort_values('n')

    if len(meeting_df) == 0:
        return f"No transcript found for meeting {ymd}."

    lines = []
    for _, row in meeting_df.iterrows():
        title = str(row.get('titletidy', '')).strip()
        name = str(row.get('stablespeaker', '')).strip()
        text = str(row.get('combined', '')).strip()

        if title and name:
            speaker_label = f"{title} {name}"
        elif name:
            speaker_label = name
        else:
            speaker_label = "UNKNOWN"

        if text:
            lines.append(f"{speaker_label}: {text}")

    return "\n\n".join(lines)


def get_alternatives(ymd: str, alternatives_df: pd.DataFrame) -> List[Dict]:
    """Get policy alternatives for a meeting."""
    meeting_alts = alternatives_df[alternatives_df['ymd'] == ymd]

    if len(meeting_alts) == 0:
        return []

    return meeting_alts.sort_values('label')[['label', 'description', 'statement']].to_dict('records')


def search_transcript(transcript_text: str, search_term: str) -> List[Dict]:
    """Search transcript for a term and return matching excerpts."""
    if not search_term:
        return []

    results = []
    search_lower = search_term.lower()

    # Split into utterances
    utterances = transcript_text.split("\n\n")

    for i, utterance in enumerate(utterances):
        if search_lower in utterance.lower():
            results.append({
                "index": i,
                "text": utterance,
                "preview": utterance[:200] + "..." if len(utterance) > 200 else utterance
            })

    return results


def get_meeting_stats(ymd: str, data: Dict) -> Dict:
    """Get statistics for a meeting."""
    decisions = get_meeting_decisions(ymd, data['decisions'])
    alignments = data['alignments'][data['alignments']['ymd'] == ymd]

    num_decisions = len(decisions)
    num_speakers = alignments['stablespeaker'].nunique()
    num_pairs = len(alignments)

    return {
        'num_decisions': num_decisions,
        'num_speakers': num_speakers,
        'num_pairs': num_pairs
    }
