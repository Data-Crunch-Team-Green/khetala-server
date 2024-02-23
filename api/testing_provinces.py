import json


def open_json(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data

def counting_districts(data, crop, year):
    total_districts = ['TAPLEJUNG', 'SANKHUWASABHA', 'SOLUKHUMBU', 'PANCHTHAR', 'ILLAM', 'TERHATHUM', 
                       'DHANKUTA', 'BHOJPUR', 'KHOTANG', 'OKHALDHUNGA', 'UDAYAPUR', 'JHAPA', 'MORANG', 
                       'SUNSARI', 'SAPTARI', 'SIRAHA', 'DHANUSHA', 'MAHOTTARI', 'SARLAHI', 'RAUTAHAT', 
                       'BARA', 'PARSA', 'DOLAKHA', 'SINDHUPALCHOK', 'RASUWA', 'RAMECHAP', 'SINDHULI', 
                       'KAVRE', 'BHAKTAPUR', 'LALITPUR', 'KATHMANDU', 'NUWAKOT', 'DHADING', 'MAKAWANPUR', 
                       'CHITWAN', 'MANANG', 'MUSTANG', 'GORKHA', 'LAMJUNG', 'TANAHU', 'KASKI', 'PARBAT', 
                       'SYANGJA', 'MYAGDI', 'BAGLUNG', 'NAWALPARASI EAST', 'PALPA', 'GULMI', 'ARGHAKHANCHI', 
                       'NAWALPARASI WEST', 'RUPANDEHI', 'KAPILBASTU', 'DANG', 'BANKE', 'BARDIYA', 'RUKUM EAST', 
                       'PYUTHAN', 'ROLPA', 'DOLPA', 'MUGU', 'HUMLA', 'JUMLA', 'KALIKOT', 'RUKUM WEST', 'SALYAN', 
                       'JAJARKOT', 'DAILEKH', 'SURKHET', 'BAJURA', 'BAJHANG', 'DARCHULA', 'ACHHAM', 'DOTI', 
                       'BAITADI', 'DADELDHURA', 'KAILALI', 'KANCHANPUR']
    districts = []
    counter = 0
    for a in data:
        for key, value in a.items():
            if key == 'District':
                counter += 1
                districts.append(value)

    not_present = []
    for i in total_districts:
        if i not in districts:
            not_present.append(i)
        else:
            continue
    
    left = len(total_districts)-counter

    print(f" The total number of district in {year}, {crop}: {counter} i.e remaining - {left}.  \n District not present are {not_present}")
    return counter

if __name__ == "__main__":
    a = open_json('raw_data/2078_data/barley_yield.json')
    # b = open_json('raw_data/2078_data/barley_yield.json')
    c = open_json('raw_data/2078_data/buckwheat_yield.json')
    # d = open_json('raw_data/2079_data/wheat_yield.json')
    e = open_json('raw_data/2077_data/millet_yield2077.json')
    # f = open_json('raw_data/2077_data/wheat_yield2077.json')

    counting_districts(a, 'barley', '2076')
    # counting_districts(b, 'barley', '2078')
    counting_districts(c, 'buckwheat', '2078')
    # counting_districts(d, 'maize', '2079')
    counting_districts(e, 'millet', '2077')
    # counting_districts(f, 'buckwheat', '2077')

