import reports
# Export functions
file_name = "game_stat.txt"

with open("export.txt", "w") as export_file:
    export_file.write(str(reports.count_games(file_name)) + "\n")
    export_file.write(str(reports.decide(file_name, 1997)) + "\n")
    export_file.write(str(reports.get_latest(file_name)) + "\n")
    export_file.write(str(reports.count_by_genre(file_name, "First-person shooter")) + "\n")
    export_file.write(str(reports.get_line_number_by_title(file_name, "World of Warcraft")) + "\n")
