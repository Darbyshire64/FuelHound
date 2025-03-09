import time
import math
import time
import os
import selftests

class Commands:
    valid_commands = ["help"]

    @staticmethod
    def Help():
        print("-- Available Commands --")
        print("Help - Returns this screen")
    @staticmethod
    def Exit():
        print("Exiting CLI")
        exit(1)
    @staticmethod
    def Special():
        # ASCII characters used to render the Mystical Object
        chars = ".,-~:;=!*#$@"

        # Set up the animation duration
        duration = 5  # seconds
        end_time = time.time() + duration

        A, B = 0, 0  # Rotation angles

        while time.time() < end_time:
            output = [" "] * 1760  # Screen buffer
            z_buffer = [0] * 1760   # Depth buffer

            for j in range(0, 628, 7):  # Outer circle
                for i in range(0, 628, 2):  # Inner circle
                    # Trig calculations
                    sinA, cosA = math.sin(A), math.cos(A)
                    sinB, cosB = math.sin(B), math.cos(B)
                    sinI, cosI = math.sin(i / 100), math.cos(i / 100)
                    sinJ, cosJ = math.sin(j / 100), math.cos(j / 100)

                    h = cosJ + 2  # Donut shape
                    D = 1 / (sinI * h * sinA + sinJ * cosA + 5)  # Depth

                    t = sinI * h * cosA - sinJ * sinA  # 3D effect
                    x = int(40 + 30 * D * (cosI * h * cosB - t * sinB))
                    y = int(12 + 15 * D * (cosI * h * sinB + t * cosB))
                    o = int(x + 80 * y)
                    N = int(8 * ((sinJ * sinA - sinI * cosJ * cosA) * cosB - sinI * cosJ * sinA - sinJ * cosA - cosI * cosJ * sinB))

                    if 0 <= o < 1760 and D > z_buffer[o]:  # Depth check
                        z_buffer[o] = D
                        output[o] = chars[N if N > 0 else 0]

            # Print to terminal
            os.system("cls" if os.name == "nt" else "clear")  # Clear screen
            print("\033[H", end="")  # Move cursor to top
            print("".join(output))   # Print frame
            time.sleep(0.03)  # Control speed

            A += 0.04  # Rotate around X-axis
            B += 0.08  # Rotate around Z-axis
    @staticmethod
    def Test():
        selftests.Test()
    
class CMD:
    @staticmethod
    def Prompt():
        return input("CMD@FuelHound $ ")

    @staticmethod
    def PromptHandeler(prompt):
        for command in Commands.valid_commands:
            if prompt.lower() == "help":
                Commands.Help()
            if prompt.lower() == 'exit':
                Commands.Exit()
            if prompt.lower() == 'donut':
                Commands.Special()
            if prompt.lower() == 'test':
                Commands.Test()
                print("Debug 1")

print("Welcome to the FuelHound Command Line. Enter 'help' to get started.")
print("This is an offline service that does not require a connection to Fuel Hound servers. Instead, it fetches data directly from the price servers.")

while True:
    command = CMD.Prompt()
    CMD.PromptHandeler(command)
