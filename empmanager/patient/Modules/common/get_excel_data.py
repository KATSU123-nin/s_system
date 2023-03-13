from datetime import datetime

import pandas as pd

from patient.models import Patient
from .update_patient_data import update_patient_data

EXCEL_URL = '/Users/katsuto/Documents/IdeaProjects/Learn/Python/s_system/新・総合実施計画書管理フォルダ/総合実施計画書 therapist_nameデータ.xlsm'


url_list = []
replace_list = ['平','榊原', '藤野', '美和', 'セラピスト' ]

for replace_str in replace_list:
    url_list.append(EXCEL_URL.replace('therapist_name', replace_str))

def get_excel_data():
    for url in url_list:

        df = pd.read_excel(url, sheet_name='全件', skiprows=7, header= [0])

        name = df['名前'].iloc[:]
        therapist = df['担当'].iloc[:]
        insurance = df['保険'].iloc[:]
        disease = df['疾患名'].iloc[:]
        start_dis = df['発症日'].iloc[:]
        start_reha = df['開始日'].iloc[:]
        karte_id = df['ID'].iloc[:]
        birth = df['生年月日'].iloc[:]
        gender = df['性別'].iloc[:]
        short_goal = df['目標'].iloc[:]
        long_goal = df['目標（終了時）'].iloc[:]
        treatment_plan = df['治療方針'].iloc[:]
        treatment_content = df['治療内容'].iloc[:]

        datas = zip(name, therapist, insurance, disease, start_dis, start_reha, karte_id,
                    birth, gender, short_goal, long_goal, treatment_plan, treatment_content)


        result_list = []

        for data in datas:

            result_dict = {
                '名前': data[0],
                'セラピスト名': data[1],
                '保健名': data[2],
                '障害名': data[3],
                '発症日': data[4],
                'リハ開始日': data[5],
                'カルテID': str(data[6]).replace('.0', ''),
                '生年月日': data[7],
                '性別': data[8],
                '短期ゴール': data[9],
                '長期ゴール': data[10],
                '治療方針': data[11],
                '治療内容': str(data[12]).replace('\u3000', ', ')
            }

            result_list.append(result_dict)

        print('データの追加が完了したよ')


        # すでに存在する患者かどうかを確認して、新しい患者を作成
        for result_dict in result_list:
            try:
                existing_patient = Patient.objects.get(name=result_dict['名前'], birth_date=result_dict['生年月日'])
                print(f"Patient already exists: {existing_patient}")

                update_patient_data(existing_patient, result_dict)  # データが異なる場合は更新する

                existing_patient.save()  # 変更を保存する

                continue  # すでに存在する場合は登録をスキップ
            except Patient.DoesNotExist:
                print(f"{result_dict['名前']}のデータがないよ・・・。")
                patient = Patient.objects.create(
                    name=result_dict['名前'],
                    therapist_name=result_dict['セラピスト名'],
                    insurance=result_dict['保健名'],
                    disease=result_dict['障害名'],
                    onset_date=result_dict['発症日'],
                    reha_start=result_dict['リハ開始日'],
                    karte_id=result_dict['カルテID'],
                    birth_date=result_dict['生年月日'],
                    sex=result_dict['性別'],
                    short_term_goal=result_dict['短期ゴール'],
                    long_term_goal=result_dict['長期ゴール'],
                    treatment_policy=result_dict['治療方針'],
                    treatment_content=result_dict['治療内容']
                )
                patient.save()
                print(f"{result_dict['名前']}のデータを登録しといたよ！")

