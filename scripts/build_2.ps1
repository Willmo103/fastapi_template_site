# param(
#     [string]$source,
#     [string]$build_script
# )

# # Check if source directory exists
# if (!(Test-Path $source)) {
#     Write-Output "Error: Source directory does not exist."
#     exit
# }

# # Create build script
# New-Item -ItemType File -Path $build_script -Force

# # Add command to set the destination path in the build script
# Add-Content $build_script "param([string] `$dest)"

# # Get all files and directories in source directory
# $items = Get-ChildItem -Path $source -Recurse
# $dir = $source
# foreach ($item in $items) {
#     Write-Output $dir
#     if ($item.PSIsContainer -eq $false) {
#         $ext = [IO.Path]::GetExtension($item.FullName)
#         $fileName = [IO.Path]::GetFileName($item.FullName)
#         # Check if file is text or code file
#         if ($ext -eq ".txt" -or $ext -eq ".py" -or $ext -eq ".ps1" -or $ext -eq ".js" -or $ext -eq ".html" -or $ext -eq ".css" -or $ext -eq ".md") {
#             # Add command to create file and write its content to build script
#             Add-Content $build_script "New-Item -ItemType File -Path "$fileName" -Force"
#             Add-Content $build_script "Write-Output ""$(Get-Content $item.FullName -Raw)"" | Out-File "$fileName""
#         }
#     }
#     else {
#         # Add command to create directory to build script
#         $dir = $item.Name
#         Add-Content $build_script "New-Item -ItemType Directory -Path "$destinationPath""
#     }
# }

param(
    [string]$source,
    [string]$build_script
)

# Check if source directory exists
if (!(Test-Path $source)) {
    Write-Output "Error: Source directory does not exist."
    exit
}

# Create build script
New-Item -ItemType File -Path $build_script -Force

# Add command to set the destination path in the build script
Add-Content $build_script "param([string] `$dest)"

# Get all files and directories in source directory
$items = Get-ChildItem -Path $source -Recurse
$dir = $source
foreach ($item in $items) {
    Write-Output $dir
    if ($item.PSIsContainer -eq $false) {
        $ext = [IO.Path]::GetExtension($item.FullName)
        $fileName = [IO.Path]::GetFileName($item.FullName)
        # Check if file is text or code file
        if ($ext -eq ".txt" -or $ext -eq ".py" -or $ext -eq ".ps1" -or $ext -eq ".js" -or $ext -eq ".html" -or $ext -eq ".css" -or $ext -eq ".md") {
            # Add command to create file and write its content to build script
            Add-Content $build_script "New-Item -ItemType File -Path "$fileName" -Force"
            Add-Content $build_script "Write-Output ""$(Get-Content $item.FullName -Raw)"" | Out-File "$fileName""
        }
    }
    else {
        # Add command to create directory to build script
        $dir = $item.Name
        Add-Content $build_script "New-Item -ItemType Directory -Path "$destinationPath""
    }
}
