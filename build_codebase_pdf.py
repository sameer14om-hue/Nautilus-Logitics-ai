import os
import subprocess

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Nautilus Logistics AI — Codebase & Data Flow Architecture</title>
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 12mm 14mm 12mm;
    @bottom-right {
      content: counter(page);
    }
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    line-height: 1.45;
    font-size: 9pt;
  }

  .header-card {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f3d56 100%);
    color: #ffffff;
    padding: 22px 26px;
    border-radius: 12px;
    margin-bottom: 18px;
    border: 1px solid rgba(255,255,255,0.1);
  }

  .header-card h1 {
    font-size: 19pt;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #38bdf8;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .header-card p.subtitle {
    font-size: 10pt;
    color: #cbd5e1;
    margin-bottom: 12px;
    font-weight: 400;
  }

  .meta-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    background: rgba(15, 23, 42, 0.6);
    padding: 10px 14px;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.08);
  }

  .meta-item span.label {
    font-size: 7pt;
    text-transform: uppercase;
    color: #94a3b8;
    display: block;
    font-weight: 600;
  }

  .meta-item span.val {
    font-size: 8.5pt;
    color: #f8fafc;
    font-weight: 700;
  }

  h2.section-title {
    font-size: 12pt;
    font-weight: 700;
    color: #0f172a;
    border-bottom: 2px solid #0284c7;
    padding-bottom: 4px;
    margin-top: 18px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 6px;
    page-break-after: avoid;
  }

  h3.subsection-title {
    font-size: 10pt;
    font-weight: 700;
    color: #0369a1;
    margin-top: 12px;
    margin-bottom: 6px;
    page-break-after: avoid;
  }

  p {
    margin-bottom: 8px;
    color: #334155;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 14px;
    font-size: 8pt;
    page-break-inside: auto;
  }

  tr {
    page-break-inside: avoid;
    page-break-after: auto;
  }

  th {
    background-color: #0f172a;
    color: #f8fafc;
    font-weight: 700;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #334155;
    font-size: 7.5pt;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }

  td {
    padding: 5px 8px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
    color: #1e293b;
  }

  tr:nth-child(even) {
    background-color: #f8fafc;
  }

  .badge {
    display: inline-block;
    padding: 1px 5px;
    border-radius: 4px;
    font-size: 7pt;
    font-weight: 700;
    text-transform: uppercase;
  }

  .badge-critical { background-color: #fee2e2; color: #991b1b; border: 1px solid #f87171; }
  .badge-high { background-color: #e0f2fe; color: #0369a1; border: 1px solid #38bdf8; }
  .badge-medium { background-color: #fef3c7; color: #92400e; border: 1px solid #fcd34d; }
  .badge-low { background-color: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; }

  .code-text {
    font-family: "Cascadia Code", Consolas, Monaco, "Courier New", monospace;
    font-size: 7.5pt;
    font-weight: 600;
    color: #095988;
    background-color: #e0f2fe;
    padding: 1px 4px;
    border-radius: 3px;
  }

  .diagram-box {
    background-color: #0f172a;
    color: #e2e8f0;
    padding: 12px 14px;
    border-radius: 8px;
    font-family: "Cascadia Code", Consolas, Monaco, "Courier New", monospace;
    font-size: 7pt;
    line-height: 1.25;
    white-space: pre;
    overflow-x: hidden;
    margin: 10px 0 14px 0;
    border: 1px solid #334155;
    page-break-inside: avoid;
  }

  .flow-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #0284c7;
    border-radius: 6px;
    padding: 10px 12px;
    margin-bottom: 10px;
    page-break-inside: avoid;
  }

  .flow-card h4 {
    font-size: 9pt;
    color: #0f172a;
    font-weight: 700;
    margin-bottom: 4px;
  }

  .flow-card p {
    font-size: 8pt;
    margin-bottom: 4px;
  }

  .flow-card ul {
    margin-left: 16px;
    font-size: 7.5pt;
    color: #334155;
  }

  .page-break {
    page-break-before: always;
  }

  .footer-note {
    margin-top: 20px;
    padding-top: 8px;
    border-top: 1px solid #cbd5e1;
    font-size: 7.5pt;
    color: #64748b;
    text-align: center;
  }
</style>
</head>
<body>

  <!-- Cover Header -->
  <div class="header-card">
    <h1>⚓ Nautilus Logistics AI</h1>
    <p class="subtitle">Complete Codebase File Explanation & End-to-End Data Flow Architecture</p>
    <div class="meta-grid">
      <div class="meta-item">
        <span class="label">System Version</span>
        <span class="val">v2.0.0 Production</span>
      </div>
      <div class="meta-item">
        <span class="label">Architecture</span>
        <span class="val">Polyglot C++/Py/TS</span>
      </div>
      <div class="meta-item">
        <span class="label">Core Modules</span>
        <span class="val">59 Managed Files</span>
      </div>
      <div class="meta-item">
        <span class="label">Compliance</span>
        <span class="val">IMO MARPOL / SagarSetu</span>
      </div>
    </div>
  </div>

  <!-- Summary Statistics -->
  <h2 class="section-title">1. Codebase Summary & Layer Distribution</h2>
  <p>The Nautilus Logistics AI codebase is built on a 5-tier architecture ensuring sub-millisecond calculation speed, predictive accuracy, and zero-dependency standalone execution.</p>

  <table>
    <thead>
      <tr>
        <th style="width: 22%;">Layer / Subsystem</th>
        <th style="width: 28%;">Primary Languages</th>
        <th style="width: 15%;">File Count</th>
        <th style="width: 35%;">Key Responsibilities</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Frontend & UI</strong></td>
        <td>TypeScript, TSX, CSS3, HTML5</td>
        <td>21 Files</td>
        <td>Liquid Glass UI, Recharts forward curves, Leaflet geospatial mapping, bilingual i18n.</td>
      </tr>
      <tr>
        <td><strong>AI & Analytics</strong></td>
        <td>Python 3.11</td>
        <td>7 Files</td>
        <td>Freight rate prediction, KAVACH weather risk, IMO Scope-3 carbon, AIS fleet tracking.</td>
      </tr>
      <tr>
        <td><strong>C/C++ Native Core</strong></td>
        <td>C (C11), C++ (C++17)</td>
        <td>8 Files</td>
        <td>Microsecond Great Circle geodesic math, forward azimuth bearings, voyage financials.</td>
      </tr>
      <tr>
        <td><strong>Launcher & Installer</strong></td>
        <td>C++17, Win32 API, Winsock2</td>
        <td>10 Files</td>
        <td>Zero-dependency desktop launcher, in-memory unpacker, Authenticode digital signing.</td>
      </tr>
      <tr>
        <td><strong>Project Ops & Config</strong></td>
        <td>JSON, TOML, Batch, Python</td>
        <td>13 Files</td>
        <td>Vite bundler config, TypeScript configs, Netlify cloud deployment, release pipelines.</td>
      </tr>
      <tr style="background-color: #e2e8f0; font-weight: bold;">
        <td>TOTAL PLATFORM</td>
        <td>Polyglot Multi-Tier Stack</td>
        <td>59 Files</td>
        <td>Complete End-to-End Autonomous Maritime Freight Optimization Platform</td>
      </tr>
    </tbody>
  </table>

  <!-- Table 1: Frontend & UI -->
  <h2 class="section-title">2. Frontend Architecture & UI Layer (<code>src/</code> & <code>public/</code>)</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 24%;">File Path</th>
        <th style="width: 16%;">Languages</th>
        <th style="width: 48%;">Purpose & Functionality</th>
        <th style="width: 12%;">Importance</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="code-text">src/App.tsx</span></td>
        <td>TypeScript, TSX</td>
        <td>Primary React application controller. Manages state, 5-column parameter bar, KPI cards (Action Signal, Net Savings, Confidence), 5D vessel optimizer, forward curve charts, and view routing.</td>
        <td><span class="badge badge-critical">Critical</span></td>
      </tr>
      <tr>
        <td><span class="code-text">src/main.tsx</span></td>
        <td>TypeScript, TSX</td>
        <td>Application bootstrap entrypoint. Renders root <App /> with React 19 StrictMode into index.html.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">src/SeaPortsMap.tsx</span></td>
        <td>TypeScript, TSX</td>
        <td>Interactive geospatial maritime route map using Leaflet.js. Renders 18 Indian ports, 12 global gateways, great-circle trade lanes, and live vessel telemetry markers.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">src/translations.ts</span></td>
        <td>TypeScript</td>
        <td>Bilingual internationalization (i18n) dictionary. Provides full localization in English and Hindi (हिन्दी) across all metrics, labels, port names, and tooltips.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">src/index.css</span></td>
        <td>CSS3, Tailwind v4</td>
        <td>Global stylesheet implementing Liquid Glassmorphic backdrop blur (blur(42px)), neon glows, ambient lighting, custom scrollbars, and keyframe animations.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">src/components/sagarsetu/AISVesselTracker.tsx</span></td>
        <td>TypeScript, TSX</td>
        <td>SagarSetu AIS fleet tracking component. Displays vessel names, MMSI, SOG (Speed Over Ground), headings, draft, and destination ETAs.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">src/components/sagarsetu/GreenFreightCarbon.tsx</span></td>
        <td>TypeScript, TSX</td>
        <td>IMO MARPOL Annex VI carbon accounting card. Displays Scope-3 CO₂ footprint, CII ratings (Class A–E), carbon offset surcharges, and Green Scores.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">src/components/sagarsetu/KAVACHWeatherCard.tsx</span></td>
        <td>TypeScript, TSX</td>
        <td>KAVACH meteorological risk intelligence card. Displays 3-point weather risk (Origin, Transit Corridor, Destination), wave heights, wind speeds, and weather delay premiums.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">src/components/OfflineNoticeModal.tsx</span></td>
        <td>TypeScript, TSX</td>
        <td>Offline PWA modal alerting users when internet connectivity drops and confirming cached model execution.</td>
        <td><span class="badge badge-medium">Medium</span></td>
      </tr>
      <tr>
        <td><span class="code-text">src/assets/world-countries.json</span></td>
        <td>GeoJSON / JSON</td>
        <td>GeoJSON polygon dataset providing global coastlines and boundaries for the interactive Leaflet sea map.</td>
        <td><span class="badge badge-medium">Medium</span></td>
      </tr>
      <tr>
        <td><span class="code-text">public/index.html</span></td>
        <td>HTML5</td>
        <td>Root HTML5 single-page application document. Configures viewport, PWA headers, fonts, and DOM root.</td>
        <td><span class="badge badge-critical">Critical</span></td>
      </tr>
      <tr>
        <td><span class="code-text">public/manifest.json</span></td>
        <td>JSON</td>
        <td>Progressive Web App manifest declaring application name, standalone display mode, theme colors, and icons.</td>
        <td><span class="badge badge-medium">Medium</span></td>
      </tr>
      <tr>
        <td><span class="code-text">public/sw.js</span></td>
        <td>JavaScript</td>
        <td>PWA Service Worker script providing offline asset caching and sub-millisecond local loading.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">public/icon.ico & icon-512.png</span></td>
        <td>Binary ICO/PNG</td>
        <td>Official application iconography used across desktop shortcuts, taskbars, and mobile home screens.</td>
        <td><span class="badge badge-medium">Medium</span></td>
      </tr>
      <tr>
        <td><span class="code-text">public/_headers & _redirects</span></td>
        <td>Plain Text</td>
        <td>Netlify cloud server rules enforcing strict MIME types, CORS headers, and SPA URL fallback rewrites.</td>
        <td><span class="badge badge-medium">Medium</span></td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- Table 2: AI & Python Engine -->
  <h2 class="section-title">3. AI & Machine Learning Engine (<code>python_engine/</code>)</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 26%;">File Path</th>
        <th style="width: 14%;">Languages</th>
        <th style="width: 48%;">Purpose & Functionality</th>
        <th style="width: 12%;">Importance</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="code-text">python_engine/freight_predictor.py</span></td>
        <td>Python 3.11</td>
        <td>Core time-series freight forecasting model. Generates 30, 60, and 90-day forward price curves, seasonal Fourier cycles, commodity volatility curves, and Bayesian confidence intervals (±3.2% to ±6.8%).</td>
        <td><span class="badge badge-critical">Critical</span></td>
      </tr>
      <tr>
        <td><span class="code-text">python_engine/weather_kavach.py</span></td>
        <td>Python 3.11</td>
        <td>KAVACH meteorological AI. Computes 3-point composite oceanic risk score (25% Origin + 50% Sea Lane + 25% Destination), wave swell height, wind drag, and adverse sea-state delay surcharges.</td>
        <td><span class="badge badge-critical">Critical</span></td>
      </tr>
      <tr>
        <td><span class="code-text">python_engine/carbon_cii.py</span></td>
        <td>Python 3.11</td>
        <td>IMO MARPOL Annex VI carbon accounting module. Audits voyage fuel burn, computes Scope-3 emissions (3.114 t CO₂ / t VLSFO), evaluates CII vessel grades (A–E), and calculates carbon offset costs.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">python_engine/ais_tracker.py</span></td>
        <td>Python 3.11</td>
        <td>AIS fleet telemetry engine. Ingests simulated and live NMEA AIS vessel positions, parsing speed over ground, heading, draught, and destination ETA across maritime trade lanes.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">python_engine/c_cpp_bridge.py</span></td>
        <td>Python 3.11 (ctypes)</td>
        <td>Foreign Function Interface (FFI) bridge linking Python with native compiled maritime_math.dll for microsecond geodesic distance and bearing calculations.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">python_engine/server.py</span></td>
        <td>Python 3.11</td>
        <td>Local development HTTP web server with automated port conflict discovery, explicit MIME-type mapping, and SPA fallback routing.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">python_engine/run_pipeline.py</span></td>
        <td>Python 3.11</td>
        <td>End-to-end testing script validating forecast curves, weather risks, and carbon metrics simultaneously.</td>
        <td><span class="badge badge-medium">Medium</span></td>
      </tr>
    </tbody>
  </table>

  <!-- Table 3: C/C++ Engine -->
  <h2 class="section-title">4. High-Performance C/C++ Engine (<code>c_cpp_engine/</code>)</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 26%;">File Path</th>
        <th style="width: 14%;">Languages</th>
        <th style="width: 48%;">Purpose & Functionality</th>
        <th style="width: 12%;">Importance</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="code-text">c_cpp_engine/maritime_math.c</span></td>
        <td>C (C11)</td>
        <td>Ultra-fast geodesic math engine. Implements Haversine distance, Great Circle nautical miles, forward azimuth bearings, voyage steaming hours, and 6-bit NMEA AIS bitstream decoding.</td>
        <td><span class="badge badge-critical">Critical</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/maritime_math.h</span></td>
        <td>C / C++ Header</td>
        <td>Header declarations, mathematical constants (EARTH_RADIUS_NM), and DLL export function prototypes (__declspec(dllexport)).</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/maritime_math.dll</span></td>
        <td>C (Compiled DLL)</td>
        <td>Compiled 64-bit Windows Dynamic Link Library invoked by Python ctypes and C++ modules at runtime.</td>
        <td><span class="badge badge-critical">Critical</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/freight_optimizer.cpp</span></td>
        <td>C++ (C++17)</td>
        <td>Voyage financial optimizer. Computes vessel daily hire, fuel burn curves, port wait demurrage penalties, and deadfreight curves.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/freight_optimizer.hpp</span></td>
        <td>C++ Header</td>
        <td>Data structure definitions (VoyageParameters, OptimizationResult) and class interfaces for the freight optimizer.</td>
        <td><span class="badge badge-medium">Medium</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/build.bat</span></td>
        <td>Windows Batch</td>
        <td>Automated MinGW compilation script building maritime_math.dll and nautilus_core.exe with -O3 optimization flags.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/nautilus_core.exe</span></td>
        <td>C++ Binary</td>
        <td>Standalone native executable executing core C++ maritime calculations.</td>
        <td><span class="badge badge-medium">Medium</span></td>
      </tr>
    </tbody>
  </table>

  <!-- Table 4: Launcher & Installer -->
  <h2 class="section-title">5. Desktop Launcher & Setup Installer Subsystem</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 28%;">File Path</th>
        <th style="width: 14%;">Languages</th>
        <th style="width: 46%;">Purpose & Functionality</th>
        <th style="width: 12%;">Importance</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="code-text">c_cpp_engine/app_launcher/launcher_main.cpp</span></td>
        <td>C++17, Win32, Winsock2</td>
        <td>Native Windows desktop executable (Nautilus Logistics AI.exe). Embeds a multi-threaded Winsock2 HTTP server, launches Edge/Chrome in app mode, creates Desktop shortcuts, and manages the System Tray icon.</td>
        <td><span class="badge badge-critical">Critical</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/app_launcher/manifest.xml</span></td>
        <td>XML</td>
        <td>Application manifest declaring Windows 10/11 compatibility, DPI awareness (PerMonitorV2), and non-admin privilege (asInvoker).</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/setup_builder/setup_main.cpp</span></td>
        <td>C++17, Win32 API</td>
        <td>GUI Setup Installer (Nautilus Logistics AI Setup.exe). Features instant in-memory package unpacking (~40ms), animated progress bar, Desktop/Start Menu shortcut generation, and Add/Remove Programs registry registration.</td>
        <td><span class="badge badge-critical">Critical</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/setup_builder/app_payload.bin</span></td>
        <td>Binary Data</td>
        <td>Optimized binary package containing all 34 production files, serialized with 16-byte magic headers for in-memory setup extraction.</td>
        <td><span class="badge badge-critical">Critical</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/setup_builder/uninstall_main.cpp</span></td>
        <td>C++17, Win32 API</td>
        <td>Clean uninstaller (uninstall.exe). Removes shortcuts, registry keys, and installation directories on demand.</td>
        <td><span class="badge badge-high">High</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/setup_builder/Nautilus_Developer_Certificate.cer</span></td>
        <td>X.509 Certificate</td>
        <td>Official code-signing certificate for Nautilus Maritime AI Technologies Inc. providing Authenticode verified publisher status.</td>
        <td><span class="badge badge-medium">Medium</span></td>
      </tr>
      <tr>
        <td><span class="code-text">c_cpp_engine/setup_builder/Trust_Developer_Certificate.bat</span></td>
        <td>Windows Batch</td>
        <td>1-click helper adding the developer certificate to Windows TrustedPublisher and Root stores via certutil.</td>
        <td><span class="badge badge-medium">Medium</span></td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- End-to-End Data Flow Architecture -->
  <h2 class="section-title">6. End-to-End Data Flow Architecture</h2>
  <p>The diagram below illustrates how user parameters and real-time maritime telemetry propagate across the multi-tier engine to produce predictive rate trajectories, 5D vessel recommendations, and carbon audits.</p>

  <div class="diagram-box">
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
  </div>

  <h2 class="section-title">7. Step-by-Step Pipeline Mechanics</h2>

  <div class="flow-card">
    <h4>Pipeline 1: Geodesic & Hydrodynamic Distance Resolution</h4>
    <p><strong>Files Involved:</strong> <code>src/App.tsx</code> &rarr; <code>python_engine/c_cpp_bridge.py</code> &rarr; <code>c_cpp_engine/maritime_math.dll</code></p>
    <ul>
      <li><strong>Input:</strong> Origin and Destination coordinates extracted from port catalog.</li>
      <li><strong>Execution:</strong> C11 compiled <code>calculate_haversine_distance()</code> and <code>calculate_initial_bearing()</code> execute Great-Circle math in &lt; 2 microseconds.</li>
      <li><strong>Output:</strong> Exact Nautical Mile distance (NM), voyage steaming days, and initial forward heading.</li>
    </ul>
  </div>

  <div class="flow-card">
    <h4>Pipeline 2: KAVACH Meteorological & Oceanic Risk Scoring</h4>
    <p><strong>Files Involved:</strong> <code>python_engine/weather_kavach.py</code> &rarr; <code>src/components/sagarsetu/KAVACHWeatherCard.tsx</code></p>
    <ul>
      <li><strong>Input:</strong> 3-point voyage waypoints (Origin Port, Transit Sea Lane, Destination Port).</li>
      <li><strong>Execution:</strong> Evaluates wave swell height, wind velocity, and barometric depression using the composite equation: <code>Risk = 25% Origin + 50% Route + 25% Destination</code>.</li>
      <li><strong>Output:</strong> Weather risk score (0–100%), adverse sea-state friction coefficient, and weather insurance surcharges ($/MT).</li>
    </ul>
  </div>

  <div class="flow-card">
    <h4>Pipeline 3: 5-Dimensional Multi-Factor Vessel Optimizer</h4>
    <p><strong>Files Involved:</strong> <code>c_cpp_engine/freight_optimizer.cpp</code> &harr; <code>src/App.tsx</code></p>
    <ul>
      <li><strong>Input:</strong> Cargo batch quantity, 10 bulk carrier class profiles, port limiting drafts, KAVACH weather coefficient.</li>
      <li><strong>Execution:</strong> Evaluates all 10 bulk carrier classes against Draft feasibility, Cargo batch consolidation, Weather seakeeping bonus, Gear fit (4x30t cranes), and Net Savings.</li>
      <li><strong>Output:</strong> Recommended hull class, multi-voyage consolidation strategy, and all-in net savings against Baltic benchmarks.</li>
    </ul>
  </div>

  <div class="flow-card">
    <h4>Pipeline 4: IMO MARPOL Annex VI Carbon & CII Accounting</h4>
    <p><strong>Files Involved:</strong> <code>python_engine/carbon_cii.py</code> &rarr; <code>src/components/sagarsetu/GreenFreightCarbon.tsx</code></p>
    <ul>
      <li><strong>Input:</strong> Vessel engine fuel burn profile (32.4 MT/day Capesize vs 26.8 Panamax) and total steaming days.</li>
      <li><strong>Execution:</strong> Multiplies total fuel consumption by IMO MARPOL standard emission factor (3.114 t CO₂ / t VLSFO).</li>
      <li><strong>Output:</strong> Scope-3 voyage CO₂ footprint, Carbon Intensity Indicator grade (Class A–E), and Green Score (0–100).</li>
    </ul>
  </div>

  <div class="footer-note">
    <strong>Nautilus Logistics AI &copy; 2026.</strong> Official Technical Architecture & Codebase Explanation Report. All rights reserved.
  </div>

</body>
</html>
"""

HTML_PATH = r"C:\Users\HP\OneDrive\Projects\Nautilus Logistics AI\codebase_architecture_doc.html"
PDF_PATH = r"C:\Users\HP\OneDrive\Projects\Nautilus Logistics AI\Nautilus_Logistics_AI_Codebase_and_Data_Flow_Architecture.pdf"
ROOT_PDF_PATH = r"C:\Users\HP\OneDrive\Projects\Nautilus_Logistics_AI_Codebase_and_Data_Flow_Architecture.pdf"

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"[SUCCESS] Wrote HTML template: {HTML_PATH}")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={PDF_PATH}",
    HTML_PATH
]

print(f"[INFO] Compiling PDF via Edge Headless...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0 and os.path.exists(PDF_PATH):
    # Also copy to root projects folder
    import shutil
    shutil.copy2(PDF_PATH, ROOT_PDF_PATH)
    pdf_size_kb = os.path.getsize(PDF_PATH) / 1024
    print(f"[SUCCESS] Generated PDF: {PDF_PATH} ({pdf_size_kb:.1f} KB)")
    print(f"[SUCCESS] Copied to Root: {ROOT_PDF_PATH}")
else:
    print(f"[ERROR] PDF generation failed: {res.stderr}")
