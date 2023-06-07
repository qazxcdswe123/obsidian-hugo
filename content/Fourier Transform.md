---
aliases: []
date created: Mar 1st, 2023
date modified: Jun 5th, 2023
---

## What
Transforms a function of time, a signal, into a function of frequency.

The Fourier Transform decomposes or breaks down a time-based function into a sum of sine waves of different frequencies. Each sine wave corresponds to a certain frequency, and the size (or amplitude) of that sine wave represents how much of that particular frequency is present in the original signal. This gives us a frequency spectrum of the signal.

The result of the Fourier Transform is a function in the frequency domain, where the X-axis represents frequencies (not time), and the Y-axis represents the amount of each frequency present in the original signal.

## How
$$F(w) = ∫_{-∞}^{∞} f(t) e^{-iwt} dt$$

## Applications
- Decomposing frequency from sound.
- If earthquake vibrations can be separated into "ingredients" (vibrations of different speeds & amplitudes), buildings can be designed to avoid interacting with the strongest ones.
- If sound waves can be separated into ingredients (bass and treble frequencies), we can boost the parts we care about, and hide the ones we don't. The crackle of random noise can be removed. Maybe similar "sound recipes" can be compared (music recognition services compare recipes, not the raw audio clips).
- If computer data can be represented with oscillating patterns, perhaps the least-important ones can be ignored. This "lossy [[compression]]" can drastically shrink file sizes (and why JPEG and MP3 files are much smaller than raw .bmp or .wav files).
- If a radio wave is our signal, we can use filters to listen to a particular channel. In the smoothie world, imagine each person paid attention to a different ingredient: Adam looks for apples, Bob looks for bananas, and Charlie gets cauliflower (sorry bud).

## Links
- [Fourier Transforms - MATLAB & Simulink](https://www.mathworks.com/help/matlab/math/fourier-transforms.html)
- [[Fourier Series]]