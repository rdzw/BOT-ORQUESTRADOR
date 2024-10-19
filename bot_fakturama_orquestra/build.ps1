$exclude = @("venv", "bot_fakturama_orquestra.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_fakturama_orquestra.zip" -Force