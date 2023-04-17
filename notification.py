from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("VISITOR MANAGEMENT SYSTEM", "You have a new visitor!!", duration=10, icon_path="path/to/icon.ico")
