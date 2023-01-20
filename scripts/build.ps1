# Define the parameters
param($source, $build_script)

# Create the new script file
New-Item -Path $build_script -ItemType File -Force

# Recursively loop through the source directory and create the commands to recreate the files and subfolders
$commands = Get-ChildItem -Path $source -Recurse | ForEach-Object {
    if ($_.PSIsContainer) {
        "New-Item -Path `"$($_.Parent.FullName)`" -ItemType Directory -Name `"$($_.Name)`""
    }
    else {
        "New-Item -Path `"$($_.DirectoryName)`" -Name `"$($_.Name)`"`n`"`"Write-Output `"`"$(Get-Content $_.FullName)`"`" > `"$($_.FullName)`""
    }
}

# Write the commands to the new script file
$commands | Add-Content $build_script
