from django.db import models
import numpy as np
import pandas as pd


# Create your models here.

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            self.head.next = newnode
    def display(self):
        temp=self.head

        while temp is not None:
            print(temp.data)
            temp=temp.next
    def intersect(self):
        temp=self.head.next
        while temp is not None:
            arr=self.head.data.intersection(temp.data)
            temp=temp.next
        return arr
    '''
    def sym_z(self):
        dis_arr = linklist.intersect()
        dis_arr = dis_arr.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
        i = 0
        dis_num = []
        for i in range(len(df1.columns)):
            for j in range(len(dis_arr)):
                if dis_arr[j] == df1.columns[i]:
                    dis_num.append(i)
        dis_symp = np.empty([0, len(dis_num)], dtype=object)
        for i in range(0, len(dis_num)):
            dis_symp = np.union1d(dis_symp, np.array(
                pd.DataFrame(df1.iloc[:, dis_num[i]].where(df1.iloc[:, dis_num[i]] == 1).dropna()).index))

        dis_symp_inters = np.empty([0, len(dis_num)], dtype=object)
        for i in range(0, len(dis_num) - 1):
            dis1 = np.array(pd.DataFrame(df1.iloc[:, dis_num[i]].where(df1.iloc[:, dis_num[i]] == 1).dropna()).index)
            dis2 = np.array(
                pd.DataFrame(df1.iloc[:, dis_num[i + 1]].where(df1.iloc[:, dis_num[i + 1]] == 1).dropna()).index)
            dis_symp_inters = np.union1d(dis_symp_inters, np.intersect1d(dis1, dis2))
        return np.setdiff1d(dis_symp, dis_symp_inters)
        '''
linklist=LinkedList()
models.IntegerField(default=0)
class inp(models.Model):
    itching=models.IntegerField(default=0)
    skin_rash=models.IntegerField(default=0)
    nodal_skin_eruptions=models.IntegerField(default=0)
    continuous_sneezing=models.IntegerField(default=0)
    shivering=models.IntegerField(default=0)
    chills=models.IntegerField(default=0)
    joint_pain=models.IntegerField(default=0)
    stomach_pain=models.IntegerField(default=0)
    acidity=models.IntegerField(default=0)
    ulcers_on_tongue=models.IntegerField(default=0)
    muscle_wasting=models.IntegerField(default=0)
    vomiting=models.IntegerField(default=0)
    burning_mvicturition=models.IntegerField(default=0)
    spotting=models.IntegerField(default=0)
    urination=models.IntegerField(default=0)
    fatigue=models.IntegerField(default=0)
    weight_gain=models.IntegerField(default=0)
    anxiety=models.IntegerField(default=0)
    cold_hands_and_feets=models.IntegerField(default=0)
    mood_swings=models.IntegerField(default=0)
    weight_loss=models.IntegerField(default=0)
    restlessness=models.IntegerField(default=0)
    lethargy=models.IntegerField(default=0)
    patches_in_throat=models.IntegerField(default=0)
    irregular_sugar_level=models.IntegerField(default=0)
    cough=models.IntegerField(default=0)
    high_fever=models.IntegerField(default=0)
    sunken_eyes=models.IntegerField(default=0)
    breathlessness=models.IntegerField(default=0)
    sweating=models.IntegerField(default=0)
    dehydration=models.IntegerField(default=0)
    indigestion=models.IntegerField(default=0)
    headache=models.IntegerField(default=0)
    yellowish_skin=models.IntegerField(default=0)
    dark_urine=models.IntegerField(default=0)
    nausea=models.IntegerField(default=0)
    loss_of_appetite=models.IntegerField(default=0)
    pain_behind_the_eyes=models.IntegerField(default=0)
    back_pain=models.IntegerField(default=0)
    constipation=models.IntegerField(default=0)
    abdominal_pain=models.IntegerField(default=0)
    diarrhoea=models.IntegerField(default=0)
    mild_fever=models.IntegerField(default=0)
    yellow_urine=models.IntegerField(default=0)
    yellowing_of_eyes=models.IntegerField(default=0)
    acute_liver_failure=models.IntegerField(default=0)
    fluid_overload=models.IntegerField(default=0)
    swelling_of_stomach=models.IntegerField(default=0)
    swelled_lymph_nodes=models.IntegerField(default=0)
    malaise=models.IntegerField(default=0)
    blurred_and_distorted_vision=models.IntegerField(default=0)
    phlegm=models.IntegerField(default=0)
    throat_irritation=models.IntegerField(default=0)
    redness_of_eyes=models.IntegerField(default=0)
    sinus_pressure=models.IntegerField(default=0)
    runny_nose=models.IntegerField(default=0)
    congestion=models.IntegerField(default=0)
    chest_pain=models.IntegerField(default=0)
    weakness_in_limbs=models.IntegerField(default=0)
    fast_heart_rate=models.IntegerField(default=0)
    pain_during_bowel_movements=models.IntegerField(default=0)
    pain_in_anal_region=models.IntegerField(default=0)
    bloody_stool=models.IntegerField(default=0)
    irritation_in_anus=models.IntegerField(default=0)
    neck_pain=models.IntegerField(default=0)
    dizziness=models.IntegerField(default=0)
    cramps=models.IntegerField(default=0)
    bruising=models.IntegerField(default=0)
    obesity=models.IntegerField(default=0)
    swollen_legs=models.IntegerField(default=0)
    swollen_blood_vessels=models.IntegerField(default=0)
    puffy_face_and_eyes=models.IntegerField(default=0)
    enlarged_thyroid=models.IntegerField(default=0)
    brittle_nails=models.IntegerField(default=0)
    swollen_extremeties=models.IntegerField(default=0)
    excessive_hunger=models.IntegerField(default=0)
    extra_marital_contacts=models.IntegerField(default=0)
    drying_and_tingling_lips=models.IntegerField(default=0)
    slurred_speech=models.IntegerField(default=0)
    knee_pain=models.IntegerField(default=0)
    hip_joint_pain=models.IntegerField(default=0)
    muscle_weakness=models.IntegerField(default=0)
    stiff_neck=models.IntegerField(default=0)
    swelling_joints=models.IntegerField(default=0)
    movement_stiffness=models.IntegerField(default=0)
    spinning_movements=models.IntegerField(default=0)
    loss_of_balance=models.IntegerField(default=0)
    unsteadiness=models.IntegerField(default=0)
    weakness_of_one_body_side=models.IntegerField(default=0)
    loss_of_smell=models.IntegerField(default=0)
    bladder_discomfort=models.IntegerField(default=0)
    foul_smell_of_urine=models.IntegerField(default=0)
    continuous_feel_of_urine=models.IntegerField(default=0)
    passage_of_gases=models.IntegerField(default=0)
    internal_itching=models.IntegerField(default=0)
    toxic_look_typhos=models.IntegerField(default=0)
    depression=models.IntegerField(default=0)
    irritability=models.IntegerField(default=0)
    muscle_pain=models.IntegerField(default=0)
    altered_sensorium=models.IntegerField(default=0)
    red_spots_over_body=models.IntegerField(default=0)
    belly_pain=models.IntegerField(default=0)
    abnormal_menstruation=models.IntegerField(default=0)
    dischromic_patches=models.IntegerField(default=0)
    watering_from_eyes=models.IntegerField(default=0)
    increased_appetite=models.IntegerField(default=0)
    polyuria=models.IntegerField(default=0)
    family_history=models.IntegerField(default=0)
    mucoid_sputum=models.IntegerField(default=0)
    rusty_sputum=models.IntegerField(default=0)
    lack_of_concentration=models.IntegerField(default=0)
    visual_disturbances=models.IntegerField(default=0)
    receiving_blood_transfusion=models.IntegerField(default=0)
    receiving_unsterile_injections=models.IntegerField(default=0)
    coma=models.IntegerField(default=0)
    stomach_bleeding=models.IntegerField(default=0)
    distention_of_abdomen=models.IntegerField(default=0)
    history_of_alcohol_consumption=models.IntegerField(default=0)
    fluid_overload=models.IntegerField(default=0)
    blood_in_sputum=models.IntegerField(default=0)
    prominent_veins_on_calf=models.IntegerField(default=0)
    palpitations=models.IntegerField(default=0)
    painful_walking=models.IntegerField(default=0)
    pus_filled_pimples=models.IntegerField(default=0)
    blackheads=models.IntegerField(default=0)
    scurring=models.IntegerField(default=0)
    skin_peeling=models.IntegerField(default=0)
    silver_like_dusting=models.IntegerField(default=0)
    small_dents_in_nails=models.IntegerField(default=0)
    inflammatory_nails=models.IntegerField(default=0)
    blister=models.IntegerField(default=0)
    red_sore_around_nose=models.IntegerField(default=0)
    yellow_crust_ooze=models.IntegerField(default=0)
    prognosis=models.CharField(max_length=250)



