#!/bin/bash
echo "Starting Bar Exam Practice App on http://localhost:8000"
echo "Press Ctrl+C to stop the server"
cd bar_exam_app
# Use python3 to serve the files from the root of the app folder
python3 -m http.server 8000
