import pandas as pd
from scraper import Scraper
from logger import Logger

def main():
    # Charger les données depuis Excel
    df = pd.read_excel("data.xlsx")

    logger = Logger()
    scraper = Scraper(logger)

    for index, row in df.iterrows():
        user = str(row["User"])
        password = str(row["Password"])
        site = str(row["Site"])
        print(f"🔄 Tentative : {user} sur {site}")
        scraper.login_and_capture(site, user, password)

    scraper.close()
    print("✅ Tous les tests sont terminés.")

if __name__ == "__main__":
    main()
