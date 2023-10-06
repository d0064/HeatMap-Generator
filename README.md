# Heatmap Video Generator

This Python script (`heatmap.py`) allows you to generate a heatmap video from a source video. The heatmap video visualizes the areas of the pixels changing on the video and after it will display a orange/red as that changing pixel and the rest background as a black background .

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- OpenCV (cv2) library
- NumPy library

You can install the required libraries using pip:

```bash
pip install opencv-python numpy
Usage
Follow these steps to generate a heatmap video:

Clone or download this repository to your local machine.

Navigate to the project directory in your command line terminal:

bash
cd path/to/heatmap.py
Run the script using the following command:

bash
python heatmap.py
The script will open a file dialog for you to select the source video.

After selecting the source video, the script will process it and generate the heatmap.

The heatmap will be saved as heatmap.avi in the same directory as the script.

Once the script completes, you can find the heatmap video (heatmap.avi) in the same directory as the script.


License
This project is licensed under the MIT License. See the LICENSE file for details.
