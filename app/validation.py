from fastapi import HTTPException

def validate_lat_lon(lat, lon):
    if lat < -90 or lat > 90:
        raise HTTPException(status_code=400, detail="Latitude must be between -90 and 90")
    if lon < -180 or lon > 180:
        raise HTTPException(status_code=400, detail="Longitude must be between -180 and 180")


def ensure_results(rows):
    if not rows:
        raise HTTPException(status_code=404, detail="No articles found for this query")
