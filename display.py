import Tkinter as tk

def inc_label(name, username, msg, followers, holding):
  def count():
    if not holding:
          f = open('in', 'r+')
          lines = f.read().splitlines()
          for line in lines:
            holding.append(line.split(','))
          f.truncate(0)
          f.close()
    if holding:
      temp = holding.pop(0)
      name.config(text=temp[0])
      username.config(text=temp[1])
      msg.config(text=temp[2])
      followers.config(text="Number of followers: " + temp[3])
      name.after(10000, count)
    else:
      name.after(100, count)
  count()


main = tk.Tk()
main.title("Display")
name = tk.Label(main, fg="black")
name.pack()
username = tk.Label(main, fg="black")
username.pack()
msg = tk.Label(main, fg="black")
msg.pack()
followers = tk.Label(main, fg="black")
followers.pack()

inc_label(name, username, msg, followers, [])
button = tk.Button(main, text='Stop', width=25, command=main.destroy)
button.pack()
main.mainloop()
