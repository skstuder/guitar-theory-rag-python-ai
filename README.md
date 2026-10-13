# guitar-theory-rag-python-ai

A prototype for asking music theory questions related to guitar that showcases retrieval augmentation generation for better output

## Data used

I pulled music theory data from (This repo)[https://github.com/seancolsen/music-theory-data] for music theory context

## Setup

- Requires Python and an OpenAI API key.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

- Add your OpenAI key to `.env`, see `.env.example` for reference

```sh
python store_data.py  # Build the local vector database
python main.py        # Start the assistant
```

- Prompt the assistance with music theory questions
- `prompts/music_theory_assistant.txt` has the prompt for OpenAI if you want to tweak it
- Example output

```
Loading weights: 100%|█████████████████████████████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 8495.67it/s]
Music Theory Assistant
Ask a question, or type 'quit' to exit.

Example questions:
- What is a diminished seventh chord?
- How does a half-diminished chord differ from a diminished chord?
- Where can I play a C major triad near the 7th fret?

You: How does a half-diminished chord differ from a diminished chord? Give a guitar tab for each to showcase the difference

Retrieved source records:
[Source 1] data/source_music_theory/music_data/Chords.yaml (Chords:11)
[Source 2] data/source_music_theory/music_data/Chords.yaml (Chords:9)
[Source 3] data/source_music_theory/music_data/Intervals.yaml (Intervals:138)
[Source 4] data/source_music_theory/music_data/Intervals.yaml (Intervals:133)
[Source 5] data/source_music_theory/music_data/Intervals.yaml (Intervals:74)
[Source 6] data/source_music_theory/music_data/Intervals.yaml (Intervals:115)
[Source 7] data/source_music_theory/music_data/Chords.yaml (Chords:0)
[Source 8] data/source_music_theory/music_data/Intervals.yaml (Intervals:129)

Assistant:
RELEVANT INFORMATION FOUND IN THE RAG SOURCE
- The half-diminished chord is also called half-diminished seventh, minor seventh flat five, and is written as ø7, ø, or m7♭5 [Source 1].
- The diminished chord can mean a diminished triad or diminished seventh chord, with the diminished seventh chord abbreviated as dim7 or o7 [Source 2], and the diminished triad as dim or ° [Source 7].
- Specific intervals related to diminished chords are noted but do not directly define the chord differences in the retrieved records [Sources 3-8].

ANSWER BUILT FROM THAT INFORMATION
A half-diminished chord differs from a fully diminished chord primarily in the seventh interval:
- Half-diminished chord: minor seventh (♭7) interval above the root, and diminished fifth (♭5) — formula: root, minor third, diminished fifth, minor seventh.
- Fully diminished chord (commonly diminished seventh chord): diminished seventh (double-flatted seventh) instead of minor seventh — formula: root, minor third, diminished fifth, diminished seventh.

Example in C:
- Half-diminished Cø7: C - E♭ - G♭ - B♭
- Diminished seventh Cdim7: C - E♭ - G♭ - B𝄫 (A)

Guitar tabs in standard tuning (EADGBE):

C half-diminished (Cm7♭5)
```

e|---x---
B|---4--- (Bb)
G|---3--- (Gb)
D|---4--- (Eb)
A|---3--- (C)
E|---x---

```

C diminished seventh (Cdim7)
```

e|---2--- (Bb♭ = A)
B|---1--- (Gb)
G|---2--- (Eb)
D|---1--- (C)
A|---x---
E|---x---

```

This shows the voicing difference wher

```
