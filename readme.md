# Wiener Linien Departure Board

## Introduction

A small project that uses the OGD Realtime API from Vienna's public transport provider, **Wiener Linien**. It automatically fetches current departures from a selected station and displays them in an HTML frontend. Also included are three Python scripts that generate a JSON file containing all IDs for each station using publicly available CSV data. If you want to build your own departure display at home, this is for you!

![Image displaying the frontend](/project/img1.png)

## Description

### About the API

Wiener Linien provides a free, open API for fetching realtime departure information and traffic data. To use the API, you need to provide the **RBL ID** (*Rechnergesteuertes Betriebs-Leitsystem*, "computer-controlled service management system"). Each RBL ID corresponds to:

1. A specific station or stop  
2. A specific line  
3. A specific direction

For example, ID **4903** refers to:

1. The station **Rochusgasse**
2. The line **U3**
3. The direction **Ottakring**

### ID sources and compilation

Matching RBL IDs with their station names can be tricky. We can download four CSV files from **data.gv.at**:

- `wienerlinien-ogd-fahrwegverläufe.csv`
- `wienerlinien-ogd-haltepunkte.csv`
- `wienerlinien-ogd-haltestellen.csv`
- `wienerlinien-ogd-linien.csv`

To build accurate name–ID mappings, these files need to be merged. This project includes three Python scripts:

- `extract_raw.py`  
  First version, deprecated but included for reference
- `extract.py`  
  Second version, outputs cleaned data
- `group_stops.py`  
  Groups entries with the same name but different IDs, because one station usually has several IDs for different lines and directions

These scripts generate `stops_grouped.json`, which acts as a registry containing all station IDs. The frontend uses this registry to list stations. When a user selects a station, the corresponding IDs are fetched and passed to the API, and the results are displayed.

### Quirk with multiple entries

There may still be multiple entries for what appears to be the same station. Bus and tram stops often have different internal names than subway stations. Despite the “U” appearing in the name for some entries, those may refer to tram/bus stops announcing a subway connection rather than the subway platforms themselves. Generally, the first entries are subway stops, and entries containing “S”, “U”, or “<>” tend to be tram/bus entries. This is still a work in progress.

### Backend

The backend uses the `requests` library and FastAPI to serve data to the frontend. Note that Wiener Linien’s fair-use guidelines recommend a minimum polling interval of **15 seconds**. The default here is **30 seconds**, but large stations (e.g., *Karlsplatz*) may still cause timeouts. If you encounter missing data or slow responses, try increasing the interval to **60 seconds**.

To change this, edit the `startAutoRefresh()` function in `script.js` and change the timeout value from `30000` to `60000` milliseconds.

More details about the API can be found in `project/api_description.md`.

### Frontend

The frontend (`frontend/`) consists of vanilla HTML, CSS, and JavaScript. It calls the backend, which in turn queries the OGD API. Station names and IDs are fetched from the backend, and the frontend periodically pings the backend to avoid outdated information.

## Setup

All software in this repo *should* work on any OS. If something doesn’t work, feel free to [contact me](https://tk-dev-software.com#contact).

1. Clone the repo and install the dependencies from `requirements.txt`
2. Download the 4 CSV files from [data.gv.at](https://www.data.gv.at/datasets/522d3045-0b37-48d0-b868-57c99726b1c4)  
   - "Distributionen" tab  
   - Download:
     - `wienerlinien-ogd-fahrwegverläufe.csv`
     - `wienerlinien-ogd-haltepunkte.csv`
     - `wienerlinien-ogd-haltestellen.csv`
     - `wienerlinien-ogd-linien.csv`
3. Move the files to `backend/data/`
4. In a terminal, `cd` to the `/data` folder
5. Run `py -m extract.py`
6. Run `py -m group_stops.py`
7. You should now have:
   - `stops_clean.json`
   - `stops_grouped.json`
8. `cd` back to `/backend`
9. Run `uvicorn main:app --reload`
10. Open `frontend/index.html` in your browser

You're all set!

![Image displaying the frontend](/project/img2.png)

## Usage

Select any station from the dropdown. Press `e` to hide it. You'll see `Updating...` above the table. Once data arrives, departures for the next ~70 minutes will appear. The table refreshes every 30 seconds.

To quit, press `CTRL+C` in the terminal, then close the browser tab.

## Tips and Tricks

- One entry can contain multiple subway lines or multiple tram/bus lines, but never both. If multiple entries exist, the first ones usually belong to the subway.
- If no data appears, check the terminal for `500 Internal Server Error`. Some IDs in the registry may not return data.
- Switching stations rapidly may overwhelm the API. If lines are missing, wait a moment and try again.
- When the dropdown is focused, you can type to search for station names.

## Links

[Data source for the CSV files - data.gv.at](https://www.data.gv.at/datasets/522d3045-0b37-48d0-b868-57c99726b1c4)

[Explanation what the RBL does - strassenbahnjournal.at](https://strassenbahnjournal.at/wiki/index.php?title=RBL)

[The API page - wienerlinien.at/ogd_realtime/](https://www.wienerlinien.at/ogd_realtime/)

[Official documentation for the API (German) - wienerlinien.at](https://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-echtzeitdaten-dokumentation.pdf)

[Information page about Open Data - wienerlinien.at](https://www.wienerlinien.at/open-data)

## License and Disclaimer

This project is released under the MIT License (see `license.md`). I do not own or provide any transport data, nor am I responsible for misuse of the API. Please follow the API fair-use guidelines.
