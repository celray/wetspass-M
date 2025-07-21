installer = """# Include MUI2 for a better interface
!include "MUI2.nsh"

!define versionString "{versionString}"

# Configuration for Modern UI
!define MUI_ABORTWARNING  ; Prompt the user if they try to cancel the installation
!define MUI_ICON "..\\WetSpass-M\\WetSpass-M\\wetspass-M.ico"
!define MUI_UNICON "..\\WetSpass-M\\WetSpass-M\\wetspass-M.ico"  ; Uninstaller icon
!define MUI_BRANDINGTEXT "WetSpass-M Installer"  ; Custom branding text



BrandingText "WETSPASS-M Installer" 

# Set up the pages
!insertmacro MUI_PAGE_INSTFILES

# Uninstaller pages (if needed)
!insertmacro MUI_UNPAGE_INSTFILES

# Uninstaller Title
!define MUI_UNWINDOWTITLE "WetSpass-M Uninstall"


# Define basic information about the installer
OutFile "Installers\\WetSPASS-v${{versionString}}.exe"
Name "WetSpass-M"
InstallDir "C:\\WetSpass-M"
Icon "..\\WetSpass-M\\WetSpass-M\\wetspass-M.ico"
RequestExecutionLevel user  ; Does not require admin rights
!define PRODUCT_NAME "WetSpass-M"

# Define installer properties
VIProductVersion "${{versionString}}.0"
VIAddVersionKey /LANG=1033 "ProductName" "WetSpass-M"
VIAddVersionKey /LANG=1033 "CompanyName" "Celray James & HYDR-VUB"
VIAddVersionKey /LANG=1033 "FileVersion" "${{versionString}}.0"
VIAddVersionKey /LANG=1033 "FileDescription" "Installer for WetSpass-M"
VIAddVersionKey /LANG=1033 "LegalCopyright" "Copyright © Celray James & HYDR-VUB {currentYear}"

Function DotNetMessage
    MessageBox MB_OK|MB_ICONINFORMATION ".NET 4.0 Runtime is needed to run this software. If you have not installed it, you can install it after this installation, otherwise, installation will continue. After the finish window, you will find WetSpass-M in Start Menu"
FunctionEnd

!define UNINSTALLER_KEY "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${{PRODUCT_NAME}}"

Function .onInit
    Call DotNetMessage
FunctionEnd

# Installer Sections
Section "Main Files" SEC01
  SetOutPath "$INSTDIR"  ; Set the output path to the installation directory

  # Add all files from the specified directory
  File /r "..\\WetSpass-M\\*.*"

  # Create registry entries for Add/Remove Programs
  WriteRegStr HKCU "${{UNINSTALLER_KEY}}" "DisplayName" "WetSpass-M"
  WriteRegStr HKCU "${{UNINSTALLER_KEY}}" "UninstallString" "$\\"$INSTDIR\\Uninstall.exe$\\""
  WriteRegStr HKCU "${{UNINSTALLER_KEY}}" "DisplayIcon" "$INSTDIR\\WetSpass-M\\wetspass-M.ico"
  WriteRegStr HKCU "${{UNINSTALLER_KEY}}" "DisplayVersion" "${{versionString}}"
  WriteRegStr HKCU "${{UNINSTALLER_KEY}}" "URLInfoAbout" "https://github.com/celray/WetSpass-M"
  WriteRegStr HKCU "${{UNINSTALLER_KEY}}" "Publisher" "Celray James & HYDR-VUB"
  WriteRegDWORD HKCU "${{UNINSTALLER_KEY}}" "NoModify" 1
  WriteRegDWORD HKCU "${{UNINSTALLER_KEY}}" "NoRepair" 1
  # Optional: set the estimated size of the installed program (in KB)
  WriteRegDWORD HKCU "${{UNINSTALLER_KEY}}" "EstimatedSize" 95700

  # Create a shortcut on the desktop and in the start menu
  CreateDirectory "$DESKTOP"
  CreateShortCut "$DESKTOP\\WetSpass-M.lnk" "$INSTDIR\\WetSpass-M.exe"
  CreateDirectory "$SMPROGRAMS\\WetSpass-M"
  CreateShortCut "$SMPROGRAMS\\WetSpass-M\\WetSpass-M.lnk" "$INSTDIR\\WetSpass-M.exe"

  # Write the uninstaller
  WriteUninstaller "$INSTDIR\\Uninstall.exe"
  # ExecShell "open" "$INSTDIR\\WetSpass-M.exe"
SectionEnd

# Uninstaller Sections
Section "Uninstall"
    ; First delete all files in the installation directory
    RMDir /r "$INSTDIR"

    ; Now attempt to remove the installation directory itself
    RMDir "$INSTDIR"

    ; Remove shortcuts
    Delete "$DESKTOP\\WetSpass-M.lnk"
    Delete "$SMPROGRAMS\\WetSpass-M\\WetSpass-M.lnk"
    RMDir "$SMPROGRAMS\\WetSpass-M"

    ; Remove registry keys for file association
    DeleteRegKey HKCR ".spt"
    DeleteRegKey HKCR "WetSpass.Project"

    ; Remove the uninstaller itself
    Delete "$INSTDIR\\Uninstall.exe"

    # Remove registry keys
    DeleteRegKey HKCU "${{UNINSTALLER_KEY}}"

SectionEnd
"""


import sys, os, shutil
import subprocess
from genericpath import exists
from ccfx import writeFile, deleteFile
import datetime

if len(sys.argv) < 2:
    print("Error: Please provide the version number")
    sys.exit()

version = sys.argv[1]

# function to run nsi script

# one level up from file directory
os.chdir(os.path.dirname(__file__))
os.chdir("../")


def runNSIScript(scriptPath, nsisPath):
    if not scriptPath.endswith('.nsi'):
        print("Error: scriptPath should be a .nsi file")
        return
    subprocess.run(f'"{nsisPath}" "{scriptPath}"', shell=True)

mainInstallerScript = os.path.join(os.path.dirname(__file__), "../tmp1.nsi")

writeFile(mainInstallerScript, installer.format(versionString=version, currentYear=datetime.datetime.now().year))

# create folder 'Installers' if it does not exis
if not os.path.exists("Installers"): os.makedirs("Installers")
makensisPath = "C:/Program Files (x86)/NSIS/Bin/makensis.exe"

if not exists(makensisPath):
    print("Error: NSIS makensis.exe not found at", makensisPath)
    sys.exit()

runNSIScript(mainInstallerScript, makensisPath)

deleteFile(mainInstallerScript)
print("done!")
