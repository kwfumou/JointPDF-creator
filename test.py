from flask import request

if request.headers.getlist("X-Forwarded-For"):
   ip = request.headers.getlist("X-Forwarded-For")[0]
else:
   ip = request.remote_addr

print(ip)