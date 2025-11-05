const backendUrl = "http://127.0.0.1:8000/api/stop";
const stopsUrl = "http://127.0.0.1:8000/api/stops";
const pingUrl = "http://127.0.0.1:8000/api/ping";


const stopSelect = document.getElementById("stopSelect");
const label = document.getElementById("stopSelectLabel");
const departuresContainer = document.getElementById("departuresContainer");
const updateMsg = document.getElementById("updateMsg");
const departuresTitle = document.getElementById("departuresTitle");
const backendWarning = document.getElementById("backendWarning");


const lineColors = {
	U1: "#E20613",
	U2: "#A762A4",
	U3: "#EF7C00",
	U4: "#029540",
	U5: "#3F8D95", // one step ahead ;)
	U6: "#9C6830",
	tram: "#c4121a",
	bus: "#0a295d",
	wlb: "#005794",
};

function getLineColor(line) {
	if (line.startsWith("WLB")) return lineColors.wlb;
	if (line.startsWith("U")) return lineColors[line] || "#666";
	if (/^\d+$/.test(line) || ["D", "E", "O"].some(p => line.startsWith(p))) return lineColors.tram;
	return lineColors.bus;
}

function formatDate(ts) {
	const d = new Date(ts);
	return d.toLocaleString("de-AT", {
		weekday: "short",
		hour: "2-digit",
		minute: "2-digit"
	});
}

let stopGroups = [];

async function loadStops() {
	try {
		const res = await fetch(stopsUrl);
		stopGroups = await res.json();

		stopGroups.sort((a, b) => a.name.localeCompare(b.name, "de-AT"));

		populateStops();
		if (stopGroups.length > 0) fetchDeparturesForStation(0);
	} catch (err) {
		console.error("Error loading stops JSON", err);
	}
}

function populateStops() {
	stopSelect.innerHTML = "";
	stopGroups.forEach((group, idx) => {
		const option = document.createElement("option");
		option.value = idx;
		option.textContent = group.name;
		stopSelect.appendChild(option);
	});
}



async function fetchDeparturesForStation(groupIndex) {
	updateMsg.style.visibility = "visible";
	const group = stopGroups[groupIndex];
	const allDeps = [];
	let traffic = [];

	for (const stopId of group.stops) {
		try {
			const res = await fetch(`${backendUrl}/${stopId}`);
			if (!res.ok) continue;
			const data = await res.json();

			allDeps.push(...data.departures);

			if (data.traffic && data.traffic.length > 0) {
				traffic.push(...data.traffic);
			}
		} catch (err) {
			console.warn("Error fetching stop:", stopId, err);
		}
	}

	// Sort by time
	allDeps.sort((a, b) => a.countdown - b.countdown);

	displayDepartures({
		departures: allDeps,
		traffic: traffic
	});
}

function displayDepartures(data) {
	const trafficContainer = document.getElementById("traffic");

	departuresContainer.innerHTML = data.departures.map(dep => {
		const color = getLineColor(dep.line);
		const wheelchair = dep.barrier_free ? ` <span class="accessibility-icon" alt="Barrier Free">♿</span>` : "";

		updateMsg.style.visibility = "hidden";

		return `
    <tr>
      <td><span class="line-badge" style="background:${color};">${dep.line}</span></td>
      <td>Direction ${dep.direction.trim()}${wheelchair}</td>
      <td><span class="countdown">${dep.countdown}</span> min</td>
      <td>${new Date(dep.planned).toLocaleTimeString("de-AT", { hour: "2-digit", minute: "2-digit" })}</td>
    </tr>
  `;
	}).join("");


	if (data.traffic.length > 0) {
		trafficContainer.innerHTML = data.traffic.map(t => `
      <div class="traffic-item">
        ⚠️ <strong>${t.msg || ""}</strong><br>
        <small>${"Start: " + formatDate(t.start) || ""}</small><br>
        <small>${"End: " + formatDate(t.end) || ""}</small><br>
        <small><i>${"ID: " + t.type || ""}</i></small>
      </div>
    `).join("<br>");
	} else {
		trafficContainer.innerHTML = `
      <div class="traffic-item no-traffic">
        ✅ <strong>No current messages</strong>   
      </div>`;
	}
}

document.addEventListener('keydown', function(event) {
	if (event.key === 'e') {
		event.preventDefault();
		if (stopSelect.style.visibility === 'hidden') {
			stopSelect.style.visibility = 'visible';
			label.style.visibility = 'visible';
		} else {
			stopSelect.style.visibility = 'hidden';
			label.style.visibility = 'hidden';
		}
	}
});


let refreshInterval = null;

function startAutoRefresh() {
	if (refreshInterval) clearInterval(refreshInterval);
	refreshInterval = setInterval(() => {
		const selected = stopSelect.value;
		if (selected !== null && selected !== undefined) {
			fetchDeparturesForStation(selected);
		}
	}, 30000); // refresh every 30 seconds, change this to adjust interval - Reminder: Do not go below 15000!
}

async function checkBackend() {
	try {
		const res = await fetch(pingUrl, {
			cache: "no-store"
		});
		if (!res.ok) throw new Error();
		backendWarning.style.display = "none";
		return true;
	} catch {
		backendWarning.style.display = "block";
		updateMsg.style.display = "none";
		return false;
	}
}


function doTime() {
	var str = "";
	var now = new Date();
	str += now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds();
	document.getElementById("departuresTitle").innerHTML = `Live Departures - ${str}`;
}

setInterval(doTime, 1000);
setInterval(checkBackend, 5000);

loadStops().then(() => {
	startAutoRefresh();
});

stopSelect.addEventListener("change", e => {
	fetchDeparturesForStation(e.target.value);
	startAutoRefresh();
});