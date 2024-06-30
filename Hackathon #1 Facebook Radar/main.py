from database import create_tables
import gui

def main():
    create_tables()
    root = gui.tk.Tk()
    app = gui.FacebookRadarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


