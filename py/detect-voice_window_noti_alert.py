from plyer import notification
import sounddevice as sd
import numpy as np

# ฟังก์ชันสำหรับตรวจจับระดับเสียงและแจ้งเตือน
def detect_loudness(indata, frames, time, status):
    # คำนวณระดับเสียงเฉลี่ยในแต่ละช่วงเวลา
    rms = np.sqrt(np.mean(indata**2))
    # แปลงระดับเสียงเป็น dBFS (dB full scale)
    dBFS = 20 * np.log10(rms)

    # ตรวจสอบระดับเสียง
    if dBFS > -4:
        notification.notify(
            title="แจ้งเตือน",
            message="เสียงเบาๆดิ",
            app_name="ตรวจจับระดับเสียง",
        )

# ตั้งค่าการอ่านข้อมูลเสียง
sd.default.device = None
with sd.InputStream(callback=detect_loudness):
    sd.sleep(1000000)