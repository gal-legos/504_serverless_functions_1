import requests
import json


#removed url because of github security policies

# Example test cases
test_inputs = [
   {"hba1c": 5.4},   # Normal
]


for i, data in enumerate(test_inputs, start=1):
   print(f"\nTest case {i}: {data}")
   r = requests.post(url, json=data)
  
   try:
       resp = r.json()  # Parse JSON response
       if "error" in resp:
           print("Error:", resp["error"])
       else:
           # Pretty-print JSON (this keeps your Unicode characters visible)
           print(json.dumps(resp, indent=2, ensure_ascii=False))
   except Exception as e:
       print("Failed to parse JSON:", e)
       print("Raw response:", r.text)