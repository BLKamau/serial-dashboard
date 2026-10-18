# Project Plan — Serial/Sensor Dashboard & Logger

**Framework:** PySide6
**Dependency management:** Poetry
**Plan structure:** Sequential phases, each with tasks, deliverables, and an exit criterion. A phase is complete when its exit criterion is met, not when a date passes.

---

## 1. Objective

Build a desktop tool that connects to a microcontroller over serial, parses incoming data in real time, visualizes and logs it, and lets the user send commands back. The application opens directly into the main window, with no login step, so effort goes into the quality of the core data pipeline.

## 2. Scope

### In scope

- Serial port discovery, connect/disconnect, baud rate selection, and automatic reconnect
- Non-blocking serial reading on a worker thread
- Raw data view alongside parsed output
- Configurable parser (CSV, delimited, JSON) with validation and error reporting
- Live multi-channel plots with pause/resume, channel visibility toggles, and adjustable buffer size
- Gauge/indicator widgets
- Timestamped CSV logging, with session metadata in SQLite
- Command console, command history, and mappable command buttons
- Per-device profiles
- Persistent settings
- Simulated serial source for hardware-free development and testing
- Packaging as a distributable executable

### Out of scope (initial version)

- User accounts, login, and registration
- Network protocols (TCP, UDP, MQTT, Bluetooth)
- Multiple simultaneous device connections
- Cloud sync or web dashboard
- Firmware flashing
- Advanced signal processing (FFT, filtering)

## 3. Key Technical Decisions

| Decision               | Choice                                | Reason                                                                 |
| ---------------------- | ------------------------------------- | ---------------------------------------------------------------------- |
| GUI framework          | PySide6                               | LGPL licensing, official Qt binding                                    |
| Threading              | `QThread` worker with `Signal`/`Slot` | Keeps the GUI responsive; widgets are only touched from the GUI thread |
| Plotting               | pyqtgraph                             | Low-latency streaming plots                                            |
| Relational storage     | SQLite                                | Profiles and session metadata                                          |
| High-rate data storage | CSV files                             | Avoids per-row database overhead                                       |
| Application entry      | Main window directly                  | No authentication layer; simpler startup and fewer moving parts        |

---

## 4. Phases

### Phase 0 — Planning & Design

**Tasks**

- Finalize requirements, flowcharts, and window breakdown
- Design the database schema (`profiles`, `sessions`)
- Set up repository, Poetry environment, `.gitignore`, README

**Deliverables:** requirements document, flowcharts, schema design, initialized repository
**Exit criterion:** Environment installs cleanly with `poetry install` and the repository structure is committed.

### Phase 1 — Foundation & Simulated Source

**Tasks**

- Create the package skeleton (`core/`, `serial_comm/`, `data/`, `ui/`)
- Implement SQLite connection and table creation
- Build the Main Window shell with dockable panel placeholders and menu bar
- Implement the simulated serial source that emits sample data in each supported format

**Deliverables:** application launching straight into the Main Window, working simulated data source
**Exit criterion:** The app starts directly into the Main Window, the database initializes on first run, and the simulator produces data usable by later phases.

### Phase 2 — Serial Communication Core

**Tasks**

- Implement port scanning with refresh
- Implement the Serial Worker (`QThread`) with connect/disconnect
- Emit received lines to the GUI thread via signals
- Build the Connection Settings panel (port, baud rate, status)
- Build the raw data view with auto-scroll and clear
- Handle unexpected disconnects and read errors without crashing
- Implement optional automatic reconnect

**Deliverables:** raw serial lines displayed live, resilient connection handling
**Exit criterion:** The app connects to a real or simulated device, shows incoming lines without freezing, and recovers from an unplugged cable.

### Phase 3 — Parsing

**Tasks**

- Implement the Data Parser (CSV, delimited, JSON) with field names and types
- Validate each line and route malformed lines to a warning path with a running error count
- Build the Parser Configuration window with a live preview against sample input
- Cover the parser with unit tests, including edge cases (empty lines, partial lines, extra or missing fields)

**Deliverables:** configurable, tested parser
**Exit criterion:** Lines from the device parse into named numeric fields; malformed lines are discarded and counted without interrupting the stream.

### Phase 4 — Visualization

**Tasks**

- Integrate pyqtgraph for live, auto-scaling multi-channel plots
- Add pause/resume, channel visibility toggles, and adjustable buffer size
- Throttle redraws so plotting keeps pace with high data rates
- Build the Gauge/Indicator panel with latest values and min/max tracking

**Deliverables:** responsive live plots and indicators
**Exit criterion:** Parsed fields appear on plots and indicators in real time at high baud rates without GUI lag, and pausing the plot does not stop logging or data intake.

### Phase 5 — Logging & Data Management

**Tasks**

- Implement timestamped CSV logging with start/stop control
- Create the `sessions` table and record session metadata
- Build the Logging & Export panel with row count and duration
- Add export of completed sessions
- Flush logs periodically and on disconnect so no rows are lost

**Deliverables:** reliable logging and export
**Exit criterion:** A logged session opens directly in a spreadsheet or Python without cleanup, and no rows are lost during a sustained run or an unexpected disconnect.

### Phase 6 — Command Console & Profiles

**Tasks**

- Build the Command Console panel and command history
- Implement mappable command buttons with configurable line endings
- Implement the Profile Manager and `profiles` table
- Build the Profile Manager window

**Deliverables:** two-way device communication, saved device profiles
**Exit criterion:** Commands reach the device; switching profiles restores parser, commands, and connection defaults.

### Phase 7 — Polish, Settings & Packaging

**Tasks**

- Build the Settings/Preferences window and persist values with `QSettings`
- Build the About/Help window
- Run a testing pass: disconnect handling, malformed data, high baud-rate stress, long-duration logging
- Package with PyInstaller and test the build on a clean machine

**Deliverables:** distributable executable, completed documentation
**Exit criterion:** The packaged app runs on a machine without Python or Poetry installed and passes the full test suite.

---

## 5. Testing Strategy

- **Unit tests:** parser, CSV logger, profile manager, database layer
- **Qt tests (pytest-qt):** signals and slots, panel updates, parser configuration window
- **Hardware-free testing:** the simulated serial source, available from Phase 1, so development does not depend on a physical device
- **Manual checks:** disconnect/reconnect, malformed input, long-duration logging

## 6. Risks and Mitigations

| Risk                                  | Mitigation                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------- |
| GUI freezes under high data rates     | Keep all serial I/O on the worker thread; throttle plot redraws; cap plot buffer size |
| Widgets updated from the wrong thread | Communicate only through signals/slots                                                |
| Lost or corrupted log rows            | Flush periodically and on disconnect; test with sustained runs                        |
| Parser too rigid for real devices     | Keep format definitions configurable and stored in profiles                           |
| Packaging issues with Qt plugins      | Build and test the executable early in Phase 7, on a clean machine                    |
| No hardware available                 | Use the simulated serial source                                                       |

## 7. Definition of Done (Whole Project)

- All in-scope features implemented and reachable from the UI
- App opens directly into the Main Window
- App survives device disconnect and reconnect without restart
- Logged data is directly usable in external tools
- Test suite passes
- README and this plan are up to date
- Packaged executable runs on a clean machine

## 8. Next Design Steps

- Database schema: `profiles` and `sessions`
- Module interfaces: what `database.py`, `serial_worker.py`, `parser.py`, and `csv_logger.py` expose
- Simulated serial source design
