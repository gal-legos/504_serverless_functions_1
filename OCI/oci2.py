import io
import json
from func import handler 


# Fake OCI context for local testing
class FakeCtx:
   def SetResponseHeaders(self, headers, status_code):
       pass  # ignore for local testing


# List of test inputs
test_inputs = [
   {"hba1c": 5.4},  # Normal
   {"hba1c": 6.0},  # Prediabetes
   {"hba1c": 6.8}   # Diabetes
]


for input_data in test_inputs:
   data = io.BytesIO(json.dumps(input_data).encode())
   resp = handler(FakeCtx(), data)


   # Use resp.body() if it’s callable
   if callable(getattr(resp, "body", None)):
       output = resp.body()
   else:
       output = resp


   # Convert bytes to string if necessary
   if isinstance(output, bytes):
       output = output.decode()


   # Pretty-print JSON
   print(json.dumps(json.loads(output), indent=4))
   print("-" * 50)
