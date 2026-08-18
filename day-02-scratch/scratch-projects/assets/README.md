Official Scratch library costumes, bundled so the `.sb3` files open with the intended art.

| File | Scratch library sprite | Used as |
|------|------------------------|---------|
| `d147f16e3e2583719c073ac5b55fe3ca.svg` | **Bowl** | Basket |
| `3826a4091a33e4d26f87a2fac7cf796b.svg` | **Apple** | Fruit |
| `46dde2baba61a7e48463ae8e58441470.svg` | **Referee** | Referee |
| `cd21514d0531fdffb22204e0ec5ed84a.svg` | Default backdrop | Stage |
| `c9630e30e59e4565e785a26f58568904.svg` | **Cloud** | Cloud |
| `406808d86aff20a15d592b308e166a32.svg` | **Sun** | Sun |
| `1c44b7494dec047371f74c705f1d99fc.svg` | **Ball** (costume e) | Droplet |
| `grass-strip.svg` | Custom full-width grass | Ground |

Source: [Scratch sprite library](https://github.com/scratchfoundation/scratch-gui/tree/develop/src/lib/libraries) (MIT-licensed Scratch assets).

To refresh assets:

```bash
curl -L "https://cdn.assets.scratch.mit.edu/internalapi/asset/d147f16e3e2583719c073ac5b55fe3ca.svg/get/" -o d147f16e3e2583719c073ac5b55fe3ca.svg
```

Then run `python day-02-scratch/scratch-projects/build_solutions.py`.
