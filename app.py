# Import Libraries
from flask import Flask, request, render_template, send_from_directory

import model


# importing model library
import pickle

# importing the numpy library
import numpy as np

# importing the statistics library
from scipy.stats import mode

# handling warnings
import warnings
warnings.filterwarnings("ignore")

# loading the models from the file
model = pickle.load(open("nb.sav", 'rb'))
model2 = pickle.load(open("svm.sav", 'rb'))
model3 = pickle.load(open("rf.sav", 'rb'))


# creating a dictionary - for comparison purposes of string into numerical data
dict = {'symptom_index': {'Itching': 0,
                          'Skin Rash': 1,
                          'Nodal Skin Eruptions': 2,
                          'Continuous Sneezing': 3,
                          'Shivering': 4,
                          'Chills': 5,
                          'Joint Pain': 6,
                          'Stomach Pain': 7,
                          'Acidity': 8,
                          'Ulcers On Tongue': 9,
                          'Muscle Wasting': 10,
                          'Vomiting': 11,
                          'Burning Micturition': 12,
                          'Spotting  urination': 13,
                          'Fatigue': 14,
                          'Weight Gain': 15,
                          'Anxiety': 16,
                          'Cold Hands And Feets': 17,
                          'Mood Swings': 18,
                          'Weight Loss': 19,
                          'Restlessness': 20,
                          'Lethargy': 21,
                          'Patches In Throat': 22,
                          'Irregular Sugar Level': 23,
                          'Cough': 24,
                          'High Fever': 25,
                          'Sunken Eyes': 26,
                          'Breathlessness': 27,
                          'Sweating': 28,
                          'Dehydration': 29,
                          'Indigestion': 30,
                          'Headache': 31,
                          'Yellowish Skin': 32,
                          'Dark Urine': 33,
                          'Nausea': 34,
                          'Loss Of Appetite': 35,
                          'Pain Behind The Eyes': 36,
                          'Back Pain': 37,
                          'Constipation': 38,
                          'Abdominal Pain': 39,
                          'Diarrhoea': 40,
                          'Mild Fever': 41,
                          'Yellow Urine': 42,
                          'Yellowing Of Eyes': 43,
                          'Acute Liver Failure': 44,
                          'Fluid Overload': 45,
                          'Swelling Of Stomach': 46,
                          'Swelled Lymph Nodes': 47,
                          'Malaise': 48,
                          'Blurred And Distorted Vision': 49,
                          'Phlegm': 50,
                          'Throat Irritation': 51,
                          'Redness Of Eyes': 52,
                          'Sinus Pressure': 53,
                          'Runny Nose': 54,
                          'Congestion': 55,
                          'Chest Pain': 56,
                          'Weakness In Limbs': 57,
                          'Fast Heart Rate': 58,
                          'Pain During Bowel Movements': 59,
                          'Pain In Anal Region': 60,
                          'Bloody Stool': 61,
                          'Irritation In Anus': 62,
                          'Neck Pain': 63,
                          'Dizziness': 64,
                          'Cramps': 65,
                          'Bruising': 66,
                          'Obesity': 67,
                          'Swollen Legs': 68,
                          'Swollen Blood Vessels': 69,
                          'Puffy Face And Eyes': 70,
                          'Enlarged Thyroid': 71,
                          'Brittle Nails': 72,
                          'Swollen Extremeties': 73,
                          'Excessive Hunger': 74,
                          'Extra Marital Contacts': 75,
                          'Drying And Tingling Lips': 76,
                          'Slurred Speech': 77,
                          'Knee Pain': 78,
                          'Hip Joint Pain': 79,
                          'Muscle Weakness': 80,
                          'Stiff Neck': 81,
                          'Swelling Joints': 82,
                          'Movement Stiffness': 83,
                          'Spinning Movements': 84,
                          'Loss Of Balance': 85,
                          'Unsteadiness': 86,
                          'Weakness Of One Body Side': 87,
                          'Loss Of Smell': 88,
                          'Bladder Discomfort': 89,
                          'Foul Smell Of urine': 90,
                          'Continuous Feel Of Urine': 91,
                          'Passage Of Gases': 92,
                          'Internal Itching': 93,
                          'Toxic Look (typhos)': 94,
                          'Depression': 95,
                          'Irritability': 96,
                          'Muscle Pain': 97,
                          'Altered Sensorium': 98,
                          'Red Spots Over Body': 99,
                          'Belly Pain': 100,
                          'Abnormal Menstruation': 101,
                          'Dischromic  Patches': 102,
                          'Watering From Eyes': 103,
                          'Increased Appetite': 104,
                          'Polyuria': 105,
                          'Family History': 106,
                          'Mucoid Sputum': 107,
                          'Rusty Sputum': 108,
                          'Lack Of Concentration': 109,
                          'Visual Disturbances': 110,
                          'Receiving Blood Transfusion': 111,
                          'Receiving Unsterile Injections': 112,
                          'Coma': 113,
                          'Stomach Bleeding': 114,
                          'Distention Of Abdomen': 115,
                          'History Of Alcohol Consumption': 116,
                          'Fluid Overload.1': 117,
                          'Blood In Sputum': 118,
                          'Prominent Veins On Calf': 119,
                          'Palpitations': 120,
                          'Painful Walking': 121,
                          'Pus Filled Pimples': 122,
                          'Blackheads': 123,
                          'Scurring': 124,
                          'Skin Peeling': 125,
                          'Silver Like Dusting': 126,
                          'Small Dents In Nails': 127,
                          'Inflammatory Nails': 128,
                          'Blister': 129,
                          'Red Sore Around Nose': 130,
                          'Yellow Crust Ooze': 131}, 'predictions_classes': ['(vertigo) Paroymsal  Positional Vertigo', 'AIDS', 'Acne',
        'Alcoholic hepatitis', 'Allergy', 'Arthritis', 'Bronchial Asthma',
                                                                             'Cervical spondylosis', 'Chicken pox', 'Chronic cholestasis',
                                                                             'Common Cold', 'Dengue', 'Diabetes ',
                                                                             'Dimorphic hemmorhoids(piles)', 'Drug Reaction',
                                                                             'Fungal infection', 'GERD', 'Gastroenteritis', 'Heart attack',
                                                                             'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
                                                                             'Hypertension ', 'Hyperthyroidism', 'Hypoglycemia',
                                                                             'Hypothyroidism', 'Impetigo', 'Jaundice', 'Malaria', 'Migraine',
                                                                             'Osteoarthristis', 'Paralysis (brain hemorrhage)',
                                                                             'Peptic ulcer diseae', 'Pneumonia', 'Psoriasis', 'Tuberculosis',
                                                                             'Typhoid', 'Urinary tract infection', 'Varicose veins',
                                                                             'hepatitis A'], }


def predictDisease(symptoms):
    symptoms = symptoms.split(",")

    # creating input data for the models
    input_data = [0] * len(dict["symptom_index"])
    for symptom in symptoms:
        index = dict["symptom_index"][symptom]
        input_data[index] = 1

    # reshaping the input data and converting it
    # into suitable format for model predictions
    input_data = np.array(input_data).reshape(1, -1)

    # generating individual outputs
    rf_prediction = dict["predictions_classes"][model.predict(input_data)[0]]
    nb_prediction = dict["predictions_classes"][model2.predict(input_data)[0]]
    svm_prediction = dict["predictions_classes"][model3.predict(input_data)[0]]

    # making final prediction by taking mode of all predictions
    final_prediction = mode(
        [rf_prediction, nb_prediction, svm_prediction])[0][0]

    return final_prediction


app = Flask(__name__, template_folder="templates", static_folder='static')


@app.route('/')
@app.route('/index')
def home_page():
    return render_template('index.html')


@app.route('/p', methods=['GET'])
def pr():
    return render_template('Predict.html')


@app.route('/predict', methods=['POST'])
def predict():

    symptoms = (request.form['symptoms'])
    # predict the price of house by calling model.py
    X = predictDisease(symptoms)
    if (X == "Benign Paroxysmal Positional Vertigo"):
        diagnosis = '''The detected  disease is Benign Paroxysmal Positional Vertigo.

            Recommended Medicines : meclizine (Antivert, Bonine, Dramamine II, D-Vert),
diazepam (Valium),
dimenhydrinate (Dramamine),
promethazine (Phenergan),
scopolamine (Isopto, Scopace),

Recommended Yoga Asanas : Balasana (Baby Pose)
Viparita Karani (Legs Up The Wall Pose)
Halasana (Plow Pose)
Paschimottanasana (Seated Forward Bent Pose)
Shavasana (Corpse Pose)

'''
    elif (X == "AIDS"):
        diagnosis = '''The detected  disease is AIDS.
             Recommended Medicines :Abacavir (Ziagen, ABC)
Didanosine (Videx, dideoxyinosine, ddI)
Emtricitabine (Emtriva, FTC)
Lamivudine (Epivir, 3TC)
Stavudine (Zerit, d4T)
Tenofovir (Viread, TDF)
Zalcitabine (Hivid, ddC)
Zidovudine (Retrovir, ZDV or AZT)

             Recommended Yoga Asanas :Antiretroviral Therapy
NATUROPATHY

            '''
    elif (X == "Acne"):
        diagnosis = '''The detected  disease is Acne.
             Recommended Medicines :tetracycline (minocycline, doxycycline)
macrolide (erythromycin, azithromycin)
tretinoin (Avita, Retin-A, others)
adapalene (Differin)
tazarotene (Tazorac, Avage, others)

             Recommended Yoga Asanas :Kapal Bhati
Mountain Pose
Fish Pose
Headstand

            '''
    elif (X == "Alcoholic hepatitis"):
        diagnosis = '''The detected  disease is Alcoholic hepatitis.
             Recommended Medicines :Corticosteroids
Pentoxifylline
Prednisolone
Ondansetron
Metadoxine
Silymarin

             Recommended Yoga Asanas :Kapalbhati
Pranayama
matsyasan
dhanurasan
go-mukh asan

            '''
    elif (X == "Fungal infection"):
        diagnosis = '''The detected  disease is Fungal infection.\n
Recommended Medicines :clotrimazole (Canesten)
terbinafine (Lamisil)
fluconazole (Diflucan)
nystatin (Nystan)
ketoconazole (Daktarin)\n

Recommended Yoga Asanas :Shatkarmas
Sarvangasana
Matsyasana
pachhimottanasana
surya namaskar

            '''
    elif (X == "allergy"):
        diagnosis = '''The detected  disease is allergy.\n
Recommended Medicines :Cetirizine (Zyrtec, Zyrtec Allergy)
Desloratadine (Clarinex)
Fexofenadine (Allegra, Allegra Allergy)
Levocetirizine (Xyzal, Xyzal Allergy)
Loratadine (Alavert, Claritin)\n

Recommended Yoga Asanas :matsyasan
shoulder stand
dund baithak
surya namaskar
Bhastrika

            '''
    elif (X == "Arthritis"):
        diagnosis = '''The detected  disease is Arthritis.\n
Recommended Medicines :celecoxib (Celebrex)
ibuprofen (prescription strength)
nabumetone (Relafen)
naproxen (Naprosyn)
naproxen sodium (Anaprox)
piroxicam (Feldene)\n

Recommended Yoga Asanas :Adho Mukhi Marjari Asana.
anulom vilom
Marjariasana.
Setubandhasana.
Trikonasana.
Urdhva Mukhi Marjari Asana.
Virabhadrasana.
Vrikshasana.

            '''
    elif (X == "bronchial asthma"):
        diagnosis = '''The detected  disease is bronchial asthma.\n
Recommended Medicines :Fluticasone (Flovent HFA, Arnuity Ellipta, others)
Budesonide (Pulmicort Flexhaler)
Mometasone (Asmanex Twisthaler)
Beclomethasone (Qvar RediHaler)
Ciclesonide (Alvesco)\n

Recommended Yoga Asanas : Nadi Shodhan pranayama (Alternate Nostril Breathing technique)
Kapal Bhati
Ardha Matsyendrasana (Sitting Half Spinal Twist)
Pavanamuktasana (Wind Relieving Pose)
Setu Bandhasana (Bridge Pose)
Bhujangasana (Cobra Pose)
Adho Mukha Svanasana (Downward-Facing Dog Pose)
Badhakonasana (Butterfly Pose)
Poorvottanasana (Upward Plank Pose)
Shavasana (Corpse Pose)

            '''
    elif (X == "Cervical spondylosis"):
        diagnosis = '''The detected  disease is Cervical spondylosis.\n
Recommended Medicines :Corticosteroids
Ibuprofen (Advil, Motrin IB)
naproxen sodium (Aleve)
Methocarbamol (Robaxin)
Tylenol (acetaminophen)\n

Recommended Yoga Asanas :tadasan
ustrasan
Bhujangasana (Cobra Pose)
Ardha Matsyendrasana (Sitting Half-Spinal Twist)
Dhanurasana (Bow Pose)
Marjariasana (Cat Pose)
Setu Bandhasana (Bridge Pose)
Matsyasana (Fish Pose)

            '''
    elif (X == "chicken pox"):
        diagnosis = '''The detected  disease is chicken pox.\n
Recommended Medicines :Calamine lotion
cool bath in baking soda water
aciclovir
valtrexOn
zoviraxOn\n

Recommended Yoga Asanas :Nadi Shuddi Pranayam
Bhujangasana - immune booster asana
Shashankasana
Kapal Bhati
Ujjayi
Bhastrika

            '''
    elif (X == "Chronic cholestasis"):
        diagnosis = '''The detected  disease is Chronic cholestasis.\n
Recommended Medicines :chlorpromazine
ibuprofen
amiodarone
Ampicillin
 penicillin
 ursodiol (Actigall, Urso, Urso Forte)\n

Recommended Yoga Asanas :Nadi Shuddi Pranayam

            '''
    elif (X == "Dimorphic hemmorhoids(piles)"):
        diagnosis = '''The detected  disease is Dimorphic hemmorhoids(piles).\n
Recommended Medicines :Benzocaine
Docusate
Hydrocortisone
Lidocaine
Rutin\n

Recommended Yoga Asanas :balasan
viparita karani
pawanmuktasana
baddha konasana

            '''
    elif (X == "dengue"):
        diagnosis = '''The detected  disease is dengue.\n
Recommended Medicines :Acetaminophen (paracetamol)
aspirin
Ibuprofen
Nemuslide
Calpol
combiflam\n

Recommended Yoga Asanas :Dandasana or Staff Pose
Malasana or Waste Evacuation Pose
Vajrasana or Thunderbolt Pose/Diamond Pose
Paschimottanasana or Seated Forward Bend
            '''
    elif (X == "Diabetes"):
        diagnosis = '''The detected  disease is Diabetes.\n
Recommended Medicines :glimepiride (Amaryl)
glimepiride-pioglitazone (Duetact)
"Insulin (long- and rapid-acting)
Metformin (biguanide class)
Glipizide (sulfonylurea class)
Glimepiride (sulfonylurea class)
Invokana (sodium glucose cotransporter 2 inhibitor class)
Jardiance (SGLT2 class)​​​​​​​\n

Recommended Yoga Asanas :dhanurasan
balasan
bhujangasan
shavasan
tadasan
mandukasan
            '''
    elif (X == "Gastroenteritis"):
        diagnosis = '''The detected  disease is Gastroenteritis.\n
Recommended Medicines :loperamide link (Imodium)
bismuth subsalicylate link (Pepto-Bismol, Kaopectate)
Cefixime
ciprofloxacin
Metronidazole
Azithromycin\n

Recommended Yoga Asanas :Seated Side Bend (Parsva Sukhasana)
Seated Twist (Ardha Matsyendrasana)
Supine Spinal Twist (Supta Matsyendrasana)
Knees to Chest (Apanasana)
Cat-Cow (Marjaryasana-Bitilasana)
Cobra Pose (Bhujangasana)
Bow Pose (Dhanurasana)

            '''
    elif (X == "hyper tension"):
        diagnosis = '''The detected  disease is hyper tension.\n
Recommended Medicines :Benazepril hydrochloride (Lotensin)
Captopril (Capoten)
Enalapril Maleate (Vasotec)
Fosinopril sodium (Monopril)
Lisinopril (Prinivil, Zestril)
Moexipril (Univasc)
Perindopril (Aceon)
Quinapril hydrochloride (Accupril)\n

Recommended Yoga Asanas :Uttanasana (Standing forward bend pose)
Viparita Karani (Legs-up-the-wall pose)
Adho mukha svanasana (Downward-facing dog pose)
Pashchimottanasana (Seated Forward Bend Pose)
Setu Bandhasana (Bridge pose)
            '''
    elif (X == "Malaria"):
        diagnosis = '''The detected  disease is Malaria.\n
Recommended Medicines :Quinine sulfate (Qualaquin) & doxycycline
artesunate(injection)
Artemether
Atovaquone/Proguanil (Malarone)
Chloroquine
Doxycycline
Mefloquine
Primaquine
Tafenoquine (ArakodaTM)\n

Recommended Yoga Asanas :Nadi shodhan pranayama
Siddha Walk
Shakti Mudra or Gesture of Power
Bhastrika Pranayama
Adequate rest for recovery
            '''
    elif (X == "Jaundice"):
        diagnosis = '''The detected  disease is Jaundice.\n
Recommended Medicines :cholestyramine
Ceftriaxone
Trisoliv
Rifampin
Naltrexone
Sertraline
Phenobarbital\n

Recommended Yoga Asanas :Kapal Bhati
Bhramari pranayama
Anulom Vilom
Udgith Pranayama
Sheetkari pranayama
            '''
    elif (X == "Tuberculosis  "):
        diagnosis = '''The detected  disease is Tuberculosis .\n
Recommended Medicines :Rifampin (RIF),
Isoniazid (INH),
Pyrazinamide (PZA), and.
Ethambutol (EMB)\n

Recommended Yoga Asanas :Bhastrika Pranayama
Bhujangasana
Kapalbhati Pranayama
Tadasana

            '''
    elif (X == "Typhoid"):
        diagnosis = '''The detected  disease is Typhoid.\n
Recommended Medicines :Ciprofloxacin (Cipro)
Azithromycin (Zithromax)
Ceftriaxone
ofloxacin
Chloramphenicol\n

Recommended Yoga Asanas :Nadi shodhan pranayama
Siddha Walk
Shakti Mudra or Gesture of Power
Bhastrika Pranayama
Adequate rest for recovery

            '''
    elif (X == "pneumonia"):
        diagnosis = '''The detected  disease is pneumonia.\n
Recommended Medicines :Fluoroquinolones. Delafloxacin (Baxdela)
Macrolides. Azithromycin (Zithromax)
Monobactams. Aztreonam (Azactam)
Antibiotics, Lincosamide. Clindamycin (Cleocin)
Tetracyclines. Doxycycline (
    Bio-Tab, Doryx, Doxy, Periostat, Vibramycin, Vibra-Tabs)
Carbapenems. Ertapenem (Invanz)
Oxazolidinones. Linezolid (Zyvox)
Aminoglycoside\n

Recommended Yoga Asanas :Dandasana or Staff Pose
Malasana or Waste Evacuation Pose
Vajrasana or Thunderbolt Pose/Diamond Pose
Paschimottanasana or Seated Forward Bend

            '''
    elif (X == "Peptic ulcer"):
        diagnosis = '''The detected  disease is Peptic ulcer.\n
Recommended Medicines :pantoprazole (Protonix)
esomeprazole (Nexium)
rabeprazole (Aciphex)
olansoprazole (Prevacid)
omeprazole (Prilosec)
Psidium guajava Linn\n

Recommended Yoga Asanas :Kapalbhati Pranayama
Pavanamuktasana
Uttanapadasana
Vajrasana
            '''
    elif (X == "hyperthyroidism "):
        diagnosis = '''The detected  disease is hyperthyroidism .\n
Recommended Medicines :propylthiouracil
methimazole (also known as Tapazole)
Carbimazole
thionamides
potassium perchlorate\n

Recommended Yoga Asanas :plow pose
matsyasan
tadasan
legs-up-the-wall pose
            '''
    elif (X == "hepatitis c"):
        diagnosis = '''The detected  disease is hepatitis c.\n
Recommended Medicines :Boceprevir
Daclatasvir
Glecaprevir and Pibrentasvir
Interferon Alfa-2b and Ribavirin
Interferon Alfacon-1
Interferon Alpha- Two B
Ledipasvir and Sofosbuvir
Simeprevir\n

Recommended Yoga Asanas :Shavasan
pranayam
shoulder rotation

            '''
    elif (X == "hemorrhage"):
        diagnosis = '''The detected  disease is hemorrhage.\n
Recommended Medicines :Tranexamic acid (TXA)
controlled hemorrhagic shock (chs)
"Cyklokapron (tranexamic acidAntifibrinolytics
Methergine (methylergonovine)
Amicar (aminocaproic acid)
Nymalize
nimodipine
Andexxa"\n

Recommended Yoga Asanas :none(might help-Dandasan)
            '''
    elif (X == "migraine"):
        diagnosis = '''The detected  disease is migraine.\n
Recommended Medicines :Almotriptan (Axert)
Eletriptan (Relpax)
Frovatriptan (Frova)
Naratriptan (Amerge)
Rizatriptan (Maxalt)
Sumatriptan (Alsuma, Imitrex, Onzetra, Sumavel, Zembrace)
Zolmitriptan (Zomig)\n

Recommended Yoga Asanas :Adho mukha svanasana (Downward facing dog pose)
Prasarita padottanasana (Wide-legged forward bend pose)
Shishuasana (Child pose)
Janusirsasana ( Head to knee pose)
Hastapadasana (Standing forward bend pose)
            '''
    elif (X == "hypoglycemia"):
        diagnosis = '''The detected  disease is hypoglycemia.\n
Recommended Medicines :Sulfonylureas (glipizide, glyburide, gliclazide, glimepiride)
Meglitinides (repaglinide and nateglinide)
Biguanides (metformin)
Thiazolidinediones (rosiglitazone, pioglitazone)
alpha-Glucosidase inhibitors (acarbose, miglitol, voglibose)\n

Recommended Yoga Asanas :Dhanurasana (Bow Pose)
Balasana (Child pose)
Bhujangasana (Upward-Facing Dog Pose)
Corpse Pose (Shavasana)
Legs Up the Wall (Viparita Karani)
Mountain Pose (Tadasana)
Mandukasana (Frog Pose)
Chakarasna (Wheel Pose)
            '''
    elif (X == "Urinary tract infection"):
        diagnosis = '''The detected  disease is Urinary tract infection.\n
Recommended Medicines :Trimethoprim and sulfamethoxazole (Bactrim, Bactrim DS)
Fosfomycin (Monurol)
Nitrofurantoin (Macrodantin, Macrobid, Furadantin)
Cephalexin
Ceftriaxone\n

Recommended Yoga Asanas :none
            '''
    elif (X == "osteoarthritis"):
        diagnosis = '''The detected  disease is osteoarthritis.\n
Recommended Medicines :celecoxib (Celebrex)
diflunisal
etodolac
fenoprofen (Nalfon)
flurbiprofen
i
    app.run(debug=True)
