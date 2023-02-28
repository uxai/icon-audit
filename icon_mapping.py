import csv
from prettytable import PrettyTable

prefix = "icon-"

def check_size(icon, loc, size):
  if icon[loc] == "x":
    i = prefix + icon[0].lower().replace(" ", "-") + f"-{size}"
    if icon[-2] == "fit" or icon[-1] == "fit":
      i += "-fit"
    if icon[-1] == "colored":
      i += "-colored"
    return i
  elif icon[loc] == "deprecated":
    return "deprecated"
  else:
    return "-"

icons = []
with open('standard_icons_data.csv') as f:
    icon_file = csv.reader(f)
    for icon in icon_file:
      if icon:
        icons.append(icon)

table = PrettyTable()
table.field_names = ["Original", "64x64 (-large)", "24x24", "20x20 (-medium)", "16x16(-small)", "12x12 (-extra-small)"]

for icon in range(0, len(icons), 5):
  i = icons[icon][0].lower().replace(" ", "-")

  _64 = check_size(icons[icon], 1, "64")
  _24 = check_size(icons[icon], 2, "24")
  _20 = check_size(icons[icon], 3, "20")
  _16 = check_size(icons[icon], 4, "16")
  _12 = check_size(icons[icon], 5, "12")

  if icons[icon+3][0] == "N/A":
   original = "N/A"
  else:
    original = f"icon--{icons[icon+3][0]}"

  table.add_row([original, _64, _24, _20,  _16, _12])

table.align = "l"
print(table)
with open('results_standard.csv', 'w', newline='') as f_output:
    f_output.write(table.get_csv_string())
