import practice6_6 as pc
import pandas as pd
students = [
    {'name': 'Tom', 'score': 90},
    {'name': 'Jerry', 'score': 55},
    {'name': 'Bob', 'score': 78},
    {'name': 'Alice', 'score': 82}
]
def processed_stu(stu):
    return(pc.filter_passed(pc.add_garde(pc.sorted(stu))))
processed_stu(students)
df = pd.DataFrame(students)
print(df)