import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Step 1: Import the image
img = cv2.imread('images/cell.tif', cv2.IMREAD_GRAYSCALE)

# Step 2: Run Canny with default parameters
# OpenCV default is typically (100, 200)
edges_default = cv2.Canny(img, 100, 200)

# Step 3 & 4: Choose optimized parameters
# σ = 1.5 (moderate smoothing to reduce noise while keeping cell features)
# low = 20 (normalized threshold for OpenCV)
# high = 60 (typically 2-3x the low threshold)
sigma = 1.5
low = 20
high = 60

# Apply Gaussian blur with sigma before Canny for optimization
blurred = cv2.GaussianBlur(img, (5, 5), sigma)
edges_optimized = cv2.Canny(blurred, low, high)

# Step 5: Display all three in one figure (like the reference image)
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Original image
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Original', fontsize=14, fontweight='bold')
axes[0].axis('off')

# Canny with default parameters
axes[1].imshow(edges_default, cmap='gray')
axes[1].set_title('Canny (Default)', fontsize=14, fontweight='bold')
axes[1].axis('off')

# Canny with optimized parameters
axes[2].imshow(edges_optimized, cmap='gray')
axes[2].set_title(f'Canny (Optimized)', fontsize=14, fontweight='bold')
axes[2].axis('off')

plt.tight_layout()

# Save to images folder with auto-numbering if file exists
output_dir = 'images'
base_filename = 'canny_comparison.png'
output_path = os.path.join(output_dir, base_filename)

# Check if file exists, if so create numbered version
if os.path.exists(output_path):
    counter = 2
    while os.path.exists(os.path.join(output_dir, f'canny_comparison{counter}.png')):
        counter += 1
    output_path = os.path.join(output_dir, f'canny_comparison{counter}.png')

plt.savefig(output_path, dpi=150, bbox_inches='tight')
print(f"\n✓ Comparison image saved to: {output_path}")

plt.show()

# Print the optimized parameters
print("\n" + "="*50)
print("OPTIMIZED CANNY EDGE DETECTOR PARAMETERS")
print("="*50)
print(f"σ (Sigma):           {sigma}")
print(f"Low Threshold:       {low}")
print(f"High Threshold:      {high}")
print(f"Threshold Ratio:     {high/low:.2f}:1")
print("="*50 + "\n")
