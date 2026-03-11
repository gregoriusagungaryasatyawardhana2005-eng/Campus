import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "emergency-warning-system-united-states-313128.mp3"
    is_running = True
    
    # Inisialisasi mixer di luar loop
    pygame.mixer.init()

    while is_running: 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("WAKTU HABIS! BANGUN!")
            pygame.mixer.music.load(sound_file) 
            pygame.mixer.music.play()

            # Loop khusus saat alarm bunyi
            while pygame.mixer.music.get_busy():
                # Input ada di sini, jadi dia cuma "stalling" (menunggu) 
                # KALAU alarm sudah bunyi.
                stop_alarm = input("Press Q to stop alarm: ").upper()
                
                if stop_alarm == "Q":
                    pygame.mixer.music.stop()
                    is_running = False
                    break # Keluar dari loop musik
        
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)