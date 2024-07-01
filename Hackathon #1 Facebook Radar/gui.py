import tkinter as tk
from tkinter import messagebox
import webbrowser
from model import Report

class FacebookRadarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Facebook Radar")
        self.root.geometry("800x500")
        
        self.create_widgets()

    def create_widgets(self):
        self.welcome_label = tk.Label(self.root, text="Welcome to the Facebook Radar!")
        self.welcome_label.pack()

        self.name_label = tk.Label(self.root, text="What is your name?")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root, width=50)
        self.name_entry.pack()

        self.name_submit_button = tk.Button(self.root, text="Submit", width=20, height=2, command=self.on_name_submit)
        self.name_submit_button.pack()

    def on_name_submit(self):
        username = self.name_entry.get().strip()
        if username:
            self.clear_frame()
            self.show_menu(username)
        else:
            messagebox.showwarning("Input Error", "Please enter your name.")

    def show_menu(self, username):
        self.clear_frame()

       
        question_label = tk.Label(self.root, text=f"What would you like to do, {username}?")
        question_label.pack()


        self.report_button = tk.Button(self.root, text="Report", width=20, height=2, command=self.report)
        self.report_button.pack()

        self.comment_button = tk.Button(self.root, text="Comment", width=20, height=2, command=self.comment)
        self.comment_button.pack()

     
        self.exit_button = tk.Button(self.root, text="Exit", width=20, height=2, command=self.root.quit)
        self.exit_button.pack()

    def report(self):
        self.clear_frame()
        tk.Label(self.root, text="Please, write a topic of the post:").pack()
        self.topic_entry = tk.Entry(self.root, width=70)
        self.topic_entry.pack()

        tk.Label(self.root, text="Please, provide a link (it shouldn't be private):").pack()
        self.link_entry = tk.Entry(self.root, width=70)
        self.link_entry.pack()

        tk.Button(self.root, text="Submit", width=20, height=2, command=self.submit_report).pack()

    def submit_report(self):
        username = self.name_entry.get()
        topic = self.topic_entry.get()
        link = self.link_entry.get()

        if username and topic and link:
            Report.add_report(username, topic, link)
            messagebox.showinfo("Success", "Thank you for adding the information.")
            self.clear_frame() 
            self.show_menu(username)  
        else:
            messagebox.showwarning("Input Error", "All fields are required.")
       
    def open_link(self, id, url):
        if isinstance(url, str) and url.strip():
            Report.increment_click_count(id)  # Increment click count - doesn't work
            webbrowser.open_new(url)
        else:
            messagebox.showerror("Error", "Invalid URL")

    def comment(self):
        self.clear_frame()
        reports = Report.get_reports()

        for report in reports:
            id, username, topic, link, clicks, report_date = report
            report_text = f"{username} reported {topic}"
            tk.Label(self.root, text=report_text).pack()
            link_button = tk.Button(self.root, text="Open Link", width=20, height=2, command=lambda id=id, url=link: self.open_link(id, url))
            link_button.pack()
                    
        # for report in reports:
        #     id, username, topic, link, clicks, report_date = report
        #     print(f"Username: {username}, Topic: {topic}, Link: {link}")


    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.pack_forget() 

if __name__ == "__main__":
    root = tk.Tk()
    app = FacebookRadarApp(root)
    root.mainloop()
