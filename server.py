from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import csv
import json

app = FastAPI()

# Atļauj piekļuvi no pārlūkprogrammas
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/export")
async def export_csv(data: list):
    csv_filename = "kopigi_dati.csv"

    with open(csv_filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Galvenes daļa
        writer.writerow(data[0].keys())
        
        # ieraksta datus
        for row in data:
            writer.writerow(row.values())

    # atver failu un nosūta to lejupielādei lietoājam
    with open(csv_filename, "rb") as f:
        csv_content = f.read()

    return Response(content=csv_content, media_type="text/csv", headers={"Content-Disposition": f"attachment; filename={csv_filename}"})

# Lai palaistu serveri: uvicorn server:app --reload --port 5500 (man strādā ar to :) s)
