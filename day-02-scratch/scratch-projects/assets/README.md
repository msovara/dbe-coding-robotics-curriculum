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
| `d903687e5ae79a777b4720f3bc7966fa.svg` | Custom full-width grass | Ground |
| `f52bde34d8027aab14b53f228fe5cc14.svg` | **Avery** | Guide |
| `e7ce31db37f7abd2901499db2e9ad83a.svg` | **Pico** | Scientist |
| `89679608327ad572b93225d06fe9edda.svg` | **Robot** | Robot |

Source: [Scratch sprite library](https://github.com/scratchfoundation/scratch-gui/tree/develop/src/lib/libraries) (MIT-licensed Scratch assets).

To refresh assets:

```bash
curl -L "https://cdn.assets.scratch.mit.edu/internalapi/asset/d147f16e3e2583719c073ac5b55fe3ca.svg/get/" -o d147f16e3e2583719c073ac5b55fe3ca.svg
```

Then run `python day-02-scratch/scratch-projects/build_solutions.py`.
