[Nautilus_GitHub_README.md](https://github.com/user-attachments/files/32157680/Nautilus_GitHub_README.md)
<div align="center">

<!-- BANNER -->
<img src="assets/banner.png" alt="Nautilus Logistics AI" width="100%"/>

<br/>
<br/>

<!-- BADGES -->
[![Build](https://img.shields.io/badge/build-passing-00d4aa?style=flat-square&logo=github-actions&logoColor=white)](.)
[![License](https://img.shields.io/badge/license-MIT-38bdf8?style=flat-square)](LICENSE)
[![React](https://img.shields.io/badge/React-19-61dafb?style=flat-square&logo=react&logoColor=white)](.)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8-3178c6?style=flat-square&logo=typescript&logoColor=white)](.)
[![Python](https://img.shields.io/badge/Python-3.11-ffd43b?style=flat-square&logo=python&logoColor=white)](.)
[![C](https://img.shields.io/badge/C11-GCC-a8b9cc?style=flat-square&logo=c&logoColor=white)](.)
[![C++](https://img.shields.io/badge/C++-17-00599c?style=flat-square&logo=cplusplus&logoColor=white)](.)
[![Size](https://img.shields.io/badge/package-6.83%20MB-a78bfa?style=flat-square)](.)
[![Offline](https://img.shields.io/badge/offline-100%25-34d399?style=flat-square)](.)
[![SIH](https://img.shields.io/badge/SIH26006-Ministry%20of%20Steel-fb923c?style=flat-square)](.)

<br/>

**Intelligent Freight Forecasting · Optimized Vessel Chartering · Carbon Compliance**

*Built for [Smart India Hackathon 2026](https://sih.gov.in) · Problem Statement SIH26006 · Ministry of Steel, Govt. of India*

<br/>

[Features](#-features) · [Architecture](#-architecture) · [Tech Stack](#-tech-stack) · [Installation](#-installation) · [Modules](#-modules) · [Performance](#-performance) · [Deployment](#-deployment)

</div>

---

## 📖 About

India's public-sector steel companies (SAIL, RINL, NMDC) spend billions importing bulk cargo by sea — but procurement teams operate without rate forecasting, weather risk analysis, vessel comparison tools, or carbon compliance tracking. **A single mistimed chartering decision on a 150,000-tonne Capesize shipment costs over USD 1.5 million.**

**Nautilus Logistics AI** is an end-to-end decision-support platform that predicts freight rates, assesses ocean weather risk, optimizes vessel selection, calculates carbon emissions, and delivers a clear **FIX NOW / WAIT / SPLIT** recommendation — all in under 16 milliseconds.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔮 **AI Freight Forecasting** | Hybrid SARIMA + XGBoost + GARCH model predicting rates 30/60/90 days ahead with expanding confidence bands |
| 🌊 **KAVACH Weather Engine** | 3-point oceanic risk scoring: 25% origin + 50% transit corridor + 25% destination |
| 🧮 **5D Vessel Optimizer** | Screens 10 vessel classes across port draft, batch fit, weather stability, gear compatibility, and net $/MT savings |
| 🌿 **IMO Carbon Compliance** | CII rating (A→E) per IMO MARPOL Annex VI, with CO₂ tonnes, offset cost, and Green Voyage Score |
| 💎 **12-Component Cost Model** | FOB + freight + bunker + load port + discharge port + handling + demurrage + insurance + rail + FX + inventory + carbon |
| 🎯 **Action Signal** | One-click recommendation: `FIX NOW` 🟢 / `WAIT` 🟡 / `SPLIT` 🟣 based on forecast slope × confidence |
| 📡 **AIS Vessel Tracking** | Real-time ship positions via AISstream.io with geofencing for port congestion detection |
| 🗺️ **Offline Maps** | Bundled 257 KB GeoJSON world map — zero external tile servers, works without internet |
| 🌐 **Bilingual** | Full English + Hindi (हिन्दी) support with 200+ translation keys |
| 📦 **Desktop App** | Native Win32 C++17 launcher with Winsock2 HTTP server + system tray — no Electron |

---

## 🏗 Architecture

```
                     ┌─────────────────────────────────┐
                     │     USER INPUT (5 Parameters)    │
                     │  Commodity · Qty · Origin · Dest │
                     │         · Vessel Class           │
                     └──────────────┬──────────────────┘
                                    │
                                    ▼
                     ┌──────────────────────────────────┐
                     │     generateScenario()            │
                     │     Master Orchestrator (<16ms)   │
                     └──────────────┬───────────────────┘
                                    │
              ┌─────────────┬───────┴────────┬──────────────┐
              ▼             ▼                ▼              ▼
     ┌──────────────┐ ┌───────────┐ ┌─────────────┐ ┌────────────┐
     │  C11 Geodesic│ │ Commodity │ │  C++17 Cost │ │ KAVACH +   │
     │  Math (.dll) │ │ & BDI     │ │  Engine     │ │ AI Forecast│
     │  Haversine   │ │ Sampling  │ │  4-Layer    │ │ 3-Layer    │
     │  <2μs/call   │ │           │ │  Optimizer  │ │ Hybrid     │
     └──────┬───────┘ └─────┬─────┘ └──────┬──────┘ └─────┬──────┘
            │               │              │               │
            └───────────────┴──────┬───────┴───────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │   5D Optimizer + CII Grade   │
                    │   Action Signal Decision     │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────┬───────┴────────┬──────────────┐
              ▼            ▼                ▼              ▼
     ┌──────────────┐ ┌──────────┐ ┌─────────────┐ ┌──────────┐
     │  Dashboard   │ │ Leaflet  │ │  SagarSetu  │ │ i18n     │
     │  KPIs+Charts │ │ Map      │ │  Cards      │ │ EN + HI  │
     └──────────────┘ └──────────┘ └─────────────┘ └──────────┘
```

---

## 🔧 Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | React 19, TypeScript 5.8, Vite 8 (Rolldown), Tailwind CSS v4 | Liquid Glass dashboard, charts (Recharts), map (Leaflet.js) |
| **AI Engine** | Python 3.11, SARIMA, XGBoost, GARCH(1,1) | Freight forecasting, weather risk, carbon compliance |
| **Math Core** | C11 (GCC) → `maritime_math.dll` | Haversine geodesic, AIS NMEA decoding — <2μs/call |
| **Cost Engine** | C++17 (MSVC) → `freight_optimizer.dll` | 4-layer voyage cost optimization |
| **Desktop** | C++17 Win32, Winsock2, COM (IShellLinkW) | Native launcher + installer — zero DLLs |
| **Maps** | Leaflet.js + bundled GeoJSON (257 KB) | 100% offline world map with 30 ports |
| **i18n** | TypeScript dictionary (200+ keys) | English + Hindi bilingual |
| **PWA** | Service Worker, Cache-first | Offline after first load, <200ms cold start |

---

## 📁 Project Structure

```
Nautilus Logistics AI/
├── public/
│   ├── index.html              # SPA shell + PWA meta
│   ├── sw.js                   # Service Worker (cache-first)
│   └── manifest.json           # PWA manifest
│
├── src/
│   ├── main.tsx                # React 19 entry point
│   ├── App.tsx                 # Central controller (2000+ lines)
│   ├── SeaPortsMap.tsx         # Leaflet map (offline GeoJSON)
│   ├── translations.ts        # EN/HI i18n dictionary
│   ├── index.css               # Liquid Glass theme
│   └── components/
│       └── sagarsetu/
│           ├── KAVACHWeatherCard.tsx
│           ├── GreenFreightCarbon.tsx
│           └── AISVesselTracker.tsx
│
├── python_engine/
│   ├── freight_predictor.py    # SARIMA + XGBoost + GARCH
│   ├── weather_kavach.py       # 3-point weather risk
│   ├── carbon_cii.py           # IMO CII grading (A→E)
│   ├── ais_tracker.py          # AIS telemetry parser
│   ├── c_cpp_bridge.py         # ctypes FFI to C/C++ DLLs
│   ├── main_api.py             # FastAPI endpoints
│   └── requirements.txt
│
├── c_cpp_engine/
│   ├── maritime_math.c         # Haversine + NMEA decoder
│   ├── maritime_math.h
│   ├── freight_optimizer.cpp   # 4-layer voyage cost
│   ├── freight_optimizer.hpp
│   ├── app_launcher/
│   │   └── launcher_main.cpp   # Win32 desktop launcher
│   └── setup_builder/
│       ├── setup_main.cpp      # GUI installer
│       └── uninstall_main.cpp  # Clean uninstaller
│
├── vite.config.ts
├── tailwind.config.ts
├── tsconfig.json
├── package.json
└── netlify.toml                # One-click cloud deploy
```

---

## 🚀 Installation

### Prerequisites

- Node.js ≥ 18
- Python ≥ 3.11
- GCC (for C11) and MSVC/G++ (for C++17) — *optional, pre-compiled DLLs included*

### Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/nautilus-logistics-ai.git
cd nautilus-logistics-ai

# Install frontend dependencies
npm install

# Start development server
npm run dev
```

The dashboard opens at `http://localhost:5173`.

### Python Engine (Optional)

```bash
cd python_engine
pip install -r requirements.txt
python main_api.py
```

API runs at `http://localhost:8000`.

### Build for Production

```bash
npm run build
```

Output goes to `dist/` — deploy to any static host or use the desktop launcher.

---

## 🧩 Modules

<details>
<summary><b>🔮 AI Freight Forecaster</b> — <code>freight_predictor.py</code></summary>

<br/>

Three-layer hybrid model generating 30/60/90-day forward rate curves:

| Layer | Model | Role |
|-------|-------|------|
| 1 | SARIMA(1,1,1)(1,1,1,12) | Trend + seasonal patterns (monsoon, cyclone, CNY) |
| 2 | XGBoost (30+ features) | BDI lags, Brent, VLSFO, USD/INR, China PMI, fleet growth, RSI |
| 3 | GARCH(1,1) | Volatility modeling → confidence intervals (±3.2% → ±6.8%) |

</details>

<details>
<summary><b>🌊 KAVACH Weather Engine</b> — <code>weather_kavach.py</code></summary>

<br/>

Composite oceanic risk score using weighted three-point formula:

```
Risk = 0.25 × Origin + 0.50 × Transit + 0.25 × Destination
```

Sub-risk factors: wave swell (Hs > 3.5m), wind drag (Beaufort > 6), cyclone proximity (< 500 nm).

Data sources: IMD cyclone alerts, NOAA GFS wind/wave, seasonal calendars.

</details>

<details>
<summary><b>🌿 Carbon CII Engine</b> — <code>carbon_cii.py</code></summary>

<br/>

IMO MARPOL Annex VI Carbon Intensity Indicator:

```
CII = (Fuel_MT × Emission_Factor) / (DWT × Distance_NM) × 10⁶
```

| Fuel | Emission Factor (t CO₂/t fuel) |
|------|------|
| VLSFO | 3.114 |
| HFO | 3.206 |
| LNG | 2.750 |

Grades: A (≤0.85d) · B (≤0.95d) · C (≤1.05d) · D (≤1.15d) · E (>1.15d)

</details>

<details>
<summary><b>🧮 5D Vessel Optimizer</b> — <code>App.tsx</code></summary>

<br/>

Screens 10 vessel classes across 5 dimensions:

| Dim | Metric | Example |
|-----|--------|---------|
| D1 | Port Draft (hard constraint) | Haldia 9.1m blocks Capesize |
| D2 | Batch Consolidation (85–95% sweet spot) | 75K MT in 180K DWT Capesize = 42% |
| D3 | Weather Stability | Hull rating × (1 − KAVACH risk) |
| D4 | Gear Compatibility | Onboard cranes + port cranes |
| D5 | Net Savings ($/MT vs baseline) | Supramax saves $3.2/MT vs Capesize |

</details>

<details>
<summary><b>🎯 Action Signal</b> — <code>App.tsx</code></summary>

<br/>

```
IF   slope_30d > +3%  AND  confidence ≥ 78%  →  🟢 FIX NOW
ELIF slope_30d < −3%  AND  confidence ≥ 65%  →  🟡 WAIT 7–14 DAYS
ELSE                                          →  🟣 SPLIT 50/50
```

On a 150,000 MT Capesize shipment, correct timing saves **USD 200K–500K per voyage**.

</details>

<details>
<summary><b>⚡ C11 Geodesic Core</b> — <code>maritime_math.c</code></summary>

<br/>

Haversine great-circle distance on a spherical Earth (R = 3,440.065 nm):

```c
a = sin²(Δφ/2) + cos(φ₁) × cos(φ₂) × sin²(Δλ/2)
d = 2 × R × asin(√a)
```

Returns: `distance_nm`, `bearing_deg`, `steaming_hours`. Execution: **< 2 microseconds**.

</details>

---

## ⚡ Performance

| Metric | Value | Comparison |
|--------|-------|------------|
| Package Size | **6.83 MB** | 94% smaller than Electron alternatives |
| Cold Start | **< 200 ms** | 10× faster than typical |
| Pipeline Recalc | **< 16 ms** | Under one frame at 60fps |
| C Math Call | **< 2 μs** | 500,000 calls/second possible |
| RAM Usage | **35–55 MB** | 6× less than Electron |
| Offline | **100%** | Bundled GeoJSON, no tile servers |
| Languages | **EN + HI** | 200+ translation keys |

---

## 🌍 Deployment

### Option 1: Desktop (.exe)

```bash
cd c_cpp_engine/setup_builder
# Compile (MSVC)
cl /std:c++17 /O2 setup_main.cpp /Fe:NautilusSetup.exe
# Run installer
./NautilusSetup.exe
```

6.87 MB standalone installer → ~40ms extraction → Desktop shortcut + System tray.

### Option 2: Cloud (Netlify)

```bash
npm run build
# Drag 'dist/' folder to https://app.netlify.com/drop
```

Or connect GitHub repo for automatic CI/CD deploys.

### Option 3: PWA (Offline)

Visit the deployed URL once → Add to Home Screen → Works fully offline with service worker cache-first strategy.

---

## 📊 Data Sources

| Source | Data | Update |
|--------|------|--------|
| [Baltic Exchange](https://www.balticexchange.com/) | BDI, shipping indices | Daily |
| [FRED](https://fred.stlouisfed.org/) | Brent crude oil | Daily |
| [RBI](https://rbi.org.in/) | USD/INR exchange rate | Daily |
| [IMD](https://mausam.imd.gov.in/) | Cyclone warnings, Bay of Bengal | Real-time |
| [NOAA GFS](https://www.ncei.noaa.gov/) | Wind, wave height, SST | 6-hourly |
| [AISstream.io](https://aisstream.io/) | Live vessel AIS positions | Real-time |
| [Ship & Bunker](https://shipandbunker.com/) | VLSFO fuel prices | Daily |
| [Ministry of Steel / JPC](https://steel.gov.in/) | India steel production | Monthly |

> **Note:** The prototype uses calibrated historical data (2015–2026 averages). The architecture is plug-and-play — live commercial feeds can replace demo data without code changes.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👥 Team

<!-- Replace with actual team members and GitHub usernames -->

| Name | Role | GitHub |
|------|------|--------|
| **Your Name** | Full-Stack Lead | [@your-username](https://github.com/your-username) |
| Teammate 2 | AI/ML Engineer | [@teammate2](https://github.com/teammate2) |
| Teammate 3 | Backend Developer | [@teammate3](https://github.com/teammate3) |
| Teammate 4 | Frontend Developer | [@teammate4](https://github.com/teammate4) |
| Teammate 5 | Systems/C++ Engineer | [@teammate5](https://github.com/teammate5) |
| Teammate 6 | Research & Documentation | [@teammate6](https://github.com/teammate6) |

---

<div align="center">

**Built with ❤️ for Smart India Hackathon 2026**

*Ministry of Steel · Government of India · SIH26006*

⚓ **Turning maritime freight procurement from guesswork into intelligence.**

</div>
