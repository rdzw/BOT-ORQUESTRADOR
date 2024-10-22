$exclude = @("venv", "bot_user_name.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_user_name.zip" -Force