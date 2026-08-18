# Catch Game — Facilitator block annotations

**Audience:** Facilitators and provincial specialists (Day 2 workshop)  
**Use this for:** What to **say** while explaining each block — not text to paste into Scratch.

**Companion files**

| File | Purpose |
|------|---------|
| [Project 1 memo](../projects/project-templates.md#project-1-catch-game) | Clean block scripts (answer key) |
| [`01-catch-game.sb3`](solutions/01-catch-game.sb3) | Working project to demo |
| [Video script](videos/01-catch-game-video-script.md) | Narrated walkthrough |

---

## Before you demo (2 minutes)

Say something like:

> We are building a **catch game**: the player moves a basket, fruit **clones** fall from the top, each catch adds 1 to **score**, and at **20 points** the game stops with a win message.  
> Three ideas today: **cloning** (one hidden sprite spawns many copies), a **variable for all sprites** (shared score), and **broadcast** (tell another sprite “you win”).

**Check on screen before coding**

| Item | Setting | What to say |
|------|---------|-------------|
| Variable `score` | **For all sprites** | “Every sprite — basket, fruit, referee — reads the same score.” |
| Message `win` | In **Messages** | “A broadcast is like shouting a message other sprites can hear.” |
| Sprites | `Basket`, `Fruit`, `Referee` | “Three roles: player, falling objects, game rules.” |

---

## Basket sprite — one script

**Role in the game:** The player’s paddle at the bottom.

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Starts when the game begins. | “Green flag = start button for every `when green flag` script.” |
| `go to x: (0) y: (-145)` | Puts the bowl at the **bottom centre**. | “y is up/down; negative y is toward the bottom of the stage.” |
| `show` | Makes the basket visible. | “If you forget `show`, the sprite might stay hidden from a previous test.” |
| `forever` | Keeps checking keys for the whole game. | “`forever` never ends unless we `stop all` elsewhere.” |
| `if ‹key (left arrow) pressed?›` | Is the player pressing left? | “Sensing blocks are hexagons — they are true or false.” |
| `change x by (-10)` | Move **left** 10 steps. | “x is left/right; negative x = left.” |
| `if ‹key (right arrow) pressed?›` | Is the player pressing right? | “Two separate `if`s — not `else`, so both can be checked each loop.” |
| `change x by (10)` | Move **right** 10 steps. | “Teachers can change 10 to 15 for a faster basket.” |

**Demo tip:** Click green flag and move with arrow keys before adding fruit.

---

## Fruit sprite — Script 1 (spawn clones)

**Role:** Hide the “master” apple and keep creating falling copies.

**Important:** Both Fruit scripts live on the **same sprite** — two hats, one sprite.

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Starts spawning when the game begins. | “Script 1 runs on the **original** fruit only.” |
| `hide` | Hides the original apple. | “If we skip `hide`, one apple sits in the middle while clones also fall — looks broken.” |
| `forever` | Keeps making clones for the whole game. | “The original never moves; only **clones** use Script 2.” |
| `create clone of (myself)` | Makes a copy that runs **when I start as a clone**. | “`myself` means this sprite — Fruit. Each clone is independent.” |
| `wait (pick random (1) to (3)) seconds` | Pause before the next spawn. | “Random wait = apples don’t fall in a perfect rhythm — feels more like a game.” |

---

## Fruit sprite — Script 2 (each clone)

**Role:** Each clone appears at the top, falls, scores or misses, then **disappears**.

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when I start as a clone` | Runs **once per clone** when it is created. | “This hat never runs on the hidden original — only on copies.” |
| `go to x: (pick random (-200) to (200)) y: (170)` | Random horizontal position at the **top**. | “y = 170 is near the top edge; random x spreads apples across the stage.” |
| `show` | Shows **this clone** only. | “Clones can start hidden like the parent; `show` makes this copy visible.” |
| `forever` | Fall loop until caught or off screen. | “We use `forever` here because of how the loop must end — see facilitator pitfalls below.” |
| `if ‹touching (Basket)? or (y position) < (-170)›` | Stop when **caught** or **past the bottom**. | “Two ways to finish: hit the bowl, or miss and fall off the stage.” |
| `if ‹touching (Basket)?›` (inside) | Only when the bowl caught this apple. | “Nested `if` — score only on a catch, not on a miss.” |
| `change (score) by (1)` | Add one point. | “Score must be **for all sprites** or this block updates the wrong variable.” |
| `delete this clone` | Remove this apple from the game. | “Without this, apples pile up at the bottom — a very common bug.” |
| `stop (this script)` | End this clone’s script after cleanup. | “Put **`delete` and score before `stop`** — `stop` ends the whole script immediately.” |
| `change y by (-5)` | Move **down** 5 steps. | “Negative y = downward. Smaller steps + short wait = smoother fall.” |
| `wait (0.03) seconds` | Small pause between steps. | “Without `wait`, the fall is instant and hard to see.” |

### Facilitator pitfalls (Script 2)

| Mistake | Symptom | Fix |
|---------|---------|-----|
| `score` is “for this sprite only” | Score stays 0 when catching | Recreate `score` as **for all sprites** |
| `delete this clone` **below** the `forever` loop | Apples stack at bottom; score stuck | Move **score + delete inside** the outer `if`, before `stop` |
| Only `stop (this script)` inside the `if` | Same — clones freeze on screen | Add **delete this clone** (and score `if`) before `stop` |
| Script 2 on a **second** sprite | Clones never fall correctly | Both hats on **Fruit** |
| Sprite named “Bowl” but code says `Basket` | Touching never true | Rename sprite or change `touching` menu to match |
| No `hide` on Script 1 | One apple visible in centre | Add `hide` after green flag on Script 1 |

---

## Referee sprite — Script 1 (reset and win check)

**Role:** Reset score at start; detect win at 20 points.

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Starts with the game. | “Referee is optional for teaching, but nice for a clear win moment.” |
| `set (score) to (0)` | Reset score. | “Do this on green flag so every replay starts at zero.” |
| `hide` | Hide referee until win. | “Players focus on basket and fruit; referee appears for celebration.” |
| `wait until ‹(score) > (19)›` | Wait until **20 or more** points. | “`> 19` means 20 catches — same as ‘score reaches 20’.” |
| `broadcast (win)` | Tell all sprites that listen for `win`. | “Broadcast doesn’t move sprites — it triggers other scripts.” |

---

## Referee sprite — Script 2 (celebration)

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when I receive (win)` | Runs when Script 1 broadcasts `win`. | “Second hat on Referee — event-driven, like Script 2 on Fruit.” |
| `show` | Show the referee. | “Celebration character enters the stage.” |
| `say [You win!] for (3) seconds` | Message in a speech bubble. | “Stage cannot `say` — use a sprite for text.” |
| `stop (all)` | Stop every script in the project. | “Game over — nothing keeps spawning or moving.” |

---

## Suggested teaching order (45–60 min)

1. **Basket only** — move with arrows (5–10 min).  
2. **Add `score` for all sprites** — show monitor on stage (2 min).  
3. **Fruit Script 1** — hide + clone + wait; confirm clones appear (10 min).  
4. **Fruit Script 2** — fall, score, delete; debug in pairs (15–20 min).  
5. **Referee + broadcast** — win at 20 (10 min).  
6. **Playtest** — green flag, catch 20, red stop sign to reset (5 min).

---

## Quick demo script (60 seconds)

> “Green flag starts three things: the basket listens for arrows, the fruit hides and spawns clones every few seconds, and the referee resets score.  
> Each clone drops from a random spot. Catch it with the bowl — score goes up, clone disappears. Miss — it falls off and still disappears.  
> At twenty points, the referee broadcasts **win**, says **You win!**, and everything stops.”

---

## Links

- **Download `.sb3`:** [raw GitHub file](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-02-scratch/scratch-projects/solutions/01-catch-game.sb3)  
- **Run guide:** [scratch-projects README](README.md#how-to-run-01-catch-gamesb3)
