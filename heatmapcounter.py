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
    counter_video_file = os.path.join(video_dir, 'counter_video.avi')

    heatmap_accumulator = np.zeros((height, width, 3), dtype=np.uint8)
    alpha = 0.1

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    heatmap_out = cv2.VideoWriter(heatmap_video_file, fourcc, 30.0, (width, height), isColor=True)
    counter_out = cv2.VideoWriter(counter_video_file, fourcc, 30.0, (width, height), isColor=True)

    total_changed_pixels = 0

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

            changed_pixels = np.sum(frame_diff_gray > 20)
            total_changed_pixels += changed_pixels

            counter_frame = frame.copy()
            text = f"Changed Pixels: {total_changed_pixels}"
            cv2.putText(counter_frame, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            counter_out.write(counter_frame)

        prev_frame = frame.copy()

        heatmap_out.write(heatmap_accumulator)

    cap.release()
    heatmap_out.release()
    counter_out.release()

    messagebox.showinfo("Info", f"Heatmap video saved as {heatmap_video_file} and Counter video saved as {counter_video_file}")

root = tk.Tk()
root.title("Video Heatmap and Counter Generator")

open_button = tk.Button(root, text="Open Video File", command=open_file)
open_button.pack(padx=20, pady=20)

root.mainloop()
