import Tkinter as tk

master = tk.Tk()

teams = [
    {"name" : "team1", "score" : 0},
    {"name" : "team2", "score" : 0},
    {"name" : "team3", "score" : 0}
]

#establish the frames
name_frame = tk.Frame(master)
score_frame = tk.Frame(master)

name_frame.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)
score_frame.pack(expand=True, side=tk.RIGHT, fill=tk.BOTH)

counter = 0

for team in teams:
    team_name = tk.Label(name_frame, text=team["name"], bg="red")
    score = tk.Label(score_frame, text=team["score"], bg="blue")

    score.pack(fill=tk.BOTH, expand=True)
    team_name.pack(fill=tk.BOTH, expand=True)

    counter += 1

master.mainloop()
