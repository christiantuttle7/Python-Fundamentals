with open("csv_out.csv", "w") as file:
    header = ["Date", "Temp", "Feels_Like"]
    file.write(','.join(header))
    for i in range(100):
        output = f"{i},{i*3/2},'-11'\n"
        file.write(output)