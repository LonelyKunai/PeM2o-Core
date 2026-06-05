import time
import threading
from pathlib import Path
import math

from pynput import keyboard


OUTPUT_FILE = "movements.txt"
WINDOW_SECONDS = 5.0

STEP_SECONDS = {
    "walk": 0.235,
    "run": 0.19,
    "bike": 0.14,
}

ARROWS = {
    keyboard.Key.up: "u",
    keyboard.Key.down: "d",
    keyboard.Key.left: "l",
    keyboard.Key.right: "r",
}

MODE_KEYS = {
    "x": "run",
    "1": "bike",
}


def ensure_file_exists(file_path):
    path = Path(file_path)
    if not path.exists():
        path.touch()


def file_has_content(file_path):
    path = Path(file_path)
    return path.exists() and path.stat().st_size > 0


def append_line(file_path, line, add_leading_blank=False):
    ensure_file_exists(file_path)
    with open(file_path, "a", encoding="utf-8") as f:
        if add_leading_blank:
            f.write("\n")
        f.write(line + "\n")


class SegmentStepLogger:
    def __init__(self):
        self.lock = threading.Lock()
        self.active_modes = {"run": False, "bike": False}
        self.key_down = {}
        self.press_time = {}
        self.current_direction = None
        self.current_state = "walk"
        self.segment_time = 0.0
        self.segment_direction = None
        self.segment_state = "walk"
        self.last_tick = time.time()
        self.window_start = time.time()
        self.startup_needs_blank = file_has_content(OUTPUT_FILE)
        ensure_file_exists(OUTPUT_FILE)

    def get_state(self):
        if self.active_modes["bike"]:
            return "bike"
        if self.active_modes["run"]:
            return "run"
        return "walk"

    def toggle_mode(self, mode):
        self.active_modes[mode] = not self.active_modes[mode]
        print(f"[MODE] {mode} -> {self.active_modes[mode]}")

    def _steps_from_time(self, seconds, state):
        raw = seconds / STEP_SECONDS[state]
        steps = math.floor(raw)
        if raw > 0 and steps == 0:
            steps = 1
        return steps

    def _write_step(self, direction, steps):
        if steps <= 0:
            return
        line = f"{steps}{direction}"
        append_line(OUTPUT_FILE, line, add_leading_blank=self.startup_needs_blank)
        self.startup_needs_blank = False
        print(line)

    def _finish_segment(self):
        if self.segment_direction is None or self.segment_time <= 0:
            self.segment_time = 0.0
            self.segment_direction = None
            self.segment_state = self.get_state()
            return

        steps = self._steps_from_time(self.segment_time, self.segment_state)
        self._write_step(self.segment_direction, steps)

        self.segment_time = 0.0
        self.segment_direction = None
        self.segment_state = self.get_state()

    def on_press(self, key):
        with self.lock:
            if key in ARROWS:
                if key not in self.key_down:
                    self.key_down[key] = True
                    self.press_time[key] = time.time()
                    self.current_direction = ARROWS[key]
                    self.current_state = self.get_state()
                    self.segment_direction = self.current_direction
                    self.segment_state = self.current_state
                    self.segment_time = 0.0
                return

            try:
                ch = key.char.lower()
            except AttributeError:
                return

            if ch in MODE_KEYS:
                self.toggle_mode(MODE_KEYS[ch])

    def on_release(self, key):
        with self.lock:
            if key in ARROWS and key in self.key_down:
                held = time.time() - self.press_time.get(key, time.time())
                self.key_down.pop(key, None)
                self.press_time.pop(key, None)

                if self.current_direction == ARROWS[key]:
                    self.current_direction = None

                if held > 0:
                    self.segment_time = held
                    self.segment_direction = ARROWS[key]
                    self.segment_state = self.get_state()
                    self._finish_segment()

    def run(self):
        print("Iniciado.")
        print(f"Guardando en: {Path(OUTPUT_FILE).resolve()}")
        print("Flechas = mover, x = correr toggle, 1 = bici toggle, por defecto caminar.")
        print(f"Escritura en archivo cada {WINDOW_SECONDS}s, pero solo al soltar la tecla.")

        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()

        try:
            while True:
                time.sleep(0.05)
                now = time.time()
                if now - self.window_start >= WINDOW_SECONDS:
                    self.window_start = now
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    SegmentStepLogger().run()
