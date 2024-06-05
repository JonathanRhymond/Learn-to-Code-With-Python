class SmartPhone():
    def __init__(self):
        # _ is common syntax to tell developers to avoid calling or modifying directly
        self._company = "Apple"
        self._firmware = 10.0

    def get_os_version(self):
        return self._firmware
    
    def update_firmware(self):
        print("Reaching out to the server for next version")
        self._firmware += 1

iPhone = SmartPhone()
print(iPhone._company)
print(iPhone._firmware)

print(iPhone.update_firmware())
print(iPhone._firmware)
