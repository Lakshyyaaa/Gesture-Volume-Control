# Gesture-Volume-Control
The Gesture Volume Control program uses hand tracking via a webcam to adjust system volume dynamically based on the distance between the thumb and index finger. It provides real-time visual feedback with a volume bar and percentage, making it a hands-free and interactive way to control audio levels.

Features
Real-Time Hand Tracking: Tracks the position of the thumb and index finger using Mediapipe's hand detection.
Dynamic Volume Control: Adjusts the volume proportionally to the distance between the two fingers.
Visual Feedback: Displays a volume bar and percentage on-screen, along with a graphical representation of the hand landmarks.
Seamless Interaction: Enables hands-free audio control, making it practical for presentations, multitasking, or accessibility needs.

How It Works
The program uses the Mediapipe library to detect and track hand landmarks.
The distance between the thumb tip and index finger tip is measured.
This distance is mapped to a volume range (0% to 100%).
The system volume is adjusted using platform-specific commands (e.g., osascript for macOS).
A graphical interface provides feedback with a live feed, volume bar, and current percentage.
