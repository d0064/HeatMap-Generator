# Heatmap Video Generator

This Python script (`heatmap.py`) allows you to generate a heatmap video from a source video. The heatmap script searches for pixel changes and turns them into a red/orange depends on how much the pixel changed over 2 frames and after the 2 frames it will fade away slowly

## Required Libraries

Before running the script, make sure you have the following libraries installed:

- Python 3.x
- OpenCV (cv2) library
- NumPy library

You can install the required libraries using pip:

pip install opencv-python numpy

```bash
Usage
Follow these steps to generate a heatmap video:

Clone or download this repository to your local machine.

Navigate to the project directory in your command line terminal:

cd Downloads
Wherever the file of heatmap.py or anything else is just go to there
If you dont know how to do this follow this tutorial https://www.youtube.com/watch?v=BfXh11ryBJg
You have to select the folder where you want to go and drag it in cmd, For example if the file heatmap.py is in downloads directory in cmd type cd. After typing cd drag your downloads directory from file explorer quick access and drag it into cmd. Make sure there is a space between cd and the directory
 
Run the script using the following command:

python heatmap.py
The script will open a file dialog for you to select the source video.

After selecting the source video, the script will process it and generate the heatmap.

The heatmap will be saved as heatmap.avi in the same directory as the video, But you can also see the directory where it was saved after it finishes processing.

Once the script completes, you can find the heatmap video (heatmap.avi) in the same directory as the video.

License
This project is licensed under the MIT License. See the LICENSE file for details.
