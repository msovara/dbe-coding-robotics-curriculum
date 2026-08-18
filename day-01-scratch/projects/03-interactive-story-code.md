# Interactive Story (Day 1)

**Time:** 60–90 minutes  
**Concepts:** events, backdrops, broadcast

### Task

Make a three-scene story: Home → Road → School. The player turns the page with a **click** and the **right arrow**.

### Requirements

- Sprites: **Child**, **Friend**.
- Backdrops: **Home**, **Road**, **School** (in that order).
- Green flag starts at Home. Friend stays **hidden**.
- Clicking **Child** shows a line of dialogue.
- Right arrow broadcasts `scene 2`: backdrop Road, Child hides, Friend appears.
- Right arrow again goes to School and the ending line.

### Memo: suggested Scratch script

**Scratch file:** [`03-interactive-story.sb3`](../scratch-projects/solutions/03-interactive-story.sb3) — open in Scratch to see and test the blocks.

**Download:** [Download `03-interactive-story.sb3`](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-01-scratch/scratch-projects/solutions/03-interactive-story.sb3)

**Facilitator annotations (what to say for each block):** [Interactive Story facilitator annotations](03-interactive-story-facilitator-guide.md) — separate from the scripts below; use while explaining, not in Scratch.

**How to run:** Load the `.sb3` (**File → Load from your computer**). Green flag (Home, Child speaks) → **click** Child → **right arrow** (Road, Friend appears) → **right arrow** (School, ending line).

**Setup:** sprites `Child`, `Friend`. Backdrops `Home`, `Road`, `School` (in that order). Message `scene 2`. Friend starts hidden.

**Stage**

```text
when green flag clicked
switch backdrop to (Home)
```

```text
when I receive (scene 2)
switch backdrop to (Road)
```

**Child — start position**

```text
when green flag clicked
show
go to x: (-80) y: (-60)
switch backdrop to (Home)
say [I missed the taxi. I am late for school.] for (2) seconds
```

**Child — click**

```text
when this sprite clicked
say [I need help. Press the right arrow.] for (2) seconds
```

**Child — next scene**

```text
when [right arrow] key pressed
broadcast (scene 2)
hide
```

**Friend — start hidden**

```text
when green flag clicked
hide
go to x: (80) y: (-60)
```

**Friend — scene 2**

```text
when I receive (scene 2)
show
say [Walk with me. Press the arrow again.] for (2) seconds
```

**Friend — ending**

```text
when [right arrow] key pressed
switch backdrop to (next backdrop)
say [We arrived on time. Next time I will leave earlier.] for (2) seconds
```

**Check:** three named backdrops; Friend hidden on green flag; `scene 2` spelled the same on broadcast and receive. In the `.sb3`, each arrow script also checks the backdrop name so the first press is Road and the second is School.

**Other say lines (same scripts, change only the text)**

| Prompt | Child on flag | Child on click | Friend on `scene 2` | Friend on last arrow |
|--------|---------------|----------------|---------------------|----------------------|
| Kindness | My classmate dropped their books. | I will help you pick them up. | Thank you. Press the arrow. | We did it together. Kindness helps. |
| Water | The tap is running. We are wasting water. | Close the tap. Save water. | The tap is closed. Press the arrow. | We saved water. |
| Two languages | Hello! Sawubona! | How are you? Unjani? | I am fine. Ngiyaphila. | Goodbye! Hamba kahle! |
