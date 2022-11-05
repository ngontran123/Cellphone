import pandas as pd
from datetime import datetime as dt


def filer_most_3_recent_month(id, date):
    file_csv = pd.read_excel('df_fake.xlsx')
    date_split = date.split('-')
    year = date_split[0]
    month = int(date_split[1])
    if month < 3:
        past_month = 12 + month - 2
        change_year = int(year) - 1
    else:
        past_month=month-2
        change_year=int(year)
    from_month = '{year}-{past_month}-{day}'.format(year=str(change_year), past_month=str(past_month), day=date_split[2])
    to_month = '{year}-{month}-{day}'.format(year=str(year), month=str(month), day=date_split[2])
    print(from_month)
    print(to_month)
    file_csv = file_csv.loc[file_csv.employeeid == id]
    file_csv = file_csv.loc[file_csv['evaluate_month'].isin(pd.date_range(from_month, to_month))]
    print(file_csv)

def filtre():
    csv=pd.read_excel('df_fake.xlsx')
    print(csv.iloc[:10])


if __name__ == "__main__":
    filtre()
