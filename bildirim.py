import notifypy as bildirim
import pyqrcode as code
url=input("enter :")
isim=input("enter file path :")
kod=code.create(url)
notification = bildirim.Notify()
notification.title = "QRcodeCreater"
notification.message = f"qrcode generated"
erorbildirim=bildirim.Notify()
erorbildirim.title="QRcodeCreater"
try:
    kod.svg(f"{isim}.svg",scale=8)
    try:
        
        notification.send()
    except:
        print("error :|")
        
    

except:
    print("error :|")
    erorbildirim.send()
    

