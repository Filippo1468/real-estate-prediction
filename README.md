# Real Estate Price Prediction Model

## Descrizione progetto

Questo progetto prevede l'uso di un modello di regressione lineare per prevedere il **prezzo per unità di area** di proprietà immobiliari in base a variabili come **età della casa**, **distanza dalla stazione MRT**, **numero di negozi nelle vicinanze**, **latitudine** e **longitudine**.

Sono stati creati due modelli:

1. **Model 1 (features1)**: Usa le variabili **età della casa**, **distanza dalla stazione MRT**, e **numero di negozi nelle vicinanze**.
2. **Model 2 (features2)**: Usa le variabili **latitudine** e **longitudine**.

## Dataset

Il dataset utilizzato per l'addestramento del modello proviene da un set di dati di valutazione immobiliare, contenente informazioni su proprietà in un'area urbana, incluse le seguenti variabili:

- **X2 house age**: Età della casa (in anni)
- **X3 distance to the nearest MRT station**: Distanza dalla stazione MRT più vicina (in km)
- **X4 number of convenience stores**: Numero di negozi di convenienza nelle vicinanze
- **X5 latitude**: Latitudine della proprietà
- **X6 longitude**: Longitudine della proprietà
- **Y house price of unit area**: Prezzo per unità di area (target)

## Installazione
1. **Clonare il repository**:
   ```bash
   git clone https://github.com/Filippo1468/real-estate-prediction.git
   cd real-estate-prediction
2. **Installare le dipendenze**:
   ```bash
   pip install -r requirements.txt
3. **Esecuzione Web app**: 
   ```bash
   cd app
   streamlit run app.py
