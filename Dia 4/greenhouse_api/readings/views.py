from rest_framework.response import Response
from rest_framework.decorators import api_view

# Datos simulados (como en Node.js)
READINGS = [
    {"device_id": "dev001", "ts_utc": "2024-06-01T10:00:00Z", "temp_c": 22.5, "hum_pct": 45.0},
    {"device_id": "dev001", "ts_utc": "2024-06-01T11:00:00Z", "temp_c": 23.0, "hum_pct": 50.0},
    {"device_id": "dev001", "ts_utc": "2024-06-01T12:00:00Z", "temp_c": 24.0, "hum_pct": 55.0},
    {"device_id": "dev001", "ts_utc": "2024-06-01T13:00:00Z", "temp_c": 25.5, "hum_pct": 60.0},
    {"device_id": "dev002", "ts_utc": "2024-06-01T12:05:00Z", "temp_c": 21.1, "hum_pct": 48.0},
]

# GET /latest/<device_id>
@api_view(['GET'])
def latest_reading(request, device_id):
    data = [r for r in READINGS if r["device_id"].lower() == device_id.lower()]
    if not data:
        return Response({"error": "no data"}, status=404)
    # ordenar por ts_utc descendente (string ISO se ordena bien)
    data = sorted(data, key=lambda r: r["ts_utc"], reverse=True)
    return Response(data[0])

# GET /average/<device_id>
@api_view(['GET'])
def average_reading(request, device_id):
    data = [r for r in READINGS if r["device_id"].lower() == device_id.lower()]
    if not data:
        return Response({"error": "no data"}, status=404)
    avg_temp = sum(r["temp_c"] for r in data) / len(data)
    avg_hum = sum(r["hum_pct"] for r in data) / len(data)
    return Response({
        "device_id": device_id,
        "avg_temp_c": round(avg_temp, 2),
        "avg_hum_pct": round(avg_hum, 2),
        "count": len(data),
    })
