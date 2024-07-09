import random
import time

probabilities = {
    'Paslı kolye':1/3,
    'Eski kitap':1/5,
    'Gümüş saat':1/10,
    'Kumsaati':1/25,
    'Eski fotoğraf':1/30
}
xp_rewards = {
    'Paslı kolye': 6,
    'Eski kitap':10,
    'Gümüş saat':20,
    'Kumsaati':40,
    'Eski fotoğraf':55
    
}

admin = False

total_probability = sum(probabilities.values())

if total_probability > 1:
    raise ValueError('Olasılıkların toplamı 1den buyuk. Lutfen kontrol edin')
elif total_probability <1:
    print("Dikkat: Olasılıkların toplamı 1'den küçük. Geriye kalan olasılık 'diğer' olarak kabul edilecek.")

xp = 0
roll_count = 0

def normalize_probabilities():
    total = sum(probabilities.values())
    for key in probabilities:
        probabilities[key] /= total
        

def adjust_probabilites_for_xp():
    for key in probabilities:
        probabilities[key] += xp * 0.0001 # xpye göre olasılıkları arttırmak için
    normalize_probabilities() # Olasılıkları normale cevirir.

def roll():
    global roll_count,xp
    roll_count += 1
    
    adjust_probabilites_for_xp()


    rand_value = random.random()
    cumulative_probability = 0.0
    for key, probability in probabilities.items():
        cumulative_probability += probability
        if rand_value < cumulative_probability:
            xp += xp_rewards[key]
            return f"\n{key} bulundu, {xp_rewards[key]} XP kazandın!!\n"
            


while True:
    command = input("'roll' yazarak çarkı cevirebilirsiniz (çıkmak için 'exit' yazın): ").strip().lower()

    if command == 'roll':
        result = roll()
        print(result)
        print(f"Güncel XP: {xp}")
        # print(f"Güncel olasılıklar: {probabilities}")
    elif command == 'admin':
        admin = True
        print('Admin availabled')

    elif command == 'exit':
        break
    else:
        print("Geçersiz komut. Lütfen 'roll' veya 'exit' yazın.")