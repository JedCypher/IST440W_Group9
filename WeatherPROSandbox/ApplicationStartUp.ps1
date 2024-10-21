Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
cd "$env:USERPROFILE\PycharmProjects\WeatherPROSandbox"
.\.venv\Scripts\Activate
Start-Process powershell "python -m http.server --cgi 8090"
Start-Process "msedge.exe" "http://localhost:8090/Weathepro.html", "--inprivate"

