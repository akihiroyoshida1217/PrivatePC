import os
import subprocess
import traceback
import pwd
#import sys

def update_extension():
    try:
        ld = open("/etc/passwd", "r")
        lines = ld.read()
        ld.close()

        result = [[subprocess.check_output(
            ["env", "CODE_EXTENSION=" + l , "UID=" + i , "HOME=" + pwd.getpwuid(int(i))[5] , 
            "/usr/local/bin/docker-compose", "-f", "/opt/docker-image/vscode-extension-package/docker-compose.yml", "run", "--rm", "vscode-extension"]) 
            for l in subprocess.check_output(["sudo", "-u#" + i , "/usr/bin/code", "--list-extensions"]).decode('utf-8').splitlines()] 
            for i in ["1000", "1001", "1002" ] if ("x:" + i) in lines ]
    except:
        traceback.print_exc()
    print(result)

if __name__ == "__main__":
    update_extension()