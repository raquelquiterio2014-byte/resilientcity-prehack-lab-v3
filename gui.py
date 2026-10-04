import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

from pydantic import ValidationError

from resilientcity.graph import build_graph
from resilientcity.models import Incident

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"


class ResilientCityGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ResilientCity AI — Pre-Hackathon Multi-Agent Lab")
        # Small screens (e.g. 1366x768 laptops) get a compact layout with half-size images
        self.compact = self.winfo_screenheight() < 900
        self.geometry("1380x900")
        self.minsize(1000, 600)
        self.state("zoomed")
        self.configure(bg="#071a2b")
        self.images = {}
        self.app = build_graph()
        self._configure_style()
        self._build_ui()

    def _configure_style(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), foreground="#0b3558", background="#eef4f8")
        style.configure("Sub.TLabel", font=("Segoe UI", 10), foreground="#49657a", background="#eef4f8")
        style.configure("Card.TLabelframe", background="#ffffff", relief="solid", borderwidth=1)
        style.configure("Card.TLabelframe.Label", font=("Segoe UI", 11, "bold"), foreground="#0b3558", background="#ffffff")
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)
        style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), padding=10)

    def _load_image(self, filename):
        path = ASSET_DIR / filename
        if not path.exists():
            return None
        image = tk.PhotoImage(file=str(path))
        if self.compact:
            image = image.subsample(2)
        self.images[filename] = image
        return image

    def _build_ui(self):
        header = tk.Frame(self, bg="#071a2b")
        header.pack(fill="x", padx=18, pady=(12, 8))
        hero = self._load_image("resilientcity_hero.png")
        if hero:
            tk.Label(header, image=hero, bg="#071a2b").pack(side="left")
        title_box = tk.Frame(header, bg="#071a2b")
        title_box.pack(side="left", fill="both", expand=True, padx=18)
        tk.Label(title_box, text="ResilientCity AI", bg="#071a2b", fg="white",
                 font=("Segoe UI", 25, "bold")).pack(anchor="w", pady=(14, 0))
        tk.Label(title_box,
                 text="Explainable Multi-Agent System for Urban Flood Incident Response",
                 bg="#071a2b", fg="#47c7ff", font=("Segoe UI", 11, "bold"),
                 wraplength=390, justify="left").pack(anchor="w", pady=(4, 8))
        tk.Label(title_box,
                 text="Planner • Evidence • Risk • Decision • Critic • Safety • Reporter",
                 bg="#071a2b", fg="#c8d9e8", font=("Segoe UI", 9)).pack(anchor="w")

        # Footer is packed before the main area so it stays visible when space is tight
        footer = tk.Label(
            self,
            text="AI recommends. AI explains. Humans decide.  |  Educational pre-hackathon lab — no autonomous emergency actions.",
            bg="#0b3558", fg="white", font=("Segoe UI", 9), pady=8,
        )
        footer.pack(fill="x", side="bottom")

        pad = 10 if self.compact else 16
        main = tk.Frame(self, bg="#eaf2f7")
        main.pack(fill="both", expand=True, padx=24, pady=6 if self.compact else 10)
        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=2)
        main.grid_columnconfigure(2, weight=1)
        main.grid_rowconfigure(0, weight=1)

        left = ttk.LabelFrame(main, text="Incident Input", style="Card.TLabelframe", padding=pad)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        right = ttk.LabelFrame(main, text="Multi-Agent Analysis", style="Card.TLabelframe", padding=pad)
        right.grid(row=0, column=1, sticky="nsew", padx=10)
        visual = ttk.LabelFrame(main, text="Agent Architecture", style="Card.TLabelframe", padding=10)
        visual.grid(row=0, column=2, sticky="nsew", padx=(0, 10))

        self.incident_id = tk.StringVar(value="LAB-001")
        self.location = tk.StringVar(value="Central Avenue")
        self.rainfall = tk.StringVar(value="72.0")
        self.road_status = tk.StringVar(value="unknown")

        self._field(left, "Incident ID", self.incident_id, 0)
        self._field(left, "Location", self.location, 1)
        self._field(left, "Rainfall (mm)", self.rainfall, 2)

        ttk.Label(left, text="Road status").grid(row=6, column=0, sticky="w", pady=(10, 4))
        ttk.Combobox(
            left,
            textvariable=self.road_status,
            values=["unknown", "open", "closed", "flooded"],
            state="readonly",
        ).grid(row=7, column=0, sticky="ew")

        ttk.Label(left, text="Incident description").grid(row=8, column=0, sticky="w", pady=(12, 4))
        self.description = tk.Text(left, width=1, height=3 if self.compact else 7, wrap="word", font=("Segoe UI", 10), relief="solid", borderwidth=1)
        self.description.grid(row=9, column=0, sticky="nsew")
        self.description.insert("1.0", "Heavy rainfall and reported street flooding near an intersection.")

        buttons = tk.Frame(left, bg="#ffffff")
        buttons.grid(row=10, column=0, sticky="ew", pady=(10 if self.compact else 16, 0))
        ttk.Button(buttons, text="Run Multi-Agent Analysis", style="Accent.TButton", command=self.run_analysis).pack(fill="x")
        ttk.Button(buttons, text="Clear Results", command=self.clear_results).pack(fill="x", pady=(8, 0))
        ops = None if self.compact else self._load_image("operations_reference.png")
        if ops:
            tk.Label(left, image=ops, bg="#ffffff").grid(row=11, column=0, pady=(12, 0))
        left.grid_columnconfigure(0, weight=1)
        left.grid_rowconfigure(9, weight=1)

        summary = tk.Frame(right, bg="#ffffff")
        summary.pack(fill="x")
        self.priority_value = self._metric(summary, "Priority", "—", 0)
        self.confidence_value = self._metric(summary, "Confidence", "—", 1)
        self.safety_value = self._metric(summary, "Safety / Human Gate", "—", 2)

        notebook = ttk.Notebook(right)
        notebook.pack(fill="both", expand=True, pady=(14, 0))
        report_tab = tk.Frame(notebook, bg="#ffffff")
        trace_tab = tk.Frame(notebook, bg="#ffffff")
        state_tab = tk.Frame(notebook, bg="#ffffff")
        notebook.add(report_tab, text="Explainable Report")
        notebook.add(trace_tab, text="Agent Trace")
        notebook.add(state_tab, text="Shared State")

        self.report = self._text_area(report_tab)
        self.trace = self._text_area(trace_tab)
        self.state_view = self._text_area(state_tab)

        agent_img = self._load_image("agent_reference.png")
        if agent_img:
            tk.Label(visual, image=agent_img, bg="#ffffff").pack(anchor="n")
        tk.Label(visual, text="Operational lab flow", bg="#ffffff", fg="#0b3558",
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(10, 3))
        tk.Label(visual,
                 text="Planner → Evidence → Risk → Decision → Critic\n"
                      "↳ Revision when evidence is insufficient\n"
                      "→ Safety → Reporter → Human decision",
                 bg="#ffffff", fg="#49657a", font=("Segoe UI", 9),
                 justify="left", wraplength=250).pack(anchor="w")

    def _field(self, parent, label, variable, row):
        base = row * 2
        ttk.Label(parent, text=label).grid(row=base, column=0, sticky="w", pady=(8 if row else 0, 4))
        ttk.Entry(parent, textvariable=variable).grid(row=base + 1, column=0, sticky="ew")

    def _metric(self, parent, label, initial, column):
        card = tk.Frame(parent, bg="#f5f9fc", highlightbackground="#cbd9e4", highlightthickness=1)
        card.grid(row=0, column=column, sticky="nsew", padx=(0 if column == 0 else 6, 0))
        parent.grid_columnconfigure(column, weight=1)
        tk.Label(card, text=label, bg="#f5f9fc", fg="#49657a", font=("Segoe UI", 9)).pack(anchor="w", padx=10, pady=(8, 2))
        value = tk.Label(card, text=initial, bg="#f5f9fc", fg="#0b3558", font=("Segoe UI", 12, "bold"), wraplength=190, justify="left")
        value.pack(anchor="w", padx=10, pady=(0, 8))
        return value

    def _text_area(self, parent):
        # width/height=1 lets the text area grow into the window instead of forcing an 80x24 minimum
        text = tk.Text(parent, width=1, height=1, wrap="word", font=("Consolas", 10), bg="#fbfdff", relief="flat", padx=12, pady=12)
        scroll = ttk.Scrollbar(parent, orient="vertical", command=text.yview)
        text.configure(yscrollcommand=scroll.set)
        text.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        return text

    def run_analysis(self):
        try:
            incident = Incident(
                incident_id=self.incident_id.get().strip(),
                location=self.location.get().strip(),
                description=self.description.get("1.0", "end").strip(),
                rainfall_mm=float(self.rainfall.get()),
                road_status=self.road_status.get(),
            )
            result = self.app.invoke({"incident": incident.model_dump(), "revision_count": 0, "trace": []})
        except (ValidationError, ValueError) as exc:
            messagebox.showerror("Invalid incident data", str(exc))
            return
        except Exception as exc:
            messagebox.showerror("Execution error", f"The multi-agent workflow could not run:\n\n{exc}")
            return

        decision = result.get("decision", {})
        safety = result.get("safety", {})
        self.priority_value.config(text=decision.get("priority", "—"))
        confidence = decision.get("confidence")
        self.confidence_value.config(text=f"{confidence:.0%}" if isinstance(confidence, (int, float)) else "—")
        self.safety_value.config(text=safety.get("status", "—"))

        self._replace(self.report, result.get("final_report", "No report generated."))
        self._replace(self.trace, "\n".join(f"{i + 1:02d}. {event}" for i, event in enumerate(result.get("trace", []))))

        state_lines = []
        for key in ("incident", "evidence", "risk", "decision", "critic", "safety", "revision_count"):
            if key in result:
                state_lines.append(f"[{key.upper()}]\n{result[key]}\n")
        self._replace(self.state_view, "\n".join(state_lines))

    def clear_results(self):
        self.priority_value.config(text="—")
        self.confidence_value.config(text="—")
        self.safety_value.config(text="—")
        for widget in (self.report, self.trace, self.state_view):
            self._replace(widget, "")

    @staticmethod
    def _replace(widget, value):
        widget.delete("1.0", "end")
        widget.insert("1.0", value)


if __name__ == "__main__":
    ResilientCityGUI().mainloop()
