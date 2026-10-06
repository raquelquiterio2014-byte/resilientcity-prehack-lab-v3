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

### Local GUI assets

`gui.py` resolves `assets/` relative to its own location and uses these filenames:

| File | Intended location | Compact layout |
| --- | --- | --- |
| `assets/resilientcity_hero.png` | Header | Half-size image |
| `assets/operations_reference.png` | Incident Input panel | Omitted |
| `assets/agent_reference.png` | Agent Architecture panel | Half-size image |

All three files are present in the repository inspected at commit [26cb5de](https://github.com/raquelquiterio2014-byte/resilientcity-prehack-lab-v3/commit/26cb5de34655bbf61a33c64b59f3ecfd9ecc1d5b).

The code requests a maximized window. When the screen height reported by Tkinter is below 900 px, it selects a compact layout, halves the header and architecture images, and omits the operations image. This is intended to improve usability on smaller screens; full visibility still requires local verification at the actual resolution and display scaling.

If an asset path is missing, `_load_image()` returns `None` and the corresponding image widget is omitted. Image decoding errors are not caught in that loader.

### Documentation images and supplied desktop images

The six images below are hosted as GitHub attachments. Their URLs are separate from the local GUI assets; this README does not establish that an attachment is identical to any PNG in `assets/`.

The reference commit above identifies the repository inspected, **not the commit used to produce the supplied images**. The images alone do not establish that the current checkout was executed successfully or that all assets loaded. No GUI execution was performed as part of this documentation inspection.

<img width="1536" height="1024" alt="ResilientCity AI flood-response project illustration" src="https://github.com/user-attachments/assets/fd22b1d0-0995-40d7-a197-a97c2b224bf3" />

Project illustration — flood-response concept. This illustration is not execution evidence.

<img width="3800" height="2520" alt="ResilientCity AI English use-case diagram" src="https://github.com/user-attachments/assets/4472f63c-3e73-437c-9406-c9e537266554" />

Use-case diagram (English) — documentation of the intended interactions, not execution evidence.

<img width="1414" height="692" alt="Supplied desktop image 1; source screen and commit unrecorded" src="https://github.com/user-attachments/assets/5e4e95aa-bb99-4742-987e-334ceb924a93" />

Supplied desktop image 1 — original attachment label: `image`. Screen/tab, capture date and source commit are not recorded.

<img width="1366" height="725" alt="Supplied desktop image 2; source screen and commit unrecorded" src="https://github.com/user-attachments/assets/761437d2-52da-4106-8dea-a4e64d65088a" />

Supplied desktop image 2 — original attachment label: `image`. Screen/tab, capture date and source commit are not recorded.

<img width="1366" height="724" alt="Supplied desktop image 3; original label Resilient City AI 2" src="https://github.com/user-attachments/assets/4d0c05a2-537e-4419-9eb3-8e2ec2e7c376" />

Supplied desktop image 3 — original attachment label: `Resilient City AI 2`. Screen/tab, capture date and source commit are not recorded.

<img width="1366" height="721" alt="Supplied desktop image 4; original label Resilient City AI 3" src="https://github.com/user-attachments/assets/04adbed2-6024-4249-8536-207468dc46f2" />

Supplied desktop image 4 — original attachment label: `Resilient City AI 3`. Screen/tab, capture date and source commit are not recorded.

### Remaining visual verification

- Open `python gui.py` from the checkout being tested and record its commit SHA.
- Confirm that the header and architecture images load; confirm the operations image appears in the normal layout and is omitted in the compact layout.
- Check for clipped content at the actual screen resolution and display scaling.
- For each execution capture, record the date, commit SHA, scenario and visible tab (Explainable Report, Agent Trace or Shared State).
- To claim that an attachment and a local asset are identical, compare the downloaded files or their hashes.

These checks remain unverified by this documentation update.
