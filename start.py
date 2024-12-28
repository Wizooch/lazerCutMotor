#!/usr/bin/env python3

print("Hello from rc.local! This script has run.")

# Write to a file so we can verify it ran
with open("/home/lasercut/rc_local_test.log", "w") as file:
    file.write("rc.local script ran successfully!\n")
