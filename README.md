# Canny Edge Detection - Cell Image Analysis

This project implements Canny edge detection to identify cell features in a microscopy image using Python.

## What It Does

- Loads a cell microscopy image (`cell.tif`)
- Runs Canny edge detection with default parameters
- Runs Canny edge detection with optimized parameters to reduce false positives
- Displays all three results side-by-side for comparison
- Saves the comparison as `canny_comparison.png`

## Setup & Installation

### Prerequisites
- Python 3.8+
- macOS/Linux/Windows with terminal access

### Step 1: Create Virtual Environment

```bash
cd /Users/andrewh/WebstormProjects/comp4932-assignment3
python3 -m venv venv
