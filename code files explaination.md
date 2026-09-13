# 🚢 Nautilus Logistics AI — Codebase & File Architecture Explanation

This document provides a comprehensive, tabular breakdown of every source file, module, script, and configuration in the **Nautilus Logistics AI** platform. It details each file's purpose, programming/markup languages, and architectural importance.

---

## 📑 Table of Contents
1. [Frontend Architecture & UI Layer (`src/` & `public/`)](#1-frontend-architecture--ui-layer-src--public)
2. [AI & Machine Learning Engine (`python_engine/`)](#2-ai--machine-learning-engine-python_engine)
3. [High-Performance C/C++ Mathematical & Financial Core (`c_cpp_engine/`)](#3-high-performance-cc-mathematical--financial-core-c_cpp_engine)
4. [Desktop Application Launcher & Setup Installer (`c_cpp_engine/app_launcher/` & `setup_builder/`)](#4-desktop-application-launcher--setup-installer)
5. [Root Configuration, Build Automation & Distribution Files](#5-root-configuration-build-automation--distribution-files)

---

## 1. Frontend Architecture & UI Layer (`src/` & `public/`)

| File Path | Languages Used | Purpose & Functionality | Importance to Platform |
| :--- | :--- | :--- | :--- |
| `src/App.tsx` | TypeScript, TSX, HTML5 | Primary React application component. Manages global state, the 5-column parameter bar (Commodity, Quantity, Origin, Destination, Vessel Class), KPI cards (Action Signal, Projected Savings, Model Confidence), dynamic 5D vessel optimizer, forward curve charts, and view routing. | **CRITICAL (Core UI Controller)**: Central hub connecting all maritime intelligence, user controls, and visualization components. |
| `src/main.tsx` | TypeScript, TSX | Application bootstrap entry point. Renders the root `<App />` component into the DOM with React 19 `StrictMode`. | **HIGH (Entry Point)**: Mounts the entire frontend application onto `index.html`. |
| `src/SeaPortsMap.tsx` | TypeScript, TSX | Interactive geospatial maritime routing map using Leaflet.js. Renders 18 Indian ports, 12 global gateways, great-circle trade lanes, and live AIS vessel markers. | **HIGH (Geospatial Intelligence)**: Provides visual situational awareness of global supply routes and vessel positions. |
| `src/translations.ts` | TypeScript | Bilingual internationalization (i18n) dictionary. Provides full localization in **English** and **Hindi (हिन्दी)** for all UI labels, port names, vessel classes, commodities, and tooltips. | **HIGH (Localization)**: Enables seamless switching between English and Hindi for domestic Indian and international operators. |
| `src/index.css` | CSS3, Tailwind CSS v4 | Global styling stylesheet. Implements custom Liquid Glassmorphic backdrop filters (`backdrop-filter: blur(42px)`), neon glows, ambient lighting effects, scrollbars, and keyframe animations. | **HIGH (Visual Design & Theme)**: Establishes the distinctive, modern liquid glass aesthetic across all screen sizes. |
| `src/components/OfflineNoticeModal.tsx` | TypeScript, TSX | Offline banner and modal dialog alerting users when internet connectivity is lost, detailing that cached models remain active. | **MEDIUM (PWA Resilience)**: Ensures graceful user feedback during network dropouts at sea or remote port areas. |
| `src/components/sagarsetu/AISVesselTracker.tsx` | TypeScript, TSX | SagarSetu AIS fleet tracking component. Displays vessel names, MMSI, SOG (Speed Over Ground), navigational status, draught, and destination ETAs. | **HIGH (Fleet Telemetry)**: Delivers live ship telemetry aligned with India's National Logistics Portal (SagarSetu). |
| `src/components/sagarsetu/GreenFreightCarbon.tsx` | TypeScript, TSX | IMO MARPOL Annex VI carbon accounting card. Displays Scope-3 CO₂ emissions, CII vessel rating (Class A–E), carbon offset surcharges, and Green Voyage Scores. | **HIGH (ESG & Decarbonization)**: Automates environmental compliance and green chartering analytics. |
| `src/components/sagarsetu/KAVACHWeatherCard.tsx` | TypeScript, TSX | KAVACH meteorological risk intelligence card. Displays 3-point weather risk (Origin, Transit Sea Corridor, Destination), wave heights, wind speeds, and weather delay premiums. | **HIGH (Weather Resilience)**: Protects charterers from severe monsoon delays and cyclone risk in the Indian Ocean. |
| `src/assets/world-countries.json` | JSON, GeoJSON | GeoJSON polygon dataset containing global national boundaries and coastlines used by Leaflet map overlays. | **MEDIUM (Map Asset)**: Renders landmasses and coastlines on the interactive route map. |
| `src/assets/maritime-logistics-logo.png` | PNG (Binary) | High-resolution official brand logo of Nautilus Logistics AI with transparent alpha channel. | **LOW (Visual Branding)**: Brand identity asset rendered in headers and splash screens. |
| `src/assets/team-logo.png` | PNG (Binary) | Official development team logo displayed across headers, about modals, and dialogs. | **LOW (Visual Branding)**: Team attribution graphic. |
| `src/assets/compass.png` | PNG (Binary) | High-resolution navigational compass rose graphic with transparent background. | **LOW (Visual Asset)**: Decorative nautical graphic for map overlays and report cards. |
| `src/assets/background.jpg` | JPG (Binary) | High-definition ocean sunset background photo used behind the translucent liquid glass cards. | **MEDIUM (UI Backdrop)**: Ambient background image that gives the glassmorphic cards their depth. |
| `public/index.html` | HTML5 | Single-page application root HTML document. Configures viewport meta tags, PWA headers, SVG icons, and the `#root` mount target. | **CRITICAL (HTML Shell)**: The foundational HTML document loaded by browsers and desktop webviews. |
| `public/manifest.json` | JSON | Progressive Web App (PWA) web app manifest declaring app name, icons, start URL, theme colors, and standalone display mode. | **MEDIUM (PWA Config)**: Enables "Add to Home Screen" and offline installation on mobile and desktop browsers. |
| `public/sw.js` | JavaScript | PWA Service Worker script managing cache storage, network-first caching strategies, and offline asset availability. | **HIGH (Offline Engine)**: Powers full offline functionality and sub-millisecond asset caching. |
| `public/favicon.svg` | SVG | Scalable vector nautical anchor icon for browser tabs and address bars. | **LOW (Iconography)**: Browser tab icon. |
| `public/icon.ico` | ICO (Binary) | Windows multi-resolution icon file ($16\times16$ to $256\times256$) for desktop shortcuts, executables, and taskbar icons. | **MEDIUM (Application Icon)**: Official desktop icon embedded into executables and shortcuts. |
| `public/icon-512.png` | PNG (Binary) | High-resolution $512\times512$ app icon for PWA splash screens and installer banners. | **LOW (App Icon)**: Large-format app icon. |
| `public/_headers` | Plain Text | Netlify web server header configuration enforcing strict MIME types, CORS headers, and security policies. | **MEDIUM (Server Config)**: Prevents browser MIME-type blocking on deployed web servers. |
| `public/_redirects` | Plain Text | Netlify SPA rewrite rules directing all client-side routes (`/*`) to `/index.html`. | **MEDIUM (SPA Routing)**: Ensures deep URLs and client routes load without 404 errors. |

---

## 2. AI & Machine Learning Engine (`python_engine/`)

| File Path | Languages Used | Purpose & Functionality | Importance to Platform |
| :--- | :--- | :--- | :--- |
| `python_engine/freight_predictor.py` | Python 3.11 | Core freight rate prediction model. Generates 30, 60, and 90-day predictive forward price curves, seasonal Fourier cycles, commodity volatility modeling, and expanding Bayesian confidence bands. | **CRITICAL (AI Forecasting)**: Produces the primary forward freight predictions that drive charter decisions. |
| `python_engine/weather_kavach.py` | Python 3.11 | KAVACH meteorological intelligence algorithm. Calculates a 3-point composite oceanic risk score ($25\% \text{ Origin} + 50\% \text{ Transit} + 25\% \text{ Destination}$), wave swell friction, wind drag, and weather insurance premiums. | **CRITICAL (Meteorological AI)**: Protects against cyclone disruptions, monsoon delays, and speed-loss penalties. |
| `python_engine/carbon_cii.py` | Python 3.11 | IMO MARPOL Annex VI carbon accounting module. Audits voyage fuel burn, computes Scope-3 emissions ($3.114\text{ t CO}_2/\text{t VLSFO}$), evaluates CII grades (Class A–E), and calculates carbon offset surcharges. | **HIGH (ESG Engine)**: Automates environmental compliance, green freight scoring, and carbon credit costs. |
| `python_engine/ais_tracker.py` | Python 3.11 | AIS telemetry engine. Ingests simulated and live NMEA AIS vessel positions, parsing speed over ground, heading, draught, and destination ETA across maritime trade lanes. | **HIGH (Tracking Pipeline)**: Drives fleet tracking analytics and port congestion monitoring. |
| `python_engine/c_cpp_bridge.py` | Python 3.11 (`ctypes`) | Foreign Function Interface (FFI) bridge linking Python with the native compiled C library (`maritime_math.dll`). Invokes microsecond C routines for Great Circle distance and bearing calculations. | **HIGH (Native Interop)**: Eliminates Python computational bottlenecks by offloading heavy math to compiled C. |
| `python_engine/run_pipeline.py` | Python 3.11 | End-to-end testing and verification orchestrator. Executes all Python analytics modules simultaneously and validates pipeline outputs. | **MEDIUM (Testing Tool)**: Verifies backend pipeline correctness before deployment. |
| `python_engine/server.py` | Python 3.11 | Local development HTTP web server with automated port conflict resolution (8000 $\rightarrow$ 8080 $\rightarrow$ free port), explicit MIME-type mapping, and SPA fallback routing. | **HIGH (Local Dev Server)**: Serves the built web platform locally on developer and testing machines. |

---

## 3. High-Performance C/C++ Mathematical & Financial Core (`c_cpp_engine/`)

| File Path | Languages Used | Purpose & Functionality | Importance to Platform |
| :--- | :--- | :--- | :--- |
| `c_cpp_engine/maritime_math.c` | C (C11) | Ultra-fast geodesic mathematics library. Implements Haversine distance, Great Circle nautical mile distances, forward azimuth bearings, voyage steaming hours, and 6-bit NMEA AIS bitstream decoding. | **CRITICAL (High-Speed Math Core)**: Executes thousands of geodesic calculations per second with microsecond latency. |
| `c_cpp_engine/maritime_math.h` | C, C++ Header | Header declarations, mathematical constants (`EARTH_RADIUS_NM`, radian conversion macros), and DLL export function prototypes (`__declspec(dllexport)`). | **HIGH (Header Interface)**: Exposes C function signatures to Python `ctypes` and C++ modules. |
| `c_cpp_engine/maritime_math.dll` | C (Compiled Binary) | Compiled native Windows 64-bit Dynamic Link Library containing the compiled `maritime_math` machine code. | **CRITICAL (Compiled Library)**: The binary library loaded at runtime by the Python analytics engine. |
| `c_cpp_engine/freight_optimizer.cpp` | C++ (C++17) | Voyage financial and deadfreight optimization engine. Calculates vessel daily hire, bunker fuel consumption curves, port wait demurrage penalties, and forward rate curves. | **HIGH (Financial Engine)**: Computes all-in voyage financial balances and deadfreight penalties. |
| `c_cpp_engine/freight_optimizer.hpp` | C++ Header | Struct declarations (`VoyageParameters`, `OptimizationResult`) and class interface for the C++ freight optimizer. | **MEDIUM (C++ Header)**: Defines the data structures used by the C++ financial engine. |
| `c_cpp_engine/main.cpp` | C++ (C++17) | CLI testing harness for the C++ freight optimizer. Instantiates test voyages (e.g. Capesize Newcastle $\rightarrow$ Paradip) and prints formatted voyage summaries. | **MEDIUM (CLI Test Harness)**: Verifies C++ optimization routines in isolation. |
| `c_cpp_engine/build.bat` | Windows Batch | Automated MinGW compilation script that compiles `maritime_math.c` into `maritime_math.dll` and `freight_optimizer.cpp` into `nautilus_core.exe`. | **HIGH (Build Script)**: Automates native C/C++ builds with optimized compiler flags (`-O3 -shared`). |
| `c_cpp_engine/nautilus_core.exe` | C++ (Compiled Binary) | Standalone compiled executable running the native C++ maritime calculation suite. | **MEDIUM (Core Binary)**: Standalone native execution binary. |

---

## 4. Desktop Application Launcher & Setup Installer

| File Path | Languages Used | Purpose & Functionality | Importance to Platform |
| :--- | :--- | :--- | :--- |
| `c_cpp_engine/app_launcher/launcher_main.cpp` | C++17, Win32 API, Winsock2 | Pure native Windows desktop launcher executable (`Nautilus Logistics AI.exe`). Embeds a multi-threaded Winsock2 HTTP server, launches Microsoft Edge/Chrome in app mode (`--app=http://127.0.0.1:8765`), creates Desktop shortcuts via `IShellLinkW`, and manages the Windows System Tray icon. | **CRITICAL (Desktop App Launcher)**: Allows users to run Nautilus Logistics AI as a 100% native Windows desktop application with zero external DLLs. |
| `c_cpp_engine/app_launcher/manifest.xml` | XML | Windows Application Manifest declaring Windows 10/11 compatibility, DPI awareness (`PerMonitorV2`), and standard user privilege level (`asInvoker`). | **HIGH (Security & DPI)**: Prevents UAC administrator prompts and ensures crisp high-DPI scaling on 4K displays. |
| `c_cpp_engine/app_launcher/resource.rc` | Windows Resource Script | Win32 resource file embedding the application icon (`icon.ico`), application manifest, and complete official PE `VERSIONINFO` metadata block. | **HIGH (PE Metadata)**: Attaches company name, version (`2.0.0.0`), and icon to eliminate generic malware heuristic flags. |
| `c_cpp_engine/setup_builder/setup_main.cpp` | C++17, Win32 API, CommCtrl | Pure native Windows GUI Setup Wizard (`Nautilus Logistics AI Setup.exe`). Features instant in-memory binary package extraction, animated progress bar, custom install path selection, Desktop/Start Menu shortcut creation, and Windows Registry uninstaller registration. | **CRITICAL (Installer Engine)**: Provides a single standalone installer executable that extracts in ~40ms with zero PowerShell/AMSI dependencies. |
| `c_cpp_engine/setup_builder/setup_resource.rc` | Windows Resource Script | Setup resource script embedding the installer icon, manifest, and the serialized binary application bundle (`app_payload.bin`). | **CRITICAL (Installer Payload)**: Packages all application files directly into the setup executable binary. |
| `c_cpp_engine/setup_builder/setup_manifest.xml` | XML | Setup installer manifest declaring standard user privileges (`asInvoker`) for clean non-admin installation into `%LocalAppData%\Programs`. | **HIGH (Installer Manifest)**: Guarantees smooth installation on school, corporate, and guest PCs without admin rights. |
| `c_cpp_engine/setup_builder/app_payload.bin` | Binary Data Bundle | Optimized binary package containing all 34 production files and assets, serialized with 16-byte magic headers for instant native in-memory unpacking. | **CRITICAL (Data Bundle)**: Embedded payload extracted by the setup installer. |
| `c_cpp_engine/setup_builder/uninstall_main.cpp` | C++17, Win32 API | Standalone uninstaller (`uninstall.exe`). Prompts confirmation, cleans up Desktop/Start Menu shortcuts, removes Registry keys, and deletes the installation directory. | **HIGH (Uninstaller)**: Integrates the platform into Windows "Installed Apps" (Add/Remove Programs) for clean removal. |
| `c_cpp_engine/setup_builder/Trust_Developer_Certificate.bat` | Windows Batch | 1-click batch script adding the Authenticode certificate to the Windows `TrustedPublisher` and `Root` stores via `certutil`. | **MEDIUM (Cert Helper)**: Optional helper for corporate networks with strict SmartScreen policies. |
| `c_cpp_engine/setup_builder/Nautilus_Developer_Certificate.cer` | X.509 Certificate | Exported public X.509 code-signing certificate for `Nautilus Maritime AI Technologies Inc.` | **MEDIUM (Security Certificate)**: Public certificate for digital signature verification. |

---

## 5. Root Configuration, Build Automation & Distribution Files

| File Path | Languages Used | Purpose & Functionality | Importance to Platform |
| :--- | :--- | :--- | :--- |
| `package.json` | JSON | Node.js project manifest. Defines frontend dependencies (React 19, Recharts, Leaflet, Tailwind CSS v4, Lucide Icons, Vite 8, TypeScript 5.9) and build scripts (`npm run build`, `npm run dev`). | **CRITICAL (Project Manifest)**: Central definition of all frontend packages, build tools, and scripts. |
| `package-lock.json` | JSON | Deterministic dependency tree lockfile recording exact cryptographic hashes and dependency versions. | **HIGH (Reproducibility)**: Guarantees identical package installations across all developer machines and CI/CD pipelines. |
| `vite.config.ts` | TypeScript | Vite 8 build bundler configuration. Configures the React compiler plugin, Tailwind CSS integration, Rolldown optimizations, and chunk splitting rules. | **HIGH (Bundler Config)**: Controls build minification, tree-shaking, and production asset packaging. |
| `tsconfig.json` | JSON | Root TypeScript configuration file referencing application and node compilation targets. | **HIGH (TS Config)**: Configures project-wide TypeScript compiler settings. |
| `tsconfig.app.json` | JSON | Frontend TypeScript compiler configuration targeting ES2022, React JSX, DOM libraries, and strict type checking. | **HIGH (App TS Config)**: Enforces type safety across the React frontend codebase. |
| `tsconfig.node.json` | JSON | TypeScript compiler configuration for Vite configuration files and Node.js build scripts. | **MEDIUM (Node TS Config)**: Configures TypeScript for build tools and scripts. |
| `netlify.toml` | TOML | Netlify cloud deployment configuration. Declares publish directory (`Netlify distributable version`), build command (`npm run build`), and custom cache-control headers. | **HIGH (Cloud Deployment)**: Automates production cloud deployment on Netlify with optimal caching rules. |
| `server.py` | Python 3.11 | Standalone Python HTTP development server. Resolves MIME types for modern ES modules, automatically finds free ports, and provides SPA client route fallbacks. | **HIGH (Local Server)**: Zero-dependency local web server for testing production builds. |
| `start_server.bat` | Windows Batch | 1-click Windows batch script that launches `server.py` and opens the platform in the default browser. | **MEDIUM (Convenience Script)**: Provides 1-click startup for non-technical users. |
| `create_release_zip.py` | Python 3.11 | Release packaging script. Automates building and zipping master archives (`Nautilus Logistics AI.zip` and `Nautilus Logistics AI Executable App.zip`) for distribution. | **HIGH (Release Packaging)**: Generates clean, production-ready release archives. |
| `README.md` | Markdown | Executive project README providing architectural overview, setup instructions, feature list, and developer guide. | **HIGH (Documentation)**: Primary entry point for developers and evaluators reviewing the codebase. |
| `Nautilus Logistics AI Setup.exe` | Windows PE Executable | Standalone signed Windows GUI Setup Installer (6.87 MB) ready for 1-click installation on any Windows 10/11 computer. | **CRITICAL (Primary Deliverable)**: The user-facing installer for deploying the platform on other computers. |
| `Nautilus Logistics AI Executable App.zip` | ZIP Archive | Portable zip archive containing the standalone desktop application (`Nautilus Logistics AI.exe`), `app_data/`, and shortcut scripts. | **HIGH (Portable Release)**: Portable archive for users who prefer running without installation. |
| `Nautilus Logistics AI.zip` | ZIP Archive | Master release archive packaging the entire source code, C/C++ engines, Python backend, documentation, and installers. | **CRITICAL (Master Archive)**: The complete project package for archival and evaluation. |

---

## 📊 Summary Statistics by Layer

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│  Layer                 Primary Languages                 File Count              │
├──────────────────────────────────────────────────────────────────────────────────┤
│  Frontend & UI         TypeScript, TSX, CSS3, HTML5      21 Files                │
│  AI & Analytics        Python 3.11                       7 Files                 │
│  C/C++ Native Core     C11, C++17, Batch                 8 Files                 │
│  Launcher & Installer  C++17, Win32 API, XML, Resource   10 Files                │
│  Project Config & Ops  JSON, TOML, Batch, Markdown       13 Files                │
│  TOTAL PROJECT FILES                                     59 Core Files           │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

*Document Generated for Nautilus Logistics AI Platform Architecture Evaluation.*

---

# 🔄 End-to-End Data Flow Architecture

This section details how data enters the system, passes through the polyglot layers (C/C++, Python, and React/TypeScript), transforms, and renders to the user.

```
                                  USER INPUTS
  (Commodity, Cargo Quantity, Origin Port, Destination Port, Vessel Class, Horizon, Currency)
                                       │
                                       ▼
                     ┌───────────────────────────────────┐
                     │            src/App.tsx            │
                     │ (State Dispatch & Parameter Bar)  │
                     └─────────────────┬─────────────────┘
                                       │
            ┌──────────────────────────┼──────────────────────────┐
            │                          │                          │
            ▼                          ▼                          ▼
 ┌──────────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐
 │  GEODESIC ROUTE MATH │   │  METEOROLOGICAL AI   │   │  TELEMETRY & FLEET   │
 │   maritime_math.c    │   │   weather_kavach.py  │   │    ais_tracker.py    │
 │  c_cpp_bridge.py     │   │  KAVACHWeatherCard   │   │   SeaPortsMap.tsx    │
 └──────────┬───────────┘   └──────────┬───────────┘   └──────────┬───────────┘
            │                          │                          │
            │  Distance (NM)           │  Weather Risk (0-100%)   │  Vessel Coords
            │  Steaming Hours          │  Wave Swell Drag         │  Port Waypoints
            │                          │  Delay Premiums          │  Live SOG
            └──────────────────────────┼──────────────────────────┘
                                       │
                                       ▼
                     ┌───────────────────────────────────┐
                     │    python_engine/freight_predictor│
                     │          src/App.tsx Engine       │
                     │  (30/60/90-Day Forward Forecasts) │
                     └─────────────────┬─────────────────┘
                                       │
                                       │ Predicted Spot Rates ($/MT)
                                       │ Daily Fixture Trajectory ($/day)
                                       │ Confidence Bounds (±3.2% to ±6.8%)
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            │                                                     │
            ▼                                                     ▼
 ┌──────────────────────┐                              ┌──────────────────────┐
 │ 5D VESSEL OPTIMIZER  │                              │ IMO CARBON & CII     │
 │ freight_optimizer.cpp│                              │ carbon_cii.py        │
 │ src/App.tsx Optimizer│                              │ GreenFreightCarbon   │
 └──────────┬───────────┘                              └──────────┬───────────┘
            │                                                     │
            │ • Draft Compliance (Origin/Dest)                    │ • Total Fuel Burn (MT)
            │ • Weather Stability Bonus                           │ • Scope-3 CO₂ Tonnes
            │ • Commodity Gear Fit (4x30t cranes)                 │ • CII Rating (A to E)
            │ • Deadfreight Elimination                           │ • Carbon Offset ($/MT)
            │ • Net Projected Savings ($/day)                     │ • Green Score (0-100)
            │                                                     │
            └──────────────────────────┬──────────────────────────┘
                                       │
                                       ▼
                     ┌───────────────────────────────────┐
                     │          ACTION SIGNALS           │
                     │   FIX NOW  │   WAIT   │   SPLIT   │
                     └─────────────────┬─────────────────┘
                                       │
                                       ▼
                     ┌───────────────────────────────────┐
                     │          UI VISUALIZATION         │
                     │  • Recharts Forward Price Curves  │
                     │  • Leaflet Interactive Geo-Map    │
                     │  • Liquid Glass Analytics Cards   │
                     │  • Bilingual EN/HI Output Engine  │
                     └───────────────────────────────────┘
```

---

## 🌊 Detailed Step-by-Step Data Pipelines

### Pipeline 1: Geodesic & Hydrodynamic Distance Resolution
```
[User Selects Origin & Destination]
           │
           ▼
[src/App.tsx] ── Lat/Lon Lookup ──► [PORT_COORDINATES Dictionary]
                                              │
                                              ▼
[python_engine/c_cpp_bridge.py] ── ctypes ──► [c_cpp_engine/maritime_math.dll]
                                              • calculate_haversine_distance()
                                              • calculate_initial_bearing()
                                              • estimate_voyage_hours()
                                              │
                                              ▼
                     [Returns Nautical Distance (NM) & Steaming Days]
```

- **Inputs**: Origin coordinates $(\phi_1, \lambda_1)$, Destination coordinates $(\phi_2, \lambda_2)$, vessel cruising speed ($12.5\text{ kts}$).
- **Transformation**: Microsecond Great-Circle trigonometry in compiled C11 machine code.
- **Outputs**: Exact nautical miles, initial azimuth heading, and base steaming duration.

---

### Pipeline 2: KAVACH Meteorological & Cyclone Risk Assessment
```
[Origin Port] ──► [Transit Sea Corridor] ──► [Destination Port]
       │                    │                       │
       ▼                    ▼                       ▼
  Weather Node         Weather Node            Weather Node
(Wind, Wave, Baro)   (Wind, Wave, Baro)      (Wind, Wave, Baro)
       │                    │                       │
       └────────────────────┼───────────────────────┘
                            ▼
          [python_engine/weather_kavach.py]
          Risk = 25%(Origin) + 50%(Route) + 25%(Dest)
                            │
                            ▼
          [src/components/sagarsetu/KAVACHWeatherCard.tsx]
          • Composite Risk Index (0 - 100%)
          • Weather Status: Favorable / Moderate / High Swell
          • Weather Fuel Surcharge ($/MT)
```

- **Inputs**: Route waypoints across Bay of Bengal, Arabian Sea, Indian Ocean, and South China Sea.
- **Transformation**: 3-point composite oceanic risk scoring evaluating wave swell height ($H_s$), surface wind speed, and atmospheric barometric depression.
- **Outputs**: Weather delay risk percentage, adverse sea-state penalty factor ($\Phi_{\text{Weather}}$), and weather insurance surcharge.

---

### Pipeline 3: Forward Freight Rate Forecasting
```
[Base Commodity Rate] ──► [Distance Multiplier: (Dist/4000)^0.65]
                                      │
                                      ▼
                        [Time-Series Decomposition]
                        • Seasonal Harmonics: sin(d * 0.07)
                        • Cyclical Waves: cos(d * 0.15 + 0.8)
                        • Commodity Volatility Multiplier
                                      │
                                      ▼
                        [python_engine/freight_predictor.py]
                        [src/App.tsx Forward Curve Engine]
                                      │
                                      ▼
                        [90-Day Price Trajectory]
                        • Day-by-day Predicted Spot Rate ($/MT & ₹/MT)
                        • Daily Voyage Cost ($/day Spot)
                        • Upper & Lower Bayesian Confidence Bounds
```

- **Inputs**: Commodity baseline spot rate, cargo tonnage, historical Baltic Exchange index weights, forecast horizon ($30/60/90\text{ days}$).
- **Transformation**: Econometric Fourier wave modeling with expanding variance bands ($\pm 3.2\%$ at 30 days to $\pm 6.8\%$ at 90 days).
- **Outputs**: High-resolution daily rate curve rendered via SVG area charts in Recharts.

---

### Pipeline 4: 5-Dimensional Multi-Factor Vessel Optimizer
```
[All 10 Vessel Classes: Handysize 35k ──► Newcastlemax 208k]
                               │
                               ▼
        ┌───────────────────────────────────────────────┐
        │ Dimension 1: Port Draught Feasibility Filter  │
        │ Draft(Vessel) <= min(Draft_Origin, Draft_Dest)│
        └──────────────────────┬────────────────────────┘
                               │
                               ▼
        ┌───────────────────────────────────────────────┐
        │ Dimension 2: Cargo Batching & Consolidation   │
        │ • Large Batches: Consolidate to 1x Large Hull │
        │ • Small Batches (<15k MT): Partial Parcel     │
        └──────────────────────┬────────────────────────┘
                               │
                               ▼
        ┌───────────────────────────────────────────────┐
        │ Dimension 3: Weather Resistance Coefficient   │
        │ Deep hulls (Capesize) get stability bonus     │
        └──────────────────────┬────────────────────────┘
                               │
                               ▼
        ┌───────────────────────────────────────────────┐
        │ Dimension 4: Commodity Specificity & Gear     │
        │ Geared Supramax (4x30t cranes) for agri/urea  │
        └──────────────────────┬────────────────────────┘
                               │
                               ▼
        ┌───────────────────────────────────────────────┐
        │ Dimension 5: Net AI Savings Calculation       │
        │ Savings = Baltic Benchmark - AI Optimized Cost│
        └──────────────────────┬────────────────────────┘
                               │
                               ▼
            [Suggested Vessel for Maximum Savings]
            • Optimal Hull Class Recommendation
            • Net Savings per Metric Ton ($/MT & ₹/MT)
            • Net Savings per Voyage Day ($/day)
            • Multi-Voyage vs Single-Voyage Strategy
```

- **Inputs**: Cargo volume, 10 bulk carrier class profiles, port limiting drafts, KAVACH weather state, commodity handling attributes.
- **Transformation**: Multi-criteria constraint minimization algorithm.
- **Outputs**: Optimal ship class, multi-voyage consolidation strategy, and all-in net savings.

---

### Pipeline 5: IMO MARPOL Carbon Accounting & CII Rating
```
[Selected Vessel Class & Steaming Distance]
                    │
                    ▼
[python_engine/carbon_cii.py]
• Eco-Burn Rate: 32.4 MT/day (Capesize) vs 26.8 MT/day (Panamax)
• Steaming Fuel = Steaming Days * Daily Burn Rate
• Idle Port Fuel = Port Wait Days * 3.5 MT/day
                    │
                    ▼
[Total Fuel Burned (MT)] ── Multiplied by 3.114 ──► [Scope-3 CO₂ (Tonnes)]
                                                              │
                                                              ▼
                                               ┌──────────────────────────────┐
                                               │ • Vessel CII Rating (A to E) │
                                               │ • Carbon Offset Surcharge    │
                                               │ • Green Voyage Score (0-100) │
                                               └──────────────────────────────┘
```

- **Inputs**: Steaming distance, vessel class hydrodynamic profile, port wait days.
- **Transformation**: IMO MARPOL Annex VI carbon conversion factor ($3.114\text{ t CO}_2/\text{t VLSFO}$).
- **Outputs**: Total voyage $\text{CO}_2$ tonnage, Carbon Intensity Indicator grade ($A$–$E$), carbon offset surcharge per metric ton, and Green ESG score.

---

### Pipeline 6: Desktop Executable & In-Memory Package Loader
```
[Nautilus Logistics AI Setup.exe]
           │
           ▼
[LockResource(1001 RCDATA)] ──► Reads 'app_payload.bin' in memory
           │
           ▼
[ExtractNativeBundle()] ──► Native Win32 File I/O (~40ms)
           │
           ▼
[Installs to %LocalAppData%\Programs\Nautilus Logistics AI]
           │
           ▼
[Nautilus Logistics AI.exe]
           │
           ├──► Starts Embedded Winsock2 Server on 127.0.0.1:8765
           │
           └──► Launches Edge/Chrome in App Mode:
                msedge.exe --app=http://127.0.0.1:8765
```

- **Inputs**: Embedded binary payload resource `app_payload.bin`.
- **Transformation**: Zero-process native memory mapping and in-process file extraction.
- **Outputs**: High-speed, standalone desktop application execution without external dependencies.
