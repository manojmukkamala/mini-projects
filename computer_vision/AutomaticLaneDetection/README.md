# Automatic Lane Detection Model

Step-by-step lane-detection pipeline on `road.jpg`, built one stage at
a time in `LaneDetection.ipynb`:

1. Grayscale conversion
2. Gaussian blur
3. Canny edge detection
4. Region-of-interest mask
5. Bitwise AND
6-7. Hough line transform (`cv2.HoughLinesP`)
8. Split detected lines into left / right lanes
9. Optimization: average slope and intercept per lane
10. (Optional) run the whole pipeline over a video

## How to run

From `computer_vision/`:

```sh
uv sync
uv run jupyter lab    # open AutomaticLaneDetection/LaneDetection.ipynb
```

`road.jpg` is included. The final "Finding Lane Lines" cell reads a
local `test2.mp4` that is not part of the repo — point it at any road
video (or drop one in this folder) to try the video path.
