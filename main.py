import asyncio

lista : list[int] = []

async def main(): 
    print('Bienvenido a tu lista de números primos\nEspere unos segundos para que se muestren')
    await asyncio.sleep(2)
    este = 1
    while len(lista) < 100: 
        if este == 1: 
            este += 1
            continue
        i = este - 1
        verdad = True
        while i != 1: 
            if (este % i) == 0: 
                verdad = False
                break
            i -= 1
        if verdad: lista.append(este)
        este += 1
    for i in range(100): 
        print(f"{i + 1}°: {lista[i]}")
        

asyncio.run(main())