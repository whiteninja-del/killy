import time
import threading
from datetime import datetime, timedelta

class CountdownTimer:
    def __init__(self):
        self.total_seconds = 0
        self.remaining_seconds = 0
        self.is_running = False
        self.is_paused = False
        self.timer_thread = None
        
    def set_time(self, hours=0, minutes=0, seconds=0):
        """Set the countdown time"""
        self.total_seconds = hours * 3600 + minutes * 60 + seconds
        self.remaining_seconds = self.total_seconds
        print(f"Timer set to {self.format_time(self.total_seconds)}")
    
    def format_time(self, seconds):
        """Format seconds into HH:MM:SS"""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    
    def start(self):
        """Start the countdown"""
        if self.remaining_seconds <= 0:
            print("Please set a time first!")
            return
            
        if self.is_running:
            print("Timer is already running!")
            return
            
        self.is_running = True
        self.is_paused = False
        self.timer_thread = threading.Thread(target=self._run_timer)
        self.timer_thread.daemon = True
        self.timer_thread.start()
        print("Timer started!")
    
    def _run_timer(self):
        """Internal timer function that runs in a separate thread"""
        while self.remaining_seconds > 0 and self.is_running:
            if not self.is_paused:
                print(f"\rTime remaining: {self.format_time(self.remaining_seconds)}", end="", flush=True)
                time.sleep(1)
                self.remaining_seconds -= 1
            else:
                time.sleep(0.1)  # Small delay when paused
        
        if self.remaining_seconds <= 0 and self.is_running:
            print(f"\n🎉 TIME'S UP! 🎉")
            self.is_running = False
    
    def pause(self):
        """Pause the countdown"""
        if not self.is_running:
            print("Timer is not running!")
            return
        
        if self.is_paused:
            self.is_paused = False
            print(f"\nTimer resumed at {self.format_time(self.remaining_seconds)}")
        else:
            self.is_paused = True
            print(f"\nTimer paused at {self.format_time(self.remaining_seconds)}")
    
    def stop(self):
        """Stop the countdown"""
        if not self.is_running:
            print("Timer is not running!")
            return
            
        self.is_running = False
        self.is_paused = False
        print(f"\nTimer stopped at {self.format_time(self.remaining_seconds)}")
    
    def reset(self):
        """Reset the countdown to original time"""
        self.is_running = False
        self.is_paused = False
        self.remaining_seconds = self.total_seconds
        print(f"Timer reset to {self.format_time(self.total_seconds)}")
    
    def status(self):
        """Show current timer status"""
        if self.is_running:
            status = "PAUSED" if self.is_paused else "RUNNING"
        else:
            status = "STOPPED"
        
        print(f"\nTimer Status: {status}")
        print(f"Time remaining: {self.format_time(self.remaining_seconds)}")
        print(f"Original time: {self.format_time(self.total_seconds)}")

def main():
    timer = CountdownTimer()
    
    print("=== Interactive Countdown Timer ===")
    print("Commands:")
    print("  set <hours> <minutes> <seconds> - Set timer (e.g., 'set 0 5 30' for 5min 30sec)")
    print("  start - Start the countdown")
    print("  pause - Pause/Resume the countdown")
    print("  stop - Stop the countdown")
    print("  reset - Reset to original time")
    print("  status - Show current status")
    print("  quit - Exit the program")
    print()
    
    while True:
        try:
            command = input("Enter command: ").strip().lower().split()
            
            if not command:
                continue
                
            if command[0] == "set":
                if len(command) == 4:
                    hours, minutes, seconds = map(int, command[1:4])
                    timer.set_time(hours, minutes, seconds)
                else:
                    print("Usage: set <hours> <minutes> <seconds>")
                    
            elif command[0] == "start":
                timer.start()
                
            elif command[0] == "pause":
                timer.pause()
                
            elif command[0] == "stop":
                timer.stop()
                
            elif command[0] == "reset":
                timer.reset()
                
            elif command[0] == "status":
                timer.status()
                
            elif command[0] == "quit":
                timer.stop()
                print("Goodbye!")
                break
                
            else:
                print("Unknown command. Type 'quit' to exit.")
                
        except ValueError:
            print("Invalid input. Please enter numbers for time values.")
        except KeyboardInterrupt:
            timer.stop()
            print("\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()