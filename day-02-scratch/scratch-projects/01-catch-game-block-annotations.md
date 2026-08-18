# Catch Game — Block-by-block annotations

Guide for **Project 1** (Day 2). Matches [`01-catch-game.sb3`](solutions/01-catch-game.sb3).

Open the `.sb3` in Scratch: each main block has a **comment bubble** (yellow note) explaining what it does. This page is the same text in table form for printing or the workshop site.

**Setup (before scripts):**

| Item | Setting | Why |
|------|---------|-----|
| Variable `score` | **For all sprites** | Basket, Fruit clones, and Referee must all read and update the same score |
| Broadcast `win` | (create in Messages) | Tells the Referee to show the win message |
| Sprites | `Basket`, `Fruit`, `Referee` | Three roles: move, spawn/fall, game rules |

---

## Basket sprite

**Role:** Player control — moves left and right at the bottom of the stage.

| Block | What it does |
|-------|----------------|
| `when green flag clicked` | Starts this script when the player begins the game. |
| `go to x: (0) y: (-145)` | Places the bowl at the **bottom centre** of the stage (y −145 is near the bottom edge). |
| `show` | Makes the basket visible on the stage. |
| `forever` | Repeats the movement checks for the **whole game**. |
| `if ‹key (left arrow) pressed?›` | Checks whether the player is holding the **left arrow** key. |
| `change x by (-10)` | Moves the basket **10 steps left** while the key is pressed. |
| `if ‹key (right arrow) pressed?›` | Checks whether the player is holding the **right arrow** key. |
| `change x by (10)` | Moves the basket **10 steps right** while the key is pressed. |

---

## Fruit sprite — Script 1 (spawn clones)

**Role:** Hide the original apple and keep creating falling clones.

Both Fruit scripts live on the **same sprite** — two separate stacks in the code area.

| Block | What it does |
|-------|----------------|
| `when green flag clicked` | Starts when the game begins. |
| `hide` | Hides the **original** fruit so players only see clones (not a static apple in the middle). |
| `forever` | Keeps spawning fruit for the entire game. |
| `create clone of (myself)` | Makes a **copy** of the Fruit sprite; each copy runs Script 2 below. |
| `wait (pick random (1) to (3)) seconds` | Waits **1–3 seconds** before the next clone — controls how fast fruit appears. |

---

## Fruit sprite — Script 2 (each clone)

**Role:** Each clone appears at the top, falls, scores or misses, then disappears.

| Block | What it does |
|-------|----------------|
| `when I start as a clone` | Runs **once per clone** when that clone is created (not for the hidden original). |
| `go to x: (pick random (-200) to (200)) y: (170)` | Places this clone at a **random horizontal** position at the **top** of the stage. |
| `show` | Makes **this clone** visible (the original stays hidden). |
| `repeat until ‹…›` | Keeps falling until **caught** or **off the bottom**. Condition: touching Basket **or** y position &lt; −170. |
| `change y by (-5)` | Moves the fruit **down 5 steps** each loop — the falling motion. |
| `wait (0.03) seconds` | Short pause so the fall looks **smooth**, not instant. |
| `if ‹touching (Basket)?›` | After the loop: was this clone **on the bowl** when it stopped? |
| `change (score) by (1)` | **Adds 1 point** for a successful catch (only runs if touching Basket). |
| `delete this clone` | Removes this clone from the stage — after a **catch or a miss**. |

---

## Referee sprite — Script 1 (score and win)

**Role:** Reset score at start; detect when the player reaches 20 points.

| Block | What it does |
|-------|----------------|
| `when green flag clicked` | Starts when the game begins. |
| `set (score) to (0)` | **Resets** the score to zero for a new game. |
| `hide` | Hides the referee until the player **wins**. |
| `forever` | Keeps checking the score until the win condition is met. |
| `wait (0.05) seconds` | Short pause so the script does not overload the computer (polls score ~20 times per second). |
| `if ‹(score) > (19)›` | True when the player has **20 or more** points (same as “score reaches 20”). |
| `broadcast (win)` | Sends the **win** message to all sprites listening for it. |
| `stop (this script)` | Stops this forever loop after broadcasting (game is won). |

---

## Referee sprite — Script 2 (win message)

**Role:** Show celebration and stop the whole project.

| Block | What it does |
|-------|----------------|
| `when I receive (win)` | Runs when Script 1 **broadcasts (win)**. |
| `show` | Makes the referee sprite **visible** on the stage. |
| `say [You win!] for (3) seconds` | Shows the win message in a speech bubble for **3 seconds**. |
| `stop (all)` | Stops **every script** in the project — game over. |

---

## How the pieces connect

```text
Green flag
  → Basket: show at bottom, listen for arrow keys
  → Fruit: hide original, spawn clones every 1–3 s
  → Referee: score = 0, watch for score > 19

Each clone: top → fall → catch? → score +1 → delete clone

Score reaches 20 → broadcast (win) → Referee says "You win!" → stop all
```

---

## Facilitator tips

- **Two hats on Fruit** — Script 1 and Script 2 are both on the **Fruit** sprite, not two different sprites.
- **Original stays hidden** — If you see one apple stuck in the centre, Script 1 is missing `hide`.
- **Score variable** — Must be **for all sprites** or clones cannot update the score.
- **Win at 20** — `score > 19` means “20 or more”; equivalent to `score = 20` after exactly twenty catches.

**See also:** [project-templates.md](../projects/project-templates.md) · [video script](videos/01-catch-game-video-script.md) · [README](README.md)
