import tkinter as tk
import sounddevice as sd
import numpy as np
import winsound

# ฟังก์ชันสำหรับตรวจจับระดับเสียงและแสดงหน้าต่างแจ้งเตือน
def detect_loudness(indata, frames, time, status):
    # คำนวณระดับเสียงเฉลี่ยในแต่ละช่วงเวลา
    rms = np.sqrt(np.mean(indata**2))
    # แปลงระดับเสียงเป็น dBFS (dB full scale)
    dBFS = 20 * np.log10(rms)

    # ตรวจสอบระดับเสียง
    if dBFS > -4:
        # สร้างหน้าต่าง Tkinter
        window = tk.Tk()
        window.title("แจ้งเตือน")
        window.geometry("300x100")
        label = tk.Label(window, text="เสียงเบาๆดิ")
        label.pack()

        # เล่นเสียง Alert
        winsound.Beep(300, 200)  # เล่นเสียงความถี่ xx Hz เป็นเวลา xx มิลลิวินาที
        winsound.Beep(400, 150)

        # เริ่มการทำงานของหน้าต่าง Tkinter
        window.mainloop()

# ตั้งค่าการอ่านข้อมูลเสียง
sd.default.device = None
with sd.InputStream(callback=detect_loudness):
    sd.sleep(1000000)
