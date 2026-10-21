# Serial/Sensor Dashboard & Logger

A cross-platform desktop application built with **PySide6** for monitoring, logging, and controlling serial devices (Arduino, STM32, ESP32, etc.). Designed for embedded developers and mechatronics engineers who need more than a basic serial monitor.

## Features

- Automatic serial port detection, with configurable baud rate
- Non-blocking serial reads via a background `QThread`
- Configurable line parser (CSV, delimited, or JSON)
- Real-time plots (pyqtgraph) and gauge/indicator widgets
- Timestamped logging to CSV, with session metadata stored in SQLite
- Command console with mappable one-click command buttons
- Per-device profiles (parser, commands, connection defaults)
- Persistent user settings

## Tech Stack

| Purpose               | Library                              |
| --------------------- | ------------------------------------ |
| GUI                   | PySide6                              |
| Live plotting         | pyqtgraph                            |
| Serial I/O            | pyserial                             |
| Storage               | SQLite (built-in `sqlite3`) + CSV    |
| OS-specific paths     | platformdirs                         |
| Dependency management | Poetry                               |
| Testing / quality     | pytest, pytest-qt, ruff, black, mypy |

## Getting Started

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)

### Installation

```bash
git clone https://github.com/BLKamau/serial-dashboard.git
cd serial-dashboard
poetry install
```

### Run the application

```bash
poetry run serial-dashboard
```

or, equivalently:

```bash
poetry run python -m serial_dashboard.main
```

### Run the tests

```bash
poetry run pytest

# or

make test
```

## Project Structure

```
src/serial_dashboard/
├── core/          # Settings and profile management
├── serial_comm/   # Port scanning, serial worker thread, line parser
├── data/          # SQLite access and CSV logging
├── ui/            # Windows, dialogs, and panels
└── resources/     # Icons and stylesheets
tests/             # Unit and Qt widget tests
```

## Documentation

- [`PROJECT_PLAN.md`](PROJECT_PLAN.md) — scope, phases, and deliverables

## Status

In active development. See the project plan for current phase and scope.

## License

MIT License
