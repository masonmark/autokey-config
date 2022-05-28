import subprocess
# Launch Flameshot via flatpak with 'gui' arg to start select-rect-to-copy UI mode:
subprocess.Popen(["flatpak", "run", "org.flameshot.Flameshot", "gui"])