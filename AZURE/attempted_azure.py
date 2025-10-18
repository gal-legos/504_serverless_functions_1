import json
import azure.functions as func
import logging


def main(req: func.HttpRequest) -> func.HttpResponse:
   logging.info("Processing HbA1c classification request.")


   # Try to get JSON body
   try:
       data = req.get_json()
   except ValueError:
       data = {}


   # Get hba1c from JSON or query parameters
   hba1c = data.get("hba1c") or req.params.get("hba1c")


   if hba1c is None:
       return func.HttpResponse(
           json.dumps({"error": "Parameter 'hba1c' is required."}, ensure_ascii=False),
           mimetype="application/json",
           status_code=400
       )


   try:
       hba1c_val = float(hba1c)
   except (TypeError, ValueError):
       return func.HttpResponse(
           json.dumps({"error": "'hba1c' must be a number."}, ensure_ascii=False),
           mimetype="application/json",
           status_code=400
       )


   # Determine category
   if hba1c_val < 5.7:
       category = "Normal"
       status = "normal"
   elif 5.7 <= hba1c_val < 6.5:
       category = "Prediabetes"
       status = "elevated"
   else:
       category = "Diabetes"
       status = "high"


   payload = {
       "hba1c": hba1c_val,
       "status": status,
       "category": category,
       "guidelines": {
           "Normal": "< 5.7%",
           "Prediabetes": "5.7–6.4%",
           "Diabetes": "≥ 6.5%"
       }
   }


   return func.HttpResponse(       json.dumps(payload, ensure_ascii=False),
       mimetype="application/json",
       status_code=200
   )
