from ..models import Patient
import pandas as pd


EXCEL_DATA = '/Users/katsuto/Documents/IdeaProjects/Learn/Python/s_system/新・総合実施計画書管理フォルダ/総合実施計画書 平データ.xlsm'

df = pd.read_excel(EXCEL_DATA, sheet_name='全件')

last_row_index = df.shape[0] - 1

# 列名のリスト
columns = df.columns.tolist()

name = df['Unnamed: 2'].iloc[:]
therapist = df['Unnamed: 3'].iloc[:]
insurance = df['Unnamed: 4'].iloc[:]
disease = df['Unnamed: 18'].iloc[:]
start_dis = df['Unnamed: 19'].iloc[:]
start_reha = df['Unnamed: 20'].iloc[:]
karte_id = df['Unnamed: 23'].iloc[:]
birth = df['Unnamed: 24'].iloc[:]
gender = df['Unnamed: 25'].iloc[:]
short_goal = df['Unnamed: 75'].iloc[:]
long_goal = df['Unnamed: 76'].iloc[:]
treatment_plan = df['Unnamed: 77'].iloc[:]
treatment_content = df['Unnamed: 78'].iloc[:]

datas = zip(name, therapist, insurance, disease, start_dis, start_reha, karte_id,
            birth, gender, short_goal, long_goal, treatment_plan, treatment_content)

result_list = []
result_dict = {}

print("REEEEESULT", datas)
for data in datas:

    result_dict = {'名前': data[0],
                   'セラピスト名': data[1],
                   '保健名': data[2],
                   '障害名': data[3],
                   '発症日': data[4],
                   'リハ開始日': data[5],
                   'カルテID': data[6],
                   '生年月日': data[7],
                   '性別': data[8],
                   '短期ゴール': data[9],
                   '長期ゴール': data[10],
                   '治療方針': data[11],
                   '治療内容': str(data[12]).replace('\u3000', ', ')
                   }

    result_list.append(result_dict)

print(result_list)


try:
    # 既存のレコードがあるか検索する
    existing_patient = Patient.objects.get(name=result_list['名前'], birth_date=result_list['生年月日'])
except Patient.DoesNotExist:
    # 既存のレコードがない場合、新しいオブジェクトを作成
    print('データがないので追加しといたよ！')
    # patient = Patient(**result_list)
    # patient.save()
else:
    # 既存のレコードがある場合、何もしない
    print('データがあったから、データを追加しなかったよ！')
    pass
