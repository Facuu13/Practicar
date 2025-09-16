const express = require("express"); // importamos express
const app = express(); // creamos la app
const PORT = process.env.PORT || 3000; // puerto

// Datos simulados (en memoria)
const readings = [
  { device_id: "dev001", ts_utc: "2024-06-01T10:00:00Z", temp_c: 22.5, hum_pct: 45.0 },
  { device_id: "dev001", ts_utc: "2024-06-01T11:00:00Z", temp_c: 23.0, hum_pct: 50.0 },
  { device_id: "dev001", ts_utc: "2024-06-01T12:00:00Z", temp_c: 24.0, hum_pct: 55.0 },
  { device_id: "dev001", ts_utc: "2024-06-01T13:00:00Z", temp_c: 25.5, hum_pct: 60.0 },
  { device_id: "dev001", ts_utc: "2024-06-01T14:00:00Z", temp_c: 26.0, hum_pct: 65.0 },
  { device_id: "dev001", ts_utc: "2024-06-01T15:00:00Z", temp_c: 27.0, hum_pct: 70.0 },
  { device_id: "dev001", ts_utc: "2024-06-01T16:00:00Z", temp_c: 28.5, hum_pct: 75.0 },
  { device_id: "dev001", ts_utc: "2024-06-01T17:00:00Z", temp_c: 29.0, hum_pct: 80.0 },
  { device_id: "dev001", ts_utc: "2024-06-01T18:00:00Z", temp_c: 30.0, hum_pct: 85.0 },
  { device_id: "dev002", ts_utc: "2024-06-01T18:05:00Z", temp_c: 21.2, hum_pct: 48.0 },
];

// Helpers
function normId(id) {
  return String(id || "").trim().toLowerCase(); // normaliza device_id saca espacios y pasa a minúsculas
}

// Filtra lecturas por device_id (case insensitive)
function readingsByDevice(id) {
  const did = normId(id); // normaliza id
  return readings.filter(r => r.device_id.toLowerCase() === did); // filtra
}

// Ordena por ts_utc descendente (más nuevo primero)
function sortByTsDesc(arr) {
  return [...arr].sort((a, b) => new Date(b.ts_utc) - new Date(a.ts_utc)); // copia y ordena
}

app.get("/", (_req, res) => {
  res.json({ ok: true });
});

// Endpoint: devuelve la última lectura de un device
app.get("/latest/:device_id", (req, res) => {
  const data = sortByTsDesc(readingsByDevice(req.params.device_id));
  if (data.length === 0) return res.status(404).json({ error: "no data" });
  res.json(data[0]); // el más nuevo
});

// Endpoint: devuelve la media de lecturas de un device
app.get("/average/:device_id", (req, res) => {
  const data = readingsByDevice(req.params.device_id);
  if (data.length === 0) return res.status(404).json({ error: "no data" });

  const sumT = data.reduce((acc, r) => acc + Number(r.temp_c), 0);
  const sumH = data.reduce((acc, r) => acc + Number(r.hum_pct), 0);
  const avgT = sumT / data.length;
  const avgH = sumH / data.length;

  res.json({
    device_id: normId(req.params.device_id),
    avg_temp_c: Number(avgT.toFixed(2)),
    avg_hum_pct: Number(avgH.toFixed(2)),
    count: data.length,
  });
});

// Endpoint: devuelve las últimas N lecturas de un device
app.get("/all/:device_id", (req, res) => {
  const limit = Math.max(1, Math.min(100, Number(req.query.limit) || 5));
  const data = sortByTsDesc(readingsByDevice(req.params.device_id)).slice(0, limit);
  if (data.length === 0) return res.status(404).json({ error: "no data" });

  res.json({
    device_id: normId(req.params.device_id),
    count: data.length,
    items: data
  });
});

app.use((_req, res) => res.status(404).json({ error: "not found" }));


app.listen(PORT, () => {
  console.log(`API listening on http://localhost:${PORT}`);
});
