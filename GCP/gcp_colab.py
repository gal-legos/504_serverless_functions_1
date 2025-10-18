import requests
import json


url = "ttps://testing504-377218309260.europe-west1.run.app"
#remove the first "h" in "https" to avoid accidental requests during testing and possible errors in github

# Example test cases
test_inputs = [
   {"hba1c": 10},   # Normal
]


for i, data in enumerate(test_inputs, start=1):
   print(f"\nTest case {i}: {data}")
   r = requests.post(url, json=data)
  
   try:
       resp = r.json()  # Parse JSON response
       if "error" in resp:
           print("Error:", resp["error"])
       else:
           print(json.dumps(resp, indent=2, ensure_ascii=False))
   except Exception as e:
       print("Failed to parse JSON:", e)
       print("Raw response:", r.text)