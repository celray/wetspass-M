# WetSPASS-M

WetSPASS-M is a spatially distributed water balance model for simulating groundwater recharge, soil water storage, evapotranspiration, runoff, and interception at monthly, seasonal, and annual scales.
Version 1.3 adds sensitivity analysis capability to the UI.

## Overview

WetSPASS is a physically-based, spatially distributed hydrological model that calculates the long-term average spatial patterns of surface runoff, actual evapotranspiration, and groundwater recharge.

## Key Features

- **Spatially Distributed**: Uses gridded input data (ESRI ASCII format)
- **Multi-temporal**: Supports monthly, seasonal, and annual simulations
- **Comprehensive Water Balance**: Calculates all major hydrological components
- **User-Friendly GUI**: Graphical interface for model setup and parameter adjustment
- **Flexible Parameterization**: Land use and soil parameters can be modified through the interface

## Model Components

### Hydrological Processes

1. **Interception**: Rainfall interception by vegetation canopy
2. **Evapotranspiration**: 
   - Actual evapotranspiration using Penman-Monteith equation
   - Separate calculation of soil evaporation and plant transpiration
   - Groundwater evapotranspiration
3. **Surface Runoff**: 
   - Runoff from vegetated, bare soil, impervious, and open water areas
   - Uses runoff coefficient method with intensity corrections
4. **Groundwater Recharge**: Net downward water flux to groundwater
5. **Soil Water Storage**: Dynamic soil moisture accounting
6. **Snow Processes** (optional): Snow accumulation and melt using degree-day method

### Input Requirements

#### Meteorological Data (Monthly)
- Precipitation (mm)
- Potential evapotranspiration (mm)
- Temperature (°C)
- Wind speed (m/s)
- Groundwater depth (m)
- Snow cover (optional)

#### Spatial Data (ESRI ASCII Grid Format)
- Digital Elevation Model (DEM)
- Land use classification
- Soil type classification  
- Slope map

#### Lookup Tables
- **Landuses.tbl**: Land use parameters (runoff coefficients, vegetation characteristics, etc.)
- **Soil.tbl**: Soil hydraulic properties (field capacity, wilting point, etc.)
- **RainyDaysPerMonth.tbl**: Number of rainy days per month
- **DegreeDaysPerMonth.tbl**: Degree days for snow melt calculation

#### Fraction Maps (Optional)
- Vegetation area fraction (`veg_area.asc`)
- Bare soil area fraction (`bare_area.asc`)  
- Impervious area fraction (`imp_area.asc`)
- Open water area fraction (`ow_area.asc`)

## Model Parameters

The model uses several calibration parameters:

- **a**: Interception coefficient
- **α (alpha)**: Evapotranspiration parameter  
- **wSlope**: Slope weight factor for runoff
- **wLanduse**: Land use weight factor for runoff
- **wSoil**: Soil weight factor for runoff
- **x**: Runoff parameter
- **LP**: Limiting factor for evapotranspiration
- **β (Beta)**: Surface runoff parameter
- **Contribution**: Base flow contribution parameter

### Snow Parameters (when enabled)
- **Base Temperature**: Threshold temperature for snow/rain
- **Melt Factor**: Degree-day factor for snow melt
- **Snow Density**: Snow density for depth calculation

## Installation

The model comes with an installer (`WetSPASS-v[version].exe`) that sets up:
- Main application (`WetSpass-M.exe`)
- Map viewer (`MapViewer.exe`)
- Mean calculator utility (`MeanCallc.exe`)
- Sample data for testing
- Required .NET Framework dependencies

### System Requirements
- Windows operating system
- .NET Framework 4.0 or higher
- NSIS (Nullsoft Scriptable Install System) for building installers

## Getting Started

1. **Installation**: Run the installer and follow the setup wizard
2. **Sample Data**: Use the provided sample data in the `SampleData` folder to familiarize yourself with the model
3. **Data Preparation**: Prepare your input maps and tables according to the required formats
4. **Model Setup**: Use the GUI to configure input paths, parameters, and output options
5. **Simulation**: Run the model and analyze results using the built-in map viewer

## Output Files

The model generates the following outputs:
- **Cell_evapotranspiration**: Actual evapotranspiration (mm)
- **Cell_runoff**: Surface runoff (mm)
- **Recharge**: Groundwater recharge (mm)
- **Interception**: Rainfall interception (mm)
- **soilwater_storage**: Soil water storage (mm)
- Additional component outputs (transpiration, soil evaporation, etc.)
- **Simulation log**: Text file with water balance summary

## Development

### Building the Installer

Use the provided Python script to build the installer:

```bash
python installStack/scripts/makeInstallFiles.py [version_number e.g. 1.3.0.0]
```

This script:
- Generates NSIS installer script
- Creates installer executable
- Sets up proper file associations and registry entries

### Project Structure

```
WetSpass-M/
├── WetSpass-M.exe              # Main application
├── MapViewer.exe               # Map visualization tool
├── MeanCallc.exe              # Mean calculation utility
├── SampleData/                # Sample input data
│   ├── Inputs/
│   │   ├── Maps/              # Input raster maps
│   │   ├── Tables/            # Parameter lookup tables
│   │   └── Fractions/         # Land cover fraction maps
│   └── ...
├── WetSpass-M/
│   ├── Wetspass-M.py         # Main model implementation
│   └── sensitivity_api.exe   # Sensitivity analysis tool
└── installStack/
    └── scripts/
        └── makeInstallFiles.py # Installer build script
```

## Version Information

- **Version**: M (Monthly)
- **Date**: January 18, 2025

## License and Usage

This software is provided for research and educational purposes. Users are encouraged to discuss their research results, experiences, and problems with the authors.

## Contact

For questions, support, or collaboration opportunities, please contact HYDR team at the Vrije Universiteit Brussel.

---

*WetSPASS has been applied successfully in various regions in Belgium and other international locations for groundwater recharge assessment and water resource management.*
