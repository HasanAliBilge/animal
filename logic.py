import sqlite3
from translate import Translator

class DB_Manager:
    def __init__(self, database):
        self.database = database
        
    def get_random_animal(self):
        with sqlite3.connect(self.database) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            
            cur.execute("SELECT * FROM animals ORDER BY RANDOM() LIMIT 1")
            result = cur.fetchone()
            
            print(f"Rastgele hayvan getirildi: {result['Animal'] if result else 'Bulunamadı'}")
            return result

class AnimalInfo:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.translator = Translator(to_lang="tr")
        
    def translate_term(self, term):
        """Tek terim çevirisi için optimize edilmiş fonksiyon"""
        return self.translator.translate(term) if term else term
            
    def get_random_info(self):
        """Rastgele hayvan bilgisi getir"""
        animal_data = self.db_manager.get_random_animal()
        
        if not animal_data:
            return "Üzgünüm, hiç hayvan bulamadım 😔"
            
        # Temel bilgileri al
        name = animal_data['Animal']
        height = animal_data['Height (cm)']
        weight = animal_data['Weight (kg)']
        color = animal_data['Color']
        habitat = animal_data['Habitat']
        diet = animal_data['Diet']
        conservation = animal_data['Conservation Status']
        
        # Değerleri çevir
        color_translated = self.translate_term(color)
        habitat_translated = self.translate_term(habitat)
        diet_translated = self.translate_term(diet)
        conservation_translated = self.translate_term(conservation)
        
        # Paragraf oluştur
        return (
            f"🎲 **Rastgele Hayvan: {name}** hakkında bilgiler:\n\n"
            f"📏 **Boy**: {height} cm\n"
            f"⚖️ **Ağırlık**: {weight} kg\n"
            f"🎨 **Renk**: {color_translated}\n"
            f"🏞️ **Yaşam Alanı**: {habitat_translated}\n"
            f"🍽️ **Beslenme**: {diet_translated}\n"
            f"🛡️ **Koruma Durumu**: {conservation_translated}"
        )