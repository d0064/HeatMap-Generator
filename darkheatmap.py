import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import numpy as np
import os

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv *.mov")])
    if file_path:
        process_video(file_path)

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        messagebox.showerror("Error", "Failed to open the video file.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    prev_frame = None

    video_dir = os.path.dirname(video_path)
    heatmap_video_file = os.path.join(video_dir, 'heatmap.avi')

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(heatmap_video_file, fourcc, 30.0, (width, height), isColor=True)

    heatmap_accumulator = np.zeros((height, width, 3), dtype=np.uint8)
    alpha = 0.1 

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if prev_frame is not None:
            frame_diff = cv2.absdiff(frame, prev_frame)
            frame_diff_gray = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
            heatmap_frame = cv2.applyColorMap(frame_diff_gray, cv2.COLORMAP_HOT)

            brightness_factor = 2.0
            heatmap_frame = cv2.convertScaleAbs(heatmap_frame, alpha=brightness_factor, beta=0)

            heatmap_accumulator = cv2.addWeighted(heatmap_accumulator, 1.0, heatmap_frame, alpha, 0)
            out.write(heatmap_accumulator)

        prev_frame = frame.copy()

    cap.release()

    for _ in range(int(frame_count * 0.1)):
        heatmap_accumulator = cv2.addWeighted(heatmap_accumulator, 0.9, np.zeros_like(heatmap_accumulator), 0.1, 0)
        out.write(heatmap_accumulator)

    out.release()

    messagebox.showinfo("Info", f"Heatmap video saved as {heatmap_video_file}")

root = tk.Tk()
root.title("Video Heatmap Generator")

open_button = tk.Button(root, text="Open Video File", command=open_file)
open_button.pack(padx=20, pady=20)

root.mainloop()
