def update_patient_data(existing_patient, result_dict):
    if existing_patient.therapist_name != result_dict['セラピスト名']:
        existing_patient.therapist_name = result_dict['セラピスト名']
        print(f"{existing_patient.name}のセラピスト名を変更しました。")

    if existing_patient.insurance != result_dict['保健名']:
        existing_patient.insurance = result_dict['保健名']
        print(f"{existing_patient.name}の保険名を変更しました。")

    if existing_patient.disease != result_dict['障害名']:
        existing_patient.disease = result_dict['障害名']
        print(f"{existing_patient.name}の障害名を変更しました。")

    if existing_patient.onset_date != result_dict['発症日']:
        existing_patient.onset_date = result_dict['発症日']
        print(f"{existing_patient.name}の発症日を変更しました。")

    if existing_patient.reha_start != result_dict['リハ開始日']:
        existing_patient.reha_start = result_dict['リハ開始日']
        print(f"{existing_patient.name}のリハ開始日を変更しました。")

    if existing_patient.karte_id != result_dict['カルテID']:
        existing_patient.karte_id = result_dict['カルテID']
        print(f"{existing_patient.name}のカルテIDを変更しました。")

    if existing_patient.birth_date != result_dict['生年月日']:
        existing_patient.birth_date = result_dict['生年月日']
        print(f"{existing_patient.name}の生年月日を変更しました。")

    if existing_patient.sex != result_dict['性別']:
        existing_patient.sex = result_dict['性別']
        print(f"{existing_patient.name}の性別を変更しました。")

    if existing_patient.short_term_goal != result_dict['短期ゴール']:
        existing_patient.short_term_goal = result_dict['短期ゴール']
        print(f"{existing_patient.name}の短期ゴールを変更しました。")

    if existing_patient.long_term_goal != result_dict['長期ゴール']:
        existing_patient.long_term_goal = result_dict['長期ゴール']
        print(f"{existing_patient.name}の長期ゴールを変更しました。")

    if existing_patient.treatment_policy != result_dict['治療方針']:
        existing_patient.treatment_policy = result_dict['治療方針']
        print(f"{existing_patient.name}の治療方針を変更しました。")

    if existing_patient.treatment_content != result_dict['治療内容']:
        existing_patient.treatment_content = result_dict['治療内容']
        print(f"{existing_patient.name}の治療内容を変更しました。")



