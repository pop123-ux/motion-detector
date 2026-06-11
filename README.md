# Motion Detector

A real-time motion detection system using OpenCV's background subtraction. Detects movement through a webcam feed, highlights motion regions with bounding boxes, and draws contour outlines.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white)

---

## How It Works

```
Webcam Frame
     │
     ▼
Background Subtractor (MOG2)
     │
     ▼
Foreground Mask (binary)
     │
     ▼
Dilation (fill gaps)
     │
     ▼
Find Contours
     │
     ├── Area > 500px → Green bounding box (significant motion)
     └── All contours  → Red outline
```

The **MOG2 background subtractor** learns what "normal" looks like over time (500 frames of history) and flags pixels that deviate from it. Dilation merges nearby regions to reduce noise, and contour detection identifies distinct motion areas.

## Usage

```bash
pip install -r requirements.txt
python motion_detector.py
```

Press `q` to quit.

## Configuration

Tweak these values in `motion_detector.py` to adjust sensitivity:

| Parameter | Default | Effect |
|-----------|---------|--------|
| `history` | 500 | Frames used to build background model — higher = slower adaptation |
| `varThreshold` | 16 | Pixel variance threshold — lower = more sensitive |
| `contourArea` | 500 | Minimum contour area in pixels — lower = detect smaller motion |
| `kernel` size | 5×5 | Dilation kernel — larger = more gap filling |

## License

MIT
