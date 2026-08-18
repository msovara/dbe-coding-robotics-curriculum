# Catch Game sprite assets (Scratch 3 library)

Official Scratch library costumes, bundled so the `.sb3` opens with the intended art.

| File | Scratch library sprite | Used as |
|------|------------------------|---------|
| `d147f16e3e2583719c073ac5b55fe3ca.svg` | **Bowl** | Basket |
| `3826a4091a33e4d26f87a2fac7cf796b.svg` | **Apple** | Fruit |
| `46dde2baba61a7e48463ae8e58441470.svg` | **Referee** | Referee |
| `cd21514d0531fdffb22204e0ec5ed84a.svg` | Default backdrop | Stage |

Source: [Scratch sprite library](https://github.com/scratchfoundation/scratch-gui/tree/develop/src/lib/libraries) (MIT-licensed Scratch assets).

To refresh assets:

```bash
curl -L "https://cdn.assets.scratch.mit.edu/internalapi/asset/d147f16e3e2583719c073ac5b55fe3ca.svg/get/" -o d147f16e3e2583719c073ac5b55fe3ca.svg
```

Then run `python day-02-scratch/scratch-projects/build_solutions.py`.
