import io
import json
from fdk import response


def handler(ctx, data: io.BytesIO = None):
   try:
       # Try to parse incoming JSON
       body = json.loads(data.getvalue())
   except Exception:
       body = {}


   # Get hba1c from JSON body
   hba1c = body.get("hba1c")


   if hba1c is None:
       return response.Response(
           ctx,
           response_data=json.dumps({
               "error": "Parameter 'hba1c' is required."
           }),
           headers={"Content-Type": "application/json"},
           status_code=400
       )


   # Validate input
   try:
       hba1c_val = float(hba1c)
   except (TypeError, ValueError):
       return response.Response(
           ctx,
           response_data=json.dumps({
               "error": "'hba1c' must be a number."
           }),
           headers={"Content-Type": "application/json"},
           status_code=400
       )


   # Classification logic based on ADA guidelines
   if hba1c_val < 5.7:
       category = "Normal"
       status = "normal"
   elif 5.7 <= hba1c_val < 6.5:
       category = "Prediabetes"
       status = "elevated"
   else:
       category = "Diabetes"
       status = "high"


   # Construct response payload
   payload = {
       "hba1c": hba1c_val,
       "status": status,
       "category": category,
       "guidelines": {
           "Normal": "< 5.7%",
           "Prediabetes": "5.7–6.4%",
           "Diabetes": "≥ 6.5%"
       },
       "reference": "American Diabetes Association. Standards of Medical Care in Diabetes—2023."
   }


   return response.Response(
       ctx,
       response_data=json.dumps(payload),
       headers={"Content-Type": "application/json"},
       status_code=200
   )
