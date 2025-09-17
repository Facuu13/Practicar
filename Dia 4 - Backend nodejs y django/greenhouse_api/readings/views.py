from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Avg
from .models import Reading

# GET /latest/<device_id>
@api_view(['GET'])
def latest_reading(request, device_id):
    obj = (Reading.objects
           .filter(device_id__iexact=device_id)
           .order_by('-ts_utc')
           .first())
    if not obj:
        return Response({"error": "no data"}, status=404)
    return Response({
        "id": obj.id,
        "device_id": obj.device_id,
        "ts_utc": obj.ts_utc.isoformat(),
        "temp_c": float(obj.temp_c),
        "hum_pct": float(obj.hum_pct),
    })

# GET /average/<device_id>
@api_view(['GET'])
def average_reading(request, device_id):
    qs = Reading.objects.filter(device_id__iexact=device_id)
    if not qs.exists():
        return Response({"error": "no data"}, status=404)

    agg = qs.aggregate(avg_temp=Avg('temp_c'), avg_hum=Avg('hum_pct'))
    return Response({
        "device_id": device_id,
        "avg_temp_c": round(float(agg['avg_temp']), 2),
        "avg_hum_pct": round(float(agg['avg_hum']), 2),
        "count": qs.count(),
    })
