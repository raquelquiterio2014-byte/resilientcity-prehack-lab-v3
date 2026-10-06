# ResilientCity AI — Pre-Hackathon Learning Lab
Disposable learning environment, not the competition implementation.

## Run on Windows
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python main.py
python -m pytest -q

## Desktop graphical interface

A Tkinter desktop interface is available in `gui.py`.

Windows quick start:

```bat
run_gui.bat
```

Or manually:

```bash
python gui.py
```

The GUI accepts incident data and displays the final recommendation, confidence, safety/human-review status, complete agent trace, and shared workflow state.

## Web demo

`web/index.html` is a self-contained page (open it in any browser, no install) that reproduces the same deterministic agent rules in JavaScript, with example scenarios, the agent workflow, the execution trace and the final report.

Photos in the web demo come from Wikimedia Commons, used under their licenses (CC BY 4.0, CC BY-SA 2.0, CC BY 2.0, CC0); authors and links are credited in the page footer.





## Visual desktop interface (v3)

The desktop GUI uses the images in `assets/` (header, agent architecture and operations reference). It opens maximized; on screens shorter than 900 px (for example 1366x768 laptops) it switches to a compact layout with half-size images so the whole window fits on screen.

<img width="1366" height="721" alt="Resilient City AI 3" src="https://github.com/user-attachments/assets/04adbed2-6024-4249-8536-207468dc46f2" />


<img width="1414" height="692" alt="image" src="https://github.com/user-attachments/assets/5e4e95aa-bb99-4742-987e-334ceb924a93" />

<img width="1366" height="725" alt="image" src="https://github.com/user-attachments/assets/761437d2-52da-4106-8dea-a4e64d65088a" />



