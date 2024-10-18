import datetime

current_date = datetime.datetime.now()
formatted_date = current_date.strftime("%b %d %Y")
my_date = datetime.datetime(1970, 1, 1)
seconds = (current_date - my_date).total_seconds()
formatted_seconds = f"{seconds:,.4f}"
scientific_seconds = f"{seconds:.4e}"
print("Seconds since January 1, 1970:", formatted_seconds, "or", scientific_seconds, "in scientific notation")
print(formatted_date)