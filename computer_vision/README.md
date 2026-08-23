# computer_vision

OpenCV + Jupyter computer-vision experiments.

> Work in Progress!

## What's inside

- `AutomaticLaneDetection/` — step-by-step lane-detection pipeline on
  a road image (grayscale → Gaussian blur → Canny → region of interest
  → Hough lines → left/right lane averaging).
- `Practice/` — OpenCV practice notebooks: color spaces, histograms,
  drawing, translations/rotations/scaling, blurring, sharpening,
  thresholding, morphology, edge detection.

## How to run

```sh
cd computer_vision
uv sync              # creates .venv from uv.lock (OpenCV, numpy, ...)
uv run jupyter lab   # open the notebooks under AutomaticLaneDetection/ or Practice/
```

The notebooks show results with `cv2.imshow`, which needs a local GUI
display (they will not display on headless machines or remote SSH
without X forwarding).
