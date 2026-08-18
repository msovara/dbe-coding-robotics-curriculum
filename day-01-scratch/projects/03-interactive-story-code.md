# Interactive Story (Day 1) — Scratch code

This page is **only the block scripts**. Teaching notes and exercises: [facilitator guide](03-interactive-story-facilitator-guide.md).

**Setup:** sprites `Child`, `Friend`. Backdrops `Home`, `Road`, `School` (in that order). Message `scene 2`.

## Stage

```text
when green flag clicked
switch backdrop to (Home)
```

```text
when I receive (scene 2)
switch backdrop to (Road)
```

## Child

```text
when green flag clicked
show
go to x: (-80) y: (-60)
switch backdrop to (Home)
say [I missed the taxi. I am late for school.] for (2) seconds
```

```text
when this sprite clicked
say [I need help. Press the right arrow.] for (2) seconds
```

```text
when [right arrow] key pressed
broadcast (scene 2)
hide
```

## Friend

```text
when green flag clicked
hide
go to x: (80) y: (-60)
```

```text
when I receive (scene 2)
show
say [Walk with me. Press the arrow again.] for (2) seconds
```

```text
when [right arrow] key pressed
switch backdrop to (next backdrop)
say [We arrived on time. Next time I will leave earlier.] for (2) seconds
```

## How to run

1. Click the **green flag** (Home; Child speaks).
2. **Click** Child.
3. Press the **right arrow** (Road; Friend appears; Child hides).
4. Press the **right arrow** again (School; ending line).

**Check:** three named backdrops; Friend hidden on green flag; `scene 2` spelled the same on broadcast and receive.

## Other say lines (same blocks, change only the text)

| Prompt | Child on flag | Child on click | Friend on `scene 2` | Friend on last arrow |
|--------|---------------|----------------|---------------------|----------------------|
| Kindness | My classmate dropped their books. | I will help you pick them up. | Thank you. Press the arrow. | We did it together. Kindness helps. |
| Water | The tap is running. We are wasting water. | Close the tap. Save water. | The tap is closed. Press the arrow. | We saved water. |
| Two languages | Hello! Sawubona! | How are you? Unjani? | I am fine. Ngiyaphila. | Goodbye! Hamba kahle! |
