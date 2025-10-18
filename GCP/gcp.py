import json
import functions_framework


@functions_framework.http
def hello_http(request):
   """
   HTTP Cloud Function that classifies HbA1c levels.
   Expects JSON or query param with 'hba1c'.
   Returns a JSON classification.
   """
   # Prefer JSON body; fall back to query parameters
   data = request.get_json(silent=True) or {}
   args = request.args or {}


   hba1c = data.get("hba1c", args.get("hba1c"))


   # Presence check
   if hba1c is None:
       return json.dumps({"error": "Parameter 'hba1c' is required."}, ensure_ascii=False), {"Content-Type": "application/json"}


   # Type/convert check
   try:
       hba1c_val = float(hba1c)
   except (TypeError, ValueError):
       return json.dumps({"error": "'hba1c' must be a number."}, ensure_ascii=False), {"Content-Type": "application/json"}


   # Classification
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


   return json.dumps(payload, ensure_ascii=False), {"Content-Type": "application/json"}


