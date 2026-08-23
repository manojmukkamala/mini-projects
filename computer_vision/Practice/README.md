# Practice

OpenCV practice notebooks.

> Work In Progress!

- `ComputerVisionPractice.ipynb` — follows the *Mastering Computer
  Vision* course lectures (reading/writing/displaying images,
  greyscaling, color spaces, histograms, drawing, translations,
  rotations, scaling/interpolation). Uses `M5.jpg` / `Mark5.jpg`.
  Some cells still reference a `C:/Users/...` path from the original
  machine — adjust `cv2.imread` to the local image.
- `CV_Practice_Feb01.ipynb` — broader OpenCV exercise on `tesla.jpg`:
  color spaces, histograms, drawing primitives, affine transforms,
  blurring, denoising, sharpening, thresholding, dilation/erosion,
  edge detection, live webcam sketch.

## How to run

From `computer_vision/`:

```sh
uv sync
uv run jupyter lab    # open the notebooks under Practice/
```
